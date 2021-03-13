# imports

from random import randint
import races

# functions


def dy(y):
    '''Sets the number of sides of the die.
    Called by xdy(x, y).'''
    return randint(1, y)


def xdy(x, y):
    '''Sets the number of dy-sided dies rolled.
    Called by roll(die).'''
    return list(dy(y) for _ in range(x))


def rollintro():
    '''Intro to the rolling question.
    Called by __main__.'''
    print("\n")
    print("It's time to find out your ability scores.")
    print("You have two options: you can roll for ability scores or you can use the default roll die is: 15, 14, 13, 12, 10, 8.")


def roll(die):
    '''Base 4d6 roll and removal of the smallest number.
    Called by def appendaj().'''
    die = xdy(4, 6)
    die.remove(min(die))
    return sum(die)


def apendaj():
    '''Appends the rolls to the base ability score list.
    Called by roller().'''
    base_ability_scores.clear()
    base_ability_scores.append(roll('dice1'))
    base_ability_scores.append(roll('dice2'))
    base_ability_scores.append(roll('dice3'))
    base_ability_scores.append(roll('dice4'))
    base_ability_scores.append(roll('dice5'))
    base_ability_scores.append(roll('dice6'))
    return base_ability_scores


def printbas():
    '''Prints the base ability scores list.
    Called by roller().'''
    return base_ability_scores


def roller():
    '''Roll a 4d6 or go with the default roll.
    Called by __main__.'''
    print("\n")
    print("It's time to find out your ability scores.")
    print("You have two options: you can roll for ability scores or you can use the default roll die is: 15, 14, 13, 12, 10, 8.")

    while True:
        roll_input = int(input("If you want to roll for your ability scores, press (1). If you want to use the default roll press (2): "))
        if roll_input == 1:

            roll_again = "yes"

            while roll_again == "yes" or "y":
                apendaj()
                print("Your roll is:")
                print(printbas())

                roll_again = input("Do you want to roll again? Write yes to roll again. Press enter if you are happy with your roll: ")
                if roll_again in ['yes', 'y']:
                    print('\n')
                else:
                    break

            break

        if roll_input == 2:

            for n in default_ability_scores:
                base_ability_scores.append(n)
            print("Your base ability scores are:", base_ability_scores)
            break


def scores_abilities(ability, abilityname):
    '''Chooses a score for an ability.
    Called by setscore().'''
    while True:
        ability = int(input(f"Select one of your scores as your {abilityname} score: "))
        if ability not in base_ability_scores:
            print("You have selected an invalid score.")
        else:
            base_ability_scores.remove(ability)
            print(f"Remaining scores to choose from: {base_ability_scores}")
            break
    charraceability = ability
    return charraceability


def setscore():
    '''Sets a score for the races.char_race.ability variables.
    Called by __main__.'''
    races.char_race.stre = scores_abilities('strength', 'strength')
    print(f"Your strength is {races.char_race.stre}.")

    races.char_race.dex = scores_abilities('dexterity', 'dexterity')
    print(f"Your dexterity is {races.char_race.dex}.")

    races.char_race.con = scores_abilities('constitution', 'constitution')
    print(f"Your constitution is {races.char_race.con}.")

    races.char_race.inte = scores_abilities('intelligence', 'intelligence')
    print(f"Your intelligence is {races.char_race.inte}.")

    races.char_race.wis = scores_abilities('wisdom', 'wisdom')
    print(f"Your wisdom is {races.char_race.wis}.")

    races.char_race.cha = scores_abilities('charisma', 'charisma')
    print(f"Your charisma is {races.char_race.cha}.")


def baseabilities():
    '''Prints base ability scores.
    Called by __main__.'''
    print('\n')
    print("You have finished choosing your base ability scores. They are: ")
    print("Ability", '\t', "Score")
    print("-------", '\t', "-----")
    print("Strength", '\t', races.char_race.stre)
    print("Dexterity", '\t', races.char_race.dex)
    print("Constitution", '\t', races.char_race.con)
    print("Intelligence", '\t', races.char_race.inte)
    print("Wisdom  ", '\t', races.char_race.wis)
    print("Charisma", '\t', races.char_race.cha)
    print("\n")


def modifyabilities():
    '''Calls on the class method to modify base ability scores.
    Called by __main__.'''
    races.char_race.stre_modified()
    races.char_race.dex_modified()
    races.char_race.con_modified()
    races.char_race.inte_modified()
    races.char_race.wis_modified()
    races.char_race.cha_modified()


