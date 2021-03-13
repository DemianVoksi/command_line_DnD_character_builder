#!/usr/bin/env python

# imports

import weapons
import armor
import races
import classes
import subclasses

# functions


def barbarianequipment():
    '''Chooses equipment for a barbarian.
    Called by __main__.'''
    print("It's time to choose two pieces of equipment: ")

    while True:
        barbarianwchoice1 = str(input("If you want to choose a greataxe, press (1). I you want to choose between any martial melee weapon, press (2). "))
        if barbarianwchoice1 == ('1'):
            barbarianwchoice1 = 'greataxe'
            weapons.charweaponschoice.append(barbarianwchoice1)
            break
        elif barbarianwchoice1 == ('2'):
            while True:
                print(f"Choose between the following: {weapons.martial_melee_weapons} ")
                barbarianwchoice1 = str(input("What is your weapon going to be? "))
                if barbarianwchoice1 in weapons.martial_melee_weapons:
                    weapons.charweaponschoice.append(barbarianwchoice1)
                    break
                else:
                    print("Please choose a weapon from the list. Write in lowercase letters.")
            break
        else:
            print("Please choose 1 or 2.")

    while True:
        barbarianwchoice2 = str(input("If you want to choose two handaxes, press (1). I you want to choose between any simple weapon, press (2). "))
        if barbarianwchoice2 == ('1'):
            barbarianwchoice2 = 'two handaxes'
            weapons.charweaponschoice.append(barbarianwchoice2)
            break
        elif barbarianwchoice2 == ('2'):
            while True:
                print(f"Choose between the following: {weapons.simple_weapons}")
                barbarianwchoice2 = str(input("What is your weapon going to be? "))
                if barbarianwchoice2 in weapons.simple_weapons:
                    weapons.charweaponschoice.append(barbarianwchoice2)
                    break
                else:
                    print("Please choose a weapon from the list. Write in lowercase letters.")
            break
        else:
            print("Please choose 1 or 2.")

    print('\n')
    print("You also get an explorer's pack and four javelins.")
    armor.charequipmentchoice.append("explorer's pack")
    weapons.charweaponschoice.append('four javelins')
    print(f"Your weapons are: {weapons.charweaponschoice}")
    print(f"Your equipment is: {armor.charequipmentchoice}")


def bardequipment():
    '''Chooses equipment for a bard.
    Called by __main__.'''
    print("It's time to choose three pieces of equipment.")

    while True:
        bardwchoice1 = str(input("If you want to choose a rapier, press (1). If you want to choose a longsword, press (2). If you want to choose any simple weapon press (3). "))
        if bardwchoice1 == ('1'):
            bardwchoice1 = 'rapier'
            weapons.charweaponschoice.append(bardwchoice1)
            break
        elif bardwchoice1 == ('2'):
            bardwchoice1 = 'longsword'
            weapons.charweaponschoice.append(bardwchoice1)
            break
        elif bardwchoice1 == ('3'):
            while True:
                print(f"You can choose from: {weapons.simple_weapons}")
                bardwchoice1 = str(input("Choose one: "))
                if bardwchoice1 in weapons.simple_weapons:
                    weapons.charweaponschoice.append(bardwchoice1)
                    break
                else:
                    print("Make sure you write the name of your choice in lowercase letters.")
            break
        else:
            print("Please choose 1, 2 or 3.")

    while True:
        bardeqchoice1 = str(input("If you want a diplomat's pack, press (1). If you want an explorer's pack, press (2). "))
        if bardeqchoice1 == ('1'):
            bardeqchoice1 = "diplomat's pack"
            armor.charequipmentchoice.append(bardeqchoice1)
            break
        elif bardeqchoice1 == ('2'):
            bardeqchoice1 = "explorer's pack"
            armor.charequipmentchoice.append(bardeqchoice1)
            break
        else:
            print("Please choose 1 or 2.")

    while True:
        bardeqchoice2 = str(input("If you want a lute, press (1). If you want any musical instrument you can think of, press (2). "))
        if bardeqchoice2 == ('1'):
            bardeqchoice2 = "lute"
            armor.charequipmentchoice.append(bardeqchoice2)
            break
        elif bardeqchoice2 == ('2'):
            bardeqchoice2 = "any musical instrument"
            armor.charequipmentchoice.append(bardeqchoice2)
            break
        else:
            print("Please choose 1 or 2.")

    print('\n')
    print("You also get leather armor and a dagger.")
    armor.chararmorchoice.append('leather')
    weapons.charweaponschoice.append('dagger')
    print(f"Your weapons are: {weapons.charweaponschoice}")
    print(f"Your armor is: {armor.chararmorchoice}")
    print(f"Your equipment is: {armor.charequipmentchoice}")


