#!/usr/bin/env python

# imports

import copy
import races
import subclasses
import mycharacter

# class


class character_class:

    def __init__(self, name, hit_die, hit_points, hit_points_final,
                 primary_ability, saving_throw_proficiencies, armorprof,
                 weaponsprof, toolsprof, subclassstart, skills):

        self.name = name
        self.hit_die = hit_die
        self.hit_points = hit_points
        self.hit_points_final = hit_points_final
        self.primary_ability = primary_ability
        self.saving_throw_proficiencies = saving_throw_proficiencies
        self.armorprof = armorprof
        self.weaponsprof = weaponsprof
        self.toolsprof = toolsprof
        self.subclassstart = subclassstart
        self.skills = skills


barbarian = character_class(
    'barbarian', 'd12', 12, 0, 'strength', 'strength' + ', ' + 'constitution',
    'light armor' + ', ' + 'medium armor' + ', ' + 'shields',
    'simple weapons' + ', ' + 'martial weapons', 'None', 3, ''
)

bard = character_class(
    'bard', 'd8', 8, 0, 'charisma', 'dexterity' + ', ' + 'charisma',
    'light armor', 'simple weapons' + ', ' + 'hand crossbow' + ', ' +
    'longsword' + ', ' + 'rapier' + ', ' + 'shorsword',
    'three musical instruments of your choice', 3, ''
)

cleric = character_class(
    'cleric', 'd8', 8, 0, 'wisdom', 'wisdom' + ', ' + 'charisma',
    'light armor' + ', ' + 'medium armor' + ', ' + 'shields',
    'simple weapons', 'None', 1, ''
)

druid = character_class(
    'druid', 'd8', 8, 0, 'wisdom', 'intelligence' + ', ' + 'wisdom',
    'light armor' + ', ' + 'medium armor' + ', ' + 'shields' + ', ' +
    '(druids will not wear armor or use shields made of metal)',
    'club' + ', ' + 'dagger' + ', ' + 'dart' + ', ' + 'javelin' +
    ', ' + 'mace' + ', ' + 'quarterstaff' + ', ' + 'scimitar' +
    ', ' + 'sickle' + ', ' + 'sling' + ', ' + 'spear', 'herbalism kit', 2, ''
)

fighter = character_class(
    'fighter', 'd10', 10, 0, 'strength or dexterity', 'strength' +
    ', ' + 'constitution', 'light armor' + ', ' + 'medium armor' +
    ', ' + 'heavy armor' + ', ' + 'shield', 'simple weapons' +
    ', ' + 'martial weapons', 'None', 3, ''
)
monk = character_class(
    'monk', 'd8', 8, 0, 'dexterity' + ' wisdom', 'strength' +
    ', ' + 'dexterity', 'None', 'simple weapons' + ', ' + 'shortsword',
    'Choose one type of artisan’s tools or one musical instrument', 3, ''
)

paladin = character_class(
    'paladin', 'd10', 10, 0, 'strength' + ' charisma', 'wisdom' +
    ', ' + 'charisma', 'light armor' + ', ' + 'medium armor' +
    ', ' + 'heavy armor' + ', ' + 'shield', 'simple weapons' +
    ', ' + 'martial weapons', 'None', 3, ''
)

ranger = character_class(
    'ranger', 'd10', 10, 0, 'dexterity' + ', ' + ' wisdom',
    'strength' + ', ' + 'dexterity', 'light armor' + ', ' +
    'medium armor' + ', ' + 'shields', 'simple weapons' +
    ', ' + 'martial weapons', 'None', 3, ''
)

rogue = character_class(
    'rogue', 'd8', 8, 0, 'dexterity', 'dexterity' + ', ' +
    'intelligence', 'light armor', 'simple weapons' + ', ' + 'hand crossbow' +
    ', ' + 'longsword' + ', ' + 'rapier' + ', ' + 'shortsword',
    'thieves’ tools', 3, ''
)

