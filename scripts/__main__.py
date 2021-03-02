#!/usr/bin/env python

# imports

import mycharacter
import races
import classes
import subclasses
import backgrounds
import roller
import equipment


# functions


def conclusion(what, id_choice):
    print(f"Ok, so your {what} is {id_choice.name}.")
    print('\n')


def main():
    mycharacter.intro()
    mycharacter.plyrname()
    mycharacter.character()
    mycharacter.level()
    mycharacter.sex()
    mycharacter.alignment()

    races.ridentitytovariable()
    conclusion('race', races.char_race)
    classes.cidentitytovariable()
    conclusion('class', classes.char_class)
    subclasses.sidentitytovariable()
    conclusion('subclass', subclasses.char_subclass)
    subclasses.subclassperks()
    backgrounds.bidentitytovariable()
    conclusion('background', backgrounds.char_background)

    roller.roller()
    roller.setscore()
    roller.baseabilities()
    roller.modifyabilities()
    if races.char_race.name != 'half elf':
        roller.modifiedabilities()
    else:
        roller.halfelf_abilities()
        roller.modifiedabilities()
    roller.declare_modifier()
    classes.hit_points_calc()

    races.print_racial_proficiencies()
    classes.allclassprof()

    if classes.char_class.name == 'barbarian':
        equipment.barbarianequipment()
    elif classes.char_class.name == 'bard':
        equipment.bardequipment()
    elif classes.char_class.name == 'cleric':
        equipment.clericequipment()
    elif classes.char_class.name == 'druid':
        equipment.druidequipment()
    elif classes.char_class.name == 'fighter':
        equipment.fighterequipment()
    elif classes.char_class.name == 'monk':
        equipment.monkequipment()
    elif classes.char_class.name == 'paladin':
        equipment.paladinequipment()
    elif classes.char_class.name == 'ranger':
        equipment.rangerequipment()
    elif classes.char_class.name == 'rogue':
        equipment.rogueequipment()
    elif classes.char_class.name == 'sorcerer':
        equipment.sorcererequipment()
    elif classes.char_class.name == 'warlock':
        equipment.warlockequipment()
    elif classes.char_class.name == 'wizard':
        equipment.wizardequipment()
    else:
        pass

    if classes.char_class.name == 'barbarian':
        classes.featandspellbarbarian()
    elif classes.char_class.name == 'bard':
        classes.featandspellbard()
    elif classes.char_class.name == 'cleric':
        classes.featandspellcleric()
    elif classes.char_class.name == 'druid':
        classes.featandspelldruid()
    elif classes.char_class.name == 'fighter':
        classes.featandspellfighter()
    elif classes.char_class.name == 'monk':
        classes.featandspellmonk()
    elif classes.char_class.name == 'paladin':
        classes.featandspellpaladin()
    elif classes.char_class.name == 'ranger':
        classes.featandspellranger()
    elif classes.char_class.name == 'rogue':
        classes.featandspellrogue()
    elif classes.char_class.name == 'sorcerer':
        classes.featandspellsorcerer()
    elif classes.char_class.name == 'warlock':
        classes.featandspellwarlock()
    elif classes.char_class.name == 'wizard':
        classes.featandspellwizard()
    else:
        pass

    mycharacter.background()
    mycharacter.finalstats()
    mycharacter.savechar()


# main

if __name__ == '__main__':
    main()
