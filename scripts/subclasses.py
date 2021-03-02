#!/usr/bin/env python

# imports

import copy
import classes

# class


class subclass:

    def __init__(self, name, masterclass, startinglevel, perks):

        self.name = name
        self.masterclass = masterclass
        self.startinglevel = startinglevel
        self.perks = perks


path_berserker = subclass(
    'path of the berserker', 'barbarian', 3, ''
)
path_totem_warrior_bear = subclass(
    'path of the totem warrior-bear', 'barbarian', 3, ''
)
path_totem_warrior_eagle = subclass(
    'path of the totem warrior-eagle', 'barbarian', 3, ''
)
path_totem_warrior_wolf = subclass(
    'path of the totem warrior-wolf', 'barbarian', 3, ''
)

college_lore = subclass('college of lore', 'bard', 3, '')
college_valor = subclass('college of valor', 'bard', 3, '')

knowledge_domain = subclass('knowledge domain', 'cleric', 1, '')
life_domain = subclass('life domain', 'cleric', 1, '')
light_domain = subclass('light domain', 'cleric', 1, '')
nature_domain = subclass('nature domain', 'cleric', 1, '')
tempest_domain = subclass('tempest domain', 'cleric', 1, '')
trickery_domain = subclass('trickery domain', 'cleric', 1, '')
war_domain = subclass('war domain', 'cleric', 1, '')

circle_land = subclass('circle of the land', 'druid', 2, '')
circle_moon = subclass('circle of the moon', 'druid', 2, '')

battle_master = subclass('battle master', 'fighter', 3, '')
champion = subclass('champion', 'fighter', 3, '')
eldrich_knight = subclass('eldrich knight', 'fighter', 3, '')

way_four_elements = subclass('way of the four elements', 'monk', 3, '')
way_open_hand = subclass('way of the open hand', 'monk', 3, '')
way_shadow = subclass('way of the shadow', 'monk', 3, '')

oath_of_the_ancients = subclass('oath of the ancients', 'paladin', 3, '')
oath_of_devotion = subclass('oath of devotion', 'paladin', 3, '')
oath_of_vengeance = subclass('oath of vengeance', 'paladin', 3, '')

beast_master = subclass('beast master', 'ranger', 3, '')
hunter = subclass('hunter', 'ranger', 3, '')

arcane_trickster = subclass('arcane trickster', 'rogue', 3, '')
assassin = subclass('assassin', 'rogue', 3, '')
thief = subclass('thief', 'rogue', 3, '')

draconic_bloodline = subclass('draconic bloodline', 'sorcerer', 1, '')
wild_magic = subclass('wild magic', 'sorcerer', 1, '')

the_archfey = subclass('the archfey', 'warlock', 1, '')
the_fiend = subclass('the fiend', 'warlock', 1, '')
the_great_old_one = subclass('the great old one', 'warlock', 1, '')

abjuration = subclass('abjuration', 'wizard', 2, '')
conjuration = subclass('conjuration', 'wizard', 2, '')
divination = subclass('divination', 'wizard', 2, '')
enchantment = subclass('enchantment', 'wizard', 2, '')
evocation = subclass('evocation', 'wizard', 2, '')
illusion = subclass('illusion', 'wizard', 2, '')
necromancy = subclass('necromancy', 'wizard', 2, '')
transmutation = subclass('transmutation', 'wizard', 2, '')

char_subclass = ()

# lists

csubclasses = [
    path_berserker, path_totem_warrior_bear, path_totem_warrior_eagle,
    path_totem_warrior_wolf, college_lore, college_valor, knowledge_domain,
    life_domain, light_domain, nature_domain, tempest_domain, trickery_domain,
    circle_land, circle_moon, battle_master, champion, eldrich_knight,
    way_four_elements, way_open_hand, way_shadow, oath_of_devotion,
    oath_of_the_ancients, oath_of_vengeance, beast_master, hunter,
    arcane_trickster, assassin, thief, draconic_bloodline, wild_magic,
    the_archfey, the_fiend, the_great_old_one, abjuration, conjuration,
    divination, enchantment, evocation, illusion, necromancy, transmutation
]

