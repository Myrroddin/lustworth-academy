label cassidy_titsout_scene:
    scene cassidytopoff with fade
    Jimmy "Wow, what are you doing?"
    play sound "audio/sfx/giggle01.ogg"
    Cassidy "I want you to be honest with me..."
    Cassidy "I think we have enough trust in each other to be sincere."
    play sound "audio/sfx/sexyintro.ogg"
    scene cassidytitsoutanimation with fade
    $ renpy.pause()
    jump titsoutloop

label titsoutloop:
    menu:
        __("Again!"):
            scene cassidytitsoutanimation with dissolve
            $ renpy.pause()
            jump titsoutloop
        __("Move on"):
            Cassidy "Do you think I'm attractive?"
            Cassidy "Do you think I'm more attractive than Christy?"
            Jimmy "Umm, I'm not sure where you're going with this."
            Cassidy "It's just a simple question."
            Cassidy "Am I more attractive than Christy?"
            Jimmy "Well, I... I think your boobs are bigger than hers."
            Jimmy "It makes you look more attractive, if that's what you're asking."
            Cassidy "What about my face?"
            Jimmy "Your face is pretty too."
            Jimmy "This is really weird, Cass."
            Jimmy "I don't think we should be doing this."
            Cassidy "Ah, come on. It's just a conversation between [roommate_male] and [roommate_female]."
            Jimmy "I think you should not compare yourself with Christy."
            Jimmy "But, if it makes you feel better, your body is hotter than hers."
            Cassidy "Thank you, [player_name]."
            return

image cassidytitsoutanimation:
    "cassidytitsoutanim01"
    pause 0.1
    "cassidytitsoutanim02"
    pause 0.1
    "cassidytitsoutanim03"
    pause 0.1
    "cassidytitsoutanim04"
    pause 0.1
    "cassidytitsoutanim05"
    pause 0.1
    "cassidytitsoutanim06"
    pause 0.1
    "cassidytitsoutanim07"
    pause 0.1
    "cassidytitsoutanim08"
    pause 0.1
    "cassidytitsoutanim09"
    pause 0.1
    "cassidytitsoutanim10"
    pause 0.1
    "cassidytitsoutanim11"
    pause 0.1

    