sorcerer = character_class(
    'sorcerer', 'd6', 6, 0, 'charisma', 'constitution' + ', ' + 'charisma',
    'None', 'dagger' + ', ' + 'dart' + ', ' + 'sling' + ', ' +
    'quarterstaff' + ', ' + 'light crossbow', 'None', 3, ''
)

warlock = character_class(
    'warlock', 'd8', 8, 0, 'charisma', 'wisdom' + ', ' + 'charisma',
    'light armor', 'simple weapons', 'None', 3, ''
)

wizard = character_class(
    'wizard', 'd6', 6, 0, 'intelligence', 'intelligence' + ', ' +
    'wisdom', 'None', 'dagger' + ', ' + 'dart' + ', ' +
    'sling' + ', ' + 'quarterstaff' + ', ' + 'light crossbow', 'None', 2, ''
)


char_class = ()


# functions


def class_choice(list_choice, classlist):
    '''Chooses a class. List_choice is classes. Classlist is cclasses.
    Deepcopies it into the variable char_class.
    Called by cidentitytovariable()'''

    print(f"""It is time to choose your class. Choose betwen: {list_choice}""")

    while True:
        identity_choice = str(input("What is your class going to be? "))
        if identity_choice in list_choice:
            break
        else:
            print("Please enter the name of your class in lowercase letters.")

    for n in classlist:
        if identity_choice in n.name:
            identity_choice = copy.deepcopy(n)
            break
        else:
            pass

    return identity_choice


def cidentitytovariable():
    '''Creates a class char_class from your chosen class.'''
    global char_class
    char_class = class_choice(classes, cclasses)


def hit_points_calc():
    '''Adds base HP and constitution modifier.'''
    char_class.hit_points_final = char_class.hit_points + races.char_race.conmodifier
    print(f"Your HP is {char_class.hit_points_final}.")


def chooseprof(a, clsskill):
    '''Template for chosing a class proficiency.
    a is "a skill" if it is chosen first or "another" if chosen later
    Clsskill is ie., allskills or barbarianskills.'''

    while True:
        choice1 = str(input(f"Please choose {a} skill from: {clsskill} "))
        if choice1 not in clsskill:
            print("You entered a wrong choice.")
        else:
            clsskill.remove(choice1)
            break
    return choice1


