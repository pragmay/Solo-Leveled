## INTRODUCTION TO PYTHON AND SQL

### Python

Python is a widely used high-level, interpreted programming language created by Guido van Rossum in 1991. It emphasizes code readability and logical simplicity, enabling developers to build complex applications using clean, concise syntax.

**Key Applications:**

- Web and Software Development
    
- Database Integration and API Management
    
- Data Analytics and Statistical Computations
    
- Automated CLI Systems and Scripting
    

**Features of Python:**

- **Easy to Learn & Read:** Object-oriented architecture with straightforward syntax rules.
    
- **Interpreted Language:** Code executes line-by-line, simplifying debugging.
    
- **Cross-Platform Compatibility:** Runs seamlessly across Windows, Linux, and macOS platforms.
    
- **Extensive Ecosystem:** Rich built-in standard libraries (`statistics`, `math`, `datetime`) and third-party database drivers (`mysql-connector-python`).
    


## INTRODUCTION TO PYTHON AND SQL

### Python

Python is a widely used high-level, interpreted programming language created by Guido van Rossum in 1991. It emphasizes code readability and logical simplicity, enabling developers to build complex applications using clean, concise syntax.

**Key Applications:**

- Web and Software Development
    
- Database Integration and API Management
    
- Data Analytics and Statistical Computations
    
- Automated CLI Systems and Scripting
    

**Features of Python:**

- **Easy to Learn & Read:** Object-oriented architecture with straightforward syntax rules.
    
- **Interpreted Language:** Code executes line-by-line, simplifying debugging.
    
- **Cross-Platform Compatibility:** Runs seamlessly across Windows, Linux, and macOS platforms.
    
- **Extensive Ecosystem:** Rich built-in standard libraries (`statistics`, `math`, `datetime`) and third-party database drivers (`mysql-connector-python`).
    


## ABOUT THE PROJECT

### Title: Solo Leveling Military Management System (Shadow Military Protocol)

The **Shadow Military Protocol** is an enterprise-grade administrative and tactical management system modeled after advanced command-and-control software architectures. It bridges tactical field metrics with centralized relational database storage to manage elite units, armory inventory, mission assignments, and combat readiness metrics.

### Key Objectives & Functionalities

1. **Role-Based Authentication Security:**
    
    - **Monarch / Captain Tier:** Full administrative access for personnel oversight, inventory procurement, requisition approvals, and system analytics.
        
    - **Shadow Soldier Tier:** Restricted access to personal combat stats, task updates, health monitoring, and weapon requisitions.
        
2. **Arsenal & Logistics Management:**
    
    - Multi-categorical inventory tracking covering Assault Rifles, Battle Rifles, LMGs, Snipers, Pistols, Shotguns, SMGs, Explosives, Ammunition, and Accessories.
        
    - Requisition order workflow with approval/rejection overrides by Captains.
        
3. **Combat Readiness & Health Analytics:**
    
    - Real-time monitoring of HP, Mana, combat ranks (S-Rank through E-Rank), and field statuses (Active, Injured, Recovering, Critical).
        
    - Automated calculation of military readiness averages using standard deviation and mean calculations via Python’s `statistics` module.
        
4. **Dynamic Mission Deployment:**
    
    - Assignment of S-Rank through C-Rank combat quests with priority filtering and status progress tracking.
        
5. **MySQL Database Persistence:**
    
    - Automatic schema initialization, automated table creation, and state synchronization between Python memory lists and MySQL tables (`shadow_army_db`).
        

## HARDWARE AND SOFTWARE SPECIFICATIONS

### Hardware Requirements

- **Processor:** x86/x64 Dual-Core CPU @ 2.0 GHz or higher (Intel Core / AMD Ryzen)
    
- **RAM:** 4 GB minimum (8 GB recommended)
    
- **Disk Space:** 500 MB available storage for database tables and application runtime logs
    
- **Input Devices:** Standard Keyboard and Mouse/Trackball
    

### Software Requirements

- **Operating System:** Windows 10/11, macOS, or Linux (Debian/Ubuntu)
    
- **Environment:** Jupyter Notebook / JupyterLab or VS Code
    
- **Python Runtime:** Python v3.9+ (64-bit)
    
- **Database Engine:** MySQL Server v8.0 or v9.0 Community Server
    
- **Required Libraries:**
    
    - `mysql-connector-python` (Database Driver)
        
    - `statistics` & `math` (Mathematical & Statistical Calculations)
        
    - `getpass` (Secure Password Input)
        
    - `datetime` (Timestamping Operations)
        

## DATABASE SCHEMA & SQL ARCHITECTURE

The backend utilizes the database **`shadow_army_db`**. Below is the structural schema derived from the database dump:

### Table Structures

#### 1. `captains`

Stores administrative user credentials.

- `id` INT AUTO_INCREMENT PRIMARY KEY
    
- `name` VARCHAR(100) UNIQUE NOT NULL
    
- `password` VARCHAR(100) NOT NULL
    

#### 2. `soldiers`

Stores combat personnel details and health state metrics.

- `id` INT AUTO_INCREMENT PRIMARY KEY
    
- `name` VARCHAR(100) UNIQUE NOT NULL
    
- `password` VARCHAR(100) NOT NULL
    
- `hp` INT NOT NULL
    
- `mana` INT NOT NULL
    
- `rank` VARCHAR(20) NOT NULL
    
- `level` INT NOT NULL
    
- `status` VARCHAR(20) NOT NULL
    

#### 3. `weapons`

Catalog of armory hardware.

- `id` INT AUTO_INCREMENT PRIMARY KEY
    
- `category` VARCHAR(50) NOT NULL
    
- `name` VARCHAR(100) NOT NULL
    
- `caliber` VARCHAR(60) NOT NULL
    
- `qty` INT NOT NULL
    

#### 4. `mission_tasks`

Operational deployments and quests.

- `id` INT AUTO_INCREMENT PRIMARY KEY
    
- `mission_id` VARCHAR(20) NOT NULL
    
- `description` VARCHAR(200) NOT NULL
    
- `assigned_to` VARCHAR(100) NOT NULL
    
- `status` VARCHAR(30) NOT NULL
    
- `priority` VARCHAR(20) NOT NULL
    

#### 5. `weapon_orders`

Logistical requisition tracking.

- `id` INT AUTO_INCREMENT PRIMARY KEY
    
- `soldier` VARCHAR(100) NOT NULL
    
- `weapon` VARCHAR(100) NOT NULL
    
- `qty` INT NOT NULL
    
- `status` VARCHAR(30) NOT NULL

# SOURCE CODE


