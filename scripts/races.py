#!/usr/bin/env python
# imports

import copy

# class


class character_race:

    def __init__(self, name, size, speed, weaponsprof,
                 armorprof, toolsprof, raceprof, language, stre, stremod,
                 stremodified, stremodifier, dex, dexmod, dexmodified,
                 dexmodifier, con, conmod, conmodified, conmodifier, inte,
                 intemod, intemodified, intemodifier, wis, wismod, wismodified,
                 wismodifier, cha, chamod, chamodified, chamodifier):
        self.name = name
        self.size = size
        self.speed = speed
        self.weaponsprof = weaponsprof
        self.armorprof = armorprof
        self.toolsprof = toolsprof
        self.raceprof = raceprof
        self.language = language
        self.stre = stre
        self.stremod = stremod
        self.stremodified = stremodified
        self.stremodifier = stremodifier
        self.dex = dex
        self.dexmod = dexmod
        self.dexmodified = dexmodified
        self.dexmodifier = dexmodifier
        self.con = con
        self.conmod = conmod
        self.conmodified = conmodified
        self.conmodifier = conmodifier
        self.inte = inte
        self.intemod = intemod
        self.intemodified = intemodified
        self.intemodifier = intemodifier
        self.wis = wis
        self.wismod = wismod
        self.wismodified = wismodified
        self.wismodifier = wismodifier
        self.cha = cha
        self.chamod = chamod
        self.chamodified = chamodified
        self.chamodifier = chamodifier

    def stre_modified(self):
        self.stremodified = int(self.stre) + int(self.stremod)

    def dex_modified(self):
        self.dexmodified = int(self.dex) + int(self.dexmod)

    def con_modified(self):
        self.conmodified = int(self.con) + int(self.conmod)

    def inte_modified(self):
        self.intemodified = int(self.inte) + int(self.intemod)

    def wis_modified(self):
        self.wismodified = int(self.wis) + int(self.wismod)

    def cha_modified(self):
        self.chamodified = int(self.cha) + int(self.chamod)


dragonborn = character_race(
    'dragonborn', 'medium', '30 ft', '', '', '',
    'Draconic ancestry' + ', ' + 'Breath weapon' + ', ' + 'Damage resistance',
    'Common and Draconic',
    0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0
)

hill_dwarf = character_race(
    'hill dwarf', 'medium', '25 ft',
    ' Battleaxe' + ', ' + ' Handaxe' + ', ' +
    ' Throwing hammer' + ', ' + ' Warhammer', '',
    "One of: stone tools, brewer's supplies, mason's tools",
    'Stonework' + ', ' + 'Dwarven toughness' +
    ', ' + 'Darkvision 60 ft' + ', ' + 'Dwarven resilience', 'Dwarvish and Common',
    0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0
)

mountain_dwarf = character_race(
    'mountain dwarf', 'medium', '25 ft',
    ' Battleaxe' + ', ' + ' Handaxe' + ', ' + ' Throwing hammer' +
    ', ' + ' Warhammer', ' Light' + ', ' + ' Medium',
    "One of: stone tools, brewer's supplies, mason's tools",
    'Stonework' + ', ' + 'Darkvision 60 ft' + ', ' +
    'Dwarven resilience', 'Dwarvish' + ', ' + 'Common',
    0, 2, 0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0
)

high_elf = character_race(
    'high elf', 'medium', '30 ft',
    ' Longsword' + ', ' + ' Shortsword' + ', ' +
    ' Longbow' + ', ' + ' Shortbow', '', '',
    'Key senses' + ', ' + 'Fey ancestry' + ', ' +
    'Trance' + ', ' + 'Extra wizard cantrip' +
    ', ' + 'Darkvision 60 ft', 'Elvish' + ', ' +
    'Common' + ', ' + 'Any extra language',
    0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0
)

wood_elf = character_race(
    'wood elf', 'medium', '35 ft', ' Longsword' +
    ', ' + ' Shortsword' + ', ' + ' Longbow' + ', ' + ' Shortbow',
    '', '', 'Mask of the wild' + ', ' + 'Darkvision 60 ft' + ', ' +
    'Keen senses' + ', ' + 'Fey ancestry' + ', ' + 'Trance', 'Elvish' +
    ', ' + 'Common',
    0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0
)

