# %% [markdown]
# #
# #  🗡️ SHADOW SOLDIERS SYSTEM - SOLO LEVELING INSPIRED 🗡️

# %%
#importing
import math, random, statistics as stat
from math import pi
from getpass import getpass
from datetime import datetime

# %%
print("="*80)
print("🗡️  INITIALIZING SHADOW MILITARY PROTOCOL  🗡️")
print("="*80)

# %% [markdown]
# ## 📊 DATABASES

# %%

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# CAPTAIN CREDENTIALS - "The Monarchs"
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
passucap = {
    "Yuvraj Hyperion" : 'CapYuvHy#7',
    "Devaksha Quantum" : 'CapDevQ!21',
    "Arinjay Solace" : 'CapArjSol$5',
    "Rudranath Eclipse" : 'CapRudEcl8',
    "Veershaad Zenith" : 'CapVeeZen#9'
}

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# SOLDIER CREDENTIALS - "The Shadow Army"
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
passusol = {
    "Vikrant Senapati X9": "Vikr@ntX9!",
    "Rudra Pratap Nova": "Rudr@Nova42",
    "Bhairav Singh Orion": "Bhai$Orion7",
    "Agniveer Kaaltron": "Agni_Kaal99",
    "Arindham Varmax": "Arin!Var88",
    "Mahaveer Rajat Prime": "MahaRajat#5",
    "Samrat Veerbhadra 7": "SamVee7!",
    "Shatrughan Devdroid": "ShatDev#12",
    "Trikand Arjun Nexus": "TriArjNex3",
    "Garudnath Keshari X": "GaruKesh$X",
    "Vajrahan Bhupendra Omega": "VajBhupOmega8",
    "Nirbhay Karunesh Flux": "NirbKar!Flux",
    "Dhananjay Kulkarni Titan": "DhanKulT#4",
    "Shivraaj Deshmukh Vortex": "ShivDesVort9",
    "Kaalnemi Pradhan Pulse": "KaalPrad!P"
}

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# SOLDIER HEALTH STATUS - Format: (HP, Mana, Rank, Level, Status)
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
soldier_health = {
    "Vikrant Senapati X9": [100, 100, "S-Rank", 45, "Active"],
    "Rudra Pratap Nova": [95, 90, "A-Rank", 38, "Active"],
    "Bhairav Singh Orion": [88, 85, "A-Rank", 35, "Injured"],
    "Agniveer Kaaltron": [100, 95, "B-Rank", 28, "Active"],
    "Arindham Varmax": [92, 88, "B-Rank", 30, "Active"],
    "Mahaveer Rajat Prime": [85, 80, "C-Rank", 22, "Recovering"],
    "Samrat Veerbhadra 7": [100, 100, "S-Rank", 42, "Active"],
    "Shatrughan Devdroid": [78, 75, "C-Rank", 20, "Injured"],
    "Trikand Arjun Nexus": [90, 92, "A-Rank", 36, "Active"],
    "Garudnath Keshari X": [100, 98, "S-Rank", 48, "Active"],
    "Vajrahan Bhupendra Omega": [88, 85, "B-Rank", 29, "Active"],
    "Nirbhay Karunesh Flux": [95, 90, "A-Rank", 40, "Active"],
    "Dhananjay Kulkarni Titan": [82, 78, "C-Rank", 25, "Recovering"],
    "Shivraaj Deshmukh Vortex": [100, 100, "S-Rank", 50, "Active"],
    "Kaalnemi Pradhan Pulse": [90, 88, "B-Rank", 32, "Active"]
}

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# WEAPONS ARMORY
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
armory = {
    "Primary_Weapons": {
        "Assault_Rifles": {
            "AK-47": "7.62×39mm",
            "AK-103": "7.62×39mm",
            "INSAS Rifle": "5.56×45mm",
            "Tavor TAR-21": "5.56×45mm",
            "M4 Carbine": "5.56×45mm",
            "SIG716": "7.62×51mm",
            "HK416": "5.56×45mm"
        },
        "Battle_Rifles": {
            "FN FAL": "7.62×51mm",
            "SCAR-H": "7.62×51mm"
        },
        "Light_Machine_Guns": {
            "PKM": "7.62×54mmR",
            "Negev NG7": "7.62×51mm",
            "M249 SAW": "5.56×45mm"
        },
        "Sniper_Rifles": {
            "Dragunov SVD": "7.62×54mmR",
            "Barrett M82": ".50 BMG",
            "AWM": ".300 Win Mag / .338 Lapua",
            "Mk 12 SPR": "5.56×45mm"
        }
    },
    "Secondary_Weapons": {
        "Pistols": {
            "Glock 17": "9×19mm",
            "SIG P226": "9×19mm",
            "Beretta M9": "9×19mm",
            "HS2000": "9×19mm",
            "MP-443 Grach": "9×19mm"
        }
    },
    "Special_Weapons": {
        "Shotguns": {
            "Benelli M4": "12-gauge shells",
            "Remington 870": "12-gauge shells"
        },
        "SMGs": {
            "MP5": "9×19mm",
            "Uzi": "9×19mm",
            "CZ Scorpion EVO": "9×19mm"
        },
        "Explosives": [
            "Hand Grenade (HE36 / M67)",
            "Smoke Grenade",
            "Flashbang"
        ]
    }
}

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# INVENTORY STOCK - Tuple format: (Item_Name, Quantity, Status)
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
inventory_stock = {
    "Ammunition": [
        ("5.56×45mm rounds", 50000, "Available"),
        ("7.62×39mm rounds", 40000, "Available"),
        ("7.62×51mm rounds", 30000, "Available"),
        ("7.62×54mmR rounds", 25000, "Low Stock"),
        ("9×19mm pistol ammo", 60000, "Available"),
        (".50 BMG ammo", 5000, "Low Stock"),
        (".338 Lapua", 3000, "Available"),
        ("12-gauge shells", 15000, "Available")
    ],
    "Accessories": [
        ("Rifle magazines", 500, "Available"),
        ("Pistol magazines", 300, "Available"),
        ("ACOG Scopes", 50, "Low Stock"),
        ("Red Dot Sights", 80, "Available"),
        ("Tactical Lights", 100, "Available"),
        ("Suppressors", 30, "Low Stock")
    ]
}

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# MISSION TASKS - Format: [Mission_ID, Description, Assigned_To, Status, Priority]
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
mission_tasks = [
    ["QUEST-001", "Secure Northern Border", "Vikrant Senapati X9", "In Progress", "S-Rank"],
    ["QUEST-002", "Weapons Training Exercise", "All Soldiers", "Pending", "B-Rank"],
    ["QUEST-003", "Recon Mission - Sector 7", "Garudnath Keshari X", "Completed", "A-Rank"],
    ["QUEST-004", "Equipment Maintenance", "Agniveer Kaaltron", "Pending", "C-Rank"],
    ["QUEST-005", "Night Patrol Duty", "Nirbhay Karunesh Flux", "In Progress", "A-Rank"]
]

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# SOLDIER WEAPON ORDERS - Format: [(Soldier_Name, Weapon, Quantity, Status)]
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
weapon_orders = []

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# PENDING RECRUITS - Format: [(Name, Rank, Level, Status)]
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
pending_recruits = []