def clericequipment():
    '''Chooses equipment for a cleric.
    Called by __main__.'''
    print("It's time to choose four pieces of equipment: ")

    if 'warhammer' in races.char_race.weaponsprof or 'warhammer' in classes.char_class.weaponsprof or 'warhammer' in subclasses.char_subclass_prof or 'martial weapons' in races.char_race.weaponsprof or 'martial weapons' in classes.char_class.weaponsprof or 'martial weapons' in subclasses.char_subclass_prof or 'melee weapons' in races.char_race.weaponsprof or 'melee weapons' in classes.char_class.weaponsprof or 'melee weapons' in subclasses.char_subclass_prof or 'martial melee weapons' in races.char_race.weaponsprof or 'martial melee weapons' in classes.char_class.weaponsprof or 'martial melee weapons' in subclasses.char_subclass_prof:
        print("Time to choose your first piece of equipment!")
        print("Press (1) to choose a mace or press (2) to choose a warhammer.")
        while True:
            clericwchoice1 = str(input("Press (1) or (2): "))
            if clericwchoice1 == ('1'):
                clericwchoice1 = 'mace'
                weapons.charweaponschoice.append(clericwchoice1)
                break
            elif clericwchoice1 == ('2'):
                clericwchoice1 = 'warhammer'
                weapons.charweaponschoice.append(clericwchoice1)
                break
            else:
                print("Choose 1 or 2.")
            break
    else:
        clericwchoice1 = 'mace'
        weapons.charweaponschoice.append(clericwchoice1)

    if 'chain mail' in races.char_race.armorprof or 'chain mail' in classes.char_class.armorprof or 'chain mail' in subclasses.char_subclass_prof or 'medium armor' in races.char_race.armorprof or 'medium armor' in classes.char_class.armorprof or 'medium armor' in subclasses.char_subclass_prof:
        print("Time to choose your first piece of armor!")
        print("Press (1) to choose scale mail, press (2) to choose leather armor and press (3) to choose chain mail.")
        while True:
            clericachoice1 = str(input("Press (1), (2) or (3): "))
            if clericachoice1 == ('1'):
                clericachoice1 = 'scale mail'
                armor.chararmorchoice.append(clericachoice1)
                break
            elif clericachoice1 == ('2'):
                clericachoice1 = 'leather armor'
                armor.chararmorchoice.append(clericachoice1)
                break
            elif clericachoice1 == ('3'):
                clericachoice1 = 'chain mail'
                armor.chararmorchoice.append(clericachoice1)
                break
            else:
                print("Choose 1, 2 or 3.")
    else:
        print("Press (1) to choose scale mail or press (2) to choose leather armor.")

    while True:
        clericwchoice2 = str(input("Press (1) for a light crossbow and (2) to choose between any simple weapon."))
        if clericwchoice2 == ('1'):
            clericwchoice2 = 'light crossbow'
            weapons.charweaponschoice.append(clericwchoice2)
            break
        elif clericwchoice2 == ('2'):
            print(f"Please choose between: {weapons.simple_weapons}")
            while True:
                clericwchoice2 = str(input("Choose one: "))
                if clericwchoice2 in weapons.simple_weapons:
                    weapons.charweaponschoice.append(clericwchoice2)
                    break
                else:
                    print("Please use lowercase letters.")
            break
        else:
            print("Press 1 or 2.")

    print("Choose between a priest's pack and an explorer's pack.")
    while True:
        clericeqchoice1 = str(input("Press (1) for the priest's pack and (2) for the explorer's pack."))
        if clericeqchoice1 == ('1'):
            clericeqchoice1 = "priest's pack"
            armor.charequipmentchoice.append(clericeqchoice1)
            break
        elif clericeqchoice1 == ('2'):
            clericeqchoice1 = "explorer's pack"
            armor.charequipmentchoice.append(clericeqchoice1)
            break
        else:
            print("Please press 1 or 2.")

    print('\n')
    print("You also get a shield and a holy symbol.")
    armor.chararmorchoice.append('shield')
    armor.charequipmentchoice.append('holy symbol')
    print(f"Your weapons are: {weapons.charweaponschoice}")
    print(f"Your armor is: {armor.chararmorchoice}")
    print(f"Your equipment is: {armor.charequipmentchoice}")


