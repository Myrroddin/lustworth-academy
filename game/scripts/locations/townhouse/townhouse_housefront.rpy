init 1 python:
    scene_defs['townhousefront'] = {
        'music': MUSIC_TOWNHOUSE,
        'altermusic': MUSIC_TOWNHOUSE,
        'maps': {
            'morning': ('housefrontfallday', 'housefrontfalldayhover'),
            'afternoon': ("housefrontfallafternoon", "housefrontfallafternoonhover"),
            'evening':   ("housefrontfallevening", "housefrontfalleveninghover"),
            'night':   ("housefrontfallnight", "housefrontfallnighthover")
        },
        'hotspots': [
            ('tothemainmap', (3, 921, 1914, 157)),
            ('tolivingroom', (744, 453, 411, 423)),
        ],
        'sprites': [
            # Sprite(key, image, (x, y, w, h), showif)
        ]
    }

#LABELS
label townhousefront:
    if quests.artProject == ACTIVE:
        if calendar.when[2] == AFTERNOON:
            jump mikuartprojectsceneintro
        else:
            Jimmy "Miku should be here in the afternoon."
    elif quests.punnyPrivateLessons == ACTIVE and moneyhelp01 == False:
        "There is something in the floor..."
        call item_pickup(ItemMoneyFound01) from _call_item_pickup_30
        $ Jimmy.money += 100
        $ moneyhelp01 = True
        Jimmy "Ohhh, 100 bucks. Lucky day!"
        $ Jimmy.inventory.remove(ItemMoneyFound01)
    jump townhousefront_loop

label townhousefront_loop:
    $ resetscene()
    call screen map('townhousefront')
    jump townhousefront_loop

label townhousefront_tolivingroom:
    $ gotoscene('townhouselivingroom')

label townhousefront_tothemainmap:
    $ gotoscene('townpierarea')