# %% [markdown]
# ##  ⚔️ CORE FUNCTIONS

# %% [markdown]
# ### Authentication System
# 

# %%
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# AUTHENTICATION SYSTEM
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

def auth():
    """Shadow Authentication Protocol"""
    brp = 0
    while brp <= 3:
        print("\n" + "─"*80)
        print("🔐 IDENTITY VERIFICATION REQUIRED")
        print("─"*80)
        username = input("👤 Hunter Name: ")
        pwd = getpass("🔑 Access Code: ")
        
        if passucap.get(username):
            if passucap[username] == pwd:
                print("\n✅ MONARCH ACCESS GRANTED")
                print(f"🌟 Welcome, Supreme Commander {username}!")
                return True, "cap", username
            else:
                print("❌ Invalid Access Code")
        elif passusol.get(username):
            if passusol[username] == pwd:
                print("\n✅ SHADOW SOLDIER ACCESS GRANTED")
                print(f"⚔️  Welcome back, Warrior {username}!")
                return True, "sol", username
            else:
                print("❌ Invalid Access Code")
        else:
            print("❌ Unknown Hunter")
            brp += 1
    return False, "break", None

# %% [markdown]
# ### Operations for soldiers
# 

# %%
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# SOLDIER OPERATIONS
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
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
        print("6. 🚪 Logout")
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
            print("\n🌙 Shadow returning to rest... Goodbye!")
            break
        else:
            print("⚠️  Invalid Operation Code!")

# %% [markdown]
# ### Order Placement

# %%