def druidequipment():
    '''Chooses equipment for a druid.
    Called by __main__.'''
    print("It's time to choose two pieces of equipment.")
    print("To choose a wooden shield, press (1) and to choose any simple weapon, press (2). ")
    while True:
        druidchoice1 = str(input("Which one do you choose? "))
        if druidchoice1 == ('1'):
            druidchoice1 = 'wooden shield'
            armor.chararmorchoice.append(druidchoice1)
            break
        elif druidchoice1 == ('2'):
            print(f"Choose between the following: {weapons.simple_weapons}")
            while True:
                druidchoice1 = str(input("Please choose one: "))
                if druidchoice1 in weapons.simple_weapons:
                    weapons.charweaponschoice.append(druidchoice1)
                    break
                else:
                    print("Make sure you write your choice from the list in lowercase letters.")
            break
        else:
            print("Please choose 1 or 2.")

    print("To choose a scimitar, press (1), and to choose between any simple melee weapon, press ('2')")
    while True:
        druidwchoice1 = str(input("Which one do you choose? "))
        if druidwchoice1 == ('1'):
            druidwchoice1 = 'scimitar'
            weapons.charweaponschoice.append(druidwchoice1)
            break
        elif druidwchoice1 == ('2'):
            print(f"Choose between the following: {weapons.simple_melee_weapons}")
            while True:
                druidwchoice1 = str(input("Please choose one: "))
                if druidwchoice1 in weapons.simple_melee_weapons:
                    weapons.charweaponschoice.append(druidwchoice1)
                    break
                else:
                    print("Make sure you write your choice from the list in lowercase letters.")
            break
        else:
            print("Please choose 1 or 2.")

    print('\n')
    print("You also get leather armor, an explorer's pack and druidic focus.")
    armor.charequipmentchoice.append("druidic focus")
    armor.charequipmentchoice.append("explorer's pack")
    armor.chararmorchoice.append('leather')
    print(f"Your weapons are: {weapons.charweaponschoice}")
    print(f"Your armor is: {armor.chararmorchoice}")
    print(f"Your equipment is: {armor.charequipmentchoice}")


def fighterequipment():
    '''Chooses equipment for a fighter.
    Called by __main__.'''
    print("It is time to choose several pieces of equipment. ")
    print("Press (1) if you want to choose leather armor and a longbow, or press (2) if you want to choose a chain mail.")
    while True:
        fighterchoice1 = str(input("Press 1 or 2: "))
        if fighterchoice1 == ('1'):
            weapons.charweaponschoice.append('longbow')
            armor.chararmorchoice.append('leather')
            break
        elif fighterchoice1 == ('2'):
            armor.chararmorchoice.append('chain mail')
            break
        else:
            print("Please choose 1 or 2.")

    print("Press (1) to choose a dungeoneer's pack or press (2) to choose an explorer's pack.")
    while True:
        fightereqchoice1 = str(input("Please press 1 or 2: "))
        if fightereqchoice1 == ('1'):
            armor.charequipmentchoice.append("dungeoneer's pack")
            break
        elif fightereqchoice1 == ('2'):
            armor.charequipmentchoice.append("explorer's pack")
            break
        else:
            print("Please choose 1 or 2.")

    print("Press (1) to choose a shield and any martial weapon or press (2) to choose two martial weapons.")
    while True:
        fightereqchoice2 = str(input("Please press 1 or 2: "))
        if fightereqchoice2 == ('1'):
            armor.chararmorchoice.append('shield')
            print(f"Now choose any of the following: {weapons.martial_weapons}")
            while True:
                fightereqchoice3 = str(input("Choose one: "))
                if fightereqchoice3 in weapons.martial_weapons:
                    weapons.charweaponschoice.append(fightereqchoice3)
                    break
                else:
                    print("Please make sure you write your choice in lowercase letters.")
            break
        elif fightereqchoice2 == ('2'):
            print(f"You can choose two weapons from this list: {weapons.martial_weapons}")
            while True:
                fightereqchoice2 = str(input("Which is the first one? "))
                if fightereqchoice2 in weapons.martial_weapons:
                    weapons.charweaponschoice.append(fightereqchoice2)
                    break
                else:
                    print("Please make sure you write your choice in lowercase letters.")
            print("Now choose the second one.")
            while True:
                fightereqchoice4 = str(input("Choose one: "))
                if fightereqchoice4 in weapons.martial_weapons:
                    weapons.charweaponschoice.append(fightereqchoice4)
                    break
                else:
                    print("Please make sure you write your choice in lowercase letters.")
            break
        else:
            print("Please press 1 or 2")

    print("Press (1) to choose a light crossbow or press (2) to choose 2 martial weapons.")
    while True:
        fighterchoice2 = str(input("Choose 1 or 2: "))
        if fighterchoice2 == ('1'):
            weapons.charweaponschoice.append('light crossbow')
            break
        elif fighterchoice2 == ('2'):
            print(f"Please choose the first weapon from this list: {weapons.martial_weapons}")
            while True:
                fighterchoice2 = str(input("So, which one is it going to be? "))
                if fighterchoice2 in weapons.martial_weapons:
                    weapons.charweaponschoice.append(fighterchoice2)
                    break
                else:
                    print("Please make sure you write your choice in lowercase letters.")
            print(f"Please choose the second weapon from this list: {weapons.martial_weapons}")
            while True:
                fighterchoice3 = str(input("So, which one is it going to be? "))
                if fighterchoice3 in weapons.martial_weapons:
                    weapons.charweaponschoice.append(fighterchoice3)
                    break
                else:
                    print("Please make sure you write your choice in lowercase letters.")
            break
        else:
            print("Please choose 1 or 2.")

    print('\n')
    print(f"Your weapons are: {weapons.charweaponschoice}")
    print(f"Your armor is: {armor.chararmorchoice}")
    print(f"Your equipment is: {armor.charequipmentchoice}")


