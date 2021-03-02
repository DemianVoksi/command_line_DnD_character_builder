#!/usr/bin/env python


class armor:

    def __init__(self, typ, name, cost, AC, strength_requirement,
                 stealth, weight_lb):

        self.typ = typ
        self.name = name
        self.cost = cost
        self.AC = AC
        self.strength_requirement = strength_requirement
        self.stealth = stealth
        self.weight_lb = weight_lb


padded = armor(
    'la', 'padded', '5 gp', 11, 'None', 'disadvantage', 8
)
leather = armor(
    'la', 'leather', '10 gp', 11, 'None', 'None', 10
)
studded_leather = armor(
    'la', 'studded leather', '45 gp', 12, 'None', 'None', 13
)

hide = armor(
    'ma', 'hide', '10 gp', 12, 'None', 'None', 12
)
chain_shirt = armor(
    'ma', 'chain shirt', '50 gp', 13, 'None', 'None', 20
)
scale_mail = armor(
    'ma', 'scale mail', '50 gp', 14, 'None', 'disadvantage', 45
)
breastplate = armor(
    'ma', 'breastplate', '400 gp', 14, 'None', 'None', 20
)
half_plate = armor(
    'ma', 'half plate', '750 gp', 15, 'None', 'disadvantage', 40
)

ring_mail = armor(
    'ha', 'ring mail', '30 gp', 14, 'None', 'disadvantage', 40
)
chain_mail = armor(
    'ha', 'chain mail', '75 gp', 16, 13, 'disadvantage', 55
)
splint = armor(
    'ha', 'splint', '200 gp', 17, 15, 'disadvantage', 60
)
plate = armor(
    'ha', 'plate', '1500 gp', 18, 15, 'disadvantage', 65
)

shield = armor(
    'sh', 'shield', '10 gp', 2, 'None', 'None', 6
)

carmor = [
    padded, leather, studded_leather, hide, chain_shirt, scale_mail,
    breastplate, half_plate, ring_mail,
    chain_mail, splint, plate, shield
]

light_armor = [
    'padded', 'leather', 'studded leather'
]

medium_armor = [
    'hide', 'chain shirt', 'scale mail', 'breastplate', 'half plate'
]

heavy_armor = [
    'ring mail', 'chain mail', 'splint', 'plate'
]

shield = ['shield']

chararmorchoice = []

charequipmentchoice = []