def order_weapons(soldier_name):
    """Place weapon requisition order"""
    print("\n" + "═"*60)
    print("🗡️  WEAPON REQUISITION SYSTEM")
    print("═"*60)
    
    # Display available weapons
    print("\n📦 AVAILABLE ARSENAL:")
    weapon_list = []
    idx = 1
    
    for category, weapons in armory["Primary_Weapons"].items():
        print(f"\n🔹 {category}:")
        for weapon, caliber in weapons.items():
            print(f"  {idx}. {weapon} ({caliber})")
            weapon_list.append((weapon, caliber))
            idx += 1
    
    for category, weapons in armory["Secondary_Weapons"].items():
        print(f"\n🔹 {category}:")
        for weapon, caliber in weapons.items():
            print(f"  {idx}. {weapon} ({caliber})")
            weapon_list.append((weapon, caliber))
            idx += 1
    
    try:
        weapon_choice = int(input("\n🎯 Select Weapon Number: ")) - 1
        quantity = int(input("📊 Quantity: "))
        
        if 0 <= weapon_choice < len(weapon_list):
            weapon_name = weapon_list[weapon_choice][0]
            order = (soldier_name, weapon_name, quantity, "Pending Approval")
            weapon_orders.append(order)
            print(f"\n✅ Order placed! {weapon_name} x{quantity} - Awaiting Captain's approval")
        else:
            print("❌ Invalid weapon selection!")
    except:
        print("❌ Invalid input!")

# %% [markdown]
# ### Soldier Health Update

# %%
def update_health_status(soldier_name):
    """Update soldier's health metrics"""
    print("\n" + "═"*60)
    print("❤️  HEALTH STATUS UPDATE")
    print("═"*60)
    
    if soldier_name in soldier_health:
        current_stats = soldier_health[soldier_name]
        print(f"\n📊 Current Stats:")
        print(f"   HP: {current_stats[0]}/100")
        print(f"   Mana: {current_stats[1]}/100")
        print(f"   Rank: {current_stats[2]}")
        print(f"   Level: {current_stats[3]}")
        print(f"   Status: {current_stats[4]}")
        
        print("\n🔄 Update Status:")
        try:
            new_hp = int(input("New HP (0-100): "))
            new_mana = int(input("New Mana (0-100): "))
            print("\nStatus Options: Active, Injured, Recovering, Critical")
            new_status = input("New Status: ")
            
            soldier_health[soldier_name][0] = max(0, min(100, new_hp))
            soldier_health[soldier_name][1] = max(0, min(100, new_mana))
            soldier_health[soldier_name][4] = new_status
            
            print("\n✅ Health Status Updated Successfully!")
            print(f"   HP: {soldier_health[soldier_name][0]}/100")
            print(f"   Mana: {soldier_health[soldier_name][1]}/100")
            print(f"   Status: {soldier_health[soldier_name][4]}")
        except:
            print("❌ Invalid input!")

# %% [markdown]
# ### View Tasks

# %%

def view_tasks(soldier_name):
    """View assigned missions"""
    print("\n" + "═"*80)
    print(f"📋 MISSIONS ASSIGNED TO {soldier_name}")
    print("═"*80)
    
    found = False
    for task in mission_tasks:
        if task[2] == soldier_name or task[2] == "All Soldiers":
            print(f"\n🎯 Mission ID: {task[0]}")
            print(f"   📝 Description: {task[1]}")
            print(f"   📊 Status: {task[3]}")
            print(f"   ⭐ Priority: {task[4]}")
            print("   " + "─"*60)
            found = True
    
    if not found:
        print("\n📭 No missions currently assigned.")

# %% [markdown]
# ### Update tasks
# 

# %%
def update_completed_tasks(soldier_name):
    """Mark missions as completed"""
    print("\n" + "═"*80)
    print("✅ UPDATE MISSION STATUS")
    print("═"*80)
    
    soldier_missions = []
    for idx, task in enumerate(mission_tasks):
        if task[2] == soldier_name and task[3] != "Completed":
            soldier_missions.append((idx, task))
    
    if not soldier_missions:
        print("\n📭 No pending missions to update.")
        return
    
    print("\n📋 Your Pending Missions:")
    for i, (idx, task) in enumerate(soldier_missions, 1):
        print(f"{i}. {task[0]} - {task[1]} ({task[3]})")
    
    try:
        choice = int(input("\n🎯 Select mission to mark as completed: ")) - 1
        if 0 <= choice < len(soldier_missions):
            task_idx = soldier_missions[choice][0]
            mission_tasks[task_idx][3] = "Completed"
            print(f"\n🎉 Mission {mission_tasks[task_idx][0]} marked as COMPLETED!")
            print(f"🌟 +{random.randint(100, 500)} XP Earned!")
        else:
            print("❌ Invalid selection!")
    except:
        print("❌ Invalid input!")