```python
import math, random, statistics as stat
from math import pi
from getpass import getpass
from datetime import datetime
import mysql.connector

# ── DATABASE CREDENTIALS ──────────────────────────────────────────────────────
DB_HOST = "localhost"
DB_USER = "root"
DB_PASS = "James_Bond"
DB_NAME = "shadow_army_db"

print("="*80)
print("🗡️  INITIALIZING SHADOW MILITARY PROTOCOL  🗡️")
print("="*80)


# ═══════════════════════════════════════════════════════════════════════════════
#  INDEX CONSTANTS
# ═══════════════════════════════════════════════════════════════════════════════

# Weapon  [NAME, CALIBER, QTY]
NAME        = 0
CALIBER     = 1
QTY         = 2

# Explosive  [NAME, QTY]
EXP_NAME    = 0
EXP_QTY     = 1

# Ammo / Accessory  [ITEM_NAME, ITEM_QTY, ITEM_STATUS]
ITEM_NAME   = 0
ITEM_QTY    = 1
ITEM_STATUS = 2

# Captain  [CAP_NAME, CAP_PASS]
CAP_NAME    = 0
CAP_PASS    = 1

# Soldier  [SOL_NAME, SOL_PASS, SOL_HP, SOL_MANA, SOL_RANK, SOL_LEVEL, SOL_STATUS]
SOL_NAME    = 0
SOL_PASS    = 1
SOL_HP      = 2
SOL_MANA    = 3
SOL_RANK    = 4
SOL_LEVEL   = 5
SOL_STATUS  = 6

# Mission  [M_ID, M_DESC, M_ASSIGNED, M_STATUS, M_PRIORITY]
M_ID        = 0
M_DESC      = 1
M_ASSIGNED  = 2
M_STATUS    = 3
M_PRIORITY  = 4

# Weapon Order  [O_SOLDIER, O_WEAPON, O_QTY, O_STATUS]
O_SOLDIER   = 0
O_WEAPON    = 1
O_QTY       = 2
O_STATUS    = 3


# ═══════════════════════════════════════════════════════════════════════════════
#  CAPTAINS                           [CAP_NAME,              CAP_PASS      ]
# ═══════════════════════════════════════════════════════════════════════════════
CAP_YUVRAJ    = ["Yuvraj Hyperion",    "CapYuvHy#7"  ]
CAP_DEVAKSHA  = ["Devaksha Quantum",   "CapDevQ!21"  ]
CAP_ARINJAY   = ["Arinjay Solace",     "CapArjSol$5" ]
CAP_RUDRANATH = ["Rudranath Eclipse",  "CapRudEcl8"  ]
CAP_VEERSHAAD = ["Veershaad Zenith",   "CapVeeZen#9" ]


# ═══════════════════════════════════════════════════════════════════════════════
#  SOLDIERS  [SOL_NAME, SOL_PASS, SOL_HP, SOL_MANA, SOL_RANK, SOL_LEVEL, SOL_STATUS]
# ═══════════════════════════════════════════════════════════════════════════════
VIKRANT    = ["Vikrant Senapati X9",      "Vikr@ntX9!",    100, 100, "S-Rank", 45, "Active"     ]
RUDRA      = ["Rudra Pratap Nova",         "Rudr@Nova42",    95,  90, "A-Rank", 38, "Active"     ]
BHAIRAV    = ["Bhairav Singh Orion",       "Bhai$Orion7",    88,  85, "A-Rank", 35, "Injured"    ]
AGNIVEER   = ["Agniveer Kaaltron",         "Agni_Kaal99",   100,  95, "B-Rank", 28, "Active"     ]
ARINDHAM   = ["Arindham Varmax",           "Arin!Var88",     92,  88, "B-Rank", 30, "Active"     ]
MAHAVEER   = ["Mahaveer Rajat Prime",      "MahaRajat#5",    85,  80, "C-Rank", 22, "Recovering" ]
SAMRAT     = ["Samrat Veerbhadra 7",       "SamVee7!",      100, 100, "S-Rank", 42, "Active"     ]
SHATRUGHAN = ["Shatrughan Devdroid",       "ShatDev#12",     78,  75, "C-Rank", 20, "Injured"    ]
TRIKAND    = ["Trikand Arjun Nexus",       "TriArjNex3",     90,  92, "A-Rank", 36, "Active"     ]
GARUDNATH  = ["Garudnath Keshari X",       "GaruKesh$X",    100,  98, "S-Rank", 48, "Active"     ]
VAJRAHAN   = ["Vajrahan Bhupendra Omega",  "VajBhupOmega8",  88,  85, "B-Rank", 29, "Active"     ]
NIRBHAY    = ["Nirbhay Karunesh Flux",     "NirbKar!Flux",   95,  90, "A-Rank", 40, "Active"     ]
DHANANJAY  = ["Dhananjay Kulkarni Titan",  "DhanKulT#4",     82,  78, "C-Rank", 25, "Recovering" ]
SHIVRAAJ   = ["Shivraaj Deshmukh Vortex",  "ShivDesVort9",  100, 100, "S-Rank", 50, "Active"     ]
KAALNEMI   = ["Kaalnemi Pradhan Pulse",    "KaalPrad!P",     90,  88, "B-Rank", 32, "Active"     ]


# ═══════════════════════════════════════════════════════════════════════════════
#  WEAPONS                            [NAME,              CALIBER,                      QTY]
# ═══════════════════════════════════════════════════════════════════════════════
AK47       = ["AK-47",           "7.62×39mm",                 120]
AK103      = ["AK-103",          "7.62×39mm",                  85]
INSAS      = ["INSAS Rifle",     "5.56×45mm",                 200]
TAVOR      = ["Tavor TAR-21",    "5.56×45mm",                  60]
M4         = ["M4 Carbine",      "5.56×45mm",                 150]
SIG716     = ["SIG716",          "7.62×51mm",                  45]
HK416      = ["HK416",           "5.56×45mm",                  70]

FNFAL      = ["FN FAL",          "7.62×51mm",                  40]
SCARH      = ["SCAR-H",          "7.62×51mm",                  35]

PKM        = ["PKM",             "7.62×54mmR",                 25]
NEGEV      = ["Negev NG7",       "7.62×51mm",                  20]
M249       = ["M249 SAW",        "5.56×45mm",                  30]

SVD        = ["Dragunov SVD",    "7.62×54mmR",                 18]
BARRETT    = ["Barrett M82",     ".50 BMG",                    10]
AWM        = ["AWM",             ".300 Win Mag / .338 Lapua",   8]
MK12       = ["Mk 12 SPR",       "5.56×45mm",                  15]

GLOCK17    = ["Glock 17",        "9×19mm",                    250]
SIGP226    = ["SIG P226",        "9×19mm",                    180]
BERETTAM9  = ["Beretta M9",      "9×19mm",                    200]
HS2000     = ["HS2000",          "9×19mm",                     90]
GRACH      = ["MP-443 Grach",    "9×19mm",                    110]

BENELLI    = ["Benelli M4",      "12-gauge shells",             35]
REM870     = ["Remington 870",   "12-gauge shells",             40]

MP5        = ["MP5",             "9×19mm",                     75]
UZI        = ["Uzi",             "9×19mm",                     55]
SCORPION   = ["CZ Scorpion EVO", "9×19mm",                     50]


# ═══════════════════════════════════════════════════════════════════════════════
#  EXPLOSIVES                         [EXP_NAME,                        EXP_QTY]
# ═══════════════════════════════════════════════════════════════════════════════
GRENADE    = ["Hand Grenade (HE36 / M67)",   300]
SMOKE      = ["Smoke Grenade",               200]
FLASHBANG  = ["Flashbang",                   150]


# ═══════════════════════════════════════════════════════════════════════════════
#  AMMUNITION                         [ITEM_NAME,               ITEM_QTY, ITEM_STATUS ]
# ═══════════════════════════════════════════════════════════════════════════════
AMMO_556     = ["5.56×45mm rounds",      50000, "Available"]
AMMO_762x39  = ["7.62×39mm rounds",      40000, "Available"]
AMMO_762x51  = ["7.62×51mm rounds",      30000, "Available"]
AMMO_762x54R = ["7.62×54mmR rounds",     25000, "Low Stock"]
AMMO_9MM     = ["9×19mm pistol ammo",    60000, "Available"]
AMMO_50BMG   = [".50 BMG ammo",           5000, "Low Stock"]
AMMO_338     = [".338 Lapua",             3000, "Available"]
AMMO_12G     = ["12-gauge shells",       15000, "Available"]


# ═══════════════════════════════════════════════════════════════════════════════
#  ACCESSORIES                        [ITEM_NAME,           ITEM_QTY, ITEM_STATUS ]
# ═══════════════════════════════════════════════════════════════════════════════
ACC_RIFLEMAG   = ["Rifle magazines",   500, "Available"]
ACC_PISTOLMAG  = ["Pistol magazines",  300, "Available"]
ACC_ACOG       = ["ACOG Scopes",        50, "Low Stock"]
ACC_REDDOT     = ["Red Dot Sights",     80, "Available"]
ACC_TACLIGHT   = ["Tactical Lights",   100, "Available"]
ACC_SUPPRESSOR = ["Suppressors",        30, "Low Stock"]


# ═══════════════════════════════════════════════════════════════════════════════
#  CATEGORY LISTS
# ═══════════════════════════════════════════════════════════════════════════════
captains         = [CAP_YUVRAJ, CAP_DEVAKSHA, CAP_ARINJAY, CAP_RUDRANATH, CAP_VEERSHAAD]

assault_rifles   = [AK47, AK103, INSAS, TAVOR, M4, SIG716, HK416]
battle_rifles    = [FNFAL, SCARH]
light_machine_guns = [PKM, NEGEV, M249]
sniper_rifles    = [SVD, BARRETT, AWM, MK12]
pistols          = [GLOCK17, SIGP226, BERETTAM9, HS2000, GRACH]
shotguns         = [BENELLI, REM870]
smgs             = [MP5, UZI, SCORPION]
explosives       = [GRENADE, SMOKE, FLASHBANG]
ammunition       = [AMMO_556, AMMO_762x39, AMMO_762x51, AMMO_762x54R,
                    AMMO_9MM, AMMO_50BMG, AMMO_338, AMMO_12G]
accessories      = [ACC_RIFLEMAG, ACC_PISTOLMAG, ACC_ACOG,
                    ACC_REDDOT, ACC_TACLIGHT, ACC_SUPPRESSOR]

s_rank    = [VIKRANT, SAMRAT, GARUDNATH, SHIVRAAJ]
a_rank    = [RUDRA, BHAIRAV, TRIKAND, NIRBHAY]
b_rank    = [AGNIVEER, ARINDHAM, VAJRAHAN, KAALNEMI]
c_rank    = [MAHAVEER, SHATRUGHAN, DHANANJAY]

all_soldiers = [VIKRANT, RUDRA, BHAIRAV, AGNIVEER, ARINDHAM, MAHAVEER,
                SAMRAT, SHATRUGHAN, TRIKAND, GARUDNATH, VAJRAHAN,
                NIRBHAY, DHANANJAY, SHIVRAAJ, KAALNEMI]

# Rank list lookup — used by add_soldier()
rank_lists = {"S-Rank": s_rank, "A-Rank": a_rank, "B-Rank": b_rank, "C-Rank": c_rank}


# ═══════════════════════════════════════════════════════════════════════════════
#  MASTER DICTIONARY
# ═══════════════════════════════════════════════════════════════════════════════
armory = {
    "Assault_Rifles"    : assault_rifles,
    "Battle_Rifles"     : battle_rifles,
    "Light_Machine_Guns": light_machine_guns,
    "Sniper_Rifles"     : sniper_rifles,
    "Pistols"           : pistols,
    "Shotguns"          : shotguns,
    "SMGs"              : smgs,
    "Explosives"        : explosives,
    "Ammunition"        : ammunition,
    "Accessories"       : accessories,
}

# Weapon categories shown during ordering (excludes Ammo, Accessories, Explosives)
ORDERABLE_WEAPON_CATS = [
    "Assault_Rifles", "Battle_Rifles", "Light_Machine_Guns",
    "Sniper_Rifles", "Pistols", "Shotguns", "SMGs"
]


# ═══════════════════════════════════════════════════════════════════════════════
#  MISSION TASKS & ORDERS
# ═══════════════════════════════════════════════════════════════════════════════
mission_tasks = [
    ["QUEST-001", "Secure Northern Border",    "Vikrant Senapati X9",  "In Progress", "S-Rank"],
    ["QUEST-002", "Weapons Training Exercise", "All Soldiers",          "Pending",     "B-Rank"],
    ["QUEST-003", "Recon Mission - Sector 7",  "Garudnath Keshari X",  "Completed",   "A-Rank"],
    ["QUEST-004", "Equipment Maintenance",     "Agniveer Kaaltron",     "Pending",     "C-Rank"],
    ["QUEST-005", "Night Patrol Duty",         "Nirbhay Karunesh Flux","In Progress", "A-Rank"],
]

weapon_orders   = []   # each entry: [O_SOLDIER, O_WEAPON, O_QTY, O_STATUS]
pending_recruits = []  # each entry: [SOL_NAME, SOL_PASS, SOL_HP, SOL_MANA, SOL_RANK, SOL_LEVEL, SOL_STATUS]


# ═══════════════════════════════════════════════════════════════════════════════
#  HELPER — find a person by name inside any list
# ═══════════════════════════════════════════════════════════════════════════════
def find_by_name(lst, name, name_idx=0):
    for entry in lst:
        if entry[name_idx] == name:
            return entry
    return None


# ═══════════════════════════════════════════════════════════════════════════════
#  USER-ADDABLE
# ═══════════════════════════════════════════════════════════════════════════════
def add_weapon(category, name, caliber, qty):
    weapon = [name, caliber, qty]
    if category not in armory:
        armory[category] = []
    armory[category].append(weapon)
    return weapon

def add_explosive(name, qty):
    explosive = [name, qty]
    armory["Explosives"].append(explosive)
    return explosive

def add_ammo(item_name, qty, status="Available"):
    ammo = [item_name, qty, status]
    armory["Ammunition"].append(ammo)
    return ammo

def add_accessory(item_name, qty, status="Available"):
    acc = [item_name, qty, status]
    armory["Accessories"].append(acc)
    return acc

def add_soldier(name, password, hp, mana, rank, level, status="Active"):
    soldier = [name, password, hp, mana, rank, level, status]
    all_soldiers.append(soldier)
    if rank in rank_lists:
        rank_lists[rank].append(soldier)
    return soldier

def add_captain(name, password):
    captain = [name, password]
    captains.append(captain)
    return captain


# ══════════════════════════════════════════════════════════════════════════════
#  AUTHENTICATION
# ══════════════════════════════════════════════════════════════════════════════
def auth():
    """Shadow Authentication Protocol"""
    brp = 0
    while brp in range(3):
        print("\n" + "─"*80)
        print("🔐 IDENTITY VERIFICATION REQUIRED")
        print("─"*80)
        username = input("👤 Hunter Name: ")
        pwd = getpass("🔑 Access Code: ")

        cap = find_by_name(captains, username, CAP_NAME)
        if cap:
            if cap[CAP_PASS] == pwd:
                print("\n✅ MONARCH ACCESS GRANTED")
                print(f"🌟 Welcome, Supreme Commander {username}!")
                return True, "cap", username
            else:
                print("❌ Invalid Access Code")
            continue

        sol = find_by_name(all_soldiers, username, SOL_NAME)
        if sol:
            if sol[SOL_PASS] == pwd:
                print("\n✅ SHADOW SOLDIER ACCESS GRANTED")
                print(f"⚔️  Welcome back, Warrior {username}!")
                return True, "sol", username
            else:
                print("❌ Invalid Access Code")
            continue

        print("❌ Unknown Hunter")
        brp += 1

    return False, "break", None


# ══════════════════════════════════════════════════════════════════════════════
#  SOLDIER OPERATIONS
# ══════════════════════════════════════════════════════════════════════════════
def soldier_menu(soldier_name):
    """Shadow Soldier Command Center"""
    while True:
        print("\n" + "═"*80)
        print(f"⚔️  SHADOW SOLDIER OPERATIONS - {soldier_name}")
        print("═"*80)
        print("1. 🗡️  Order Weapons")
        print("2. ❤️  Update Health Status")
        print("3. 📋 View Assigned Missions")
        print("4. ✅ Update Completed Missions")
        print("5. 📊 View My Stats")
        print("6. 📦 View My Weapon Orders")
        print("7. 🚪 Logout")
        print("─"*80)

        choice = input("Select Operation: ")

        if choice == "1":
            order_weapons(soldier_name)
        elif choice == "2":
            update_health_status(soldier_name)
        elif choice == "3":
            view_tasks(soldier_name)
        elif choice == "4":
            update_completed_tasks(soldier_name)
        elif choice == "5":
            view_soldier_stats(soldier_name)
        elif choice == "6":
            view_my_orders(soldier_name)
        elif choice == "7":
            print("\n🌙 Shadow returning to rest... Goodbye!")
            break
        else:
            print("⚠️  Invalid Operation Code!")


def order_weapons(soldier_name):
    """Place weapon requisition order"""
    print("\n" + "═"*60)
    print("🗡️  WEAPON REQUISITION SYSTEM")
    print("═"*60)

    print("\n📦 AVAILABLE ARSENAL:")
    weapon_list = []
    idx = 1

    for cat in ORDERABLE_WEAPON_CATS:
        print(f"\n🔹 {cat.replace('_', ' ')}:")
        for weapon in armory[cat]:
            print(f"  {idx}. {weapon[NAME]} ({weapon[CALIBER]}) — Stock: {weapon[QTY]}")
            weapon_list.append(weapon)
            idx += 1

    try:
        weapon_choice = int(input("\n🎯 Select Weapon Number: ")) - 1
        quantity = int(input("📊 Quantity: "))

        if 0 <= weapon_choice < len(weapon_list):
            chosen = weapon_list[weapon_choice]
            order = [soldier_name, chosen[NAME], quantity, "Pending Approval"]
            weapon_orders.append(order)
            db_insert_order(order)
            print(f"\n✅ Order placed! {chosen[NAME]} x{quantity} - Awaiting Captain's approval")
        else:
            print("❌ Invalid weapon selection!")
    except:
        print("❌ Invalid input!")


def update_health_status(soldier_name):
    """Update soldier's health metrics"""
    print("\n" + "═"*60)
    print("❤️  HEALTH STATUS UPDATE")
    print("═"*60)

    sol = find_by_name(all_soldiers, soldier_name, SOL_NAME)
    if sol:
        print(f"\n📊 Current Stats:")
        print(f"   HP: {sol[SOL_HP]}/100")
        print(f"   Mana: {sol[SOL_MANA]}/100")
        print(f"   Rank: {sol[SOL_RANK]}")
        print(f"   Level: {sol[SOL_LEVEL]}")
        print(f"   Status: {sol[SOL_STATUS]}")

        print("\n🔄 Update Status:")
        try:
            new_hp     = int(input("New HP (0-100): "))
            new_mana   = int(input("New Mana (0-100): "))
            print("\nStatus Options: Active, Injured, Recovering, Critical")
            new_status = input("New Status: ")

            sol[SOL_HP]     = max(0, min(100, new_hp))
            sol[SOL_MANA]   = max(0, min(100, new_mana))
            sol[SOL_STATUS] = new_status
            db_update_soldier(sol)

            print("\n✅ Health Status Updated Successfully!")
            print(f"   HP: {sol[SOL_HP]}/100")
            print(f"   Mana: {sol[SOL_MANA]}/100")
            print(f"   Status: {sol[SOL_STATUS]}")
        except:
            print("❌ Invalid input!")


def view_tasks(soldier_name):
    """View assigned missions"""
    print("\n" + "═"*80)
    print(f"📋 MISSIONS ASSIGNED TO {soldier_name}")
    print("═"*80)

    found = False
    for task in mission_tasks:
        if task[M_ASSIGNED] == soldier_name or task[M_ASSIGNED] == "All Soldiers":
            print(f"\n🎯 Mission ID: {task[M_ID]}")
            print(f"   📝 Description: {task[M_DESC]}")
            print(f"   📊 Status: {task[M_STATUS]}")
            print(f"   ⭐ Priority: {task[M_PRIORITY]}")
            print("   " + "─"*60)
            found = True

    if not found:
        print("\n📭 No missions currently assigned.")


def update_completed_tasks(soldier_name):
    """Mark missions as completed"""
    print("\n" + "═"*80)
    print("✅ UPDATE MISSION STATUS")
    print("═"*80)

    soldier_missions = [
        (idx, task) for idx, task in enumerate(mission_tasks)
        if task[M_ASSIGNED] == soldier_name and task[M_STATUS] != "Completed"
    ]

    if not soldier_missions:
        print("\n📭 No pending missions to update.")
        return

    print("\n📋 Your Pending Missions:")
    for i, (idx, task) in enumerate(soldier_missions, 1):
        print(f"{i}. {task[M_ID]} - {task[M_DESC]} ({task[M_STATUS]})")

    try:
        choice = int(input("\n🎯 Select mission to mark as completed: ")) - 1
        if 0 <= choice < len(soldier_missions):
            task_idx = soldier_missions[choice][0]
            mission_tasks[task_idx][M_STATUS] = "Completed"
            db_update_mission(mission_tasks[task_idx])
            print(f"\n🎉 Mission {mission_tasks[task_idx][M_ID]} marked as COMPLETED!")
            print(f"🌟 +{random.randint(100, 500)} XP Earned!")
        else:
            print("❌ Invalid selection!")
    except:
        print("❌ Invalid input!")


def view_soldier_stats(soldier_name):
    """Display detailed soldier statistics"""
    print("\n" + "═"*80)
    print(f"📊 HUNTER PROFILE - {soldier_name}")
    print("═"*80)

    sol = find_by_name(all_soldiers, soldier_name, SOL_NAME)
    if sol:
        print(f"\n⚔️  COMBAT STATISTICS:")
        print(f"   ❤️  HP: {sol[SOL_HP]}/100 {'█' * (sol[SOL_HP]//10)}")
        print(f"   💙 Mana: {sol[SOL_MANA]}/100 {'█' * (sol[SOL_MANA]//10)}")
        print(f"   🏆 Rank: {sol[SOL_RANK]}")
        print(f"   ⭐ Level: {sol[SOL_LEVEL]}")
        print(f"   🎯 Status: {sol[SOL_STATUS]}")

        total_missions = sum(1 for t in mission_tasks if t[M_ASSIGNED] == soldier_name)
        completed      = sum(1 for t in mission_tasks if t[M_ASSIGNED] == soldier_name and t[M_STATUS] == "Completed")
        print(f"\n📋 MISSION RECORD:")
        print(f"   Total Missions: {total_missions}")
        print(f"   Completed: {completed}")
        print(f"   Success Rate: {(completed/total_missions*100) if total_missions > 0 else 0:.1f}%")


def view_my_orders(soldier_name):
    """View all weapon orders placed by this soldier"""
    print("\n" + "═"*80)
    print(f"📦 WEAPON ORDERS — {soldier_name}")
    print("═"*80)

    my_orders = [o for o in weapon_orders if o[O_SOLDIER] == soldier_name]

    if not my_orders:
        print("\n📭 You have no weapon orders.")
        return

    status_icons = {
        "Approved"        : "✅",
        "Rejected"        : "❌",
        "Pending Approval": "⏳",
    }

    for idx, order in enumerate(my_orders, 1):
        icon = status_icons.get(order[O_STATUS], "❓")
        print(f"\n{idx}. {icon} {order[O_WEAPON]} x{order[O_QTY]}")
        print(f"      Status: {order[O_STATUS]}")


# ══════════════════════════════════════════════════════════════════════════════
#  CAPTAIN OPERATIONS
# ══════════════════════════════════════════════════════════════════════════════
def captain_menu(captain_name):
    """Supreme Commander Control Center"""
    while True:
        print("\n" + "═"*80)
        print(f"👑 MONARCH COMMAND CENTER - {captain_name}")
        print("═"*80)
        print("1. 📦 Order Inventory Supplies")
        print("2. ✅ Approve Soldier Weapon Orders")
        print("3. ❤️  Check All Soldiers' Health Status")
        print("4. 📋 Add New Missions")
        print("5. 🗡️  Add New Weapons to Armory")
        print("6. 👥 Add New Recruits")
        print("7. 📊 View Complete Arsenal")
        print("8. 🎯 View All Missions")
        print("9. 📈 View System Statistics")
        print("10. 🚪 Logout")
        print("─"*80)

        choice = input("Select Command: ")

        if choice == "1":
            order_inventory()
        elif choice == "2":
            approve_weapon_orders()
        elif choice == "3":
            check_health_status()
        elif choice == "4":
            add_tasks()
        elif choice == "5":
            add_weapons()
        elif choice == "6":
            add_recruits()
        elif choice == "7":
            view_arsenal()
        elif choice == "8":
            view_all_missions()
        elif choice == "9":
            view_system_stats()
        elif choice == "10":
            print("\n👑 Monarch disconnecting... Farewell!")
            break
        else:
            print("⚠️  Invalid Command Code!")


def order_inventory():
    """Order supplies for inventory"""
    print("\n" + "═"*80)
    print("📦 INVENTORY SUPPLY ORDER SYSTEM")
    print("═"*80)

    for category in ["Ammunition", "Accessories"]:
        print(f"\n📌 {category}:")
        for idx, item in enumerate(armory[category], 1):
            print(f"   {idx}. {item[ITEM_NAME]}: {item[ITEM_QTY]} units — {item[ITEM_STATUS]}")

    print("\n🆕 Place New Order:")
    item_name = input("Item Name: ")
    try:
        quantity = int(input("Quantity: "))
        category = input("Category (Ammunition/Accessories): ")
        if category in armory:
            new_item = [item_name, quantity, "In Transit"]
            armory[category].append(new_item)
            if category == "Ammunition":
                db_insert_ammo(new_item)
            elif category == "Accessories":
                db_insert_accessory(new_item)
            print(f"\n✅ Order placed: {item_name} x{quantity}")
        else:
            print("❌ Invalid category!")
    except:
        print("❌ Invalid input!")


def approve_weapon_orders():
    """Approve pending weapon requisitions"""
    print("\n" + "═"*80)
    print("✅ WEAPON ORDER APPROVAL SYSTEM")
    print("═"*80)

    pending = [o for o in weapon_orders if o[O_STATUS] == "Pending Approval"]

    if not pending:
        print("\n📭 No pending weapon orders.")
        return

    print("\n📋 Pending Orders:")
    for idx, order in enumerate(pending, 1):
        print(f"{idx}. {order[O_SOLDIER]} — {order[O_WEAPON]} x{order[O_QTY]} ({order[O_STATUS]})")

    try:
        choice = int(input("\n🎯 Select order to approve (0 to cancel): "))
        if choice == 0:
            return
        if 1 <= choice <= len(pending):
            order = pending[choice - 1]
            print(f"\n📋 Order Details:")
            print(f"   Soldier: {order[O_SOLDIER]}")
            print(f"   Weapon:  {order[O_WEAPON]}")
            print(f"   Quantity:{order[O_QTY]}")

            decision = input("\n✅ Approve? (yes/no): ").lower()
            order[O_STATUS] = "Approved" if decision == "yes" else "Rejected"
            db_update_order(order)
            result = "APPROVED" if decision == "yes" else "REJECTED"
            print(f"\n{'🎉' if decision == 'yes' else '❌'} Order {result}!")
        else:
            print("❌ Invalid selection!")
    except:
        print("❌ Invalid input!")


def check_health_status():
    """View all soldiers' health metrics"""
    print("\n" + "═"*80)
    print("❤️  SHADOW ARMY HEALTH STATUS")
    print("═"*80)

    critical   = []
    injured    = []
    recovering = []
    active     = []

    for sol in all_soldiers:
        if sol[SOL_STATUS] == "Critical" or sol[SOL_HP] < 30:
            critical.append(sol)
        elif sol[SOL_STATUS] == "Injured":
            injured.append(sol)
        elif sol[SOL_STATUS] == "Recovering":
            recovering.append(sol)
        else:
            active.append(sol)

    def print_group(label, group, icon):
        if group:
            print(f"\n{label}:")
            for sol in group:
                print(f"   {icon} {sol[SOL_NAME]}: HP {sol[SOL_HP]}/100, Mana {sol[SOL_MANA]}/100, {sol[SOL_RANK]} Lv.{sol[SOL_LEVEL]}")

    print_group("🚨 CRITICAL STATUS", critical,   "⚠️ ")
    print_group("🩹 INJURED",         injured,    "⚠️ ")
    print_group("🏥 RECOVERING",      recovering, "💊")
    print_group("✅ ACTIVE DUTY",     active,     "⚔️ ")


def add_tasks():
    """Create new mission assignments"""
    print("\n" + "═"*80)
    print("📋 MISSION CREATION SYSTEM")
    print("═"*80)

    mission_id  = f"QUEST-{len(mission_tasks) + 1:03d}"
    description = input("\n📝 Mission Description: ")

    print("\n👥 Available Soldiers:")
    print("   0. All Soldiers")
    for idx, sol in enumerate(all_soldiers, 1):
        print(f"   {idx}. {sol[SOL_NAME]} ({sol[SOL_RANK]}) — {sol[SOL_STATUS]}")

    try:
        soldier_choice = int(input("\n🎯 Assign to (number): "))
        assigned_to = "All Soldiers" if soldier_choice == 0 else all_soldiers[soldier_choice - 1][SOL_NAME]

        print("\n⭐ Priority Levels: S-Rank, A-Rank, B-Rank, C-Rank, D-Rank")
        priority = input("Priority: ")

        mission_tasks.append([mission_id, description, assigned_to, "Pending", priority])
        db_insert_mission(mission_tasks[-1])
        print(f"\n✅ Mission {mission_id} created successfully!")
        print(f"   Assigned to: {assigned_to}")
        print(f"   Priority: {priority}")
    except:
        print("❌ Invalid input!")


def add_weapons():
    """Add new weapons to the armory"""
    print("\n" + "═"*80)
    print("🗡️  ARMORY EXPANSION SYSTEM")
    print("═"*80)

    print("\n📦 Weapon Categories:")
    for idx, cat in enumerate(ORDERABLE_WEAPON_CATS, 1):
        print(f"{idx}. {cat.replace('_', ' ')}")

    try:
        choice = int(input("\n🎯 Select Category (or 0 for new category): "))
        if choice == 0:
            category = input("New Category Name: ").replace(" ", "_")
        elif 1 <= choice <= len(ORDERABLE_WEAPON_CATS):
            category = ORDERABLE_WEAPON_CATS[choice - 1]
        else:
            print("❌ Invalid category!")
            return

        weapon_name = input("Weapon Name: ")
        caliber     = input("Caliber/Ammo Type: ")
        qty         = int(input("Quantity: "))

        new_weapon  = add_weapon(category, weapon_name, caliber, qty)
        db_insert_weapon(category, new_weapon)
        print(f"\n✅ {new_weapon[NAME]} ({new_weapon[CALIBER]}) x{new_weapon[QTY]} added to {category}!")
    except:
        print("❌ Invalid input!")


def add_recruits():
    """Add new soldiers to the system"""
    print("\n" + "═"*80)
    print("👥 RECRUITMENT SYSTEM - SHADOW AWAKENING")
    print("═"*80)

    recruit_name = input("\n📝 Recruit Name: ")
    password     = input("🔑 Set Password: ")

    print("\n⭐ Rank Assignment: S-Rank, A-Rank, B-Rank, C-Rank, D-Rank, E-Rank")
    rank = input("Initial Rank: ")

    try:
        level   = int(input("Initial Level (1-50): "))
        soldier = add_soldier(recruit_name, password, 100, 100, rank, level, "Active")
        db_insert_soldier(soldier)

        print(f"\n🎉 {recruit_name} has been awakened as a Shadow Soldier!")
        print(f"   Rank: {soldier[SOL_RANK]}")
        print(f"   Level: {soldier[SOL_LEVEL]}")
        print(f"   Status: {soldier[SOL_STATUS]}")
    except:
        print("❌ Invalid input!")


def view_arsenal():
    """Display complete weapons inventory"""
    print("\n" + "═"*80)
    print("🗡️  COMPLETE ARSENAL DATABASE")
    print("═"*80)

    for cat, weapons in armory.items():
        if cat in ("Ammunition", "Accessories"):
            continue
        print(f"\n{'═'*60}")
        print(f"🔹 {cat.replace('_', ' ').upper()}")
        print(f"{'═'*60}")
        for w in weapons:
            if len(w) == 3:   # Weapon: NAME, CALIBER, QTY
                print(f"   • {w[NAME]} — {w[CALIBER]}  (Stock: {w[QTY]})")
            else:             # Explosive: NAME, QTY
                print(f"   • {w[EXP_NAME]}  (Stock: {w[EXP_QTY]})")


def view_all_missions():
    """Display all mission assignments"""
    print("\n" + "═"*80)
    print("🎯 MISSION DATABASE")
    print("═"*80)

    statuses = {}
    for task in mission_tasks:
        statuses.setdefault(task[M_STATUS], []).append(task)

    for status, tasks in statuses.items():
        print(f"\n{'─'*60}")
        print(f"📊 STATUS: {status}")
        print(f"{'─'*60}")
        for task in tasks:
            print(f"\n   🎯 {task[M_ID]}: {task[M_DESC]}")
            print(f"      Assigned: {task[M_ASSIGNED]}")
            print(f"      Priority: {task[M_PRIORITY]}")


def view_system_stats():
    """Display comprehensive system statistics"""
    print("\n" + "═"*80)
    print("📈 SYSTEM ANALYTICS DASHBOARD")
    print("═"*80)

    total_soldiers   = len(all_soldiers)
    total_captains   = len(captains)
    active_soldiers  = sum(1 for s in all_soldiers if s[SOL_STATUS] == "Active")
    injured_soldiers = sum(1 for s in all_soldiers if s[SOL_STATUS] in ("Injured", "Recovering"))

    total_missions     = len(mission_tasks)
    completed_missions = sum(1 for t in mission_tasks if t[M_STATUS] == "Completed")
    pending_missions   = sum(1 for t in mission_tasks if t[M_STATUS] == "Pending")
    pending_orders     = sum(1 for o in weapon_orders if o[O_STATUS] == "Pending Approval")

    print(f"\n👥 PERSONNEL:")
    print(f"   Total Captains: {total_captains}")
    print(f"   Total Soldiers: {total_soldiers}")
    print(f"   Active: {active_soldiers}")
    print(f"   Injured/Recovering: {injured_soldiers}")

    print(f"\n🎯 MISSIONS:")
    print(f"   Total Missions: {total_missions}")
    print(f"   Completed: {completed_missions} ({completed_missions/total_missions*100 if total_missions > 0 else 0:.1f}%)")
    print(f"   Pending: {pending_missions}")

    print(f"\n📦 LOGISTICS:")
    print(f"   Pending Weapon Orders: {pending_orders}")
    print(f"   Inventory Categories: {len([k for k in armory if k in ('Ammunition','Accessories')])}")

    avg_hp    = stat.mean([s[SOL_HP]    for s in all_soldiers])
    avg_level = stat.mean([s[SOL_LEVEL] for s in all_soldiers])
    print(f"\n⚔️  COMBAT READINESS:")
    print(f"   Average HP: {avg_hp:.1f}/100")
    print(f"   Average Level: {avg_level:.1f}")

    rank_dist = {}
    for sol in all_soldiers:
        rank_dist[sol[SOL_RANK]] = rank_dist.get(sol[SOL_RANK], 0) + 1

    print(f"\n🏆 RANK DISTRIBUTION:")
    for rank, count in sorted(rank_dist.items(), reverse=True):
        print(f"   {rank}: {count} soldiers {'█' * count}")


# ══════════════════════════════════════════════════════════════════════════════
#  DATABASE LAYER
# ══════════════════════════════════════════════════════════════════════════════

def get_conn(database=None):
    """Return a fresh MySQL connection."""
    return mysql.connector.connect(
        host=DB_HOST, user=DB_USER, password=DB_PASS, database=database
    )


def create_tables(cursor):
    """Create all tables if they don't exist."""
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS captains (
            id       INT AUTO_INCREMENT PRIMARY KEY,
            name     VARCHAR(100) UNIQUE NOT NULL,
            password VARCHAR(100)        NOT NULL
        )
    """)
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS soldiers (
            id       INT AUTO_INCREMENT PRIMARY KEY,
            name     VARCHAR(100) UNIQUE NOT NULL,
            password VARCHAR(100)        NOT NULL,
            hp       INT                 NOT NULL,
            mana     INT                 NOT NULL,
            `rank`   VARCHAR(20)         NOT NULL,
            `level`  INT                 NOT NULL,
            `status` VARCHAR(20)         NOT NULL
        )
    """)
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS weapons (
            id       INT AUTO_INCREMENT PRIMARY KEY,
            category VARCHAR(50)  NOT NULL,
            name     VARCHAR(100) NOT NULL,
            caliber  VARCHAR(60)  NOT NULL,
            qty      INT          NOT NULL
        )
    """)
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS explosives (
            id   INT AUTO_INCREMENT PRIMARY KEY,
            name VARCHAR(100) NOT NULL,
            qty  INT          NOT NULL
        )
    """)
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS ammunition (
            id      INT AUTO_INCREMENT PRIMARY KEY,
            name    VARCHAR(100) NOT NULL,
            qty     INT          NOT NULL,
            `status` VARCHAR(20) NOT NULL
        )
    """)
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS accessories (
            id      INT AUTO_INCREMENT PRIMARY KEY,
            name    VARCHAR(100) NOT NULL,
            qty     INT          NOT NULL,
            `status` VARCHAR(20) NOT NULL
        )
    """)
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS mission_tasks (
            id          INT AUTO_INCREMENT PRIMARY KEY,
            mission_id  VARCHAR(20)  NOT NULL,
            description VARCHAR(200) NOT NULL,
            assigned_to VARCHAR(100) NOT NULL,
            `status`    VARCHAR(30)  NOT NULL,
            priority    VARCHAR(20)  NOT NULL
        )
    """)
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS weapon_orders (
            id      INT AUTO_INCREMENT PRIMARY KEY,
            soldier VARCHAR(100) NOT NULL,
            weapon  VARCHAR(100) NOT NULL,
            qty     INT          NOT NULL,
            `status` VARCHAR(30) NOT NULL
        )
    """)


def insert_all_data(cursor):
    """Pack all in-memory lists into the database (first-run only)."""

    for cap in captains:
        cursor.execute(
            "INSERT INTO captains (name, password) VALUES (%s, %s)",
            (cap[CAP_NAME], cap[CAP_PASS])
        )

    for sol in all_soldiers:
        cursor.execute(
            "INSERT INTO soldiers (name,password,hp,mana,`rank`,`level`,`status`) VALUES (%s,%s,%s,%s,%s,%s,%s)",
            (sol[SOL_NAME], sol[SOL_PASS], sol[SOL_HP], sol[SOL_MANA],
             sol[SOL_RANK], sol[SOL_LEVEL], sol[SOL_STATUS])
        )

    for cat in ORDERABLE_WEAPON_CATS:
        for w in armory[cat]:
            cursor.execute(
                "INSERT INTO weapons (category,name,caliber,qty) VALUES (%s,%s,%s,%s)",
                (cat, w[NAME], w[CALIBER], w[QTY])
            )

    for exp in armory["Explosives"]:
        cursor.execute(
            "INSERT INTO explosives (name,qty) VALUES (%s,%s)",
            (exp[EXP_NAME], exp[EXP_QTY])
        )

    for ammo in armory["Ammunition"]:
        cursor.execute(
            "INSERT INTO ammunition (name,qty,status) VALUES (%s,%s,%s)",
            (ammo[ITEM_NAME], ammo[ITEM_QTY], ammo[ITEM_STATUS])
        )

    for acc in armory["Accessories"]:
        cursor.execute(
            "INSERT INTO accessories (name,qty,status) VALUES (%s,%s,%s)",
            (acc[ITEM_NAME], acc[ITEM_QTY], acc[ITEM_STATUS])
        )

    for task in mission_tasks:
        cursor.execute(
            "INSERT INTO mission_tasks (mission_id,description,assigned_to,`status`,priority) VALUES (%s,%s,%s,%s,%s)",
            (task[M_ID], task[M_DESC], task[M_ASSIGNED], task[M_STATUS], task[M_PRIORITY])
        )


def load_from_db(cursor):
    """Load all data from existing database into in-memory lists."""

    # ── Captains ─────────────────────────────────────────────────────────────
    captains.clear()
    cursor.execute("SELECT name, password FROM captains")
    for row in cursor.fetchall():
        captains.append(list(row))

    # ── Soldiers ─────────────────────────────────────────────────────────────
    all_soldiers.clear()
    s_rank.clear(); a_rank.clear(); b_rank.clear(); c_rank.clear()

    cursor.execute("SELECT name,password,hp,mana,`rank`,`level`,`status` FROM soldiers")
    for row in cursor.fetchall():
        sol = list(row)
        all_soldiers.append(sol)
        if sol[SOL_RANK] in rank_lists:
            rank_lists[sol[SOL_RANK]].append(sol)

    # ── Weapons ──────────────────────────────────────────────────────────────
    for cat in ORDERABLE_WEAPON_CATS:
        armory[cat].clear()

    cursor.execute("SELECT category,name,caliber,qty FROM weapons")
    for row in cursor.fetchall():
        cat, name_, caliber_, qty_ = row
        weapon = [name_, caliber_, qty_]
        if cat in armory:
            armory[cat].append(weapon)
        else:
            armory[cat] = [weapon]

    # ── Explosives ───────────────────────────────────────────────────────────
    armory["Explosives"].clear()
    cursor.execute("SELECT name, qty FROM explosives")
    for row in cursor.fetchall():
        armory["Explosives"].append(list(row))

    # ── Ammunition ───────────────────────────────────────────────────────────
    armory["Ammunition"].clear()
    cursor.execute("SELECT name, qty, status FROM ammunition")
    for row in cursor.fetchall():
        armory["Ammunition"].append(list(row))

    # ── Accessories ──────────────────────────────────────────────────────────
    armory["Accessories"].clear()
    cursor.execute("SELECT name, qty, status FROM accessories")
    for row in cursor.fetchall():
        armory["Accessories"].append(list(row))

    # ── Mission Tasks ─────────────────────────────────────────────────────────
    mission_tasks.clear()
    cursor.execute("SELECT mission_id,description,assigned_to,status,priority FROM mission_tasks")
    for row in cursor.fetchall():
        mission_tasks.append(list(row))

    # ── Weapon Orders ─────────────────────────────────────────────────────────
    weapon_orders.clear()
    cursor.execute("SELECT soldier,weapon,qty,status FROM weapon_orders")
    for row in cursor.fetchall():
        weapon_orders.append(list(row))


def setup_database():
    """
    Entry point for DB setup.
    - DB missing  → create it, create tables, pack all lists into it.
    - DB exists   → connect and load existing data into lists.
    """
    print("\n⚙️  Connecting to Shadow Database...")

    # Connect without selecting a DB first so we can check existence
    conn   = get_conn()
    cursor = conn.cursor()

    cursor.execute("SHOW DATABASES LIKE %s", (DB_NAME,))
    db_found = cursor.fetchone()

    if not db_found:
        cursor.execute(f"CREATE DATABASE {DB_NAME}")

    cursor.execute(f"USE {DB_NAME}")

    # Check if tables exist (covers partial-creation from a previous failed run)
    cursor.execute("SHOW TABLES LIKE 'soldiers'")
    tables_ready = cursor.fetchone()

    if not tables_ready:
        print(f"   📦 Tables missing — creating and packing data...")
        create_tables(cursor)
        insert_all_data(cursor)
        conn.commit()
        print(f"   ✅ Database '{DB_NAME}' ready and all data packed!")
    else:
        print(f"   ✅ '{DB_NAME}' found — loading existing data...")
        load_from_db(cursor)
        print(f"   ✅ Data loaded from '{DB_NAME}'!")

    cursor.close()
    conn.close()


# ── DB SYNC HELPERS  (called by add_* functions after updating in-memory lists)
def db_insert_soldier(sol):
    conn   = get_conn(DB_NAME)
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO soldiers (name,password,hp,mana,`rank`,`level`,`status`) VALUES (%s,%s,%s,%s,%s,%s,%s)",
        (sol[SOL_NAME], sol[SOL_PASS], sol[SOL_HP], sol[SOL_MANA],
         sol[SOL_RANK], sol[SOL_LEVEL], sol[SOL_STATUS])
    )
    conn.commit(); cursor.close(); conn.close()

def db_update_soldier(sol):
    conn   = get_conn(DB_NAME)
    cursor = conn.cursor()
    cursor.execute(
        "UPDATE soldiers SET hp=%s, mana=%s, `status`=%s WHERE name=%s",
        (sol[SOL_HP], sol[SOL_MANA], sol[SOL_STATUS], sol[SOL_NAME])
    )
    conn.commit(); cursor.close(); conn.close()

def db_insert_weapon(category, w):
    conn   = get_conn(DB_NAME)
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO weapons (category,name,caliber,qty) VALUES (%s,%s,%s,%s)",
        (category, w[NAME], w[CALIBER], w[QTY])
    )
    conn.commit(); cursor.close(); conn.close()

def db_insert_ammo(ammo):
    conn   = get_conn(DB_NAME)
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO ammunition (name,qty,status) VALUES (%s,%s,%s)",
        (ammo[ITEM_NAME], ammo[ITEM_QTY], ammo[ITEM_STATUS])
    )
    conn.commit(); cursor.close(); conn.close()

def db_insert_accessory(acc):
    conn   = get_conn(DB_NAME)
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO accessories (name,qty,status) VALUES (%s,%s,%s)",
        (acc[ITEM_NAME], acc[ITEM_QTY], acc[ITEM_STATUS])
    )
    conn.commit(); cursor.close(); conn.close()

def db_insert_mission(task):
    conn   = get_conn(DB_NAME)
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO mission_tasks (mission_id,description,assigned_to,`status`,priority) VALUES (%s,%s,%s,%s,%s)",
        (task[M_ID], task[M_DESC], task[M_ASSIGNED], task[M_STATUS], task[M_PRIORITY])
    )
    conn.commit(); cursor.close(); conn.close()

def db_update_mission(task):
    conn   = get_conn(DB_NAME)
    cursor = conn.cursor()
    cursor.execute(
        "UPDATE mission_tasks SET `status`=%s WHERE mission_id=%s",
        (task[M_STATUS], task[M_ID])
    )
    conn.commit(); cursor.close(); conn.close()

def db_insert_order(order):
    conn   = get_conn(DB_NAME)
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO weapon_orders (soldier,weapon,qty,`status`) VALUES (%s,%s,%s,%s)",
        (order[O_SOLDIER], order[O_WEAPON], order[O_QTY], order[O_STATUS])
    )
    conn.commit(); cursor.close(); conn.close()

def db_update_order(order):
    conn   = get_conn(DB_NAME)
    cursor = conn.cursor()
    cursor.execute(
        "UPDATE weapon_orders SET `status`=%s WHERE soldier=%s AND weapon=%s AND qty=%s",
        (order[O_STATUS], order[O_SOLDIER], order[O_WEAPON], order[O_QTY])
    )
    conn.commit(); cursor.close(); conn.close()


# ══════════════════════════════════════════════════════════════════════════════
#  MAIN LOOP
# ══════════════════════════════════════════════════════════════════════════════
def main():
    setup_database()

    print("\n" + "="*80)
    print("🗡️  SHADOW MILITARY PROTOCOL INITIALIZED")
    print("="*80)
    print("\n💀 'Arise, Shadows of the Fallen...'")
    print("🌟 Solo Leveling Military Management System v2.0")
    print("="*80)

    while True:
        stithi, role, username = auth()

        if stithi:
            if role == "cap":
                print(f"\n{'═'*80}")
                print(f"👑 MONARCH {username} HAS ENTERED THE THRONE ROOM")
                print(f"{'═'*80}")
                captain_menu(username)
            elif role == "sol":
                print(f"\n{'═'*80}")
                print(f"⚔️  SHADOW SOLDIER {username} REPORTING FOR DUTY")
                print(f"{'═'*80}")
                soldier_menu(username)
        else:
            print("\n❌ AUTHENTICATION FAILED - ACCESS DENIED")
            print("🚫 System Lockdown Initiated...")
            break

        continue_choice = input("\n🔄 Return to main menu? (yes/no): ").lower()
        if continue_choice != "yes":
            print("\n🌙 Shadow Protocol Deactivating...")
            print("💀 'The shadows return to slumber...'")
            break

if __name__ == "__main__":
    main()
```

