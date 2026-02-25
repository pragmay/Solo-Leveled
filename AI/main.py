# %% [markdown]
# # Soldiers assemble !!!

# %%
#trying to pritn
print("Pritn")

# %%
import math, random, statistics as stat
from math import pi


rand = random.random() * (1000 - 10) +10 #getting a random number from the range of 10 to 1000
ceil = math.ceil(rand)

brainTorture  = [random.random() for i in range(0,random.randint(0,100))]
print(brainTorture)

#torture time
print(stat.mean(brainTorture))
print(stat.mode(brainTorture))
print(stat.median(brainTorture))


print(ceil) 
print(rand)

# %% [markdown]
# # These are the database of data
# 

# %%
from getpass import getpass
print("~~~"*50)
print("Welcome to the Soldier Health and Weapons Inventory Management System, Please identify yourself below")


#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#These are the usernames and password dictionaries
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

passucap = {
    "Yuvraj Hyperion" : 'CapYuvHy#7',
    "Devaksha Quantum" : 'CapDevQ!21',
    "Arinjay Solace" : 'CapArjSol$5',
    "Rudranath Eclipse" : 'CapRudEcl8',
    "Veershaad Zenith" : 'CapVeeZen#9'
}

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
    },

    "Ammo_Requirements": {
        "AK-47": {"Ammo_Type": "7.62×39mm", "Typical_Load": "6 mags × 30 rounds"},
        "SIG716": {"Ammo_Type": "7.62×51mm", "Typical_Load": "5 mags × 20 rounds"},
        "M4 / TAR-21": {"Ammo_Type": "5.56×45mm", "Typical_Load": "7 mags × 30 rounds"},
        "PKM LMG": {"Ammo_Type": "7.62×54mmR", "Typical_Load": "600–800 rounds (belt)"},
        "Dragunov SVD": {"Ammo_Type": "7.62×54mmR", "Typical_Load": "5 mags × 10 rounds"},
        "Barrett M82": {"Ammo_Type": ".50 BMG", "Typical_Load": "40–50 rounds"},
        "AWM": {"Ammo_Type": ".338 / .300", "Typical_Load": "40 rounds"},
        "Glock 17": {"Ammo_Type": "9×19mm", "Typical_Load": "3 mags × 17 rounds"},
        "Benelli M4": {"Ammo_Type": "12-gauge", "Typical_Load": "25–30 shells"}
    },

    "Refill_Inventory": {
        "Ammunition": [
            "5.56×45mm rounds",
            "7.62×39mm rounds",
            "7.62×51mm rounds",
            "7.62×54mmR rounds",
            "9×19mm pistol ammo",
            ".50 BMG ammo",
            ".338 Lapua / .300 Win Mag",
            "12-gauge shells",
            "LMG belts",
            "Grenades (HE, Smoke, Flash)"
        ],
        "Accessories": [
            "Rifle magazines",
            "Pistol magazines",
            "Sniper magazines",
            "Cleaning kits",
            "Optics (ACOG, red dot, scopes)",
            "Tactical lights",
            "Suppressors",
            "Slings",
            "Batteries for optics"
        ],
        "Maintenance": [
            "Gun oil",
            "Cleaning rods",
            "Brushes",
            "Replacement parts (firing pin, springs, extractors)"
        ]
    }
}



#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#Weapons
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~





# %% [markdown]
# # Functions
# 

# %% [markdown]
# ## The authenticator
# 

# %%
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#the auth system
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def auth():
    brp = 0 #breaking variable
    while brp <=3:
        username = input("Enter your name : ")
        pwd = getpass("Password : ")
        if passucap.get(username):
            if passucap[username] == pwd:
                print("Approved")
                return True, "cap"
            else:
                print("Wrong password")
        elif passusol.get(username):
            if passusol[username] == pwd:
                print("Approved")
                return True, "sol"
            else:
                print("Wrong password")
        else:
            print("wrong username")
            brp += 1
    return False, "break"
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# %% [markdown]
# # This is the main code
# 

# %%
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#The core program
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
while True:
    stithi, role = auth()
    if stithi:
        if role == "cap":
            print("Welcome aboard captain")
        if role == "sol":
            print("Welcome on soldier")
    else:
        print("You entered the wrong credentials, exiting")
        break
    # Example: List all assault rifles
    for rifle, caliber in armory["Primary_Weapons"]["Assault_Rifles"].items():
        print(rifle, "-", caliber)

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~