# %% [markdown]
# ### View all soldier details

# %%
def view_soldier_stats(soldier_name):
    """Display detailed soldier statistics"""
    print("\n" + "═"*80)
    print(f"📊 HUNTER PROFILE - {soldier_name}")
    print("═"*80)
    
    if soldier_name in soldier_health:
        stats = soldier_health[soldier_name]
        print(f"\n⚔️  COMBAT STATISTICS:")
        print(f"   ❤️  HP: {stats[0]}/100 {'█' * (stats[0]//10)}")
        print(f"   💙 Mana: {stats[1]}/100 {'█' * (stats[1]//10)}")
        print(f"   🏆 Rank: {stats[2]}")
        print(f"   ⭐ Level: {stats[3]}")
        print(f"   🎯 Status: {stats[4]}")
        
        # Count missions
        total_missions = sum(1 for task in mission_tasks if task[2] == soldier_name)
        completed = sum(1 for task in mission_tasks if task[2] == soldier_name and task[3] == "Completed")
        print(f"\n📋 MISSION RECORD:")
        print(f"   Total Missions: {total_missions}")
        print(f"   Completed: {completed}")
        print(f"   Success Rate: {(completed/total_missions*100) if total_missions > 0 else 0:.1f}%")

# %% [markdown]
# ## All operations for captains

# %%
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# CAPTAIN OPERATIONS
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
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

# %% [markdown]
# ### Inventory System

# %%

def order_inventory():
    """Order supplies for inventory"""
    print("\n" + "═"*80)
    print("📦 INVENTORY SUPPLY ORDER SYSTEM")
    print("═"*80)
    
    print("\n🔹 Current Inventory Stock:")
    for category, items in inventory_stock.items():
        print(f"\n📌 {category}:")
        for idx, (item, qty, status) in enumerate(items, 1):
            print(f"   {idx}. {item}: {qty} units - {status}")
    
    print("\n🆕 Place New Order:")
    item_name = input("Item Name: ")
    try:
        quantity = int(input("Quantity: "))
        
        # Add to appropriate category
        category = input("Category (Ammunition/Accessories): ")
        if category in inventory_stock:
            inventory_stock[category].append((item_name, quantity, "In Transit"))
            print(f"\n✅ Order placed: {item_name} x{quantity}")
        else:
            print("❌ Invalid category!")
    except:
        print("❌ Invalid input!")

# %% [markdown]
# ### Approval system
# 

# %%

def approve_weapon_orders():
    """Approve pending weapon requisitions"""
    print("\n" + "═"*80)
    print("✅ WEAPON ORDER APPROVAL SYSTEM")
    print("═"*80)
    
    pending = [order for order in weapon_orders if order[3] == "Pending Approval"]
    
    if not pending:
        print("\n📭 No pending weapon orders.")
        return
    
    print("\n📋 Pending Orders:")
    for idx, order in enumerate(pending, 1):
        print(f"{idx}. {order[0]} - {order[1]} x{order[2]} ({order[3]})")
    
    try:
        choice = int(input("\n🎯 Select order to approve (0 to cancel): "))
        if choice == 0:
            return
        if 1 <= choice <= len(pending):
            order_idx = weapon_orders.index(pending[choice-1])
            soldier, weapon, qty, _ = weapon_orders[order_idx]
            
            print(f"\n📋 Order Details:")
            print(f"   Soldier: {soldier}")
            print(f"   Weapon: {weapon}")
            print(f"   Quantity: {qty}")
            
            decision = input("\n✅ Approve? (yes/no): ").lower()
            if decision == "yes":
                weapon_orders[order_idx] = (soldier, weapon, qty, "Approved")
                print(f"\n🎉 Order APPROVED! {weapon} x{qty} will be issued to {soldier}")
            else:
                weapon_orders[order_idx] = (soldier, weapon, qty, "Rejected")
                print(f"\n❌ Order REJECTED")
        else:
            print("❌ Invalid selection!")
    except:
        print("❌ Invalid input!")

# %% [markdown]
# ### health system

# %%