def allclassprof():
    '''Chooses and prints your class proficiencies.'''
    print("Now it's time to choose your class proficiencies: ")

    if char_class.name == 'barbarian':
        print('\n')
        print("Since your class is barbarian, you can choose two skills.")
        char_class.skills = chooseprof('a', barbarianskills) + ', ' + chooseprof('another', barbarianskills)
        print('\n')
        print(f"Primary ability: {char_class.primary_ability}")
        print(f"Class skills: {char_class.skills}")
        print(f"Class armor proficiences: {char_class.armorprof}")
        print(f"Class weapons proficiences: {char_class.weaponsprof}")
        print(f"Class tools proficiences: {char_class.toolsprof}")
        print(f"Class saving throws proficiences: {char_class.saving_throw_proficiencies}")

    elif char_class.name == 'bard':
        print('\n')
        print("Since your class is bard, you can choose three skills.")
        char_class.skills = chooseprof('a', allskills) + ', ' + chooseprof('another', allskills) + ', ' + chooseprof('another', allskills)
        print('\n')
        print(f"Primary ability: {char_class.primary_ability}")
        print(f"Class skills: {char_class.skills}")
        print(f"Class armor proficiences: {char_class.armorprof}")
        print(f"Class weapons proficiences: {char_class.weaponsprof}")
        print(f"Class tools proficiences: {char_class.toolsprof}")
        print(f"Class saving throws proficiences: {char_class.saving_throw_proficiencies}")

    elif char_class.name == 'cleric':
        print('\n')
        print("Since your class is cleric, you can choose two skills.")
        char_class.skills = chooseprof('a', clericskills) + ', ' + chooseprof('another', clericskills)
        print('\n')
        print(f"Primary ability: {char_class.primary_ability}")
        print(f"Class skills: {char_class.skills}")
        print(f"Class armor proficiences: {char_class.armorprof}")
        print(f"Class weapons proficiences: {char_class.weaponsprof}")
        print(f"Class tools proficiences: {char_class.toolsprof}")
        print(f"Class saving throws proficiences: {char_class.saving_throw_proficiencies}")

    elif char_class.name == 'druid':
        print('\n')
        print("Since your class is druid, you can choose two skills.")
        char_class.skills = chooseprof('a', druidskills) + ', ' + chooseprof('another', druidskills)
        print('\n')
        print(f"Primary ability: {char_class.primary_ability}")
        print(f"Class skills: {char_class.skills}")
        print(f"Class armor proficiences: {char_class.armorprof}")
        print(f"Class weapons proficiences: {char_class.weaponsprof}")
        print(f"Class tools proficiences: {char_class.toolsprof}")
        print(f"Class saving throws proficiences: {char_class.saving_throw_proficiencies}")

    elif char_class.name == 'fighter':
        print('\n')
        print("Since your class is fighter, you can choose two skills.")
        char_class.skills = chooseprof('a', fighterskills) + ', ' + chooseprof('another', fighterskills)
        print('\n')
        print("You can also choose your primary ability.")
        char_class.primary_ability = fighter_primary_ability()
        print('\n')
        print(f"Primary ability: {char_class.primary_ability}")
        print(f"Class skills: {char_class.skills}")
        print(f"Class armor proficiences: {char_class.armorprof}")
        print(f"Class weapons proficiences: {char_class.weaponsprof}")
        print(f"Class tools proficiences: {char_class.toolsprof}")
        print(f"Class saving throws proficiences: {char_class.saving_throw_proficiencies}")

    elif char_class.name == 'monk':
        print('\n')
        print("Since your class is monk, you can choose two skills.")
        char_class.skills = chooseprof('a', monkskills) + ', ' + chooseprof('another', monkskills)
        print('\n')
        print(f"Primary ability: {char_class.primary_ability}")
        print(f"Class skills: {char_class.skills}")
        print(f"Class armor proficiences: {char_class.armorprof}")
        print(f"Class weapons proficiences: {char_class.weaponsprof}")
        print(f"Class tools proficiences: {char_class.toolsprof}")
        print(f"Class saving throws proficiences: {char_class.saving_throw_proficiencies}")

    elif char_class.name == 'paladin':
        print('\n')
        print("Since your class is paladin, you can choose two skills.")
        char_class.skills = chooseprof('a', paladinskills) + ', ' + chooseprof('another', paladinskills)
        print('\n')
        print(f"Primary ability: {char_class.primary_ability}")
        print(f"Class skills: {char_class.skills}")
        print(f"Class armor proficiences: {char_class.armorprof}")
        print(f"Class weapons proficiences: {char_class.weaponsprof}")
        print(f"Class tools proficiences: {char_class.toolsprof}")
        print(f"Class saving throws proficiences: {char_class.saving_throw_proficiencies}")

    elif char_class.name == 'ranger':
        print('\n')
        print("Since your class is ranger, you can choose tree skills.")
        char_class.skills = chooseprof('a', rangerskills) + ', ' + chooseprof('another', rangerskills) + '' + chooseprof('another', rangerskills)
        print('\n')
        print(f"Primary ability: {char_class.primary_ability}")
        print(f"Class skills: {char_class.skills}")
        print(f"Class armor proficiences: {char_class.armorprof}")
        print(f"Class weapons proficiences: {char_class.weaponsprof}")
        print(f"Class tools proficiences: {char_class.toolsprof}")
        print(f"Class saving throws proficiences: {char_class.saving_throw_proficiencies}")

    elif char_class.name == 'rogue':
        print('\n')
        print("Since your class is rogue, you can choose four skills.")
        char_class.skills = chooseprof('a', rogueskills) + ', ' + chooseprof('another', rogueskills) + ', ' + chooseprof('another', rogueskills) + ', ' + chooseprof('another', rogueskills)
        print('\n')
        print(f"Primary ability: {char_class.primary_ability}")
        print(f"Class skills: {char_class.skills}")
        print(f"Class armor proficiences: {char_class.armorprof}")
        print(f"Class weapons proficiences: {char_class.weaponsprof}")
        print(f"Class tools proficiences: {char_class.toolsprof}")
        print(f"Class saving throws proficiences: {char_class.saving_throw_proficiencies}")

    elif char_class.name == 'sorcerer':
        print('\n')
        print("Since your class is sorcerer, you can choose two skills.")
        char_class.skills = chooseprof('a', sorcererskills) + ', ' + chooseprof('another', sorcererskills)
        print('\n')
        print(f"Primary ability: {char_class.primary_ability}")
        print(f"Class skills: {char_class.skills}")
        print(f"Class armor proficiences: {char_class.armorprof}")
        print(f"Class weapons proficiences: {char_class.weaponsprof}")
        print(f"Class tools proficiences: {char_class.toolsprof}")
        print(f"Class saving throws proficiences: {char_class.saving_throw_proficiencies}")

    elif char_class.name == 'warlock':
        print('\n')
        print("Since your class is warlock, you can choose two skills.")
        char_class.skills = chooseprof('a', warlockskills) + ', ' + chooseprof('another', warlockskills)
        print('\n')
        print(f"Primary ability: {char_class.primary_ability}")
        print(f"Class skills: {char_class.skills}")
        print(f"Class armor proficiences: {char_class.armorprof}")
        print(f"Class weapons proficiences: {char_class.weaponsprof}")
        print(f"Class tools proficiences: {char_class.toolsprof}")
        print(f"Class saving throws proficiences: {char_class.saving_throw_proficiencies}")

    elif char_class.name == 'wizard':
        print('\n')
        print("Since your class is wizard, you can choose two skills.")
        char_class.skills = chooseprof('a', wizardskills) + ', ' + chooseprof('another', wizardskills)
        print('\n')
        print(f"Primary ability: {char_class.primary_ability}")
        print(f"Class skills: {char_class.skills}")
        print(f"Class armor proficiences: {char_class.armorprof}")
        print(f"Class weapons proficiences: {char_class.weaponsprof}")
        print(f"Class tools proficiences: {char_class.toolsprof}")
        print(f"Class saving throws proficiences: {char_class.saving_throw_proficiencies}")

    else:
        pass


