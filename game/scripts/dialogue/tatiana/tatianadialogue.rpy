label tatianadialogue:
    hide screen freeroamhud with None
    # stop music
    # show jimmy neutral
    # show tatiana neutral
    # with dissolve
    # jump .dialogmenu

# label .dialogmenu:
#     menu:
#         "Nevermind.":
#             pass
#     $ gotoscene('mainbuildingentrance')

label tatianaintro:
    stop music
    hide screen freeroamhud with None
    __("The junkyard looked like a graveyard of forgotten things—rusted lockers, splintered desks and cracked chalkboards.")
    __("[player_name] felt his feet crunching over broken bits of glass and discarded papers.")
    Jimmy "Hmm, where can I find spray paint in this mess?"
    play sound "audio/sfx/drumpractice.ogg"
    Jimmy "What's that?"
    __("[player_name] tilted his head. The beat is way too cool to ignore.")
    __("Driven by curiosity, he navigated through the junkyard maze, each step bringing him closer to the source of the music.")
    scene tatianadrumsintro with fade
    stop sound
    play music MUSIC_TATIANA_THEME
    __("There she was, a girl gripping a pair of worn drumsticks in her hands.")
    __("Around her there was an improvised drum set—a collection of dented buckets, rusted pans, and even a large pipe turned on its side.")
    Jimmy "Whoa... That was really good."  
    __("She glances at him, eyes wide with surprise.")
    play sound "audio/sfx/hey01.ogg"
    Tatiana "Oh! Uh... Thanks."  
    Jimmy "Do you have a band or something?"
    Tatiana "Not really, I only do this to release estress."
    Tatiana "I gotta come here, because the drum-sets in music class are only available during lessons."  
    Jimmy "Still, this level of improvisation it's pretty awesome."
    __("She looked down at her setup, as if just realizing how ridiculous it was.")
    Tatiana"It works, I guess."
    Jimmy "I like playing the guitar! Well... kinda. I'm still a beginner."
    play sound "audio/sfx/giggle01.ogg"
    Tatiana "That's cool. Maybe one day we could jam?"  
    Jimmy "Yeah! That'd be awesome."
    Jimmy "The name is [player_name], by the way."
    Tatiana "Tatiana, nice to meet you."
    Tatiana "So, what are you doing here?"
    Jimmy "Oh, I was looking for spray paint, at least one that still has some paint in it."
    Jimmy "I heard the greasers love painting graffitis everywhere."
    Tatiana "We like doing that, yeah."
    Jimmy "Oh..."
    play sound "audio/sfx/femaleclearthroat.ogg"
    Tatiana "Well, I don't like being called that way, but if Vincent is my brother, well... I guess I'm one of them."
    Jimmy "Well, I haven't had the pleasure of meeting Vincent yet."
    Tatiana "Uh, you're so lucky, then."
    Tatiana "One advice, don't get caught talking to his sister."
    Jimmy "Well, we are going to have to keep this a secret, then."
    Tatiana "Sure, that sounds fun."
    Tatiana "You can find one near those broken lockers over there."
    Jimmy "Thanks, Tatiana."
    Jimmy "Don't stop playing, alright? You're really good."
    Tatiana "Thanks, don't be a stranger, new guy."
    Jimmy "I won't."
    $ showscene('schoolgroundsjunkyard', transition=fade)
    __("As [player_name] left, Tatiana started playing again even cooler music.")
    call item_pickup(ItemSprayCan) from _call_item_pickup_16
    Jimmy "Here it is... Orange, it should work."
    $ quests.garyHalloweenHeist = SATISFIED
    Jimmy "Alright, I got the spray can."
    if quests.missdawsonHalloweenStaff == COMPLETE:
        show halloweenheistplansinvitation with dissolve
        Jimmy "Now, I have the invitation..."
        show halloweenheistplans06 with dissolve
        Jimmy "I got the spray paint, now I need a costume."
    else:
        show halloweenheistplans04 with dissolve
        Jimmy "Let's see what's left..."
        play sound "audio/sfx/signature02.ogg"
        show halloweenheistplans05 with dissolve
        Jimmy "I got the spray paint, now I need to get an invitation."
        Jimmy "Pete mentioned something about Miss Dawson's office."
    stop music
    if newcontentskipactive == True:
        scene nightsky with fade
        "Several days later..."
        call newcontentvariablecheck02 from _call_newcontentvariablecheck02
        $ showscene('boysdormhallway', transition=fade)
        Jimmy "So, where was I?"
        Jimmy "Right, I got everything ready for the Halloween event..."
        $ Jimmy.outfit = JIMMY_SHAGGY
        jump skip_to_halloween
    $ gotoscene('schoolgroundsjunkyard')
    return


label tatianahalloweendialogue:
    hide screen freeroamhud with None
    $ Tatiana.eventMet[HALLOWEEN_EVENT] = True
    jump halloween_tatianacostumecontest
