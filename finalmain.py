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
username = input("Enter your name")
pwd = getpass("Password : ")

print(username)


# %%



# %%



