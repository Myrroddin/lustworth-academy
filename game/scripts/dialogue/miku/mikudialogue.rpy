#VARIABLES
default quests.mikuPhotoShoot = LOCKED
default quests.mikuJacuzzi = LOCKED
default quests.mikuTitshake = LOCKED
default quests.mikuMasturbation = LOCKED
default quests.artclassBook = LOCKED
default quests.artProject = LOCKED
default quests.mikuStorypartone = LOCKED

#NEXT DAY FLAGS
default miku.nextdayflag01 = False

#LABELS
label mikudialogue:
    hide screen freeroamhud with None
    play music MUSIC_MIKUS_THEME
    # if quests.euniceChocolates != COMPLETE:
    #     jump .busy
    if not Miku.met:
        jump mikuintro
    show miku uniform neutral with dissolve
    Miku "Oh, hi, [player_name]. Do you need something?"
    jump .dialogmenu

label .dialogmenu:
    menu:
        "Ask for the Art Book" if quests.artclassBook == ACTIVE:
            Jimmy "Hey, I'm looking for a book for the art teacher."
            Jimmy "She told me to ask for it here in the library."
            Miku "Oh, yes! Miss Bakshi always sends someone to fetch a book before her class. It's like a ritual of hers."
            Miku "Seems like you were the lucky one, this time. I know exactly what you need."
            Jimmy "Great."
            call item_pickup(ItemArtBook01) from _call_item_pickup_2
            Miku "Take this one. I know exactly what Miss Bakshi likes to read."
            Jimmy "Oh... Okay, thank you."
            Miku "No problem, see you in class!"
            $ quests.artclassBook = SATISFIED
        "Ask about the Art project" if quests.artProject == ACTIVE:
            Jimmy "Hey, Miku. Can you remind me what are we going to do with the Art project?"
            Miku "Sure. We agreed to meet at your house to take some photos."
            Miku happy "I have the perfect suit for our historical character, and you told me there is room in your backyard for what we need."
            Jimmy "Yes, of course. Thank you, see you on the weekend!"
            Miku "Looking forward to it!"
        "Talk about her 'Art Shirt'" if quests.artProject == COMPLETE:
            $ mikutitshakenet = True
            Jimmy "Hey, Miku. I was thinking about that shirt you wear in art class."
            Miku "Yes?"
            Jimmy "Have you found a replacement?"
            Miku "Oh, I was thinking about something I found that might work."
            Miku "Let me put show you!"
            play sound "audio/sfx/undress01.ogg"
            call miku_titshake_scene from _call_miku_titshake_scene
        "Surprise Miku with new camera" if quests.mikuPhotoShoot == SATISFIED:
            Jimmy "Miku! I got something for you."
            $ Jimmy.inventory.remove(ItemPolaroidCamera)
            Miku blushed "Is that..."
            Miku happy "OH MY GOD! A CAMERAAAAAAAAAAA!"
            Miku "[player_name]! You shouldn't have!"
            Miku "Thank you so much!"
            Miku seductive "I want to try it as soon as possible!"
            Miku "Please, come back tomorrow! I will compensate you, I promise!"
            Jimmy "You don't need to make up for it. I just wanted to see you happy."
            Miku "Nonsense! You are so good to me. Meet me in the archive after class, please. You will like it."
            Jimmy "Alright, I'll see you tomorrow, then."
            $ quests.mikuPhotoShoot = COMPLETE
        "Nevermind":
            pass
    $ gotoscene('schoollibraryshelves')

# label .busy:
#     show miku chair with dissolve
#     Miku "Um, do you need something? I'm pretty busy studying for an astronomy exam right now."
#     Jimmy "Oh, sorry to disturb you."
#     $ gotoscene('schoollibrarymainhall')