def monkequipment():
    '''Chooses equipment for a monk.
    Called by __main__.'''
    print("It is time to choose two pieces of equipment.")
    print("Press (1) to choose a shortsword or press (2) to choose any simple weapon.")
    while True:
        monkwchoice1 = str(input("Choose 1 or 2: "))
        if monkwchoice1 == ('1'):
            weapons.charweaponschoice.append('shortsword')
            break
        elif monkwchoice1 == ('2'):
            print(f"You can choose from the following: {weapons.simple_weapons}")
            while True:
                monkwchoice1 = str(input("Choose one: "))
                if monkwchoice1 in weapons.simple_weapons:
                    weapons.charweaponschoice.append(monkwchoice1)
                    break
                else:
                    print("Please make sure you write your choice in lowercase letters.")
            break
        else:
            print("Please choose 1 or 2.")

    print("Press (1) to choose a dungeoneer's pack or press (2) to choose an explorer's pack.")
    while True:
        monkeqchoice1 = str(input("Choose 1 or 2: "))
        if monkeqchoice1 == ('1'):
            armor.charequipmentchoice.append("dungeoneer's pack")
            break
        elif monkeqchoice1 == ('2'):
            armor.charequipmentchoice.append("explorer's pack")
            break
        else:
            print("Please choose 1 or 2.")

    print('\n')
    print("You also get ten darts.")
    weapons.charweaponschoice.append('ten darts')
    print(f"Your weapons are: {weapons.charweaponschoice}")
    print(f"Your armor is: {armor.chararmorchoice}")
    print(f"Your equipment is: {armor.charequipmentchoice}")