def featsspellsintro():
    '''Intro for featandspellclass()'''
    print("It is time to see and choose your class features and spells.")


def spellchooser(spell, classspells, cantriporspell):
    '''Chooses your cantrips and spells.
    Called by featandspellclass()'''
    while True:
        spell = str(input("Choose one: "))
        if spell in classspells:
            cantriporspell.append(spell)
            break
        else:
            print("Please check if you have written your choice correctly.")


def featandspellbarbarian():
    '''Chooses/appends and prints feats and/or spells for a barbarian.'''
    class_features.append('rage')
    class_features.append('unarmored defense')

    print('\n')
    print(f"Your class features are: {class_features}")


def featandspellbard():
    '''Chooses/appends and prints feats and/or spells for a bard.'''
    print(f"You can choose two cantrips from this list: {bardcantrips}")
    spellchooser('bardcantrip1', bardcantrips, class_cantrips)
    spellchooser('bardcantrip2', bardcantrips, class_cantrips)

    print(f"You can choose four spells from this list: {bardspells1}")
    spellchooser('bardspell1', bardspells1, class_spells1)
    spellchooser('bardspell2', bardspells1, class_spells1)
    spellchooser('bardspell3', bardspells1, class_spells1)
    spellchooser('bardspell4', bardspells1, class_spells1)

    print('\n')
    class_features.append('spellcasting')
    class_features.append('bardic inspiration')
    print(f"Your class features are: {class_features}")
    print(f"Your cantrips are: {class_cantrips}")
    print(f"Your first level spells are: {class_spells1}")
    print("You get 2 spell slots.")
    print(f"Your spellcasting ability is: {char_class.primary_ability}")


