#VARIABLES

label artclass:
    hide screen freeroamhud
    $ inclass = True
    if quests.artclassBook == COMPLETE:
        scene artclassroomfallday with fade
        call subject('art') from _call_subject
        $ gotoscene('mainbuildingrighthallway', transition=fade)
    else:
        jump artbookquest

label artbookquest:
    if quests.artclassBook == LOCKED:
        scene artclassroomfallday with fade
        show aurora jumpsuit crossed with dissolve
        play music MUSIC_AURORA_THEME
        Aurora "Gud morning, sir."
        Aurora "Are you here for art class?"
        Jimmy "Good morning, yes, I am."
        Aurora "You arived early, sweetu."
        Aurora "Can you do me a favor?"
        Jimmy "Sure, Miss."
        Aurora "Go do de library and ask for a book for de art class deacher. They vill know what yur dalkin about."
        Jimmy "Uh, okay, I'll get it."
        "Umm, that's a very particular accent..."
        $ quests.artclassBook = ACTIVE
        $ gotoscene('mainbuildingrighthallway', transition=fade)
    elif quests.artclassBook == SATISFIED:
        scene artclassroomfallday with fade
        show aurora jumpsuit crossed with dissolve
        play music MUSIC_AURORA_THEME
        Aurora "Oh, yur back, sweetu."
        Jimmy "Yes, Miss. I brought the book."
        $ Aurora.relPoints += 1
        $ quests.artclassBook = COMPLETE
        $ Jimmy.inventory.remove(ItemArtBook01)
        Aurora "Oh, dhank you very much, sweetu."
        Aurora "Now I dink we are ready for class."
        Aurora "Please dake a seat."
        jump artclass
    else:
        Jimmy "Gotta get the art book from the library, first."
        $ gotoscene('mainbuildingrighthallway')



label art_minigame:
    hide miku with dissolve
    $ lesson = classes['art'].lesson
    # TODO: add more lessons
    if lesson > 1:
        return True
    call expression ('artclass_lesson' + str(lesson)) from _call_expression_5
    if art1points == 21:
        return True
    else:
        return False

## Lesson failed
label art_failintro:
    show aurora jumpsuit neutral with dissolve
    Aurora "I feel it! Today, you will make a masterpiece."
    Aurora dance "Channel your inner vibes! Create someding beautiful!"
    if quests.artProject == LOCKED:
        hide aurora with dissolve
        show miku artshirt seductive with dissolve
        Miku "Alright, let's try again, buddy."
    return

label art_failoutro:
    stop music
    play sound SOUND_RECORD_SCRATCH
    scene artclassroomfallday with fade
    show aurora jumpsuit crossed with dissolve
    Aurora "I think your vibes were misaligned today, [player_name]."
    Aurora "Sometimes that is simply out of our control."
    Aurora "Perhaps next week, they will be better aligned."
    $ inclass = False
    return