def paladinequipment():
    '''Chooses equipment for a paladin.
    Called by __main__.'''
    print("It is time to choose several pieces of equipment.")
    print("Press (1) to choose a shield and any martial weapon or press (2) to choose two martial weapons.")
    while True:
        paladineqchoice1 = str(input("Choose 1 or 2: "))
        if paladineqchoice1 == ('1'):
            armor.chararmorchoice.append('shield')
            print(f"Please choose a weapon from the list: {weapons.martial_weapons}")
            while True:
                paladineqchoice2 = str(input("Please choose a weapon from the list: "))
                if paladineqchoice2 in weapons.martial_weapons:
                    weapons.charweaponschoice.append(paladineqchoice2)
                    break
                else:
                    print("Make sure you write your choice in lowercase letters.")
            break
        elif paladineqchoice1 == ('2'):
            print(f"You can choose two weapons from this list: {weapons.martial_weapons}")
            while True:
                paladinwchoice1 = str(input("Choose the first one: "))
                if paladinwchoice1 in weapons.martial_weapons:
                    weapons.charweaponschoice.append(paladinwchoice1)
                    break
                else:
                    print("Make sure you write your choice in lowercase letters.")
            print("Choose the second one.")
            while True:
                paladinwchoice2 = str(input("Choose: "))
                if paladinwchoice2 in weapons.martial_weapons:
                    weapons.charweaponschoice.append(paladinwchoice2)
                    break
                else:
                    print("Make sure you write your choice in lowercase letters.")
            break
        else:
            print("Please choose 1 or 2.")

    print("Press (1) to choose five javelins or press (2) to choose a simple melee weapon.")
    while True:
        paladinwchoice3 = str(input("Press 1 or 2: "))
        if paladinwchoice3 == ('1'):
            weapons.charweaponschoice.append('five javelins')
            break
        elif paladinwchoice3 == ('2'):
            print(f"Please choose a weapon from the list: {weapons.simple_melee_weapons}")
            while True:
                paladinwchoice3 = str(input("Choose a weapon: "))
                if paladinwchoice3 in weapons.simple_melee_weapons:
                    weapons.charweaponschoice.append(paladinwchoice3)
                    break
                else:
                    print("Make sure you write your choice in lowercase letters.")
            break
        else:
            print("Please choose 1 or 2.")

    print("Press (1) to choose a priest's pack or press (2) to choose an explorer's pack.")
    while True:
        paladineqchoice3 = str(input("Press 1 or 2: "))
        if paladineqchoice3 == ('1'):
            armor.charequipmentchoice.append("priest's pack")
            break
        elif paladineqchoice3 == ('2'):
            armor.charequipmentchoice.append("explorer's pack")
            break
        else:
            print("Please choose 1 or 2.")

    print('\n')
    print("You also get a holy symbol and chain mail.")
    armor.charequipmentchoice.append('holy symbol')
    armor.chararmorchoice.append('chain mail')
    print(f"Your weapons are: {weapons.charweaponschoice}")
    print(f"Your armor is: {armor.chararmorchoice}")
    print(f"Your equipment is: {armor.charequipmentchoice}")


def rangerequipment():
    '''Chooses equipment for a ranger.
    Called by __main__.'''
    print("It is time to choose several pieces of equipment.")
    print("Press (1) to choose scale mail or press (2) to choose leather armor.")
    while True:
        rangereqchoice1 = str(input("Choose one: "))
        if rangereqchoice1 == ('1'):
            armor.chararmorchoice.append('scale mail')
            break
        elif rangereqchoice1 == ('2'):
            armor.chararmorchoice.append('leather')
            break
        else:
            print("Please choose 1 or 2.")

    print("Press (1) to choose two shortswords or press (2) to choose two simple melee weapons.")
    while True:
        rangerwchoice1 = str(input("Press 1 or 2: "))
        if rangerwchoice1 == ('1'):
            weapons.charweaponschoice.append('two shortswords')
            break
        elif rangerwchoice1 == ('2'):
            print(f"Choose two weapons from {weapons.simple_melee_weapons}")
            while True:
                rangerwchoice1 = str(input("Choose the first one: "))
                if rangerwchoice1 in weapons.simple_melee_weapons:
                    weapons.charweaponschoice.append(rangerwchoice1)
                    break
                else:
                    print("Please write your choice in lowercase letters.")
            while True:
                rangerwchoice2 = str(input("Choose the second one: "))
                if rangerwchoice2 in weapons.simple_melee_weapons:
                    weapons.charweaponschoice.append(rangerwchoice2)
                    break
                else:
                    print("Please write your choice in lowercase letters.")
            break
        else:
            print("Please choose 1 or 2.")

    print("Press (1) to choose a dungeoneer's pack or press (2) to choose an explorer's pack.")
    while True:
        rangereqchoice2 = str(input("Please choose 1 or 2: "))
        if rangereqchoice2 == ('1'):
            armor.charequipmentchoice.append("dungeoneer's pack")
            break
        elif rangereqchoice2 == ('2'):
            armor.charequipmentchoice.append("explorer's pack")
            break
        else:
            print("Please choose 1 or 2")

    print('\n')
    print("You also get a longbow.")
    weapons.charweaponschoice.append('longbow')
    print(f"Your weapons are: {weapons.charweaponschoice}")
    print(f"Your armor is: {armor.chararmorchoice}")
    print(f"Your equipment is: {armor.charequipmentchoice}")


