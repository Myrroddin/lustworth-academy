default quests.euniceBoobytrap = LOCKED

label euniceboobytrap:
    hide screen freeroamhud
    $ showscene('schoolgymstorageroom', transition=fade)
    play sound "audio/sfx/doorclose01.ogg"
    __("{i}[player_name] entered the storage room expecting to meet Eunice as she requested.{/i}")
    __("{i}However, there was someone else in there...{/i}")
    Jimmy "Miku?"
    show miku uniform sit with dissolve
    play sound "audio/sfx/hey01.ogg"
    play music MUSIC_MIKUS_THEME
    Miku "Hey, [player_name]..."
    Miku "Expecting someone else?"
    Jimmy "Mhmm..."
    play sound "audio/sfx/frustratedhum.ogg"
    Miku "How dare you?"
    Jimmy "..."
    Miku "I know you're trying to get to Eunice."
    play sound "audio/sfx/femaleclearthroat.ogg"
    Miku "After everything we've been through..."
    Miku "You want to mess with my best friend?"
    Jimmy "Uhh..."
    play sound "audio/sfx/stopmusiceffect.ogg"
    stop music
    $ renpy.pause()
    show miku uniform happy with vpunch
    play sound "audio/sfx/laugh01.ogg"
    play music "audio/music/crazymoment01.ogg"
    Miku happy "HAHAHAHAHAHAHA! You should have seen the look on your face!"
    Miku "I have never seen a man feeling so guilty!"
    Jimmy "..."
    Miku "Oh, my god. I'm so sorry, [player_name]."
    Miku "Come on, I told you I didn't wanted to our relationship to be so serious."
    Jimmy "Ah, ha, ha, yeah, right."
    Miku "I'm just messing with you."
    Miku "Look, my best friend likes you, a lot."
    Miku "I know you have been good to her, and since she met you her humor has improved so much."
    Miku "But, she's very shy, you know? And sensitive..."
    play sound "audio/sfx/laugh03.ogg"
    Miku seductive "She asked for my help, because being my best friend, she obviously knows about what we did in Halloween."
    Miku "Uhh, my mouth is watering thinking about it..."
    Miku "So, I just wanted to ask you to please be gentle with her."
    Miku "She has never even touched a man before."
    Miku "Can you do that for me?"
    Jimmy "Wow, I... You too are really close, huh?"
    Miku "Yes, we are, handsome. And if you are smart enough, some things can happen between us... three, I mean."
    Jimmy "Uhh, I like the sound of that."
    Miku "I'm sure you do..."
    Miku "I'm gonna look for her, alright? I'll watch the door until you two are finished."
    play sound "audio/sfx/dooropen01.ogg"
    Miku "Wait here..."
    stop music
    play sound "audio/sfx/fewmomentslater.ogg"
    scene fewmomentslater with fade
    $ renpy.pause()
    $ showscene('schoolgymstorageroom', transition=fade)
    show eunice uniform neutral with dissolve
    play music MUSIC_EUNICES_THEME
    Eunice blushed "..."
    Jimmy "Hey..."
    play sound "audio/sfx/hey02.ogg"
    Eunice "Hey, [player_name]."
    Eunice "I'm sorry, I'm very nervous."
    Jimmy "Don't worry, I understand."
    play sound "audio/sfx/hum01.ogg"
    Eunice seductive "So... Um... Can you sit over there on that mat?"
    Jimmy "Sure."
    __("{i}[player_name] did what she requested. With a timid look in her eyes, Eunice started taking her clothes off...{/i}")
    call eunice_gymtitjob_scene from _call_eunice_gymtitjob_scene_1
    $ quests.euniceBoobytrap = COMPLETE
    $ Eunice.relPoints += 1
    call nexttime from _call_nexttime_10
    $ gotoscene('schoolgym', transition=fade)