def modifiedabilities():
    '''Prints modified abilities.
    Called by __main__.'''
    print('\n')
    print("We now have to apply racial modifiers to your scores. Your modified ability scores look like this: ")
    print("Ability", '\t', "Score")
    print("-------", '\t', "-----")
    print("Strength", '\t', races.char_race.stremodified)
    print("Dexterity", '\t', races.char_race.dexmodified)
    print("Constitution", '\t', races.char_race.conmodified)
    print("Intelligence", '\t', races.char_race.intemodified)
    print("Wisdom  ", '\t', races.char_race.wismodified)
    print("Charisma", '\t', races.char_race.chamodified)
    print("\n")


def halfelf_choice():
    '''Calculates half elf modified abilities.
    Called by halfelf_abilities()'''
    while True:
        x = str(input("What is the ability you want to add 1 point to? Enter the name of the ability in lowercase letters: "))
        if x == 'strength':
            races.char_race.stremodified = races.char_race.stremodified + 1
            break
        elif x == 'dexterity':
            races.char_race.dexmodified = races.char_race.dexmodified + 1
            break
        elif x == 'constitution':
            races.char_race.conmodified = races.char_race.conmodified + 1
            break
        elif x == 'intelligence':
            races.char_race.intemodified = races.char_race.intemodified + 1
            break
        elif x == 'wisdom':
            races.char_race.wismodified = races.char_race.wismodified + 1
            break
        elif x == 'charisma':
            races.char_race.chamodified = races.char_race.chamodified + 1
            break
        else:
            print("Check your spelling.")


def halfelf_abilities():
    '''Sets half elf modified abilities.
    Called by __main__.'''
    print('''But, since your character is a half elf, there is one more step to complete.''')
    print('''Half elves automatically increase their charisma by 2 points, but can add one more point to two abilities of their choosing.''')
    halfelf_choice()
    halfelf_choice()


def modifiers_intro():
    '''Intro to modifiers. 
    Called by __main__.'''
    print("Now that you have your modified ability scores, we have to see how your scores will influence your game.")
    print("A lot of the time that you try to do something in D&D, you will have to roll a dice to see how well your attempt to do so went.")
    print("For example, if you try to hit your enemy with a rock, you might have to roll to see how good that went.")
    print("For such an attempt, it would be good if you had high dexterity.")
    print("On every such roll, we add or subtract from your roll your ability modifier.")
    print("The ability modifier for a score depends on how high (or low) your score was.")
    print("Let's see yours!")
    print("\n")


def modifiers(ab):
    '''Ab is the ability score (races.char_race.abilitymodified),
    and the function calculates the ability modifier according
    to the ability score.
    Called by declare_modifier().'''
    if ab == int(1):
        abb = int(-5)
        return abb
    elif ab == int(2) or ab == int(3):
        abb = int(-4)
        return abb
    elif ab == int(4) or ab == int(5):
        abb = int(-3)
        return abb
    elif ab == int(6) or ab == int(7):
        abb = int(-2)
        return abb
    elif ab == int(8) or ab == int(9):
        abb = int(-1)
        return abb
    elif ab == int(10) or ab == int(11):
        abb = int(0)
        return abb
    elif ab == int(12) or ab == int(13):
        abb = int(1)
        return abb
    elif ab == int(14) or ab == int(15):
        abb = int(2)
        return abb
    elif ab == int(16) or ab == int(17):
        abb = int(3)
        return abb
    elif ab == int(18) or ab == int(19):
        abb = int(4)
        return abb
    elif ab == int(20) or ab == int(21):
        abb = int(5)
        return abb
    elif ab == int(22) or ab == int(23):
        abb = int(6)
        return abb
    elif ab == int(24) or ab == int(25):
        abb = int(7)
        return abb
    elif ab == int(26) or ab == int(27):
        abb = int(8)
        return abb
    elif ab == int(28) or ab == int(29):
        abb = int(9)
        return abb
    elif ab == int(30):
        abb = int(10)
        return abb
    else:
        abb = ("Well, you're off the fucking charts, buddy.")
        return abb


def declare_modifier():
    '''Called by main module.'''
    races.char_race.stremodifier = modifiers(races.char_race.stremodified)
    races.char_race.dexmodifier = modifiers(races.char_race.dexmodified)
    races.char_race.conmodifier = modifiers(races.char_race.conmodified)
    races.char_race.intemodifier = modifiers(races.char_race.intemodified)
    races.char_race.wismodifier = modifiers(races.char_race.wismodified)
    races.char_race.chamodifier = modifiers(races.char_race.chamodified)


# lists

base_ability_scores = []

default_ability_scores = [15, 14, 13, 12, 10, 8]
