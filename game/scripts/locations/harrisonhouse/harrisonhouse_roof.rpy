init 1 python:
    scene_defs['harrisonhouseroof'] = {
        'music': MUSIC_HARRISONPARTYROOF_THEME,
        'altermusic': MUSIC_HARRISONPARTYROOF_THEME,
        'maps': {
            'default': ('harrisonhouseroof', 'harrisonhouseroofhover'),
        },
        'hotspots': [
            ('jacuzzidoor', (136, 222, 129, 530)),
            ('backdown', (58, 899, 1203, 181)),
            ('flagpole', (1641, 0, 277, 1080)),
        ],
        'sprites': [
        ]
    }

#LABELS
label harrisonhouseroof:
    jump harrisonhouseroof_loop

label harrisonhouseroof_loop:
    $ resetscene()
    call screen map('harrisonhouseroof')
    jump harrisonhouseroof_loop

label harrisonhouseroof_jacuzzidoor:
    Jimmy "I think there is a jacuzzi inside."
    Jimmy "But it's closed."
    jump harrisonhouseroof_loop

label harrisonhouseroof_backdown:
    $ gotoscene('harrisonhousefloor2')

label harrisonhouseroof_flagpole:
    Jimmy "Here's the flag."
    Jimmy "Let me replace it with the one Gary gave us."
    scene harrisonhouseroofflag with fade
    Jimmy "Oh, no... The preps are going to be pissed."
    Jimmy "Gary has a really fucked-up sense of humor."
    $ quests.halloweenFakeFlag = COMPLETE
    $ Jimmy.inventory.remove(ItemFakeFlag)
    $ gotoscene('harrisonhouseroofflag')