def featandspellcleric():
    '''Chooses/appends and prints feats and/or spells for a cleric.'''
    print(f"You can choose three cantrips from this list: {clericcantrips}")
    spellchooser('clericcantrip1', clericcantrips, class_cantrips)
    spellchooser('clericcantrip2', clericcantrips, class_cantrips)
    spellchooser('clericcantrip3', clericcantrips, class_cantrips)

    print(f"You automatically know these spells: {clericspells1}")
    for n in clericspells1:
        class_spells1.append(n)

    if subclasses.char_subclass.name == 'knowledge domain':
        for n in clericknowledge1:
            class_spells1.append(n)

    elif subclasses.char_subclass.name == 'life domain':
        for n in clericlife1:
            class_spells1.append(n)

    elif subclasses.char_subclass.name == 'light domain':
        for n in clericlight1:
            class_spells1.append(n)

    elif subclasses.char_subclass.name == 'nature domain':
        for n in clericnature1:
            class_spells1.append(n)

    elif subclasses.char_subclass.name == 'tempest domain':
        for n in clerictempest1:
            class_spells1.append(n)

    elif subclasses.char_subclass.name == 'trickery domain':
        for n in clerictrickery1:
            class_spells1.append(n)

    elif subclasses.char_subclass.name == 'war domain':
        for n in clericwar1:
            class_spells1.append(n)

    else:
        pass

    print('\n')
    class_features.append('spellcasting')
    class_features.append('divine domain')
    print(f"Your class features are: {class_features}")
    print(f"Your cantrips are: {class_cantrips}")
    print(f"Your first level spells are: {class_spells1}")
    print("You do not have to prepare the last two spells on that list.")
    print("As for the others, you have to prepare them before you have them available for casting.")
    print("You get 2 spell slots.")
    print(f"You can prepare {races.char_race.wismodifier} + {mycharacter.character1.level}, between each resting period.")
    print(f"Your spellcasting ability is {char_class.primary_ability}")


def featandspelldruid():
    '''Chooses/appends and prints feats and/or spells for a druid.'''
    print(f"You can choose two cantrips from this list: {druidcantrips}")
    spellchooser('druidcantrip1', druidcantrips, class_cantrips)
    spellchooser('druidcantrip2', druidcantrips, class_cantrips)

    print(f"You automatically know these spells: {druidspells1}")
    for n in druidspells1:
        class_spells1.append(n)

    print('\n')
    class_features.append('spellcasting')
    class_features.append('druidic')
    print(f"Your class features are: {class_features}")
    print(f"Your cantrips are: {class_cantrips}")
    print(f"Your first level spells are: {class_spells1}")
    print("You have to prepare your spells before you have them available for casting.")
    print("You get 2 spell slots.")
    print(f"You can prepare {races.char_race.wismodifier} + {mycharacter.character1.level}, between each resting period.")
    print(f"Your spellcasting ability is: {char_class.primary_ability}")


def featandspellfighter():
    '''Chooses/appends and prints feats and/or spells for a fighter.'''
    print(f"Choose your fighting style between: {fighter_fighting_styles}")
    while True:
        fighting_style1 = str(input("Choose your fighting style: "))
        if fighting_style1 in fighter_fighting_styles:
            break
        else:
            print("Please make sure you have written your choice correctly.")

    print('\n')
    class_features.append(fighting_style1)
    class_features.append('second wind')
    print(f"Your class features are: {class_features}")


def featandspellmonk():
    '''Chooses/appends and prints feats and/or spells for a monk.'''
    print('\n')
    class_features.append('unarmored defense')
    class_features.append('martial arts')
    print(f"Your class features are: {class_features}")


def featandspellpaladin():
    '''Chooses/appends and prints feats and/or spells for a paladin.'''
    print('\n')
    class_features.append('divine sense')
    class_features.append('lay on hands')
    print(f"Your class features are: {class_features}")


