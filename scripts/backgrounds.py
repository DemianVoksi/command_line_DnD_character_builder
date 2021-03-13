#!/usr/bin/env python

# imports

import copy

# class


class character_background:

    def __init__(self, name, skill_proficiencies, tool_proficiencies,
                 languages, equipment, money, feature):

        self.name = name
        self.skill_proficiencies = skill_proficiencies
        self.tool_proficiencies = tool_proficiencies
        self.languages = languages
        self.equipment = equipment
        self.money = money
        self.feature = feature


acolyte = character_background(
    'acolyte', 'insight and religion', 'None', 'two of your choice',
    'a holy symbol (a gift to you when you entered the priesthood), a prayer book or prayer wheel, 5 sticks of incense, vestments, and a set of common clothes',
    '15 gp', 'Shelter of the Faithful'
)

charlatan = character_background(
    'charlatan', 'deception and sleight of hand',
    'disguise kit and forgery kit', 'None',
    'a set of fine clothes, a disguise kit, tools of the con of your choice(ten stoppered bottles filled with colored liquid, a set of weighted dice, a deck of mared cards, or a signet ring of an imaginary duke)',
    '15 gp', 'False Identity'
)

criminal = character_background(
    'criminal', 'deception and stealth',
    "one type of gaming set, thieves' tools", 'None',
    'a crowbar, and a set of dark common clothes including a hood',
    '15 gp', 'Criminal Contact'
)

criminal_spy = character_background(
    'criminal (spy)', 'deception and stealth',
    "one type of gaming set, thieves' tools", 'None',
    'a crowbar, and a set of dark common clothes including a hood',
    '15 gp', 'Spy Contact'
)

entertainer = character_background(
    'entertainer', 'acrobatics and performance',
    'disguise kit and one type of musical instrument', 'None',
    'a musical instrument (one of your choice), the favor of an admirer (love letter, lock of hair, or trinket) and costume clothes',
    '15 gp', "By Popular Demand"
)

entertainer_gladiator = character_background(
    'entertainer (gladiator)', 'acrobatics and performance',
    'disguise kit and one type of musical instrument', 'None',
    'an inexpensive but unusual weapon, such as a trident or net (one of your choice), the favor of an admirer (love letter, lock of hair, or trinket) and costume clothes',
    '15 gp', "By Popular Demand"
)

folk_hero = character_background(
    'folk hero', 'animal handling and survival',
    "one type of artisan's tools, vehicles (land)", 'None',
    "a set of artisan's tools (one of your choice), a shovel, an iron pot, and a set of common clothes",
    '10 gp', 'Rustic Hospitality'
)

guild_artisan = character_background(
    'guild artisan', 'insight and persuasion', "one type of artisan's tools",
    'one of your choice',
    "a set of artisan's tools (one of your choice), a letter of introduction from your guild, and a set of traveler's clothes",
    '15 gp', 'Guild Membership'
)

guild_artisan_guild_merchant = character_background(
    'guild artisan (guild merchant)', 'insight and persuasion',
    "one type of artisan's tools, or navigator's tools, or an additional language",
    'one of your choice',
    "a set of artisan's tools (one of your choice) or a mule and cart, a letter of introduction from your guild, and a set of traveler's clothes",
    '15 gp', 'Guild Membership'
)

hermit = character_background(
    'hermit', 'medicine and religion', 'herbalism kit', 'one of your choice',
    "a scroll case stuffed full of notes from your studies or prayers, a winter blanket, a set of common clothes, and an herbalism kit",
    '5 gp', 'Discovery'
)

noble = character_background(
    'noble', 'history and persuasion', 'one type of gaming set',
    'one of your choice',
    "a set of fine clothes, a signet ring, and a scroll of pedigree",
    '25 gp', 'Position of Privilege'
)

noble_knight = character_background(
    'noble (knight)', 'history and persuasion', 'one type of gaming set',
    'one of your choice',
    "a set of fine clothes, a signet ring, and a scroll of pedigree",
    '25 gp', 'Retainers'
)

outlander = character_background(
    'outlander', 'athletics and survival', 'one type of musical instrument',
    'one of your choice',
    "a staff, a hunting trap, a trophy from an animal you killed, and a set of traveler's clothes",
    '10 gp', 'Wanderer'
)

sage = character_background(
    'sage', 'arcana and history', 'None', 'two of your choice',
    'a bottle of black ink, a quill, a small knife, a letter from a dead colleague posing a question you have not yet been able to answer, and a set of common clothes',
    '10 gp', 'Researcher'
)

sailor = character_background(
    'sailor', 'athletics and perception', "navigator's tools, vehicles (water)",
    'None',
    "a belaying pin (club), silk rope (50 feet), a lucky charm such as a rabbit foot or a small stone with a hole in the center, and a set of common clothes",
    '10 gp', "Ship's passage"
)

sailor_pirate = character_background(
    'sailor (pirate)', 'athletics and perception', "navigator's tools, vehicles (water)", 'None',
    "a belaying pin (club), silk rope (50 feet), a lucky charm such as a rabbit foot or a small stone with a hole in the center, and a set of common clothes",
    '10 gp', "Bad Reputation"
)

soldier = character_background(
    'soldier', 'athletics and intimidation',
    'one type of gaming set and vehicles (land)', 'None',
    "an insignia of rank, a trophy taken from a fallen enemy (a dagger, broken blade, or piece of a banner), a bone dice set or playing card set, and a set of common clothes",
    '10 gp', 'Military Rank'
)

urchin = character_background(
    'urchin', 'sleight of hand and stealth', "Disguise kit, Thieves' tools",
    'None',
    "a small knife, a map of the city you grew up in, a pet mouse, a token to remember your parents by, and a set of common clothes",
    '10 gp', 'City Secrets'
)


char_background = ()


# lists

cbackgrounds = [
    acolyte, charlatan, criminal, criminal_spy, entertainer,
    entertainer_gladiator, folk_hero, guild_artisan,
    guild_artisan_guild_merchant, hermit, noble, noble_knight,
    outlander, sage, sailor, sailor_pirate, soldier, urchin
]

backgrounds = [
    'acolyte', 'charlatan', 'criminal', 'criminal spy',
    'entertainer', 'entertainer gladiator', 'folk hero',
    'guild artisan', 'guild artisan guild merchant', 'hermit',
    'noble', 'noble knight', 'outlander', 'sage',
    'sailor', 'sailor pirate', 'soldier', 'urchin'
]


# functions


def background_choice():
    '''Chooses a character background.
    Called by bidentitytovariable()'''
    print("\n")
    print(f"It is time to choose your character's background. You can choose between the following: {backgrounds}")

    while True:
        identity_choice = str(input("What is your character's background going to be? "))
        if identity_choice in backgrounds:
            break
        else:
            print("Please check if you have wrote the name of your background correctly. Use lowercase letters.")

    for n in cbackgrounds:
        if identity_choice in n.name:
            identity_choice = copy.deepcopy(n)
            break
        else:
            pass

    return identity_choice


def bidentitytovariable():
    '''Ports background choice to class char_background.
    Called by __main__.'''
    global char_background
    char_background = background_choice()
