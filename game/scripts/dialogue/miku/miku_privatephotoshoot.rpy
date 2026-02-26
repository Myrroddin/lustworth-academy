label mikuprivatephotoshootscene:
    $ showscene('schoollibraryarchives', transition=fade)
    hide screen freeroamhud
    __("{i}As [player_name] entered the archives section of the library, he was taken by the smell of leather and old parchment.{/i}")
    __("{i}What mysteries were hiding among these timeworn tomes?{/i}")
    __("{i}Perhaps a treasure map, or a magic spell, or a secret plot from the Russians to take over the world using monsters from a dark dimension, or...{/i}")
    __("{i}[player_name] didn't have much time to dwell on those thoughts, however, before Miku showed up.{/i}")
    play music MUSIC_MIKUS_THEME
    show miku bunny seductive with dissolve
    Miku "..."
    Jimmy "You look stunning."
    Miku "Thanks..."
    Miku "I'm sorry, I'm a little ashamed of wearing this in front of someone else."
    Jimmy "We can do this another time, if you feel like it."
    Miku "No! No, I'm okay."
    Miku complacent "I want you to take some photos."
    Jimmy "Alright, let me set up the camera."
    Miku "Do you know how to operate this?"
    Jimmy "I know the basics. And old friend of mine was fond of photography."
    Miku seductive "Wow, you're full of surprises."
    Jimmy "Let's start with something simple, right?"
    scene mikubunnypose01 onlayer cutscene with fade
    Miku "Like this?"
    Jimmy "Umm, yes. That looks really nice."
    Miku "Do you think I'm a good model?"
    Jimmy "Oh, more than good, babe."
    Miku "Uhmm... babe?"
    Jimmy "Sorry, I just..."
    Miku "Don't worry. I... I like it."
    Jimmy "Alright, babe. I got some good photos here. Wanna try a different pose?"
    Miku "Okay."
    scene mikubunnypose02 onlayer cutscene with dissolve
    __("Holy shit. That suit is barely covering her parts.")
    Miku "It's getting hot in here, huh?"
    Jimmy "Oh, yeah. Very hot."
    Miku "I'm starting to sweat, haha."
    Jimmy "Let me take the photo real quick."
    Jimmy "You're really flexible."
    Miku "Oh, yeah. I join my mom when she trains aerobics and yoga."
    Jimmy "Good to know."
    Miku "Here, let me show you a very hard pose."
    scene mikubunnypose03 onlayer cutscene with dissolve
    __("Oh shit, her pussy just popped out of the suit.")
    __("Is she really sweating or is she wet?")
    __("Fuck, that's so hot. I'm getting an erection.")
    Miku "[player_name], are you okay?"
    Jimmy "Umm, yeah. I just... That looks like a painful pose."
    Miku "Well, it's actually really..."
    Miku "Um, [player_name], there's a big bulge in your pants."
    Jimmy "Oh, uh, yeah..."
    Miku "Oh my god, is that...?"
    __("{i}Miku stood up and put on her glasses.{/i}")
    scene onlayer cutscene
    with fade
    Miku "[player_name], you're aroused..."
    Jimmy "Look, you're really really hot, so I just... I can't control that."
    Miku "Can I take a closer look?"
    Jimmy "Oh... Umm, yeah, sure."
    Miku "My mom always talks about men's stuff."
    Miku "You know, trying to educate me..."
    Miku "Do you mind taking your pants off?"
    call miku_photoshootblowjob_scene from _call_miku_photoshootblowjob_scene
    Miku "Thank you for the photos."
    Jimmy "Oh, yeah... The photos..."
    $ quests.mikuStorypartone = COMPLETE
    call nexttime from _call_nexttime_17
    $ gotoscene('schoollibrarymainhall', transition=fade)