def featandspellranger():
    '''Chooses/appends and prints feats and/or spells for a ranger.'''
    print('\n')
    class_features.append('favored enemy')
    class_features.append('natural explorer')
    print(f"Your class features are: {class_features}")


def featandspellrogue():
    '''Chooses/appends and prints feats and/or spells for a rogue.'''
    print('\n')
    class_features.append('expertise')
    class_features.append('sneak attack')
    class_features.append("thieves' can't")
    print(f"Your class features are: {class_features}")


def featandspellsorcerer():
    '''Chooses/appends and prints feats and/or spells for a sorcerer.'''
    print(f"You can choose four cantrips from this list: {sorcerercantrips}")
    spellchooser('sorcerercantrip1', sorcerercantrips, class_cantrips)
    spellchooser('sorcerercantrip2', sorcerercantrips, class_cantrips)
    spellchooser('sorcerercantrip3', sorcerercantrips, class_cantrips)
    spellchooser('sorcerercantrip4', sorcerercantrips, class_cantrips)

    print(f"You can choose two spells from this list: {sorcererspells1}")
    spellchooser('sorcererspell1', sorcererspells1, class_spells1)
    spellchooser('sorcererspell2', sorcererspells1, class_spells1)

    class_features.append('spellcasting')
    class_features.append('sorcerous origin')

    if subclasses.char_subclass.name == 'wild magic':
        class_features.append('wild magic surge')
        class_features.append('tides of chaos')
    else:
        pass

    print('\n')
    print(f"Your class features are: {class_features}")
    print(f"Your cantrips are: {class_cantrips}")
    print(f"Your first level spells are: {class_spells1}")
    print("You get 2 spell slots.")
    print(f"Your spellcasting ability is: {char_class.primary_ability}")


def featandspellwarlock():
    '''Chooses/appends and prints feats and/or spells for a warlock.'''
    print(f"You can choose two cantrips from this list: {warlockcantrips}")
    spellchooser('warlockcantrip1', warlockcantrips, class_cantrips)
    spellchooser('warlockcantrip2', warlockcantrips, class_cantrips)

    print(f"You can choose two spells from this list: {warlockspells1}")
    spellchooser('warlockspell1', warlockspells1, class_spells1)
    spellchooser('warlockspell2', warlockspells1, class_spells1)

    class_features.append('otherworldly patron')
    class_features.append('pact magic')

    print('\n')
    print(f"Your class features are: {class_features}")
    print(f"Your cantrips are: {class_cantrips}")
    print(f"Your first level spells are: {class_spells1}")
    print("You get 1 spell slot.")
    print(f"Your spellcasting ability is {char_class.primary_ability}")


def featandspellwizard():
    '''Chooses/appends and prints feats and/or spells for a wizard.'''
    print(f"You can choose three cantrips from this list: {wizardcantrips}")
    spellchooser('wizardcantrip1', wizardcantrips, class_cantrips)
    spellchooser('wizardcantrip2', wizardcantrips, class_cantrips)
    spellchooser('wizardcantrip3', wizardcantrips, class_cantrips)

    print(f"You can choose six spells from this list: {wizardspells1}")
    spellchooser('wizardspell1', wizardspells1, class_spells1)
    spellchooser('wizardspell2', wizardspells1, class_spells1)
    spellchooser('wizardspell3', wizardspells1, class_spells1)
    spellchooser('wizardspell4', wizardspells1, class_spells1)
    spellchooser('wizardspell5', wizardspells1, class_spells1)
    spellchooser('wizardspell6', wizardspells1, class_spells1)

    class_features.append('spellcasting')
    class_features.append('arcane recovery')

    print('\n')
    print(f"Your class features are: {class_features}")
    print(f"Your cantrips are: {class_cantrips}")
    print(f"Your first level spells are: {class_spells1}")
    print("You get 2 spell slots.")
    print(f"Your spellcasting ability is: {char_class.primary_ability}")