csubclasses_barbarian = [
    path_berserker, path_totem_warrior_bear, path_totem_warrior_eagle,
    path_totem_warrior_wolf
]

csubclasses_bard = [
    college_lore, college_valor
]

csubclasses_cleric = [
    knowledge_domain, life_domain, light_domain,
    nature_domain, tempest_domain, trickery_domain
]

csubclasses_druid = [
    circle_land, circle_moon
]

csubclasses_fighter = [
    battle_master, champion, eldrich_knight
]

csubclasses_monk = [
    way_four_elements, way_open_hand, way_shadow
]

csubclasses_paladin = [
    oath_of_devotion, oath_of_the_ancients, oath_of_vengeance
]

csubclasses_ranger = [
    beast_master, hunter
]

csubclasses_rogue = [
    arcane_trickster, assassin, thief
]

csubclasses_sorcerer = [
    draconic_bloodline, wild_magic
]

csubclasses_warlock = [
    the_archfey, the_fiend, the_great_old_one
]

csubclasses_wizard = [
    abjuration, conjuration, divination, enchantment,
    evocation, illusion, necromancy, transmutation
]


subclasses = [
    'path of the berserker', 'path of the totem warrior-bear',
    'path of the totem warrior-eagle', 'path of the totem warrior-wolf',
    'college of lore', 'college of valor', 'knowledge domain', 'life domain',
    'light domain', 'nature domain', 'tempest domain', 'trickery domain',
    'circle of the land', 'circle of the moon', 'battle master',
    'champion', 'eldrich knight', 'way of the four elements',
    'way of the open hand', 'way of the shadow',
    'oath of devotion', 'oath of the ancients', 'oath of vengeance',
    'beast master', 'hunter', 'arcane trickster',
    'assassin', 'thief', 'draconic bloodline', 'wild magic', 'the archfey',
    'the fiend', 'the great old one', 'abjuration', 'conjuration',
    'divination', 'enchantment', 'evocation',
    'illusion', 'necromancy', 'transmutation'
]

subclasses_barbarian = [
    'path of the berserker', 'path of the totem warrior-bear',
    'path of the totem warrior-eagle', 'path of the totem warrior-wolf'
]

subclasses_bard = [
    'college of lore', 'college of valor'
]

subclasses_cleric = [
    'knowledge domain', 'life domain', 'light domain',
    'nature domain', 'tempest domain', 'trickery domain'
]

subclasses_druid = [
    'circle of the land', 'circle of the moon'
]

subclasses_fighter = [
    'battle master', 'champion', 'eldrich knight'
]

subclasses_monk = [
    'way of the four elements', 'way of the open hand', 'way of the shadow'
]

subclasses_paladin = [
    'oath of devotion', 'oath of the ancients', 'oath of vengeance'
]

subclasses_ranger = [
    'beast master', 'hunter'
]

subclasses_rogue = [
    'arcane trickster', 'assassin', 'thief'
]

subclasses_sorcerer = [
    'draconic bloodline', 'wild magic'
]

subclasses_warlock = [
    'the archfey', 'the fiend', 'the great old one'
]

subclasses_wizard = [
    'abjuration', 'conjuration', 'divination', 'enchantment',
    'evocation', 'illusion', 'necromancy', 'transmutation'
]

char_subclass_perks = []


# functions


def motherclass():
    '''Checks your character class to see what subclass choices you have.'''
    if classes.char_class.name == 'barbarian':
        cls = subclasses_barbarian

    elif classes.char_class.name == 'bard':
        cls = subclasses_bard

    elif classes.char_class.name == 'cleric':
        cls = subclasses_cleric

    elif classes.char_class.name == 'druid':
        cls = subclasses_druid

    elif classes.char_class.name == 'fighter':
        cls = subclasses_fighter

    elif classes.char_class.name == 'monk':
        cls = subclasses_monk

    elif classes.char_class.name == 'paladin':
        cls = subclasses_paladin

    elif classes.char_class.name == 'ranger':
        cls = subclasses_ranger

    elif classes.char_class.name == 'rogue':
        cls = subclasses_rogue

    elif classes.char_class.name == 'sorcerer':
        cls = subclasses_sorcerer

    elif classes.char_class.name == 'warlock':
        cls = subclasses_warlock

    elif classes.char_class.name == 'wizard':
        cls = subclasses_wizard

    else:
        pass

    return cls


