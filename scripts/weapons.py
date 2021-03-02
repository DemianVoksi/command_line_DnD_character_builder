#!/usr/bin/env python


class weapon:

    def __init__(self, typ, name, cost, damage, weight_lb, properties):

        self.typ = typ
        self.name = name
        self.cost = cost
        self.damage = damage
        self.weight_lb = weight_lb
        self.properties = properties


# simple melee weapons

club = weapon(
    'smw', 'club', '1 sp', '1d4 bludgeoning', 1, 'light'
)
dagger = weapon(
    'smw', 'dagger', '2 gp', '1d4 piercing', 1,
    'finesse, light, thrown (range 20/60)'
)
greatclub = weapon(
    'smw', 'greatclub', '2 sp', '1d8 bludgeoning',
    10, 'two-handed'
)
handaxe = weapon(
    'smw', 'handaxe', '5 gp', '1d6 slashing', 2,
    'light, thrown (range 20/60'
)
javelin = weapon(
    'smw', 'javelin', '5 sp', '1d6 piercing',
    2, 'thrown (range 30/120)'
)
light_hammer = weapon(
    'smw', 'light hammer', '2 gp', '1d4 bludgeoning',
    4, 'light, thrown (range 20/60)'
)
mace = weapon(
    'smw', 'mace', '5 gp', '1d6 bludgeoning', 4, 'None'
)
quarterstaff = weapon(
    'smw', 'quarterstaff', '2 sp',
    '1d6 bludgeoning', 4, 'versatile(1d8)'
)
sickle = weapon(
    'smw', 'sickle', '1 gp', '1d4 slashing', 2, 'light'
)
spear = weapon(
    'smw', 'spear', '1 gp', '1d6 piercing',
    3, 'thrown (range 20/60), versatile (1d8)'
)

# simple ranged weapons

light_crossbow = weapon(
    'srw', 'light crossbow', '25 gp', '1d8 piercing',
    5, 'ammunition (range 80/320), loading, two-handed'
)
dart = weapon(
    'srw', 'dart', '5 cp', '1d4 piercing',
    0.25, 'finesse, thrown (range 20/60)'
)
shortbow = weapon(
    'srw', 'shortbow', '25 gp', '1d6 piercing',
    2, 'ammunition (range 80/320), two-handed'
)
sling = weapon(
    'srw', 'sling', '1 sp', '1d4 bludgeoning',
    'None', 'ammunition (range 30/120)'
)

# martial melee weapons

battleaxe = weapon(
    'mmw', 'battleaxe', '10 gp', '1d8 slashing', 4, 'versatile (1d10)'
)
flail = weapon(
    'mmw', 'flail', '10 gp', '1d8 bludgeoning', 2, 'None'
)
glaive = weapon(
    'mmw', 'glaive', '20 gp', '1d10 slashing',
    6, 'heavy, reach, two-handed'
)
greataxe = weapon(
    'mmw', 'greataxe', '30 gp', '1d12 slashing',
    7, 'heavy, two-handed'
)
greatsword = weapon(
    'mmw', 'greatsword', '50 gp', '2d6 slashing',
    6, 'heavy, two-handed'
)
halberd = weapon(
    'mmw', 'halberd', '20 gp', '1d10 slashing',
    6, 'heavy, reash, two-handed'
)
lance = weapon(
    'mmw', 'lance', '10 gp', '1d12 piercing', 6, 'reach, special'
)
longsword = weapon(
    'mmw', 'longsword', '15 gp', '1d8 slashing',
    3, 'versatile (1d10)'
)
maul = weapon(
    'mmw', 'maul', '10 gp', '2d6 bludgeoning',
    10, 'heavy, two-handed'
)
morningstar = weapon(
    'mmw', 'morningstar', '15 gp', '1d8 piercing', 4, 'None'
)
pike = weapon(
    'mmw', 'pike', '5 gp', '1d10 piercing',
    18, 'heavy, reach, two-handed'
)
rapier = weapon(
    'mmw', 'rapier', '25 gp', '1d8 piercing', 2, 'finesse'
)
scimitar = weapon(
    'mmw', 'scimitar', '25 gp', '1d6 slashing',
    3, 'finesse, light'
)
shortsword = weapon(
    'mmw', 'shortsword', '10 gp',
    '1d6 piercing', 2, 'finesse, light'
)
trident = weapon(
    'mmw', 'trident', '5 gp', '1d6 piercing',
    4, 'thrown (range 20/60), versatile (1d8)'
)
war_pick = weapon(
    'mmw', 'war pick', '5 gp', '1d8 piercing', 2, 'None'
)
warhammer = weapon(
    'mmw', 'warhammer', '15 gp',
    '1d8 bludgeoning', 2, 'versatile (1d10)'
)
whip = weapon(
    'mmw', 'whip', '2 gp', '1d4 slashing',
    3, 'finesse, reach'
)