# EXECUTION & OUTPUT DOCUMENTATION
### Output 1: System Initialization & Database Handshake

```python
================================================================================
🗡️  INITIALIZING SHADOW MILITARY PROTOCOL  🗡️
================================================================================

⚙️  Connecting to Shadow Database...
   📦 Tables missing — creating and packing data...
   ✅ Database 'shadow_army_db' ready and all data packed!

================================================================================
🗡️  SHADOW MILITARY PROTOCOL INITIALIZED
================================================================================

💀 'Arise, Shadows of the Fallen...'
🌟 Solo Leveling Military Management System v2.0
================================================================================
```
Above it created the database when it couldn't find it.
```python
================================================================================
🗡️  INITIALIZING SHADOW MILITARY PROTOCOL  🗡️
================================================================================

⚙️  Connecting to Shadow Database...
   ✅ 'shadow_army_db' found — loading existing data...
   ✅ Data loaded from 'shadow_army_db'!

================================================================================
🗡️  SHADOW MILITARY PROTOCOL INITIALIZED
================================================================================

💀 'Arise, Shadows of the Fallen...'
🌟 Solo Leveling Military Management System 
================================================================================
```
Here it found the database and successfully loaded it.
### Output 2: Identity Verification System (`auth()`)

```python
────────────────────────────────────────────────────────────────────────────────
🔐 IDENTITY VERIFICATION REQUIRED
────────────────────────────────────────────────────────────────────────────────

👤 Hunter Name:  Pranav
🔑 Access Code:  ········

❌ Unknown Hunter

────────────────────────────────────────────────────────────────────────────────
🔐 IDENTITY VERIFICATION REQUIRED
────────────────────────────────────────────────────────────────────────────────

👤 Hunter Name:  Anmol
🔑 Access Code:  ········

❌ Unknown Hunter

────────────────────────────────────────────────────────────────────────────────
🔐 IDENTITY VERIFICATION REQUIRED
────────────────────────────────────────────────────────────────────────────────

👤 Hunter Name:  Advaya
🔑 Access Code:  ········

❌ Unknown Hunter

❌ AUTHENTICATION FAILED - ACCESS DENIED
🚫 System Lockdown Initiated...
```
Unauthorised users are blocked and system goes into lockdown after 3 unsuccessful tries
```python
────────────────────────────────────────────────────────────────────────────────
🔐 IDENTITY VERIFICATION REQUIRED
────────────────────────────────────────────────────────────────────────────────

👤 Hunter Name:  Yuvraj Hyperion
🔑 Access Code:  ········

✅ MONARCH ACCESS GRANTED
🌟 Welcome, Supreme Commander Yuvraj Hyperion!

════════════════════════════════════════════════════════════════════════════════
👑 MONARCH Yuvraj Hyperion HAS ENTERED THE THRONE ROOM
════════════════════════════════════════════════════════════════════════════════
```
Verified users are allowed.
### Output 3: Monarch Command Center (`captain_menu()`)
```python
⚙️  Connecting to Shadow Database...
   ✅ 'shadow_army_db' found — loading existing data...
   ✅ Data loaded from 'shadow_army_db'!

================================================================================
🗡️  SHADOW MILITARY PROTOCOL INITIALIZED
================================================================================

💀 'Arise, Shadows of the Fallen...'
🌟 Solo Leveling Military Management System 
================================================================================

────────────────────────────────────────────────────────────────────────────────
🔐 IDENTITY VERIFICATION REQUIRED
────────────────────────────────────────────────────────────────────────────────

👤 Hunter Name:  Yuvraj Hyperion
🔑 Access Code:  ········

✅ MONARCH ACCESS GRANTED
🌟 Welcome, Supreme Commander Yuvraj Hyperion!

════════════════════════════════════════════════════════════════════════════════
👑 MONARCH Yuvraj Hyperion HAS ENTERED THE THRONE ROOM
════════════════════════════════════════════════════════════════════════════════

════════════════════════════════════════════════════════════════════════════════
👑 MONARCH COMMAND CENTER - Yuvraj Hyperion
════════════════════════════════════════════════════════════════════════════════
1. 📦 Order Inventory Supplies
2. ✅ Approve Soldier Weapon Orders
3. ❤️  Check All Soldiers' Health Status
4. 📋 Add New Missions
5. 🗡️  Add New Weapons to Armory
6. 👥 Add New Recruits
7. 📊 View Complete Arsenal
8. 🎯 View All Missions
9. 📈 View System Statistics
10. 🚪 Logout
────────────────────────────────────────────────────────────────────────────────

Select Command:  1

════════════════════════════════════════════════════════════════════════════════
📦 INVENTORY SUPPLY ORDER SYSTEM
════════════════════════════════════════════════════════════════════════════════

📌 Ammunition:
   1. 5.56×45mm rounds: 50000 units — Available
   2. 7.62×39mm rounds: 40000 units — Available
   3. 7.62×51mm rounds: 30000 units — Available
   4. 7.62×54mmR rounds: 25000 units — Low Stock
   5. 9×19mm pistol ammo: 60000 units — Available
   6. .50 BMG ammo: 5000 units — Low Stock
   7. .338 Lapua: 3000 units — Available
   8. 12-gauge shells: 15000 units — Available

📌 Accessories:
   1. Rifle magazines: 500 units — Available
   2. Pistol magazines: 300 units — Available
   3. ACOG Scopes: 50 units — Low Stock
   4. Red Dot Sights: 80 units — Available
   5. Tactical Lights: 100 units — Available
   6. Suppressors: 30 units — Low Stock

🆕 Place New Order:

Item Name:  Gun
Quantity:  20
Category (Ammunition/Accessories):  Pistol

❌ Invalid category!

════════════════════════════════════════════════════════════════════════════════
👑 MONARCH COMMAND CENTER - Yuvraj Hyperion
════════════════════════════════════════════════════════════════════════════════
1. 📦 Order Inventory Supplies
2. ✅ Approve Soldier Weapon Orders
3. ❤️  Check All Soldiers' Health Status
4. 📋 Add New Missions
5. 🗡️  Add New Weapons to Armory
6. 👥 Add New Recruits
7. 📊 View Complete Arsenal
8. 🎯 View All Missions
9. 📈 View System Statistics
10. 🚪 Logout
────────────────────────────────────────────────────────────────────────────────

Select Command:  1

════════════════════════════════════════════════════════════════════════════════
📦 INVENTORY SUPPLY ORDER SYSTEM
════════════════════════════════════════════════════════════════════════════════

📌 Ammunition:
   1. 5.56×45mm rounds: 50000 units — Available
   2. 7.62×39mm rounds: 40000 units — Available
   3. 7.62×51mm rounds: 30000 units — Available
   4. 7.62×54mmR rounds: 25000 units — Low Stock
   5. 9×19mm pistol ammo: 60000 units — Available
   6. .50 BMG ammo: 5000 units — Low Stock
   7. .338 Lapua: 3000 units — Available
   8. 12-gauge shells: 15000 units — Available

📌 Accessories:
   1. Rifle magazines: 500 units — Available
   2. Pistol magazines: 300 units — Available
   3. ACOG Scopes: 50 units — Low Stock
   4. Red Dot Sights: 80 units — Available
   5. Tactical Lights: 100 units — Available
   6. Suppressors: 30 units — Low Stock

🆕 Place New Order:

Item Name:  Pistol
Quantity:  10
Category (Ammunition/Accessories):  Ammunition

✅ Order placed: Pistol x10

════════════════════════════════════════════════════════════════════════════════
👑 MONARCH COMMAND CENTER - Yuvraj Hyperion
════════════════════════════════════════════════════════════════════════════════
1. 📦 Order Inventory Supplies
2. ✅ Approve Soldier Weapon Orders
3. ❤️  Check All Soldiers' Health Status
4. 📋 Add New Missions
5. 🗡️  Add New Weapons to Armory
6. 👥 Add New Recruits
7. 📊 View Complete Arsenal
8. 🎯 View All Missions
9. 📈 View System Statistics
10. 🚪 Logout
────────────────────────────────────────────────────────────────────────────────

Select Command:  2

════════════════════════════════════════════════════════════════════════════════
✅ WEAPON ORDER APPROVAL SYSTEM
════════════════════════════════════════════════════════════════════════════════

📭 No pending weapon orders.

════════════════════════════════════════════════════════════════════════════════
👑 MONARCH COMMAND CENTER - Yuvraj Hyperion
════════════════════════════════════════════════════════════════════════════════
1. 📦 Order Inventory Supplies
2. ✅ Approve Soldier Weapon Orders
3. ❤️  Check All Soldiers' Health Status
4. 📋 Add New Missions
5. 🗡️  Add New Weapons to Armory
6. 👥 Add New Recruits
7. 📊 View Complete Arsenal
8. 🎯 View All Missions
9. 📈 View System Statistics
10. 🚪 Logout
────────────────────────────────────────────────────────────────────────────────

Select Command:  3

════════════════════════════════════════════════════════════════════════════════
❤️  SHADOW ARMY HEALTH STATUS
════════════════════════════════════════════════════════════════════════════════

🩹 INJURED:
   ⚠️  Bhairav Singh Orion: HP 88/100, Mana 85/100, A-Rank Lv.35
   ⚠️  Shatrughan Devdroid: HP 78/100, Mana 75/100, C-Rank Lv.20

🏥 RECOVERING:
   💊 Mahaveer Rajat Prime: HP 85/100, Mana 80/100, C-Rank Lv.22
   💊 Dhananjay Kulkarni Titan: HP 82/100, Mana 78/100, C-Rank Lv.25

✅ ACTIVE DUTY:
   ⚔️  Vikrant Senapati X9: HP 100/100, Mana 100/100, S-Rank Lv.45
   ⚔️  Rudra Pratap Nova: HP 95/100, Mana 90/100, A-Rank Lv.38
   ⚔️  Agniveer Kaaltron: HP 100/100, Mana 95/100, B-Rank Lv.28
   ⚔️  Arindham Varmax: HP 92/100, Mana 88/100, B-Rank Lv.30
   ⚔️  Samrat Veerbhadra 7: HP 100/100, Mana 100/100, S-Rank Lv.42
   ⚔️  Trikand Arjun Nexus: HP 90/100, Mana 92/100, A-Rank Lv.36
   ⚔️  Garudnath Keshari X: HP 100/100, Mana 98/100, S-Rank Lv.48
   ⚔️  Vajrahan Bhupendra Omega: HP 88/100, Mana 85/100, B-Rank Lv.29
   ⚔️  Nirbhay Karunesh Flux: HP 95/100, Mana 90/100, A-Rank Lv.40
   ⚔️  Shivraaj Deshmukh Vortex: HP 100/100, Mana 100/100, S-Rank Lv.50
   ⚔️  Kaalnemi Pradhan Pulse: HP 90/100, Mana 88/100, B-Rank Lv.32

════════════════════════════════════════════════════════════════════════════════
👑 MONARCH COMMAND CENTER - Yuvraj Hyperion
════════════════════════════════════════════════════════════════════════════════
1. 📦 Order Inventory Supplies
2. ✅ Approve Soldier Weapon Orders
3. ❤️  Check All Soldiers' Health Status
4. 📋 Add New Missions
5. 🗡️  Add New Weapons to Armory
6. 👥 Add New Recruits
7. 📊 View Complete Arsenal
8. 🎯 View All Missions
9. 📈 View System Statistics
10. 🚪 Logout
────────────────────────────────────────────────────────────────────────────────

Select Command:  4

════════════════════════════════════════════════════════════════════════════════
📋 MISSION CREATION SYSTEM
════════════════════════════════════════════════════════════════════════════════

📝 Mission Description:  Docmentation of python

👥 Available Soldiers:
   0. All Soldiers
   1. Vikrant Senapati X9 (S-Rank) — Active
   2. Rudra Pratap Nova (A-Rank) — Active
   3. Bhairav Singh Orion (A-Rank) — Injured
   4. Agniveer Kaaltron (B-Rank) — Active
   5. Arindham Varmax (B-Rank) — Active
   6. Mahaveer Rajat Prime (C-Rank) — Recovering
   7. Samrat Veerbhadra 7 (S-Rank) — Active
   8. Shatrughan Devdroid (C-Rank) — Injured
   9. Trikand Arjun Nexus (A-Rank) — Active
   10. Garudnath Keshari X (S-Rank) — Active
   11. Vajrahan Bhupendra Omega (B-Rank) — Active
   12. Nirbhay Karunesh Flux (A-Rank) — Active
   13. Dhananjay Kulkarni Titan (C-Rank) — Recovering
   14. Shivraaj Deshmukh Vortex (S-Rank) — Active
   15. Kaalnemi Pradhan Pulse (B-Rank) — Active

🎯 Assign to (number):  0

⭐ Priority Levels: S-Rank, A-Rank, B-Rank, C-Rank, D-Rank

Priority:  S-Rank

✅ Mission QUEST-006 created successfully!
   Assigned to: All Soldiers
   Priority: S-Rank

════════════════════════════════════════════════════════════════════════════════
👑 MONARCH COMMAND CENTER - Yuvraj Hyperion
════════════════════════════════════════════════════════════════════════════════
1. 📦 Order Inventory Supplies
2. ✅ Approve Soldier Weapon Orders
3. ❤️  Check All Soldiers' Health Status
4. 📋 Add New Missions
5. 🗡️  Add New Weapons to Armory
6. 👥 Add New Recruits
7. 📊 View Complete Arsenal
8. 🎯 View All Missions
9. 📈 View System Statistics
10. 🚪 Logout
────────────────────────────────────────────────────────────────────────────────

Select Command:  5

════════════════════════════════════════════════════════════════════════════════
🗡️  ARMORY EXPANSION SYSTEM
════════════════════════════════════════════════════════════════════════════════

📦 Weapon Categories:
1. Assault Rifles
2. Battle Rifles
3. Light Machine Guns
4. Sniper Rifles
5. Pistols
6. Shotguns
7. SMGs

🎯 Select Category (or 0 for new category):  4
Weapon Name:  Snipe
Caliber/Ammo Type:  Propreitary
Quantity:  1

✅ Snipe (Propreitary) x1 added to Sniper_Rifles!

════════════════════════════════════════════════════════════════════════════════
👑 MONARCH COMMAND CENTER - Yuvraj Hyperion
════════════════════════════════════════════════════════════════════════════════
1. 📦 Order Inventory Supplies
2. ✅ Approve Soldier Weapon Orders
3. ❤️  Check All Soldiers' Health Status
4. 📋 Add New Missions
5. 🗡️  Add New Weapons to Armory
6. 👥 Add New Recruits
7. 📊 View Complete Arsenal
8. 🎯 View All Missions
9. 📈 View System Statistics
10. 🚪 Logout
────────────────────────────────────────────────────────────────────────────────

Select Command:  6

════════════════════════════════════════════════════════════════════════════════
👥 RECRUITMENT SYSTEM - SHADOW AWAKENING
════════════════════════════════════════════════════════════════════════════════

📝 Recruit Name:  Prax Prix
🔑 Set Password:  Prix_Prax

⭐ Rank Assignment: S-Rank, A-Rank, B-Rank, C-Rank, D-Rank, E-Rank

Initial Rank:  S-Rank
Initial Level (1-50):  50

🎉 Prax Prix has been awakened as a Shadow Soldier!
   Rank: S-Rank
   Level: 50
   Status: Active

════════════════════════════════════════════════════════════════════════════════
👑 MONARCH COMMAND CENTER - Yuvraj Hyperion
════════════════════════════════════════════════════════════════════════════════
1. 📦 Order Inventory Supplies
2. ✅ Approve Soldier Weapon Orders
3. ❤️  Check All Soldiers' Health Status
4. 📋 Add New Missions
5. 🗡️  Add New Weapons to Armory
6. 👥 Add New Recruits
7. 📊 View Complete Arsenal
8. 🎯 View All Missions
9. 📈 View System Statistics
10. 🚪 Logout
────────────────────────────────────────────────────────────────────────────────

Select Command:  7

════════════════════════════════════════════════════════════════════════════════
🗡️  COMPLETE ARSENAL DATABASE
════════════════════════════════════════════════════════════════════════════════

════════════════════════════════════════════════════════════
🔹 ASSAULT RIFLES
════════════════════════════════════════════════════════════
   • AK-47 — 7.62×39mm  (Stock: 120)
   • AK-103 — 7.62×39mm  (Stock: 85)
   • INSAS Rifle — 5.56×45mm  (Stock: 200)
   • Tavor TAR-21 — 5.56×45mm  (Stock: 60)
   • M4 Carbine — 5.56×45mm  (Stock: 150)
   • SIG716 — 7.62×51mm  (Stock: 45)
   • HK416 — 5.56×45mm  (Stock: 70)

════════════════════════════════════════════════════════════
🔹 BATTLE RIFLES
════════════════════════════════════════════════════════════
   • FN FAL — 7.62×51mm  (Stock: 40)
   • SCAR-H — 7.62×51mm  (Stock: 35)

════════════════════════════════════════════════════════════
🔹 LIGHT MACHINE GUNS
════════════════════════════════════════════════════════════
   • PKM — 7.62×54mmR  (Stock: 25)
   • Negev NG7 — 7.62×51mm  (Stock: 20)
   • M249 SAW — 5.56×45mm  (Stock: 30)

════════════════════════════════════════════════════════════
🔹 SNIPER RIFLES
════════════════════════════════════════════════════════════
   • Dragunov SVD — 7.62×54mmR  (Stock: 18)
   • Barrett M82 — .50 BMG  (Stock: 10)
   • AWM — .300 Win Mag / .338 Lapua  (Stock: 8)
   • Mk 12 SPR — 5.56×45mm  (Stock: 15)
   • Snipe — Propreitary  (Stock: 1)

════════════════════════════════════════════════════════════
🔹 PISTOLS
════════════════════════════════════════════════════════════
   • Glock 17 — 9×19mm  (Stock: 250)
   • SIG P226 — 9×19mm  (Stock: 180)
   • Beretta M9 — 9×19mm  (Stock: 200)
   • HS2000 — 9×19mm  (Stock: 90)
   • MP-443 Grach — 9×19mm  (Stock: 110)

════════════════════════════════════════════════════════════
🔹 SHOTGUNS
════════════════════════════════════════════════════════════
   • Benelli M4 — 12-gauge shells  (Stock: 35)
   • Remington 870 — 12-gauge shells  (Stock: 40)

════════════════════════════════════════════════════════════
🔹 SMGS
════════════════════════════════════════════════════════════
   • MP5 — 9×19mm  (Stock: 75)
   • Uzi — 9×19mm  (Stock: 55)
   • CZ Scorpion EVO — 9×19mm  (Stock: 50)

════════════════════════════════════════════════════════════
🔹 EXPLOSIVES
════════════════════════════════════════════════════════════
   • Hand Grenade (HE36 / M67)  (Stock: 300)
   • Smoke Grenade  (Stock: 200)
   • Flashbang  (Stock: 150)

════════════════════════════════════════════════════════════════════════════════
👑 MONARCH COMMAND CENTER - Yuvraj Hyperion
════════════════════════════════════════════════════════════════════════════════
1. 📦 Order Inventory Supplies
2. ✅ Approve Soldier Weapon Orders
3. ❤️  Check All Soldiers' Health Status
4. 📋 Add New Missions
5. 🗡️  Add New Weapons to Armory
6. 👥 Add New Recruits
7. 📊 View Complete Arsenal
8. 🎯 View All Missions
9. 📈 View System Statistics
10. 🚪 Logout
────────────────────────────────────────────────────────────────────────────────

Select Command:  8

════════════════════════════════════════════════════════════════════════════════
🎯 MISSION DATABASE
════════════════════════════════════════════════════════════════════════════════

────────────────────────────────────────────────────────────
📊 STATUS: In Progress
────────────────────────────────────────────────────────────

   🎯 QUEST-001: Secure Northern Border
      Assigned: Vikrant Senapati X9
      Priority: S-Rank

   🎯 QUEST-005: Night Patrol Duty
      Assigned: Nirbhay Karunesh Flux
      Priority: A-Rank

────────────────────────────────────────────────────────────
📊 STATUS: Pending
────────────────────────────────────────────────────────────

   🎯 QUEST-002: Weapons Training Exercise
      Assigned: All Soldiers
      Priority: B-Rank

   🎯 QUEST-004: Equipment Maintenance
      Assigned: Agniveer Kaaltron
      Priority: C-Rank

   🎯 QUEST-006: Docmentation of python
      Assigned: All Soldiers
      Priority: S-Rank

────────────────────────────────────────────────────────────
📊 STATUS: Completed
────────────────────────────────────────────────────────────

   🎯 QUEST-003: Recon Mission - Sector 7
      Assigned: Garudnath Keshari X
      Priority: A-Rank

════════════════════════════════════════════════════════════════════════════════
👑 MONARCH COMMAND CENTER - Yuvraj Hyperion
════════════════════════════════════════════════════════════════════════════════
1. 📦 Order Inventory Supplies
2. ✅ Approve Soldier Weapon Orders
3. ❤️  Check All Soldiers' Health Status
4. 📋 Add New Missions
5. 🗡️  Add New Weapons to Armory
6. 👥 Add New Recruits
7. 📊 View Complete Arsenal
8. 🎯 View All Missions
9. 📈 View System Statistics
10. 🚪 Logout
────────────────────────────────────────────────────────────────────────────────

Select Command:  9

════════════════════════════════════════════════════════════════════════════════
📈 SYSTEM ANALYTICS DASHBOARD
════════════════════════════════════════════════════════════════════════════════

👥 PERSONNEL:
   Total Captains: 5
   Total Soldiers: 16
   Active: 12
   Injured/Recovering: 4

🎯 MISSIONS:
   Total Missions: 6
   Completed: 1 (16.7%)
   Pending: 3

📦 LOGISTICS:
   Pending Weapon Orders: 0
   Inventory Categories: 2

⚔️  COMBAT READINESS:
   Average HP: 92.7/100
   Average Level: 35.6

🏆 RANK DISTRIBUTION:
   S-Rank: 5 soldiers █████
   C-Rank: 3 soldiers ███
   B-Rank: 4 soldiers ████
   A-Rank: 4 soldiers ████

════════════════════════════════════════════════════════════════════════════════
👑 MONARCH COMMAND CENTER - Yuvraj Hyperion
════════════════════════════════════════════════════════════════════════════════
1. 📦 Order Inventory Supplies
2. ✅ Approve Soldier Weapon Orders
3. ❤️  Check All Soldiers' Health Status
4. 📋 Add New Missions
5. 🗡️  Add New Weapons to Armory
6. 👥 Add New Recruits
7. 📊 View Complete Arsenal
8. 🎯 View All Missions
9. 📈 View System Statistics
10. 🚪 Logout
────────────────────────────────────────────────────────────────────────────────

Select Command:  10

👑 Monarch disconnecting... Farewell!

🔄 Return to main menu? (yes/no):  no

🌙 Shadow Protocol Deactivating...
💀 'The shadows return to slumber...'
```
All captain features.
### Output 4: Armory Inventory & Requisition Approval (`approve_weapon_orders()`)
Here our newly added recruit got his first weapon order approved but second one disapproved
```python
================================================================================
🗡️  INITIALIZING SHADOW MILITARY PROTOCOL  🗡️
================================================================================

⚙️  Connecting to Shadow Database...
   ✅ 'shadow_army_db' found — loading existing data...
   ✅ Data loaded from 'shadow_army_db'!

================================================================================
🗡️  SHADOW MILITARY PROTOCOL INITIALIZED
================================================================================

💀 'Arise, Shadows of the Fallen...'
🌟 Solo Leveling Military Management System 
================================================================================

────────────────────────────────────────────────────────────────────────────────
🔐 IDENTITY VERIFICATION REQUIRED
────────────────────────────────────────────────────────────────────────────────

👤 Hunter Name:  Prax Prix
🔑 Access Code:  ········

✅ SHADOW SOLDIER ACCESS GRANTED
⚔️  Welcome back, Warrior Prax Prix!

════════════════════════════════════════════════════════════════════════════════
⚔️  SHADOW SOLDIER Prax Prix REPORTING FOR DUTY
════════════════════════════════════════════════════════════════════════════════

════════════════════════════════════════════════════════════════════════════════
⚔️  SHADOW SOLDIER OPERATIONS - Prax Prix
════════════════════════════════════════════════════════════════════════════════
1. 🗡️  Order Weapons
2. ❤️  Update Health Status
3. 📋 View Assigned Missions
4. ✅ Update Completed Missions
5. 📊 View My Stats
6. 📦 View My Weapon Orders
7. 🚪 Logout
────────────────────────────────────────────────────────────────────────────────

Select Operation:  1

════════════════════════════════════════════════════════════
🗡️  WEAPON REQUISITION SYSTEM
════════════════════════════════════════════════════════════

📦 AVAILABLE ARSENAL:

🔹 Assault Rifles:
  1. AK-47 (7.62×39mm) — Stock: 120
  2. AK-103 (7.62×39mm) — Stock: 85
  3. INSAS Rifle (5.56×45mm) — Stock: 200
  4. Tavor TAR-21 (5.56×45mm) — Stock: 60
  5. M4 Carbine (5.56×45mm) — Stock: 150
  6. SIG716 (7.62×51mm) — Stock: 45
  7. HK416 (5.56×45mm) — Stock: 70

🔹 Battle Rifles:
  8. FN FAL (7.62×51mm) — Stock: 40
  9. SCAR-H (7.62×51mm) — Stock: 35

🔹 Light Machine Guns:
  10. PKM (7.62×54mmR) — Stock: 25
  11. Negev NG7 (7.62×51mm) — Stock: 20
  12. M249 SAW (5.56×45mm) — Stock: 30

🔹 Sniper Rifles:
  13. Dragunov SVD (7.62×54mmR) — Stock: 18
  14. Barrett M82 (.50 BMG) — Stock: 10
  15. AWM (.300 Win Mag / .338 Lapua) — Stock: 8
  16. Mk 12 SPR (5.56×45mm) — Stock: 15
  17. Snipe (Propreitary) — Stock: 1

🔹 Pistols:
  18. Glock 17 (9×19mm) — Stock: 250
  19. SIG P226 (9×19mm) — Stock: 180
  20. Beretta M9 (9×19mm) — Stock: 200
  21. HS2000 (9×19mm) — Stock: 90
  22. MP-443 Grach (9×19mm) — Stock: 110

🔹 Shotguns:
  23. Benelli M4 (12-gauge shells) — Stock: 35
  24. Remington 870 (12-gauge shells) — Stock: 40

🔹 SMGs:
  25. MP5 (9×19mm) — Stock: 75
  26. Uzi (9×19mm) — Stock: 55
  27. CZ Scorpion EVO (9×19mm) — Stock: 50

🎯 Select Weapon Number:  26
📊 Quantity:  5

✅ Order placed! Uzi x5 - Awaiting Captain's approval

════════════════════════════════════════════════════════════════════════════════
⚔️  SHADOW SOLDIER OPERATIONS - Prax Prix
════════════════════════════════════════════════════════════════════════════════
1. 🗡️  Order Weapons
2. ❤️  Update Health Status
3. 📋 View Assigned Missions
4. ✅ Update Completed Missions
5. 📊 View My Stats
6. 📦 View My Weapon Orders
7. 🚪 Logout
────────────────────────────────────────────────────────────────────────────────

Select Operation:  7

🌙 Shadow returning to rest... Goodbye!

🔄 Return to main menu? (yes/no):  yes

────────────────────────────────────────────────────────────────────────────────
🔐 IDENTITY VERIFICATION REQUIRED
────────────────────────────────────────────────────────────────────────────────

👤 Hunter Name:  Yuvraj Hyperion
🔑 Access Code:  ········

✅ MONARCH ACCESS GRANTED
🌟 Welcome, Supreme Commander Yuvraj Hyperion!

════════════════════════════════════════════════════════════════════════════════
👑 MONARCH Yuvraj Hyperion HAS ENTERED THE THRONE ROOM
════════════════════════════════════════════════════════════════════════════════

════════════════════════════════════════════════════════════════════════════════
👑 MONARCH COMMAND CENTER - Yuvraj Hyperion
════════════════════════════════════════════════════════════════════════════════
1. 📦 Order Inventory Supplies
2. ✅ Approve Soldier Weapon Orders
3. ❤️  Check All Soldiers' Health Status
4. 📋 Add New Missions
5. 🗡️  Add New Weapons to Armory
6. 👥 Add New Recruits
7. 📊 View Complete Arsenal
8. 🎯 View All Missions
9. 📈 View System Statistics
10. 🚪 Logout
────────────────────────────────────────────────────────────────────────────────

Select Command:  2

════════════════════════════════════════════════════════════════════════════════
✅ WEAPON ORDER APPROVAL SYSTEM
════════════════════════════════════════════════════════════════════════════════

📋 Pending Orders:
1. Prax Prix — Uzi x5 (Pending Approval)

🎯 Select order to approve (0 to cancel):  1

📋 Order Details:
   Soldier: Prax Prix
   Weapon:  Uzi
   Quantity:5

✅ Approve? (yes/no):  yes

🎉 Order APPROVED!

════════════════════════════════════════════════════════════════════════════════
👑 MONARCH COMMAND CENTER - Yuvraj Hyperion
════════════════════════════════════════════════════════════════════════════════
1. 📦 Order Inventory Supplies
2. ✅ Approve Soldier Weapon Orders
3. ❤️  Check All Soldiers' Health Status
4. 📋 Add New Missions
5. 🗡️  Add New Weapons to Armory
6. 👥 Add New Recruits
7. 📊 View Complete Arsenal
8. 🎯 View All Missions
9. 📈 View System Statistics
10. 🚪 Logout
────────────────────────────────────────────────────────────────────────────────

Select Command:  10

👑 Monarch disconnecting... Farewell!

🔄 Return to main menu? (yes/no):  yes

────────────────────────────────────────────────────────────────────────────────
🔐 IDENTITY VERIFICATION REQUIRED
────────────────────────────────────────────────────────────────────────────────

👤 Hunter Name:  Prax Prix
🔑 Access Code:  ········

✅ SHADOW SOLDIER ACCESS GRANTED
⚔️  Welcome back, Warrior Prax Prix!

════════════════════════════════════════════════════════════════════════════════
⚔️  SHADOW SOLDIER Prax Prix REPORTING FOR DUTY
════════════════════════════════════════════════════════════════════════════════

════════════════════════════════════════════════════════════════════════════════
⚔️  SHADOW SOLDIER OPERATIONS - Prax Prix
════════════════════════════════════════════════════════════════════════════════
1. 🗡️  Order Weapons
2. ❤️  Update Health Status
3. 📋 View Assigned Missions
4. ✅ Update Completed Missions
5. 📊 View My Stats
6. 📦 View My Weapon Orders
7. 🚪 Logout
────────────────────────────────────────────────────────────────────────────────

Select Operation:  6

════════════════════════════════════════════════════════════════════════════════
📦 WEAPON ORDERS — Prax Prix
════════════════════════════════════════════════════════════════════════════════

1. ✅ Uzi x5
      Status: Approved

════════════════════════════════════════════════════════════════════════════════
⚔️  SHADOW SOLDIER OPERATIONS - Prax Prix
════════════════════════════════════════════════════════════════════════════════
1. 🗡️  Order Weapons
2. ❤️  Update Health Status
3. 📋 View Assigned Missions
4. ✅ Update Completed Missions
5. 📊 View My Stats
6. 📦 View My Weapon Orders
7. 🚪 Logout
────────────────────────────────────────────────────────────────────────────────

Select Operation:  7

🌙 Shadow returning to rest... Goodbye!

🔄 Return to main menu? (yes/no): yes

────────────────────────────────────────────────────────────────────────────────
🔐 IDENTITY VERIFICATION REQUIRED
────────────────────────────────────────────────────────────────────────────────

👤 Hunter Name:  Prix Prax
🔑 Access Code:  ········

❌ Unknown Hunter

────────────────────────────────────────────────────────────────────────────────
🔐 IDENTITY VERIFICATION REQUIRED
────────────────────────────────────────────────────────────────────────────────

👤 Hunter Name:  Prax Prix
🔑 Access Code:  ········

✅ SHADOW SOLDIER ACCESS GRANTED
⚔️  Welcome back, Warrior Prax Prix!

════════════════════════════════════════════════════════════════════════════════
⚔️  SHADOW SOLDIER Prax Prix REPORTING FOR DUTY
════════════════════════════════════════════════════════════════════════════════

════════════════════════════════════════════════════════════════════════════════
⚔️  SHADOW SOLDIER OPERATIONS - Prax Prix
════════════════════════════════════════════════════════════════════════════════
1. 🗡️  Order Weapons
2. ❤️  Update Health Status
3. 📋 View Assigned Missions
4. ✅ Update Completed Missions
5. 📊 View My Stats
6. 📦 View My Weapon Orders
7. 🚪 Logout
────────────────────────────────────────────────────────────────────────────────

Select Operation:  1

════════════════════════════════════════════════════════════
🗡️  WEAPON REQUISITION SYSTEM
════════════════════════════════════════════════════════════

📦 AVAILABLE ARSENAL:

🔹 Assault Rifles:
  1. AK-47 (7.62×39mm) — Stock: 120
  2. AK-103 (7.62×39mm) — Stock: 85
  3. INSAS Rifle (5.56×45mm) — Stock: 200
  4. Tavor TAR-21 (5.56×45mm) — Stock: 60
  5. M4 Carbine (5.56×45mm) — Stock: 150
  6. SIG716 (7.62×51mm) — Stock: 45
  7. HK416 (5.56×45mm) — Stock: 70

🔹 Battle Rifles:
  8. FN FAL (7.62×51mm) — Stock: 40
  9. SCAR-H (7.62×51mm) — Stock: 35

🔹 Light Machine Guns:
  10. PKM (7.62×54mmR) — Stock: 25
  11. Negev NG7 (7.62×51mm) — Stock: 20
  12. M249 SAW (5.56×45mm) — Stock: 30

🔹 Sniper Rifles:
  13. Dragunov SVD (7.62×54mmR) — Stock: 18
  14. Barrett M82 (.50 BMG) — Stock: 10
  15. AWM (.300 Win Mag / .338 Lapua) — Stock: 8
  16. Mk 12 SPR (5.56×45mm) — Stock: 15
  17. Snipe (Propreitary) — Stock: 1

🔹 Pistols:
  18. Glock 17 (9×19mm) — Stock: 250
  19. SIG P226 (9×19mm) — Stock: 180
  20. Beretta M9 (9×19mm) — Stock: 200
  21. HS2000 (9×19mm) — Stock: 90
  22. MP-443 Grach (9×19mm) — Stock: 110

🔹 Shotguns:
  23. Benelli M4 (12-gauge shells) — Stock: 35
  24. Remington 870 (12-gauge shells) — Stock: 40

🔹 SMGs:
  25. MP5 (9×19mm) — Stock: 75
  26. Uzi (9×19mm) — Stock: 55
  27. CZ Scorpion EVO (9×19mm) — Stock: 50

🎯 Select Weapon Number:  3
📊 Quantity:  200

✅ Order placed! INSAS Rifle x200 - Awaiting Captain's approval

════════════════════════════════════════════════════════════════════════════════
⚔️  SHADOW SOLDIER OPERATIONS - Prax Prix
════════════════════════════════════════════════════════════════════════════════
1. 🗡️  Order Weapons
2. ❤️  Update Health Status
3. 📋 View Assigned Missions
4. ✅ Update Completed Missions
5. 📊 View My Stats
6. 📦 View My Weapon Orders
7. 🚪 Logout
────────────────────────────────────────────────────────────────────────────────

Select Operation:  7

🌙 Shadow returning to rest... Goodbye!

🔄 Return to main menu? (yes/no):  yes

────────────────────────────────────────────────────────────────────────────────
🔐 IDENTITY VERIFICATION REQUIRED
────────────────────────────────────────────────────────────────────────────────

👤 Hunter Name:  Yuvraj Hyperion
🔑 Access Code:  ········

✅ MONARCH ACCESS GRANTED
🌟 Welcome, Supreme Commander Yuvraj Hyperion!

════════════════════════════════════════════════════════════════════════════════
👑 MONARCH Yuvraj Hyperion HAS ENTERED THE THRONE ROOM
════════════════════════════════════════════════════════════════════════════════

════════════════════════════════════════════════════════════════════════════════
👑 MONARCH COMMAND CENTER - Yuvraj Hyperion
════════════════════════════════════════════════════════════════════════════════
1. 📦 Order Inventory Supplies
2. ✅ Approve Soldier Weapon Orders
3. ❤️  Check All Soldiers' Health Status
4. 📋 Add New Missions
5. 🗡️  Add New Weapons to Armory
6. 👥 Add New Recruits
7. 📊 View Complete Arsenal
8. 🎯 View All Missions
9. 📈 View System Statistics
10. 🚪 Logout
────────────────────────────────────────────────────────────────────────────────

Select Command:  2

════════════════════════════════════════════════════════════════════════════════
✅ WEAPON ORDER APPROVAL SYSTEM
════════════════════════════════════════════════════════════════════════════════

📋 Pending Orders:
1. Prax Prix — INSAS Rifle x200 (Pending Approval)

🎯 Select order to approve (0 to cancel):  1

📋 Order Details:
   Soldier: Prax Prix
   Weapon:  INSAS Rifle
   Quantity:200

✅ Approve? (yes/no):  no

❌ Order REJECTED!

════════════════════════════════════════════════════════════════════════════════
👑 MONARCH COMMAND CENTER - Yuvraj Hyperion
════════════════════════════════════════════════════════════════════════════════
1. 📦 Order Inventory Supplies
2. ✅ Approve Soldier Weapon Orders
3. ❤️  Check All Soldiers' Health Status
4. 📋 Add New Missions
5. 🗡️  Add New Weapons to Armory
6. 👥 Add New Recruits
7. 📊 View Complete Arsenal
8. 🎯 View All Missions
9. 📈 View System Statistics
10. 🚪 Logout
────────────────────────────────────────────────────────────────────────────────

Select Command:  10

👑 Monarch disconnecting... Farewell!

🔄 Return to main menu? (yes/no):  yes

────────────────────────────────────────────────────────────────────────────────
🔐 IDENTITY VERIFICATION REQUIRED
────────────────────────────────────────────────────────────────────────────────

👤 Hunter Name:  Prax Prix
🔑 Access Code:  ········

✅ SHADOW SOLDIER ACCESS GRANTED
⚔️  Welcome back, Warrior Prax Prix!

════════════════════════════════════════════════════════════════════════════════
⚔️  SHADOW SOLDIER Prax Prix REPORTING FOR DUTY
════════════════════════════════════════════════════════════════════════════════

════════════════════════════════════════════════════════════════════════════════
⚔️  SHADOW SOLDIER OPERATIONS - Prax Prix
════════════════════════════════════════════════════════════════════════════════
1. 🗡️  Order Weapons
2. ❤️  Update Health Status
3. 📋 View Assigned Missions
4. ✅ Update Completed Missions
5. 📊 View My Stats
6. 📦 View My Weapon Orders
7. 🚪 Logout
────────────────────────────────────────────────────────────────────────────────

Select Operation:  6

════════════════════════════════════════════════════════════════════════════════
📦 WEAPON ORDERS — Prax Prix
════════════════════════════════════════════════════════════════════════════════

1. ✅ Uzi x5
      Status: Approved

2. ❌ INSAS Rifle x200
      Status: Rejected

════════════════════════════════════════════════════════════════════════════════
⚔️  SHADOW SOLDIER OPERATIONS - Prax Prix
════════════════════════════════════════════════════════════════════════════════
1. 🗡️  Order Weapons
2. ❤️  Update Health Status
3. 📋 View Assigned Missions
4. ✅ Update Completed Missions
5. 📊 View My Stats
6. 📦 View My Weapon Orders
7. 🚪 Logout
────────────────────────────────────────────────────────────────────────────────

Select Operation:  7

🌙 Shadow returning to rest... Goodbye!

🔄 Return to main menu? (yes/no):  no

🌙 Shadow Protocol Deactivating...
💀 'The shadows return to slumber...'
```