def rogueequipment():
    '''Chooses equipment for a rogue.
    Called by __main__.'''
    print("It is time to choose several pieces of equipment.")
    print("Press (1) to choose a rapier or press (2) to choose a shortsword.")
    while True:
        roguewchoice1 = str(input("Press 1 or 2: "))
        if roguewchoice1 == ('1'):
            weapons.charweaponschoice.append('rapier')
            break
        elif roguewchoice1 == ('2'):
            weapons.charweaponschoice.append('shortsword')
            break
        else:
            print("Press 1 or 2.")

    print("Press (1) to choose a shortbow or press (2) to choose a shortsword.")
    while True:
        roguewchoice2 = str(input("Press 1 or 2: "))
        if roguewchoice2 == ('1'):
            weapons.charweaponschoice.append('shortbow')
            break
        elif roguewchoice2 == ('2'):
            weapons.charweaponschoice.append('shortsword')
            break
        else:
            print("Press 1 or 2.")

    print("Press (1) to choose a burglar's pack, (2) to choose a dungeoneer's pack or (3) to choose an explorer's pack.")
    while True:
        rogueeqchoice1 = str(input("Please press 1, 2 or 3: "))
        if rogueeqchoice1 == ('1'):
            armor.charequipmentchoice.append("burglar's pack")
            break
        elif rogueeqchoice1 == ('2'):
            armor.charequipmentchoice.append("dungeoneer's pack")
            break
        elif rogueeqchoice1 == ('3'):
            armor.charequipmentchoice.append("explorer's pack")
            break
        else:
            print("Please choose 1, 2, or 3.")

    print('\n')
    print("You also get leather armor, two daggers and thieves' tools.")
    armor.chararmorchoice.append('leather')
    weapons.charweaponschoice.append('two daggers')
    armor.charequipmentchoice.append("thieves' tools")
    print(f"Your weapons are: {weapons.charweaponschoice}")
    print(f"Your armor is: {armor.chararmorchoice}")
    print(f"Your equipment is: {armor.charequipmentchoice}")


def sorcererequipment():
    '''Chooses equipment for a sorcerer.
    Called by __main__.'''
    print("Its is time to choose several pieces of equipment.")
    print("Press (1) to choose a light crossbow or press (2) to choose any simple weapon.")
    while True:
        sorcererwchoice1 = str(input("Press 1 or 2: "))
        if sorcererwchoice1 == ('1'):
            weapons.charweaponschoice.append('light crossbow')
            break
        elif sorcererwchoice1 == ('2'):
            print(f"You can choose from: {weapons.simple_weapons}")
            while True:
                sorcererwchoice1 = str(input("Which one do you choose? "))
                if sorcererwchoice1 in weapons.simple_weapons:
                    weapons.charweaponschoice.append(sorcererwchoice1)
                    break
                else:
                    print("Make sure you have written your choice in lowercase letters.")
            break
        else:
            print("Please choose 1 or 2.")

    print("Press (1) to choose a component pouch or press (2) to choose arcane focus.")
    while True:
        sorcerereqchoice1 = str(input("Press 1 or 2: "))
        if sorcerereqchoice1 == ('1'):
            armor.charequipmentchoice.append('component pouch')
            break
        elif sorcerereqchoice1 == ('2'):
            armor.charequipmentchoice.append('arcane focus')
            break
        else:
            print("Please choose 1 or 2.")

    print("Press (1) to choose a dungeoneer's pack or press (2) to choose an explorer's pack.")
    while True:
        sorcerereqchoice2 = str(input("Press 1 or 2: "))
        if sorcerereqchoice2 == ('1'):
            armor.charequipmentchoice.append("dungeoneer's pack")
            break
        elif sorcerereqchoice2 == ('2'):
            armor.charequipmentchoice.append("explorer's pack")
            break
        else:
            print("Please choose 1 or 2.")

    print('\n')
    print("You also get two daggers.")
    weapons.charweaponschoice.append('two daggers')
    print(f"Your weapons are: {weapons.charweaponschoice}")
    print(f"Your armor is: {armor.chararmorchoice}")
    print(f"Your equipment is: {armor.charequipmentchoice}")