def fighter_primary_ability():
    '''Chooses a fighter's primary ability.'''
    while True:
        ability = str(input(f"Please choose your primary ability between: {fighterprimabs} "))
        if ability in fighterprimabs:
            return ability
        else:
            print("Please choose between strength and dexterity. Use lowercase letters.")


# lists-classes

cclasses = [
    barbarian, bard, cleric, druid, fighter, monk, paladin, ranger,
    rogue, sorcerer, warlock, wizard
]

classes = [
    'barbarian', 'bard', 'cleric', 'druid', 'fighter', 'monk',
    'paladin', 'ranger', 'rogue', 'sorcerer', 'warlock', 'wizard'
]


# lists-skills

allskills = [
    'athletics', 'acrobatics', 'sleight of hand', 'stealth',
    'arcana', 'history', 'investigation', 'nature',
    'animal handling', 'insight', 'medicine', 'perception',
    'survival', 'deception', 'intimidation', 'performance', 'persuasion'
]

barbarianskills = [
    'animal handling', 'athletics', 'intimidation', 'nature',
    'perception', 'survival'
]

clericskills = [
    'history', 'insight', 'medicine', 'persuasion', 'religion'
]

druidskills = [
    'arcana', 'animal handling', 'insight', 'medicine',
    'nature', 'perception', 'religion', 'survival'
]

fighterskills = [
    'acrobatics', 'animal handling', 'athletics', 'history',
    'insight', 'intimidation', 'perception', 'survival'
]

monkskills = [
    'acrobatics', 'athletics', 'history',
    'insight', 'religion', 'stealth'
]

paladinskills = [
    'athletics', 'insight', 'intimidation', 'medicine',
    'persuasion', 'religion'
]

rangerskills = [
    'animal handling', 'athletics', 'insight',
    'investigation', 'nature', 'perception', 'stealth', 'survival'
]

rogueskills = [
    'acrobatics', 'athletics', 'deception', 'insight',
    'intimidation', 'investigation', 'perception',
    'performance', 'persuasion', 'sleight of hand', 'stealth'
]

sorcererskills = [
    'arcana', 'deception', 'insight', 'intimidation',
    'persuasion', 'religion'
]

warlockskills = [
    'arcana', 'deception', 'history', 'intimidation',
    'investigation', 'nature', 'religion'
]

wizardskills = [
    'arcana', 'history', 'insight', 'investigation',
    'medicine', 'religion'
]

fighter_fighting_styles = [
    'fighting style: archery', 'fighting style: defense',
    'fighting style: dueling',
    'fighting style: great weapon fighting',
    'fighting style: protection',
    'fighting style: two-weapon fighting'
]

fighterprimabs = [
    'strength', 'dexterity'
]

# lists-cantrips and spells

bardcantrips = [
    'blade ward', 'dancing lights', 'friends', 'light',
    'mage hand', 'mending', 'message', 'minor illusion',
    'prestidigitation', 'true strike', 'vicious mockery'
]

bardspells1 = [
    'animal friendship', 'bane', 'charm person',
    'comprehend languages', 'cure wounds', 'detect magic',
    'disguise self', 'dissonant whispers', 'faerie fire',
    'feather fall', 'healing word', 'heroism', 'identify',
    'illusory script', 'longstrider', 'silent image',
    'sleep', 'speak with animals', "tasha's hideous laughter",
    'thunderwave', 'unseen servant'
]

clericcantrips = [
    'guidance', 'light', 'mending', 'resistance',
    'sacred flame', 'spare the dying', 'thaumaturgy'
]

clericspells1 = [
    'bane', 'bless', 'command', 'create or destroy water',
    'cure wounds', 'detect evil and good', 'detect magic',
    'detect poison and disease', 'guiding bolt',
    'healing word', 'inflict wounds',
    'protection from evil and good', 'purify food and drink',
    'sanctuary', 'shield of faith'
]

clericknowledge1 = [
    'command', 'identify'
]