### Output 5: Shadow Soldier Command Center (`soldier_menu()`)

```python
================================================================================
🗡️  INITIALIZING SHADOW MILITARY PROTOCOL  🗡️
================================================================================

⚙️  Connecting to Shadow Database...
   ✅ 'shadow_army_db' found — loading existing data...
   ✅ Data loaded from 'shadow_army_db'!

================================================================================
🗡️  SHADOW MILITARY PROTOCOL INITIALIZED
================================================================================

💀 'Arise, Shadows of the Fallen...'
🌟 Solo Leveling Military Management System 
================================================================================

────────────────────────────────────────────────────────────────────────────────
🔐 IDENTITY VERIFICATION REQUIRED
────────────────────────────────────────────────────────────────────────────────

👤 Hunter Name:  Vikrant Senapati X9
🔑 Access Code:  ········

✅ SHADOW SOLDIER ACCESS GRANTED
⚔️  Welcome back, Warrior Vikrant Senapati X9!

════════════════════════════════════════════════════════════════════════════════
⚔️  SHADOW SOLDIER Vikrant Senapati X9 REPORTING FOR DUTY
════════════════════════════════════════════════════════════════════════════════

════════════════════════════════════════════════════════════════════════════════
⚔️  SHADOW SOLDIER OPERATIONS - Vikrant Senapati X9
════════════════════════════════════════════════════════════════════════════════
1. 🗡️  Order Weapons
2. ❤️  Update Health Status
3. 📋 View Assigned Missions
4. ✅ Update Completed Missions
5. 📊 View My Stats
6. 📦 View My Weapon Orders
7. 🚪 Logout
────────────────────────────────────────────────────────────────────────────────

Select Operation:  2

════════════════════════════════════════════════════════════
❤️  HEALTH STATUS UPDATE
════════════════════════════════════════════════════════════

📊 Current Stats:
   HP: 99/100
   Mana: 99/100
   Rank: S-Rank
   Level: 45
   Status: Active

🔄 Update Status:

New HP (0-100):  99
New Mana (0-100):  99

Status Options: Active, Injured, Recovering, Critical

New Status:  HyperActive

✅ Health Status Updated Successfully!
   HP: 99/100
   Mana: 99/100
   Status: HyperActive

════════════════════════════════════════════════════════════════════════════════
⚔️  SHADOW SOLDIER OPERATIONS - Vikrant Senapati X9
════════════════════════════════════════════════════════════════════════════════
1. 🗡️  Order Weapons
2. ❤️  Update Health Status
3. 📋 View Assigned Missions
4. ✅ Update Completed Missions
5. 📊 View My Stats
6. 📦 View My Weapon Orders
7. 🚪 Logout
────────────────────────────────────────────────────────────────────────────────

Select Operation:  3

════════════════════════════════════════════════════════════════════════════════
📋 MISSIONS ASSIGNED TO Vikrant Senapati X9
════════════════════════════════════════════════════════════════════════════════

🎯 Mission ID: QUEST-001
   📝 Description: Secure Northern Border
   📊 Status: Completed
   ⭐ Priority: S-Rank
   ────────────────────────────────────────────────────────────

🎯 Mission ID: QUEST-002
   📝 Description: Weapons Training Exercise
   📊 Status: Pending
   ⭐ Priority: B-Rank
   ────────────────────────────────────────────────────────────

🎯 Mission ID: QUEST-006
   📝 Description: Docmentation of python
   📊 Status: Pending
   ⭐ Priority: S-Rank
   ────────────────────────────────────────────────────────────

════════════════════════════════════════════════════════════════════════════════
⚔️  SHADOW SOLDIER OPERATIONS - Vikrant Senapati X9
════════════════════════════════════════════════════════════════════════════════
1. 🗡️  Order Weapons
2. ❤️  Update Health Status
3. 📋 View Assigned Missions
4. ✅ Update Completed Missions
5. 📊 View My Stats
6. 📦 View My Weapon Orders
7. 🚪 Logout
────────────────────────────────────────────────────────────────────────────────

Select Operation:  4

════════════════════════════════════════════════════════════════════════════════
✅ UPDATE MISSION STATUS
════════════════════════════════════════════════════════════════════════════════

📭 No pending missions to update.

════════════════════════════════════════════════════════════════════════════════
⚔️  SHADOW SOLDIER OPERATIONS - Vikrant Senapati X9
════════════════════════════════════════════════════════════════════════════════
1. 🗡️  Order Weapons
2. ❤️  Update Health Status
3. 📋 View Assigned Missions
4. ✅ Update Completed Missions
5. 📊 View My Stats
6. 📦 View My Weapon Orders
7. 🚪 Logout
────────────────────────────────────────────────────────────────────────────────

Select Operation:  5

════════════════════════════════════════════════════════════════════════════════
📊 HUNTER PROFILE - Vikrant Senapati X9
════════════════════════════════════════════════════════════════════════════════

⚔️  COMBAT STATISTICS:
   ❤️  HP: 99/100 █████████
   💙 Mana: 99/100 █████████
   🏆 Rank: S-Rank
   ⭐ Level: 45
   🎯 Status: HyperActive

📋 MISSION RECORD:
   Total Missions: 1
   Completed: 1
   Success Rate: 100.0%

════════════════════════════════════════════════════════════════════════════════
⚔️  SHADOW SOLDIER OPERATIONS - Vikrant Senapati X9
════════════════════════════════════════════════════════════════════════════════
1. 🗡️  Order Weapons
2. ❤️  Update Health Status
3. 📋 View Assigned Missions
4. ✅ Update Completed Missions
5. 📊 View My Stats
6. 📦 View My Weapon Orders
7. 🚪 Logout
────────────────────────────────────────────────────────────────────────────────

Select Operation:  6

════════════════════════════════════════════════════════════════════════════════
📦 WEAPON ORDERS — Vikrant Senapati X9
════════════════════════════════════════════════════════════════════════════════

📭 You have no weapon orders.

════════════════════════════════════════════════════════════════════════════════
⚔️  SHADOW SOLDIER OPERATIONS - Vikrant Senapati X9
════════════════════════════════════════════════════════════════════════════════
1. 🗡️  Order Weapons
2. ❤️  Update Health Status
3. 📋 View Assigned Missions
4. ✅ Update Completed Missions
5. 📊 View My Stats
6. 📦 View My Weapon Orders
7. 🚪 Logout
────────────────────────────────────────────────────────────────────────────────

Select Operation:  7

🌙 Shadow returning to rest... Goodbye!

🔄 Return to main menu? (yes/no): no

🌙 Shadow Protocol Deactivating...
💀 'The shadows return to slumber...'
```


