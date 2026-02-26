#SCREENS
init 1 python:
    scene_defs['townhousehallway'] = {
        'music': MUSIC_TOWNHOUSE,
        'altermusic': MUSIC_TOWNHOUSE,
        'maps': {
            'morning': ('townhousehallwayfallday', 'townhousehallwayfalldayhover'),
            'afternoon': ('townhousehallwayfallafternoon', 'townhousehallwayfallafternoonhover'),
            'evening': ('townhousehallwayfallevening', 'townhousehallwayfalleveninghover'),
            'night': ('townhousehallwayfallnight', 'townhousehallwayfallnighthover'),
        },
        'hotspots': [
            ('window', (0, 146, 126, 633)),
            ('jimmysroom', (387, 1, 414, 205)),
            ('blairsroom', (240, 411, 177, 353)),
            ('cassidysroom', (705, 256, 163, 586)),
            ('alicesroom', (1021, 81, 237, 859)),
            ('bathroom', (509, 352, 124, 433)),
            ('stairs', (1484, 0, 435, 1077)),
        ],
        'sprites': [
            # Sprite(key, image, (x, y, w, h), showif)
        ]
    }

#LABELS
label townhousehallway:
    $ day4night = (calendar.when == (PROLOGUE, SUNDAY, NIGHT))
    jump townhousehallway_loop

label townhousehallway_loop:
    $ resetscene()
    call screen map('townhousehallway')
    jump townhousehallway_loop

label townhousehallway_window:
    __("Looks like a sunny day.")
    jump townhousehallway_loop

label townhousehallway_jimmysroom:
    $ gotoscene('townhousejimmysroom')

label townhousehallway_bathroom:
    if day4night:
        if not prologue.cassidyShower:
            jump prologue_cassidyshower
        else:
            __("Cassidy's still in there. I shouldn't bother her.")
            __("I'll just take a shower in the morning.")
    else:
        __("I don't need to use the bathroom right now.")
    jump townhousehallway_loop

label townhousehallway_blairsroom:
    __("i}*Knock, knock.*{/i}")
    pause 0.5
    __("No answer.")
    jump townhousehallway_loop

label townhousehallway_cassidysroom:
    __("i}*Knock, knock.*{/i}")
    if quests.cassidyTrials == SATISFIED:
        if calendar.when[2] == NIGHT:
            Cassidy "Come in..."
            call cassidytrialbedroomtalk from _call_cassidytrialbedroomtalk
            jump townhousehallway_loop
        else:
            __("She's usually in her room at night.")
            jump townhousehallway_loop
    elif quests.cassidyFirstFuck == SATISFIED:
        if calendar.when[2] == NIGHT:
            Cassidy "Come in..."
            jump cassidynightdate01
        else:
            __("i}I wonder how Cassidy is doing with her cheerleader thing, thought [player_name].{/i}")
            __("i}Not knowing that his [roommate_female] was waiting for him to visit her during the night.{/i}")
    pause 0.5
    __("No answer.")
    jump townhousehallway_loop

label townhousehallway_alicesroom:
    if alice_breakfastwarning == True:
        __("I shouldn't bother her any more.")
    elif breakfast_ready == True:
        jump townhousehallway_alicereading
    else:
        __("I shouldn't bother her.")
    jump townhousehallway_loop

label townhousehallway_stairs:
    $ gotoscene('townhouselivingroom')

#CUTSCENES
label townhousehallway_alicereading:
    __("i}*Knock, knock.*{/i}")
    Alice "Come in!"
    hide screen freeroamhud
    play music MUSIC_ALICES_THEME
    scene alicereadingpose01 with fade
    __("i}When [player_name] opened the door, he found Alice in a bizarre pose.{/i}")
    __("i}From his perspective, he could clearly see the shape of her ass.{/i}")
    Alice "Who is it?"
    Jimmy "Umm, hey, it's me."
    Alice "Oh my god, [player_name]!"
    play sound SOUND_RECORD_SCRATCH
    scene alicebedroom
    show alice casual
    show jimmy neutral
    with vpunch
    Alice "I forgot you were here."
    Alice "Sorry, it must've been weird to see me like that."
    Alice "I just... like to read a lot, and I have to stretch my body so I don't get sore from being in one position."
    Jimmy unamused "Don't worry, I get it."
    Jimmy "You seem to be really... flexible."
    Alice casual blush "Oh... ha, ha... Umm, yeah, thanks."
    Jimmy "Anyways, I just wanted to let you know that breakfast is ready."
    Jimmy "Kassandra is waiting for us in the kitchen."
    Alice "Oh, thanks for telling me."
    Alice "I'll be down in a minute."
    Jimmy "Cool."
    hide jimmy with dissolve
    Alice "{i}Oh god. That was so embarassing.{/i}"
    Alice "{i}I wonder what he was thinking when he saw me like that.{/i}"
    $ alice_breakfastwarning = True
    $ sexscenes.aliceReading = True
    $ gotoscene('townhousehallway', transition=fade)