## Lesson 1
label art_lesson1intro:
    hide aurora
    play music MUSIC_CLASSROOMAMBIENCEDAY_THEME
    show miku uniform neutral with vpunch
    Miku "[player_name]! We are in the same class!"
    Jimmy "Oh, that's nice. It's good to see you."
    Miku seductive "You know, I thought about what you said about my photos."
    Miku "And I wanna know what you think about these..."
    hide miku
    show mikupolaroid02 with fade
    Jimmy "Wow, you look pretty in this one."
    play sound "audio/sfx/giggle02.ogg"
    Miku "You think so? I took that one before the one you saw in the library."
    Jimmy "It's quite a transformation."
    Miku "Ha, ha, yeah, you can say that."
    Miku "What about this one?"
    show mikupolaroid03 with dissolve
    hide mikupolaroid02
    Jimmy "That's a sexy suit."
    Miku "Oh, you really think it looks sexy?"
    Jimmy "Oh, yeah, totally."
    Miku "I like to cosplay, it's my favorite hobby. I make them myself."
    Jimmy "You have a real talent for it."
    hide mikupolaroid03
    show miku uniform happy with dissolve
    play sound "audio/sfx/laugh03.ogg"
    Miku "Aww, thank you so much for saying that."
    Miku "It feels good to have someone to share this stuff with."
    play sound "audio/sfx/femaleclearthroat.ogg"
    Aurora "Please, everyone, dake a seat."
    Miku neutral "I almost forgot we were in class. We should pay attention to the teacher."
    hide miku with dissolve
    show aurora jumpsuit neutral with dissolve
    play music MUSIC_AURORA_THEME
    Aurora "Gud morning, boys and gerls!"
    $ Aurora.met = True
    Aurora "My nim is Aurora Bakshi, and I am yur art teacher."
    Aurora "I am going to dry to make yur mind fly to de realm of imagination."
    Aurora "I feel reely good vibes in diz class."
    Aurora dance "My aura is in harmony vith yurs, I'm sure."
    Aurora "My class is going do be a safe place for de veirdness inside all of yu, okay?"
    Aurora "So, embrace de veirdness and see de beauty of all dat is around us vith a new light."
    Aurora crossed "Vee are going to start today wid classic art."
    Aurora "Doze who have seen class vith me in the past, already know you can vear special clothes when yur painting."
    Aurora "Dhat vay you avoid getting yur uniform painted."
    Aurora "Doze who ar new to diz class, you can bring something to vear in de next class."
    Aurora neutral "Let the energy of yur chakra flow truh yur brush and onto dhe canvas!"
    Aurora "Dose who want to form pairs, you can do."
    hide aurora with dissolve
    show miku artshirt neutral with dissolve
    play music MUSIC_ROCKY_THEME
    Miku "[player_name], do you want to pair with me?"
    Jimmy "Wow, what are you wearing?"
    Miku happy "Oh, this is the shirt I've been using for art class for a couple of years, I think."
    Jimmy "Right, it's a bit small, don't you think?"
    Miku seductive "Yeah, it might be time to change it, but Miss Bakshi says that when I use it, my art transforms into something special."
    Miku "So, I'm not ready yet to get rid of it."
    Miku "When I find something that matches the vibe, I will."
    Jimmy "Well, I definetely want to pair with you."
    Miku happy "That's great!"
    return

label art_lesson1outro:
    play music MUSIC_AURORA_THEME
    show aurora jumpsuit dance with dissolve
    Aurora "Wow, [player_name], yur aura is reflecting so much imagination!"
    Aurora neutral "I really think dat yuu will become a great artist."
    stop music
    # show artclassrewards01 with dissolve
    # Developer "{i}Congratulations. If you keep it up, the art class teacher will be happy to show you some abstract art of her own.{/i}"
    if quests.artProject == LOCKED:
        hide aurora with dissolve
        show miku artshirt happy with vpunch
        Miku "Yes! I'm so happy!"
        Miku "I think we are the best artist couple ever!"
        call miku_titshake_scene from _call_miku_titshake_scene_1
        Miku "Thank you, [player_name]."
        $ Miku.relPoints += 1
        Jimmy "Anytime!"
        scene artclassroomfallday with fade
        show aurora jumpsuit crossed with dissolve
        Aurora "For next veek guys, I vant yuu do choose a historic character and draw picdures or dake photos delling a bit of dheir story."
        Aurora "If yuu vant to form pairs, yuu can do."
        hide aurora with dissolve
        show miku artshirt neutral with dissolve
        Jimmy "Miku, do you want to do this with me?"
        Miku "Yes, I would love to!"
        Miku "I have a Polaroid camera, and I have an idea of which character we can choose."
        Miku "I also have the perfect outfit to wear in the pictures."
        Jimmy "Wow, you are doing all the work here."
        Jimmy "Tell you what... I have a good spot in my house, in the backyard."
        Jimmy "There is enough space there to do whatever."
        Miku happy "Sounds great!"
        Jimmy "Here's the address *gives her a small paper*"
        Miku "Alright, I'll see you there this weekend."
        Jimmy "Looking forward to it."
        $ quests.artProject = ACTIVE
        scene artclassroomfallday with dissolve
        show aurora jumpsuit crossed with dissolve
    play sound SOUND_SCHOOL_BELL
    Aurora "Well, dhat's it guys. See yuu next week!"
    $ inclass = False
    return

## Lesson 2
label art_lesson2intro:
    return

label art_lesson2outro:
    return
