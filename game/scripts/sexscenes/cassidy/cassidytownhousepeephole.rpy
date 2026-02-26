#LABELS
label cassidy_townhousepeephole_scene:
    play music MUSIC_SEXY_THEME
    show cassidydildorubbinganim01fast with dissolve
    Cassidy "Ugh, I don't know why that asshole moved into our house."
    Cassidy "Playing in the attic was more fun 'cause I could make noises and stuff."
    Cassidy "Although... He is kind of sexy."
    Cassidy "Uhh... I love rubbing stuff against my pussy."
    Cassidy "It's a shame that I can't have a real cock to rub against me."
    Cassidy "I wonder if [player_name] has a nice cock..."
    Cassidy "Oh my god, gross, Cassidy."
    Cassidy "Stop thinking about it."
    scene cassidydildopush01 with fade
    Cassidy "Fuck, I can't hold it anymore."
    Cassidy "Now, let's play with my favorite toy."
    jump cassidy_townhousepeephole_dildo

label cassidy_townhousepeephole_dildo:
label .slow:
    scene cassidydildopushinganim01slow
    Developer "{i}This animation will be changed in the Extended Edition.{/i}"
    Cassidy "Yes, it feels soo good..."
    Cassidy "My clit is vibrating so hard, I feel I'm gonna explode any moment."
    menu:
        __("Faster"):
            jump .fast

label .fast:
    scene cassidydildopushinganim01fast
    Cassidy "YES! YES! YES! Fuck, I can't make too much noise or Alice is going to notice."
    Cassidy "Fuuuuuuuuuckinggg yeeesss!"
    menu:
        __("Slower"):
            jump .slow
        __("Finish"):
            jump .finish

label .finish:
    Cassidy "I'm cumming! I'm cumming!"
    scene cassidydildofrontcum with vpunch
    __("{i}Cassidy trembled so hard the entire bed moved from side to side.{/i}")
    Cassidy "Wow, that was so good."
    Cassidy "Now I can sleep thanks to [player_name]."
    Cassidy "Maybe one of this days I could even let him watch..."
    __("Ha, if only you knew.")
    $ townhousehallwayfirstnight.cassidyRoomChecked = True
    if cassidygallery == True:
        call screen cassidygallery
    return

#ANIMATIONS
image cassidydildorubbinganim01:
    'cassidydildorub01'
    pause 0.2
    'cassidydildorub02'
    pause 0.2
    'cassidydildorub03'
    pause 0.2
    'cassidydildorub04'
    pause 0.2
    'cassidydildorub05'
    pause 0.2
    'cassidydildorub06'
    pause 0.2
    'cassidydildorub07'
    pause 0.2
    'cassidydildorub08'
    pause 0.2
    'cassidydildorub07'
    pause 0.2
    'cassidydildorub06'
    pause 0.2
    'cassidydildorub05'
    pause 0.2
    'cassidydildorub04'
    pause 0.2
    'cassidydildorub03'
    pause 0.2
    'cassidydildorub02'
    pause 0.2
    repeat

image cassidydildorubbinganim01fast:
    'cassidydildorub01'
    pause 0.1
    'cassidydildorub02'
    pause 0.1
    'cassidydildorub03'
    pause 0.1
    'cassidydildorub04'
    pause 0.1
    'cassidydildorub05'
    pause 0.1
    'cassidydildorub06'
    pause 0.1
    'cassidydildorub07'
    pause 0.1
    'cassidydildorub08'
    pause 0.1
    'cassidydildorub07'
    pause 0.1
    'cassidydildorub06'
    pause 0.1
    'cassidydildorub05'
    pause 0.1
    'cassidydildorub04'
    pause 0.1
    'cassidydildorub03'
    pause 0.1
    'cassidydildorub02'
    pause 0.1
    repeat

image cassidydildopushinganim01slow:
    'cassidydildofront01'
    pause 0.2
    'cassidydildofront02'
    pause 0.2
    'cassidydildofront03'
    pause 0.2
    'cassidydildofront04'
    pause 0.2
    'cassidydildofront05'
    pause 0.2
    'cassidydildofront06'
    pause 0.2
    'cassidydildofront05'
    pause 0.2
    'cassidydildofront04'
    pause 0.2
    'cassidydildofront03'
    pause 0.2
    'cassidydildofront02'
    pause 0.2
    repeat

image cassidydildopushinganim01fast:
    'cassidydildofront01'
    pause 0.08
    'cassidydildofront02'
    pause 0.08
    'cassidydildofront03'
    pause 0.08
    'cassidydildofront04'
    pause 0.08
    'cassidydildofront05'
    pause 0.08
    'cassidydildofront06'
    pause 0.08
    'cassidydildofront05'
    pause 0.08
    'cassidydildofront04'
    pause 0.08
    'cassidydildofront03'
    pause 0.08
    'cassidydildofront02'
    pause 0.08
    repeat
