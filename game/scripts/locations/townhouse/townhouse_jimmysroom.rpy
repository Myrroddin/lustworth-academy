#VARIABLES
default townhousejimmysroom.pcIntroCommentSaid = False

#SCREENS
init 1 python:
    scene_defs['townhousejimmysroom'] = {
        'music': MUSIC_TOWNHOUSE,
        'altermusic': MUSIC_TOWNHOUSE,
        'maps': {
            'morning': ('jimmytownroomday01', 'jimmytownroomday01hover'),
            'afternoon': ('jimmytownroomafter01', 'jimmytownroomafter01hover'),
            'default': ('jimmytownroomafter01', 'jimmytownroomafter01hover'),
            'night': ('jimmytownbedroomnight', "jimmytownroomemptyhover"),
        },
        'hotspots': [
            ('pc', (110, 394, 266, 161)),
            ('closet', (748, 391, 389, 248)),
            ('bed', (706, 648, 852, 231)),
            ('floorcrack', (1570, 980, 151, 98)),
            ('tohallway', (0, 888, 574, 192)),
        ],
        'sprites': [
            # Sprite(key, image, (x, y, w, h), showif)
        ]
    }

#LABELS
label townhousejimmysroom:
    $ day3morning   = (calendar.when == (PROLOGUE, SATURDAY, MORNING))
    $ day3afternoon = (calendar.when == (PROLOGUE, SATURDAY, AFTERNOON))
    $ day3evening   = (calendar.when == (PROLOGUE, SATURDAY, EVENING))
    $ day4night     = (calendar.when == (PROLOGUE, SUNDAY, NIGHT))
    if calendar.when == (PROLOGUE, SUNDAY, MORNING):
        jump prologue_dakotaranchintro
    elif calendar.when[1:] == (MONDAY, MORNING):
        jump townhousemondaymorning
    jump townhousejimmysroom_loop

label townhousejimmysroom_loop:
    $ resetscene()
    call screen map('townhousejimmysroom')
    jump townhousejimmysroom_loop

label townhousejimmysroom_pc:
    if day3morning:
        if quests.blairUSB == SATISFIED:
            "Alright, let's get to business."
            jump prologue_blairlesbianvideo
        elif quests.blairUSB != COMPLETE:
            "I need to find my USB stick before I can start using my computer."
        else:
            "I'll have time to use my computer later."
    elif day3afternoon and not prologue.dakotaJobOffer:
        "I'll have time to use my computer later."
    elif day4night and not prologue.cassidyShower:
        "I need to take a shower first, but maybe I could use my PC for bit after."
    else:
        if calendar.when[0] == PROLOGUE and not townhousejimmysroom.pcIntroCommentSaid:
            "{i}Sigh.{/i} I think I finally have time to use my PC for a bit."
            $ townhousejimmysroom.pcIntroCommentSaid = True
        call jimmyspc from _call_jimmyspc_2
    jump townhousejimmysroom_loop

label townhousejimmysroom_closet:
    show jimmy neutral with dissolve
    if day3morning and Jimmy.outfit == JIMMY_STEALTH:
        "It'll feel great to be in some fresh clothes again."
        $ Jimmy.outfit = JIMMY_DEFAULT
        show jimmy smug with dissolve
        "That's better."
    else:
        "I don't need to change clothes."
    hide jimmy with dissolve
    jump townhousejimmysroom_loop

label townhousejimmysroom_bed:
    $ time = calendar.when[2]
    if prologue.complete == True:
        menu:
            "Take a nap" if calendar.when[2] < NIGHT and not day3evening:
                jump nap_menu
            "Go to sleep" if not day3morning:
                hide screen freeroamhud
                if glob.halloweenEventComplete and not quests.drunkblair == COMPLETE:
                    jump blairdrunkscene
                # Handles bringing the player back to school on Monday
                elif calendar.when[1:] == (MONDAY, MORNING):
                    jump townhousemondaymorning
                else:
                    call sleep from _call_sleep_6
                $ gotoscene('townhousejimmysroom', transition=fade)
            "Nevermind":
                jump townhousejimmysroom_loop
    elif day4night:
        if prologue.cassidyShower == True:
            jump prologue_day4end
        else:
            "Gotta take a shower first."
    elif prologue.findtherope == True:
        "Alright, everything is ready. I'll wait 'til midnight to sneak out."
        $ prologue.afternoonNap = True
        call nexttime from _call_nexttime_27
        $ gotoscene('townhousejimmysroomnightinfiltration')
    elif prologue.findtherope == False:
        "I have things to do. I don't want to sleep now."
    elif day4night and not prologue.cassidyShower:
        "I need to take a shower first, I'm all sweaty after working at the ranch."
    $ gotoscene('townhousejimmysroom')

label townhousemondaymorning:
    $ showscene('townhousejimmysroom', transition=fade)
    play music MUSIC_KASSANDRAS_THEME
    show kassandra pajamas with dissolve
    Kassandra "Good morning, [player_name]!"
    Kassandra "Come have some breakfast, and then I'll take you and your [roommate_female]s to the academy."
    Kassandra "Here's your weekly allowance."
    $ Jimmy.money += 25
    call yougotmoney from _call_yougotmoney_6
    Jimmy "Thanks, [roommate_female]."
    if calendar.when[0] == PROLOGUE:
        jump chapterone_start
    scene black with fade
    $ gotoscene('schoolgroundsmaingate', transition=fade)

label townhousejimmysroom_floorcrack:
    hide screen freeroamhud
    show cassidybedroomnightpeek with dissolve
    "Looks like Cassidy's not in her room right now."
    hide cassidybedroomnightpeek with dissolve
    jump townhousejimmysroom_loop

label townhousejimmysroom_tohallway:
    if day3morning and Jimmy.outfit == JIMMY_STEALTH:
        "I should really change before I do anything else."
    else:
        $ gotoscene('townhousehallway')
    jump townhousejimmysroom_loop
