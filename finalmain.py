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
# ### The authenticator for passwords

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


#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#Weapons
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~





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
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


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

# %%



