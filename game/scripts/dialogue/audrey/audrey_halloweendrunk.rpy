default audreyhalloweendrunkscene = False

label audreyhalloweendrunk:
    scene laterthatday with fade
    pause 1.0
    play music MUSIC_FUNNY_MOMENT
    scene conciergestorageroom with fade
    play sound "audio/sfx/dooropen01.ogg"
    show audrey halloween drinking with dissolve
    Audrey "Oh, yes! Thizz is what I coll a parrty!"
    Audrey "Come on, let'zz drank!"
    Jimmy "Miss, I think you should leave that and get some sleep."
    Jimmy "You're still in the academy building."
    Audrey "Oh, cam on, don't be a puzz..."
    play sound "audio/sfx/giggle02.ogg"
    Audrey "I knooow why you brought me heere..."
    Audrey "I wazz a sstudent like yu, you know?"
    Audrey "Oh, the paaartiezz, they were waaailddd..."
    Audrey "When everyone wazz drunk as foock..."
    Audrey "Wee fuckeed! Yes, we fuckeed in the bedzz, in the closeeet, in the junkyaaard!"
    play sound "audio/sfx/girlsigh01.ogg"
    Audrey drunk "Ummm, yezzz, I'm getting wet just ssinking about it..."
    Audrey "What are you dating for... Take thozze pantz off!"
    play music MUSIC_SEXY_THEME
    scene audreyhalloweendrunk01 with vpunch
    play sound "audio/sfx/mh1.ogg"
    Audrey "Holy cow! That's a really nizze tool you have heere..."
    Audrey "Izz almost as hard as my favorit wreeeench..."
    Audrey "Yezzz, I want to fuck so baaad..."
    scene audreyhalloweendrunk02 with fade
    play sound "audio/sfx/mh1.ogg"
    Audrey "Goddamn I'm sooo fuckinnn wet..."
    Audrey "Come here, duster... Put that thang inside me!"
    Jimmy "If that's what you want... Let me close the door first."
    scene fewmomentslater with fade
    play sound "audio/sfx/doorclose02.ogg"
    Jimmy "Alright, let's do this."
    play sound SOUND_RECORD_SCRATCH
    scene audreyhalloweendrunk03 with fade
    play music MUSIC_FUNNY_MOMENT
    Jimmy "Ah, come on..."
    play sound "audio/sfx/snoring01.ogg"
    Jimmy "She sure sounds like a truck."
    Audrey "Mhmmmgsss msgsssmgsss..."
    Jimmy "I don't have time for this..."
    Jimmy "Miss Dawson is waiting for me."
    play sound "audio/sfx/doorclose01.ogg"
    $ audreyhalloweendrunkscene = True
    stop music
    $ gotoscene('cafeteriahalloween')