label mikuhalloweendialogue:
    hide screen freeroamhud with None
    $ Miku.eventMet[HALLOWEEN_EVENT] = True
    show miku wizard neutral
    with dissolve
    play sound "audio/sfx/hey01.ogg"
    Miku "Hey [player_name], having fun at the party?"
    Jimmy "Eh, it's alright."
    Miku "It's really nice to see you."
    menu:
        "How's the party going?":
            Miku "Kind of boring, to be honest."
            Miku "My mom got me the invitation, and I thought I had the perfect costume..."
            Miku "But, this place is as frivolous as it gets."
            Miku "I should have spend the night with the guys, playing Grottos and Gremlins."
            Jimmy "I'm sorry to hear that."
            Jimmy "Can I help?"
            Miku "Well, when I saw you coming up those stairs, it was like seeing Gandalf arriving to Helm's Deep with the Rohirrim."
            Jimmy "Wow, am I that cool?"
            play sound "audio/sfx/laugh01.ogg"
            Miku "Yes, you are! Ha, ha, ha, ha."
            Miku "I think I'm going to go to the roof, lay down and watch the stars."
            Jimmy "Well, let's do it, then."
            Miku "Really? You want to come with me?"
            Jimmy "Of course, watching the stars with Moaning Eagle has to be in my bucket list."
            play sound "audio/sfx/giggle01.ogg"
            Miku "Ha, ha, ha, ha, ha! You silly."
            if quests.halloweenFakeFlag == COMPLETE:
                $ showscene('harrisonhouseroofflag', transition=fade)
                play music MUSIC_MIKUS_THEME
                show miku wizard happy with dissolve
                play sound "audio/sfx/girlsigh01.ogg"
                Miku "I'm so glad you're here with me."
                scene nightsky with fade
                Miku "Look! The moon is full!"
                Miku "Wow, the sky is so pretty at night..."
                Jimmy "You are pretty at night."
                Miku "Ha, ha, ha, come on, that's so cheesy..."
                Miku "I love it."
                scene mikuwizardintro with dissolve
                play sound "audio/sfx/femaleclearthroat.ogg"
                Miku "Can I ask you something?"
                Jimmy "Shoot."
                Miku "Are you my boyfriend?"
                Jimmy "Well, I'm not sure."
                Miku "I mean, we have done stuff that couples do, right?"
                Jimmy "That's  right."
                Miku "Don't get me wrong, I don't want to put any pressure on you."
                Miku "It's just that, I have never had a boyfriend before."
                Jimmy "I can be your boyfriend, if that's what you want."
                Miku "Well, I've read a lot of books where couples have such toxic relationships."
                Miku "I don't want that for us... I want us to be together and do couple things, but don't depend on each other so much."
                Jimmy "Wow, that's a very smart idea."
                play sound "audio/sfx/giggle01.ogg"
                Miku "Thanks, ha, ha. So, boyfriend, do you want to have sex?"
                Jimmy "Oh, yeah, girlfriend, I wanna fuck."
                Miku "I think I know a private place. There are a lot of rooms in this house."
                play sound "audio/sfx/highheels.ogg"
                jump mikuhalloweensex
            else:
                $ showscene('harrisonhouseroof', transition=fade)
                show miku wizard happy with dissolve
                Miku "I'm so glad you're here with me."
                scene nightsky with fade
                Miku "Look! The moon is full!"
                Miku "Wow, the sky is so pretty at night..."
                Jimmy "You are pretty at night."
                Miku "Ha, ha, ha, come on, that's so cheesy..."
                Miku "I love it."
                scene mikuwizardintro with dissolve
                Miku "Can I ask you something?"
                Jimmy "Shoot."
                Miku "Are you my boyfriend?"
                Jimmy "Well, I'm not sure."
                Miku "I mean, we have done stuff that couples do, right?"
                Jimmy "That's  right."
                Miku "Don't get me wrong, I don't want to put any pressure on you."
                Miku "It's just that, I have never had a boyfriend before."
                Jimmy "I can be your boyfriend, if that's what you want."
                Miku "Well, I've read a lot of books where couples have such toxic relationships."
                Miku "I don't want that for us... I want us to be together and do couple things, but don't depend on each other so much."
                Jimmy "Wow, that's a very smart idea."
                Miku "Thanks, ha, ha. So, boyfriend, do you want to have sex?"
                Jimmy "Oh, yeah, girlfriend, I wanna fuck."
                Miku "I think I know a private place. There are a lot of rooms in this house."
                jump mikuhalloweensex

        "Nevermind":
            pass
    $ gotoscene('harrisonhousefloor2')