def check_health_status():
    """View all soldiers' health metrics"""
    print("\n" + "═"*80)
    print("❤️  SHADOW ARMY HEALTH STATUS")
    print("═"*80)
    
    # Sort by health status
    critical = []
    injured = []
    recovering = []
    active = []
    
    for soldier, stats in soldier_health.items():
        if stats[4] == "Critical" or stats[0] < 30:
            critical.append((soldier, stats))
        elif stats[4] == "Injured":
            injured.append((soldier, stats))
        elif stats[4] == "Recovering":
            recovering.append((soldier, stats))
        else:
            active.append((soldier, stats))
    
    if critical:
        print("\n🚨 CRITICAL STATUS:")
        for soldier, stats in critical:
            print(f"   ⚠️  {soldier}: HP {stats[0]}/100, Mana {stats[1]}/100, {stats[2]} Lv.{stats[3]}")
    
    if injured:
        print("\n🩹 INJURED:")
        for soldier, stats in injured:
            print(f"   ⚠️  {soldier}: HP {stats[0]}/100, Mana {stats[1]}/100, {stats[2]} Lv.{stats[3]}")
    
    if recovering:
        print("\n🏥 RECOVERING:")
        for soldier, stats in recovering:
            print(f"   💊 {soldier}: HP {stats[0]}/100, Mana {stats[1]}/100, {stats[2]} Lv.{stats[3]}")
    
    if active:
        print("\n✅ ACTIVE DUTY:")
        for soldier, stats in active:
            print(f"   ⚔️  {soldier}: HP {stats[0]}/100, Mana {stats[1]}/100, {stats[2]} Lv.{stats[3]}")

# %% [markdown]
# ### Task Manager

# %%


def add_tasks():
    """Create new mission assignments"""
    print("\n" + "═"*80)
    print("📋 MISSION CREATION SYSTEM")
    print("═"*80)
    
    mission_id = f"QUEST-{len(mission_tasks) + 1:03d}"
    description = input("\n📝 Mission Description: ")
    
    print("\n👥 Available Soldiers:")
    print("   0. All Soldiers")
    soldiers = list(passusol.keys())
    for idx, soldier in enumerate(soldiers, 1):
        rank = soldier_health[soldier][2] if soldier in soldier_health else "Unknown"
        status = soldier_health[soldier][4] if soldier in soldier_health else "Unknown"
        print(f"   {idx}. {soldier} ({rank}) - {status}")
    
    try:
        soldier_choice = int(input("\n🎯 Assign to (number): "))
        assigned_to = "All Soldiers" if soldier_choice == 0 else soldiers[soldier_choice - 1]
        
        print("\n⭐ Priority Levels: S-Rank, A-Rank, B-Rank, C-Rank, D-Rank")
        priority = input("Priority: ")
        
        new_mission = [mission_id, description, assigned_to, "Pending", priority]
        mission_tasks.append(new_mission)
        
        print(f"\n✅ Mission {mission_id} created successfully!")
        print(f"   Assigned to: {assigned_to}")
        print(f"   Priority: {priority}")
    except:
        print("❌ Invalid input!")

# %% [markdown]
# ### New Weapons

# %%


def add_weapons():
    """Add new weapons to the armory"""
    print("\n" + "═"*80)
    print("🗡️  ARMORY EXPANSION SYSTEM")
    print("═"*80)
    
    print("\n📦 Weapon Categories:")
    print("1. Assault_Rifles")
    print("2. Battle_Rifles")
    print("3. Light_Machine_Guns")
    print("4. Sniper_Rifles")
    print("5. Pistols")
    print("6. Shotguns")
    print("7. SMGs")
    
    try:
        category_map = {
            "1": ("Primary_Weapons", "Assault_Rifles"),
            "2": ("Primary_Weapons", "Battle_Rifles"),
            "3": ("Primary_Weapons", "Light_Machine_Guns"),
            "4": ("Primary_Weapons", "Sniper_Rifles"),
            "5": ("Secondary_Weapons", "Pistols"),
            "6": ("Special_Weapons", "Shotguns"),
            "7": ("Special_Weapons", "SMGs")
        }
        
        choice = input("\n🎯 Select Category: ")
        if choice in category_map:
            main_cat, sub_cat = category_map[choice]
            weapon_name = input("Weapon Name: ")
            caliber = input("Caliber/Ammo Type: ")
            
            armory[main_cat][sub_cat][weapon_name] = caliber
            print(f"\n✅ {weapon_name} ({caliber}) added to {sub_cat}!")
        else:
            print("❌ Invalid category!")
    except:
        print("❌ Invalid input!")