def subclass_choice():
    '''Chooses a subclass. Called by sidentitytovariable()'''
    print(f"You can choose your subclass from {motherclass()}")
    while True:
        identity_choice = str(input("Choose your subclass: "))
        if identity_choice in motherclass():
            break
        else:
            print("Please write your choice in lowercase letters.")

    for n in csubclasses:
        if identity_choice == n.name:
            identity_choice = copy.deepcopy(n)
            break
        else:
            pass

    return identity_choice


def sidentitytovariable():
    '''Creates a class in char_subclass and ports the chosen subclass to it.'''
    global char_subclass
    char_subclass = subclass_choice()


def subclassperks():
    '''Chooses subclass feats.'''
    if char_subclass.name == 'knowledge domain':
        char_subclass_perks.append('two languages of your choice')

        perks = ['arcana', 'history', 'nature', 'religion']
        print("Choose two proficiencies from:", perks)
        while True:
            perk1 = (str(input("Choose the first proficiency: ")))
            if perk1 in perks:
                char_subclass_perks.append(perk1)
                break
            else:
                print("Please use lowercase letters.")
        while True:
            perk2 = (str(input("Choose the second proficiency: ")))
            if perk2 in perks:
                char_subclass_perks.append(perk2)
                break
            else:
                print("Please use lowercase letters.")

    elif char_subclass.name == 'life domain':
        char_subclass_perks.append('heavy armor')
        char_subclass_perks.append("disciple of life")

    elif char_subclass.name == 'light domain':
        char_subclass_perks.append('bonus cantrip: light')
        char_subclass_perks.append('warding flare')

    elif char_subclass.name == 'nature domain':
        char_subclass_perks.append('heavy armor')
        char_subclass_perks.append('acolyte of nature')

        perks = ['animal handling', 'nature', 'survival']
        print("Choose one proficiency from:", perks)
        while True:
            perk1 = (str(input("Choose the proficiency: ")))
            if perk1 in perks:
                char_subclass_perks.append(perk1)
                break
            else:
                print("Please use lowercase letters.")

    elif char_subclass.name == 'tempest domain':
        char_subclass_perks.append('heavy armor')
        char_subclass_perks.append('martial weapons')
        char_subclass_perks.append('wrath of the storm')

    elif char_subclass.name == 'trickery domain':
        char_subclass_perks.append('blessing of the trickster')

    elif char_subclass.name == 'draconic bloodline':
        char_subclass_perks.append('draconic language')
        char_subclass_perks.append('if doing charisma check when interacting with dragons, proficiency bonus is doubled')
        char_subclass_perks.append('max hit points +1 at every level')
        print("Choose your draconic ancestry.")
        draconic_ancestries = ['black dragon: acid damage', 'blue dragon: lightning damage', 'brass dragon: fire damage', 'bronze dragon: lightning damage', 'copper dragon: acid damage', 'gold dragon: fire damage', 'green dragon: poison damage', 'red dragon: fire damage', 'silver dragon: cold damage', 'white dragon: cold damage']
        print("Choose your draconic ancestry between:", draconic_ancestries)
        while True:
            draconic_ancestry = str(input("Choose your draconic ancestry: "))
            if draconic_ancestry in draconic_ancestries:
                char_subclass_perks.append(draconic_ancestry)
                break
            else:
                print("Please use lowercase letters.")

    elif char_subclass.name == 'wild magic':
        char_subclass_perks.append('wild magic surge')
        char_subclass_perks.append('tides of chaos')

    elif char_subclass.name == 'the archfey':
        char_subclass_perks.append('fey presence')

    elif char_subclass.name == 'the fiend':
        char_subclass_perks.append("dark one's blessing")

    elif char_subclass.name == 'the great old one':
        char_subclass_perks.append('awakened mind')

    else:
        pass
