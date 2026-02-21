label musicclass:
    hide screen freeroamhud
    scene musicclassroomfallday with fade
    call subject('music') from _call_subject_7
    $ gotoscene('mainbuildingrighthallway', transition=fade)

label music_minigame:
    $ lesson = classes['music'].lesson
    Developer "{i}Minigame coming soon!{/i}"
    return True

## Lesson failed
label music_failintro:
    show dewey desk with dissolve
    Dewey "I can see the hunger in your eyes - this song will not break you!"
    Dewey "Let's rock!"
    return

label music_failoutro:
    Dewey "No, dude, that was way out of tune."
    Dewey "We'll try it again next time, yeah?"
    return

## Lesson 1
label music_lesson1intro:
    show dewey desk with dissolve
    Dewey "Hello, class! Welcome!"
    Dewey "My name is Mr. Schneebley."
    Dewey "That's S-C-H-N-E-E... Um, another E... No, um..."
    Dewey "You know what? Just call me Mr. S."
    $ Dewey.met = True
    Dewey "So, every year there is a contest to determine the best band in town."
    Dewey "And this year I decided to form my own band!"
    Dewey "And guess what? You're the ones who are going to help me."
    Dewey "Do any of you ever play the electric guitar?"
    Unk "I tried once, but my dad said it was a waste of time."
    Dewey "A waste of...!"
    Dewey "Your dad is a douche. Anyone else?"
    Jimmy "I used to play before moving away from my home town."
    Dewey "Oh, great! Come here, pal!"
    Dewey "Dr. Stapleneck talked to me about you. You're the new guy, right?"
    Dewey "Alright, grab this... And I guess you know what a guitar pick is."
    Dewey "Pluck along with me, if you can."
    return

label music_lesson1outro:
    Dewey "Yes! That's perfect, you're perfect!"
    # TODO: Better Battle of the Bands intro
    # Dewey "Okay, people! I think you're special, and our school project this year is going to be winning the BATTLE OF THE BANDS!"
    # Dewey "See you next week! I'm going to choose your roles!"
    Dewey "Keep it up, [player_name]! Get a guitar when you can, so you can practice."
    Dewey "See ya!"
    return

## Lesson 2
label music_lesson2intro:
    return

label music_lesson2outro:
    return
