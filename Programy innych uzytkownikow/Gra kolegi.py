import random
from enum import IntEnum
playerGold = 10000
 
Options = IntEnum('Options', 'CommonChest, RareChest, EpicChest, LegendaryChest, AddCredits, Equipment, End')
 
commonChest = ["Glock 20 C(Common)", "ASG DL60(Rare)", "Desert Eagle(Epic)", "AK-47 Gold Edition(Legendary)"]
rareChest = ["MP5A4(Common)", "M4A1(Rare)", "Revolver R8(Epic)", "M4A4(Legendary)"]
epicChest = ["AUG(Common)", "P90(Rare)", "PP-Bizon(Epic)", "Gold Knife(Legendary)"]
legendaryChest = ["AWP(Rare)", "FAMAS(Epic)", "Butterfly Knife(Legendary)", "Bowie Knife(Legendary)"]
equipment = []
while(True):
    choice = int(input(f"""Your credits:{playerGold}
What you want to do?
1 - Open common chest(1000 credits)
2 - Open rare chest(2500 credits)
3 - Open epic chest(4000 credits)
4 - Open legendary chest(6000 credits)
5 - Add credits
6 - If you see your credits
7 - End
:
"""))
    if playerGold <= 0:
        print("Add credits to your account.")
        if choice == Options.AddCredits:
            howMuch = int(input("How much credits to add:"))
            playerGold += howMuch
        continue
    elif choice == Options.CommonChest:
        chest = random.choices(commonChest, [60, 25, 14, 1])[0]
        playerGold = playerGold - 1000
        equipment.append(chest)
        print(f"Your reward is: {chest}")
    elif choice == Options.RareChest:
        chest = random.choices(rareChest, [50, 35, 13, 2])[0]
        playerGold = playerGold - 2500
        equipment.append(chest)
        print(f"Your reward is: {chest}")
    elif choice == Options.EpicChest:
        chest = random.choices(epicChest, [40,35, 22, 3])[0]
        playerGold = playerGold - 4000
        equipment.append(chest)
        print(f"Your reward is: {chest}")
    elif choice == Options.LegendaryChest:
        chest = random.choices(legendaryChest, [50, 45, 3, 2])[0]
        playerGold = playerGold - 6000
        equipment.append(chest)
        print(f"Your reward is: {chest}")
    elif choice == Options.AddCredits:
        howMuch = int(input("How much credits to add:"))
        playerGold += howMuch
    elif choice == Options.Equipment:
        print(f"Your equipment: {equipment}")
    elif choice == Options.End:
        break
    else:
        print("Wrong option, try again!")
 
    print("")
 