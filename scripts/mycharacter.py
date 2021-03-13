#!/usr/bin/env python

# imports

import copy
import sys
import races
import classes
import subclasses
import backgrounds
import weapons
import armor

# class


class mycharacter:

    def __init__(self, playername, charname, level, sex, alignment):
        self.playername = playername
        self.charname = charname
        self.level = level
        self.sex = sex
        self.alignment = alignment


character1 = mycharacter("", "", "", "", "")

# functions


def intro():
    '''Intro to the program.
    Called by __main__.'''
    print("Greetings, adventurer!")
    print("Welcome to the Dungeons & Dragons character builder.")
    print("Are you new to the game? Have no worries!")
    print("Together, you and I will build your new D&D character from scratch!")
    print("In just a few minutes, you will be ready to participate in a new quest!")


def plyrname():
    '''Requests player's name.
    Called by __main__.'''
    print("Let's find out your name and your character's name!")
    name = str(input("First of all, tell me your name: "))
    print(f"Welcome, {name}!")
    print('\n')
    character1.playername = copy.deepcopy(name)


def character():
    '''Requests character's name.
    Called by __main__.'''
    character_name = str(input("And what is your character's name? "))
    print(
        f"Ok, {character1.playername}, your character's name is {character_name}!"
    )
    print("\n")
    character1.charname = copy.deepcopy(character_name)


def level():
    '''Sets level at 1.
    Called by __main__.'''
    lvl = 1
    character1.level = copy.deepcopy(lvl)
    print(f"You will be starting at level {character1.level}.")
    print('\n')


def sex():
    '''Chooses character's sex.
    Called by __main__.'''

    print("Please choose your character's sex. Press (1) for female or press (2) for male: ")
    while True:
        charsex = str(input("Please enter your character's sex: "))
        if charsex == ('1'):
            charsex = 'female'
            print("You have chosen to be female.")
            print('\n')
            break
        elif charsex == ('2'):
            charsex = 'male'
            print("You have chosen to be male.")
            print('\n')
            break
        elif charsex in ['yes', 'y', 'YES', 'Y']:
            print("Nice try.")
            print('\n')
        else:
            print("Please select 1 or 2.")
    character1.sex = copy.deepcopy(charsex)


def alignment():
    '''Chooses character's alignment.
    Called by __main__.'''

    print(f"It is time to choose your alignment. Please choose one from {alignments}.")

    while True:
        character_alignment = str(input("Please choose your alignment: "))
        if character_alignment not in alignments:
            print("Please check your spelling and make sure you write in lowercase letters.")
        else:
            print("Ok, so you chose to be", character_alignment)
            print("\n")
            break
    character1.alignment = copy.deepcopy(character_alignment)


def background():
    '''Opportunity to write the character's backstory.
    Called by __main__.'''
    global background_story_final

    print('\n')
    print("If you want, you can write a short background story for your character. Press (1) if you want to write it or (2) if you would rather skip this step.")
    while True:
        byn = str(input("Press 1 or 2: "))
        if byn == ('1'):
            background_story = str(input("Your character's background story: "))
            break
        elif byn == ('2'):
            background_story = "You have chosen not to write a background story of your character."
            break
        else:
            print("Please press 1 or 2.")
    background_story_final = background_story


def finalstats():
    '''Prints results of the character creator process.
    Called by __main__.'''
    print('\n')
    print("Congratulations, you are done with your character build!")
    print("This is what you have created:")
    print('\n')

    print(f"Player name: {character1.playername}")
    print(f"Character name: {character1.charname}")
    print(f"Race: {races.char_race.name}")
    print(f"Class: {classes.char_class.name}")
    print(f"Subclass: {subclasses.char_subclass.name}")
    print(f"Background: {backgrounds.char_background.name}")
    print(f"Sex: {character1.sex}")
    print(f"Alignment: {character1.alignment}")
    print("\n")

    print("Ability scores:")
    print("Ability", '\t', "Score")
    print("-------", '\t', "-----")
    print("Strength", '\t', races.char_race.stremodified)
    print("Dexterity", '\t', races.char_race.dexmodified)
    print("Constitution", '\t', races.char_race.conmodified)
    print("Intelligence", '\t', races.char_race.intemodified)
    print("Wisdom  ", '\t', races.char_race.wismodified)
    print("Charisma", '\t', races.char_race.chamodified)
    print("\n")

    print("Ability modifiers:")
    print("Strength", '\t', races.char_race.stremodifier)
    print("Dexterity", '\t', races.char_race.dexmodifier)
    print("Constitution", '\t', races.char_race.conmodifier)
    print("Intelligence", '\t', races.char_race.intemodifier)
    print("Wisdom  ", '\t', races.char_race.wismodifier)
    print("Charisma", '\t', races.char_race.chamodifier)
    print("\n")

    print(f"Hit die: {classes.char_class.hit_die}")
    print(f"Hit points: {classes.char_class.hit_points_final}")
    print("\n")

    print("Racial proficiencies:")
    print(f"Weapons: {races.char_race.weaponsprof}")
    print(f"Armor: {races.char_race.armorprof}")
    print(f"Tools: {races.char_race.toolsprof}")
    print(f"Languages: {races.char_race.language}")
    print(f"Other: {races.char_race.raceprof}")
    print("\n")

    print("Class proficiencies:")
    print(f"Weapons: {classes.char_class.weaponsprof}")
    print(f"Armor: {classes.char_class.armorprof}")
    print(f"Tools: {classes.char_class.toolsprof}")
    print(f"Skills: {classes.char_class.skills}")
    print(f"Saving throws: {classes.char_class.saving_throw_proficiencies}")
    print(f"Primary ability: {classes.char_class.primary_ability}")
    print("\n")

    print("Character background proficiencies:")
    print(f"Tools: {backgrounds.char_background.tool_proficiencies}")
    print(f"Skills: {backgrounds.char_background.skill_proficiencies}")
    print(f"Languages: {backgrounds.char_background.languages}")
    print("\n")

    print("Equipment:")
    print(f"Your weapons are: {weapons.charweaponschoice}")
    print(f"Your armor is: {armor.chararmorchoice}")
    print(f"Your equipment is: {armor.charequipmentchoice}, {backgrounds.char_background.equipment}")
    print("\n")

    print("Features and spells (if applicable):")
    print(f"Your class features are: {classes.class_features}")
    print(f"Your cantrips are: {classes.class_cantrips}")
    print(f"Your first level spells are: {classes.class_spells1}")
    print("\n")

    print(f"Your background story is: {background_story_final}")
    print("\n")


def savechar():
    '''Gives option to save the created character in a text file.
    Called by __main__.'''
    while True:
        tosave = int(input("Press (1) to save your character to a text file or press (2) to skip this step: "))
        if tosave == 1:
            stdoutorigin = sys.stdout
            char = open(character1.charname + ".txt", 'w')
            sys.stdout = char
            finalstats()
            char.close()
            sys.stdout = stdoutorigin
            break
        elif tosave == 2:
            pass
            break
        else:
            print("Please select 1 or 2.")


# lists

alignments = [
    'lawful good', 'neutral good', 'chaotic good', 'lawful neutral',
    'true neutral', 'chaotic neutral', 'lawful evil',
    'neutral evil', 'chaotic evil'
]

background_story_final = ()