# martial ranged weapons

blowgun = weapon(
    'mrw', 'blowgun', '10 gp', '1 piercing',
    1, 'ammunition (range 25/100), loading'
)
hand_crossbow = weapon(
    'mrw', 'hand crossbow', '75 gp', '1d6 piercing',
    3, 'ammunition (range 30/120), light, loading'
)
heavy_crossbow = weapon(
    'mrw', 'heavy crossbow', '50 gp', '1d10 piercing',
    18, 'ammunition (range 100/400), heavy, loading, two-handed'
)
longbow = weapon(
    'mrw', 'longbow', '50 gp', '1d8 piercing',
    2, 'ammunition (range 150/600), heavy, two-handed'
)
net = weapon(
    'mrw', 'net', '1 gp', 'None',
    3, 'special, thrown (range 5/15)'
)

# lists

cweapon = [
    club, dagger, greatclub, handaxe, javelin, light_hammer,
    mace, quarterstaff, sickle, spear, light_crossbow, dart,
    shortbow, sling, battleaxe, flail, glaive, greataxe,
    greatsword, halberd, lance, longsword, maul,
    morningstar, pike, rapier, scimitar, shortsword, trident,
    war_pick, warhammer, whip, blowgun,
    hand_crossbow, heavy_crossbow, longbow, net
]

weapons = [
    'club', 'dagger', 'greatclub', 'handaxe', 'javelin',
    'light hammer', 'mace', 'quarterstaff', 'sickle', 'spear',
    'light crossbow', 'dart', 'shortbow', 'sling',
    'battleaxe', 'flail', 'glaive', 'greataxe', 'greatsword',
    'halberd', 'lance', 'longsword', 'maul', 'morningstar',
    'pike', 'rapier', 'scimitar', 'shortsword', 'trident',
    'war pick', 'warhammer', 'whip', 'blowgun',
    'hand crossbow', 'heavy crossbow', 'longbow', 'net'
]

simple_weapons = [
    'club', 'dagger', 'greatclub', 'handaxe', 'javelin',
    'light hammer', 'mace', 'quarterstaff', 'sickle',
    'spear', 'light crossbow', 'dart', 'shortbow', 'sling'
]

martial_weapons = [
    'battleaxe', 'flail', 'glaive', 'greataxe',
    'greatsword', 'halberd', 'lance', 'longsword', 'maul',
    'morningstar', 'pike', 'rapier', 'scimitar',
    'shortsword', 'trident', 'war pick', 'warhammer',
    'whip', 'blowgun', 'hand crossbow', 'heavy crossbow',
    'longbow', 'net'
]

melee_weapons = [
    'club', 'dagger', 'greatclub', 'handaxe',
    'javelin', 'light hammer', 'mace', 'quarterstaff',
    'sickle', 'spear', 'battleaxe', 'flail', 'glaive',
    'greataxe', 'greatsword', 'halberd', 'lance',
    'longsword', 'maul', 'morningstar', 'pike', 'rapier',
    'scimitar', 'shortsword', 'trident',
    'war pick', 'warhammer', 'whip'
]

ranged_weapons = [
    'light crossbow', 'dart', 'shortbow', 'sling',
    'blowgun', 'hand crossbow', 'heavy crossbow',
    'longbow', 'net'
]

simple_melee_weapons = [
    'club', 'dagger', 'greatclub', 'handaxe', 'javelin',
    'light hammer', 'mace', 'quarterstaff',
    'sickle', 'spear'
]

simple_ranged_weapons = ['light crossbow', 'dart', 'shortbow', 'sling']

martial_melee_weapons = [
    'battleaxe', 'flail', 'glaive', 'greataxe', 'greatsword',
    'halberd', 'lance', 'longsword', 'maul', 'morningstar',
    'pike', 'rapier', 'scimitar', 'shortsword',
    'trident', 'war pick', 'warhammer', 'whip'
]

martial_ranged_weapons = [
    'blowgun', 'hand crossbow',
    'heavy crossbow', 'longbow', 'net'
]

charweaponschoice = []