# %% [markdown]
# ### Recruits
# 

# %%


def add_recruits():
    """Add new soldiers to the system"""
    print("\n" + "═"*80)
    print("👥 RECRUITMENT SYSTEM - SHADOW AWAKENING")
    print("═"*80)
    
    recruit_name = input("\n📝 Recruit Name: ")
    password = input("🔑 Set Password: ")
    
    print("\n⭐ Rank Assignment: S-Rank, A-Rank, B-Rank, C-Rank, D-Rank, E-Rank")
    rank = input("Initial Rank: ")
    
    try:
        level = int(input("Initial Level (1-50): "))
        
        # Add to soldier database
        passusol[recruit_name] = password
        soldier_health[recruit_name] = [100, 100, rank, level, "Active"]
        
        print(f"\n🎉 {recruit_name} has been awakened as a Shadow Soldier!")
        print(f"   Rank: {rank}")
        print(f"   Level: {level}")
        print(f"   Status: Active")
    except:
        print("❌ Invalid input!")

# %% [markdown]
# ### All ammo

# %%


def view_arsenal():
    """Display complete weapons inventory"""
    print("\n" + "═"*80)
    print("🗡️  COMPLETE ARSENAL DATABASE")
    print("═"*80)
    
    for main_category, sub_categories in armory.items():
        print(f"\n{'═'*60}")
        print(f"🔹 {main_category.replace('_', ' ').upper()}")
        print(f"{'═'*60}")
        
        if isinstance(sub_categories, dict):
            for sub_cat, weapons in sub_categories.items():
                print(f"\n   📌 {sub_cat.replace('_', ' ')}:")
                if isinstance(weapons, dict):
                    for weapon, caliber in weapons.items():
                        print(f"      • {weapon} - {caliber}")
                elif isinstance(weapons, list):
                    for weapon in weapons:
                        print(f"      • {weapon}")

# %% [markdown]
# ### All missions

# %%


def view_all_missions():
    """Display all mission assignments"""
    print("\n" + "═"*80)
    print("🎯 MISSION DATABASE")
    print("═"*80)
    
    # Group by status
    statuses = {}
    for task in mission_tasks:
        status = task[3]
        if status not in statuses:
            statuses[status] = []
        statuses[status].append(task)
    
    for status, tasks in statuses.items():
        print(f"\n{'─'*60}")
        print(f"📊 STATUS: {status}")
        print(f"{'─'*60}")
        for task in tasks:
            print(f"\n   🎯 {task[0]}: {task[1]}")
            print(f"      Assigned: {task[2]}")
            print(f"      Priority: {task[4]}")

# %% [markdown]
# ### Everything

# %%


def view_system_stats():
    """Display comprehensive system statistics"""
    print("\n" + "═"*80)
    print("📈 SYSTEM ANALYTICS DASHBOARD")
    print("═"*80)
    
    total_soldiers = len(passusol)
    total_captains = len(passucap)
    
    active_soldiers = sum(1 for stats in soldier_health.values() if stats[4] == "Active")
    injured_soldiers = sum(1 for stats in soldier_health.values() if stats[4] == "Injured")
    
    total_missions = len(mission_tasks)
    completed_missions = sum(1 for task in mission_tasks if task[3] == "Completed")
    pending_missions = sum(1 for task in mission_tasks if task[3] == "Pending")
    
    pending_orders = sum(1 for order in weapon_orders if order[3] == "Pending Approval")
    
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
    print(f"   Total Inventory Categories: {len(inventory_stock)}")
    
    print(f"\n⚔️  COMBAT READINESS:")
    avg_hp = stat.mean([s[0] for s in soldier_health.values()])
    avg_level = stat.mean([s[3] for s in soldier_health.values()])
    print(f"   Average HP: {avg_hp:.1f}/100")
    print(f"   Average Level: {avg_level:.1f}")
    
    rank_distribution = {}
    for stats in soldier_health.values():
        rank = stats[2]
        rank_distribution[rank] = rank_distribution.get(rank, 0) + 1
    
    print(f"\n🏆 RANK DISTRIBUTION:")
    for rank, count in sorted(rank_distribution.items(), reverse=True):
        print(f"   {rank}: {count} soldiers {'█' * count}")


# %% [markdown]
# ## 🌟 MAIN EXECUTION - THE SYSTEM AWAKENS

# %%


#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# CORE PROGRAM LOOP
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def main():
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

# Run the system
if __name__ == "__main__":
    main()
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# %%