drow = character_race(
    'drow', 'medium', '30 ft', ' Rapier' + ', ' +
    ' Shortsword' + ', ' + ' Hand crossbow', '', '',
    'Keen senses' + ', ' + 'Fey ancestry' + ', ' + 'Trance' +
    ', ' + 'Darkvision 120 ft' + ', ' + 'Sunlight sensitivity' +
    ', ' + 'Drow magic', 'Elvish' + ', ' + 'Common',
    0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0
)

forest_gnome = character_race(
    'forest gnome', 'small', '25 ft', '', '', '',
    'Natural illusionist' + ', ' + 'Speak with small beasts' +
    ', ' + 'Gnome cunning' + ', ' + 'Darkvision 60 ft',
    'Common' + ', ' + 'Gnomish',
    0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0
)

rock_gnome = character_race(
    'rock gnome', 'small', '25 ft', '', '', '',
    "Artificer's lore" + ', ' + 'Tinker' + ', ' +
    'Clockwork toy' + ', ' + 'Fire starter' + ', ' +
    'Music box' + ', ' + 'Darkvision 60 ft' + ', ' +
    'Gnome cunning', 'Common' + ', ' + 'Gnomish',
    0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0
)

half_elf = character_race(
    'half elf', 'medium', '30 ft', '', '', '',
    'Darkvision 60 ft' + ', ' + 'Fey ancestry' + ', ' +
    'Skill versatility', 'Common' + ', ' + 'Elvish' +
    ', ' + 'Any extra language',
    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 0, 0
)

half_orc = character_race(
    'half orc', 'medium', '30 ft', '', '', '',
    'Darkvision 60 ft' + ', ' + 'Menacing' + ', ' +
    'Relentless endurance' + ', ' + 'Savage attacks',
    'Common' + ', ' + 'Orc',
    0, 2, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0
)

lightfoot_halfling = character_race(
    'lightfoot halfling', 'small', '25 ft',
    '', '', '', 'Naturally stealthy' + ', ' + 'Lucky' +
    ', ' + 'Brave' + ', ' + 'Halfling nimbleness', 'Common' +
    ', ' + 'Halfling',
    0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0
)

stout_halfling = character_race(
    'stout halfling', 'small', '25 ft', '', '', '',
    'Stout resilience' + ', ' + 'Lucky' + ', ' + 'Brave' +
    ', ' + 'Halfling nimbleness', 'Common' + ', ' + 'Halfling',
    0, 0, 0, 0, 0, 2, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0
)

human = character_race(
    'human', 'medium', '30 ft', '', '', '', '', 'Human' +
    ', ' + 'Any extra language',
    0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0
)

tiefling = character_race(
    'tiefling', 'medium', '30 ft', '', '', '',
    'Darkvision 60 ft' + ', ' + 'Hellish resistance' +
    ', ' + 'Infernal legacy', 'Common' + ', ' + 'Infernal',
    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 2, 0, 0
)

craces = [
    dragonborn, hill_dwarf, mountain_dwarf, high_elf, wood_elf,
    drow, forest_gnome, rock_gnome, half_elf, half_orc,
    lightfoot_halfling, stout_halfling, human, tiefling
]

races = [
    'dragonborn', 'hill dwarf', 'mountain dwarf', 'high elf',
    'wood elf', 'drow', 'forest gnome', 'rock gnome', 'half elf',
    'half orc', 'lightfoot halfling', 'stout halfling', 'human', 'tiefling'
]

char_race = ()


# functions


def race_choice(list_choice, classlist):
    '''Chooses a race. List_choice is races. Classlist is craces.
    Deepcopies it into a variable char_race.
    Called by ridentitytovariable()'''
    print(f"It is time to choose your race. Choose betwen: {list_choice}")

    while True:
        identity_choice = str(input("What is your race going to be? "))
        if identity_choice in list_choice:
            break
        else:
            print("Please enter the name of your race in lowercase letters.")

    for n in classlist:
        if identity_choice in n.name:
            identity_choice = copy.deepcopy(n)
            break
        else:
            pass

    return identity_choice


def ridentitytovariable():
    '''Turns the char_race variable into a class of a chosen race.'''
    global char_race
    char_race = race_choice(races, craces)


def print_racial_proficiencies():
    '''Prints your racial proficiencies.'''
    print("\n")
    print("Your racial proficiencies are:")
    print(f"Weapons: {char_race.weaponsprof}")
    print(f"Armor: {char_race.armorprof}")
    print(f"Tools: {char_race.toolsprof}")
    print(f"Languages: {char_race.language}")
    print(f"Other: {char_race.raceprof}")
