#VARIABLES
default girlsdormsecretfloor.introComment = False
default girlsdormsecretfloor.tatsumakisRoomEntered = False
default girlsdormsecretfloor.clairesRoomEntered = False

#SCREENS
init 1 python:
    scene_defs['girlsdormsecretfloor'] = {
        'music': MUSIC_SNEAK_THEME,
        'altermusic': MUSIC_SNEAK_THEME,
        'maps': {
            'default': ("girlsdormsecretroom", "girlsdormsecretroomhover"),
        },
        'hotspots': [
            ('angiesroom', (318, 266, 159, 552)),
            ('ivanasroom', (681, 314, 70, 244)),
            ('tatsumakisroom', (878, 299, 139, 201)),
            ('clairesroom', (1227, 288, 111, 363)),
            ('quietsroom', (1636, 181, 210, 857)),
            ('jinxroom', (801, 861, 445, 219)),
            ('exit', (0, 2, 166, 1078)),
        ],
        'sprites': [
            # Sprite(key, image, (x, y, w, h), showif)
        ]
    }

#LABELS
label girlsdormsecretfloor:
    if not girlsdormsecretfloor.introComment:
        "{i}As [player_name] emerged from the dark passages, he found himself in the middle of a fancy hallway.{/i}"
        "Oh shit, the rumors were true!"
        "It looks like the girl's dorm, but there's something strange about this place."
        "The only exit is the way I came in."
        "There are several doors. I wonder what's behind each one."
        "The first door on the left says... Angie."
        "She's the one who sent me the note."
        $ girlsdormsecretfloor.introComment = True
    jump girlsdormsecretfloor_loop

label girlsdormsecretfloor_loop:
    $ resetscene()
    call screen map('girlsdormsecretfloor')
    jump girlsdormsecretfloor_loop

label girlsdormsecretfloor_angiesroom:
    call angiesecretscene from _call_angiesecretscene
    $ gotoscene('girlsdormsecretfloor', transition=fade)

label girlsdormsecretfloor_ivanasroom:
    call ivanasecretscene from _call_ivanasecretscene
    $ gotoscene('girlsdormsecretfloor', transition=fade)

label girlsdormsecretfloor_tatsumakisroom:
    if not girlsdormsecretfloor.tatsumakisRoomEntered:
        "{i}When [player_name] entered the door, he felt his body stretching and contriving like he was being shaken by some kind of strange force.{/i}"
        "{i}He was entering a portal to a special dimension.{/i}"
        "{i}In this dimension he found a strange female waiting for him.{/i}"
        "{i}He seemed to recognize her from one of those cool anime he saw in his youth.{/i}"
        $ girlsdormsecretfloor.tatsumakisRoomEntered = True
    call tatsumakisecretscene from _call_tatsumakisecretscene
    $ gotoscene('girlsdormsecretfloor', transition=fade)

label girlsdormsecretfloor_clairesroom:
    if not girlsdormsecretfloor.clairesRoomEntered:
        "{i}When [player_name] entered the door, he felt his body stretching and contriving like he was being shaken by some kind of strange force.{/i}"
        "{i}He was entering a portal to a special dimension.{/i}"
        "{i}In this dimension he found a sexy naked gal waiting for him next to a really cool bike.{/i}"
        "{i}He seemed to recognize her from one of those cool videogames he played in his youth.{/i}"
        $ girlsdormsecretfloor.clairesRoomEntered = True
    call clairesecretscene from _call_clairesecretscene
    $ gotoscene('girlsdormsecretfloor', transition=fade)

label girlsdormsecretfloor_quietsroom:
    call quietsecretscene from _call_quietsecretscene
    $ gotoscene('girlsdormsecretfloor', transition=fade)

label girlsdormsecretfloor_jinxroom:
    call jinxsecretscene from _call_jinxsecretscene
    $ gotoscene('girlsdormsecretfloor', transition=fade)

label girlsdormsecretfloor_exit:
    $ gotoscene('boysdormtvroom', transition=fade)