clericlife1 = [
    'bless', 'cure wounds'
]

clericlight1 = [
    'burning hands', 'faerie fire'
]

clericnature1 = [
    'animal friendship', 'speak with animals'
]

clerictempest1 = [
    'fog cloud', 'thunderwave'
]

clerictrickery1 = [
    'charm person', 'disguise self'
]

clericwar1 = [
    'divine favor', 'shield of faith'
]

druidcantrips = [
    'druidcraft', 'guidance', 'mending', 'poison spray',
    'produce flame', 'resistance', 'shillelagh', 'thorn whip'
]

druidspells1 = [
    'animal friendship', 'charm person',
    'create or destroy water', 'cure wounds', 'detect magic',
    'detect poison and disease', 'entangle', 'faerie fire',
    'fog cloud', 'goodberry', 'healing word', 'jump',
    'longstrider', 'purify food and drink',
    'speak with animals', 'thunderwave'
]

paladinspells1 = [
    'bless', 'command', 'compelled duel', 'cure wounds',
    'detect evil and good', 'detect magic',
    'detect poison and disease', 'divine favor', 'heroism',
    'protection from evil and good', 'purify food and drink',
    'searing smite', 'shield of faith',
    'thunderous smite', 'wrathful smite'
]

rangerspells1 = [
    'alarm', 'animal friendship', 'cure wounds', 'detect magic',
    'detect poison and disease', 'ensnaring strike', 'fog cloud',
    'goodberry', 'hail of thorns', "hunter's mark", 'jump',
    'longstrider', 'speak with animals'
]

sorcerercantrips = [
    'acid splash', 'blade ward', 'chill touch', 'dancing lights',
    'fire bolt', 'friends', 'light', 'mage hand', 'mending',
    'message', 'minor illusion', 'poison spray', 'prestidigitation',
    'ray of frost', 'shocking grasp', 'true strike'
]

sorcererspells1 = [
    'burning hands', 'charm person', 'chromatic orb', 'color spray',
    'comprehend languages', 'detect magic', 'disguise self',
    'expeditious retreat', 'false life', 'feather fall', 'fog cloud',
    'jump', 'mage armor', 'magic missile', 'ray of sickness',
    'shield', 'silent image', 'sleep', 'thunderwave', 'witch bolt'
]

warlockcantrips = [
    'blade ward', 'chill touch', 'eldritch blast', 'friends',
    'mage hand', 'minor illusion', 'poison spray',
    'prestidigitation', 'true strike'
]

warlockspells1 = [
    'armor of agathys', 'arms of hadar', 'charm person',
    'comprehend languages', 'expeditious retreat', 'hellish rebuke',
    'hex', 'illusory script', 'protection from evil and good',
    'unseen servant', 'witch bolt'
]

warlockarchfey1 = [
    'faerie fire', 'sleep'
]

warlockfiend1 = [
    'burning hands', 'command'
]

warlockgreat1 = [
    'dissonant whispers', "tasha's hideous laughter"
]

wizardcantrips = [
    'acid splash', 'blade ward', 'chill touch', 'dancing lights',
    'fire bolt', 'friends', 'light', 'mage hand', 'mending',
    'message', 'minor illusion', 'poison spray', 'prestidigitation',
    'ray of frost', 'shocking grasp', 'true strike'
]

wizardspells1 = [
    'alarm', 'burning hands', 'charm person', 'chromatic orb',
    'color spray', 'comprehend languages', 'detect magic',
    'disguise self', 'expeditious retreat', 'false life',
    'feather fall', 'find familirar', 'fog cloud', 'grease',
    'identify', 'illusory script', 'jump', 'longstrider',
    'mage armor', 'magic missile', 'protection from evil and good',
    'ray of sickness', 'shield', 'silent image', 'sleep',
    "tasha's hideous laughter", "tenser's floating disk",
    'thunderwave', 'unseen servant', 'witch bolt'
]


class_cantrips = []

class_spells1 = []

class_features = []