## CONCLUSION

The **Shadow Military Protocol (Solo Leveling Military Management System v2.0)** successfully achieves a robust integration between object-oriented Python scripting and a relational MySQL backend database. By decoupling administrative functions from low-level data storage, the system ensures data persistence, transactional security, and modularity.

### Scope for Future Enhancement:

1. **Graphical User Interface (GUI):** Transition from a Command-Line Interface (CLI) to a desktop GUI using PyQt6 or Tkinter.
    
2. **Role-Based Access Control (RBAC) Expansion:** Implement hashed password storage using `bcrypt` or `hashlib` instead of plain-text passwords.
    
3. **Automated Combat Simulation Engine:** Integrate dynamic statistical algorithms to model mission success probability based on unit levels, HP, and available armory supplies.
    
4. **REST API Interface:** Develop a FastAPI/Flask backend to expose military management endpoints for web/mobile client applications.
    

## BIBLIOGRAPHY

- **Computer Science with Python (Class XII)** – Sumita Arora
    
- **MySQL 8.0 Reference Manual** – Oracle Documentation (`[dev.mysql.com/doc](https://dev.mysql.com/doc)`)
    
- **Python 3.x Documentation** – Official Python Reference (`docs.python.org`)
    
- **W3Schools Online Web Tutorials** (`[www.w3schools.com/python](https://www.w3schools.com/python)`, `[www.w3schools.com/sql](https://www.w3schools.com/sql)`)
    
- **GeeksforGeeks Computer Science Resources** (`www.geeksforgeeks.org`)