def warlockequipment():
    '''Chooses equipment for a warlock.
    Called by __main__.'''
    print("Its is time to choose several pieces of equipment.")
    print("Press (1) to choose a light crossbow or press (2) to choose any simple weapon.")
    while True:
        warlockwchoice1 = str(input("Press 1 or 2: "))
        if warlockwchoice1 == ('1'):
            weapons.charweaponschoice.append('light crossbow')
            break
        elif warlockwchoice1 == ('2'):
            print(f"You can choose from: {weapons.simple_weapons}")
            while True:
                warlockwchoice1 = str(input("Which one do you choose? "))
                if warlockwchoice1 in weapons.simple_weapons:
                    weapons.charweaponschoice.append(warlockwchoice1)
                    break
                else:
                    print("Make sure you have written your choice in lowercase letters.")
            break
        else:
            print("Please choose 1 or 2.")

    print("Press (1) to choose a component pouch or press (2) to choose arcane focus.")
    while True:
        warlockeqchoice1 = str(input("Press 1 or 2: "))
        if warlockeqchoice1 == ('1'):
            armor.charequipmentchoice.append('component pouch')
            break
        elif warlockeqchoice1 == ('2'):
            armor.charequipmentchoice.append('arcane focus')
            break
        else:
            print("Please choose 1 or 2.")

    print("Press (1) to choose a dungeoneer's pack or press (2) to choose an scholar's pack.")
    while True:
        warlockeqchoice2 = str(input("Press 1 or 2: "))
        if warlockeqchoice2 == ('1'):
            armor.charequipmentchoice.append("dungeoneer's pack")
            break
        elif warlockeqchoice2 == ('2'):
            armor.charequipmentchoice.append("scholar's pack")
            break
        else:
            print("Please choose 1 or 2.")

    print(f"You can choose any of the following weapons: {weapons.simple_weapons}")
    while True:
        warlockwchoice2 = str(input("Please choose one: "))
        if warlockwchoice2 in weapons.simple_weapons:
            weapons.charweaponschoice.append(warlockwchoice2)
            break
        else:
            print("Please make sure you have written your choice in lowercase letters.")

    print('\n')
    print("You also get leather armor and two daggers.")
    armor.chararmorchoice.append('leather')
    weapons.charweaponschoice.append('two daggers')
    print(f"Your weapons are: {weapons.charweaponschoice}")
    print(f"Your armor is: {armor.chararmorchoice}")
    print(f"Your equipment is: {armor.charequipmentchoice}")


def wizardequipment():
    '''Chooses equipment for a wizard.
    Called by __main__.'''
    print("Its is time to choose several pieces of equipment.")
    print("Press (1) to choose a quarterstaff or press (2) to choose a dagger.")
    while True:
        wizardwchoice1 = str(input("Press 1 or 2: "))
        if wizardwchoice1 == ('1'):
            weapons.charweaponschoice.append('quarterstaff')
            break
        elif wizardwchoice1 == ('2'):
            weapons.charweaponschoice.append('dagger')
            break
        else:
            print("Please choose 1 or 2.")

    print("Press (1) to choose a component pouch or press (2) to choose arcane focus.")
    while True:
        wizardeqchoice1 = str(input("Press 1 or 2: "))
        if wizardeqchoice1 == ('1'):
            armor.charequipmentchoice.append('component pouch')
            break
        elif wizardeqchoice1 == ('2'):
            armor.charequipmentchoice.append('arcane focus')
            break
        else:
            print("Please choose 1 or 2.")

    print("Press (1) to choose a scholar's pack or press (2) to an explorer's pack.")
    while True:
        wizardeqchoice2 = str(input("Press 1 or 2: "))
        if wizardeqchoice2 == ('1'):
            armor.charequipmentchoice.append("scholar's pack")
            break
        elif wizardeqchoice2 == ('2'):
            armor.charequipmentchoice.append("explorer's pack")
            break
        else:
            print("Please choose 1 or 2.")

    print('\n')
    print("You also get a spellbook.")
    armor.charequipmentchoice.append('spellbook')
    print(f"Your weapons are: {weapons.charweaponschoice}")
    print(f"Your armor is: {armor.chararmorchoice}")
    print(f"Your equipment is: {armor.charequipmentchoice}")
