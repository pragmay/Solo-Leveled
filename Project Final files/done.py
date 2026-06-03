# %%
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

# %%



