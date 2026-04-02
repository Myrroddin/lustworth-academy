label sally_lakemeeting_scene:
    play sound SOUND_SEXY_INTRO
    scene sallylakeanim with fade
    "{i}She was moving through the water with no splashing, no shivering—just pure redneck poise.{/i}" 
    "{i}The sunlight hit the water droplets on her skin, and for a second, [player_name] forgot why he was holding a rotten apple."
    Jimmy "Damn..."
    jump .loop
    
label .loop:
    menu:
        "Again?":
            scene sallylakeanim with dissolve
            $ renpy.pause()
            jump .loop
        "Continue":
            jump .end
    
label .end:
    "{i}[player_name] stepped on a dry branch and the snap echoed across the water like a gunshot.{/i}"
    play sound "audio/sfx/gasp01.mp3"
    scene sallylakescene02 with vpunch
    "{i}Sally didn't scream. She didn't even cover up.{/i}"
    play sound "audio/sfx/frustratedhum.mp3"
    Sally "Enjoyin' the view, huh?"
    "{i}She gracefully turned to him, and started walking toward the shore with a smirk that could melt lead.{/i}"
    scene ranchlakeshoreday with fade
    show sally topless neutral with dissolve
    play sound "audio/sfx/femaleclearthroat.mp3"
    Sally "I bet a city boy like you could catch a cold round' here."
    Sally "Mama always says men are like basic livestock—give 'em a fence and they'll spend all day lookin' for a hole to peek through."
    Sally "I figured you were a bit more original, but I guess you're just another steer in the herd."
    Jimmy "Well, I was just... getting some apples."
    Sally laugh "Apples? So, I have to believe you like the rotten ones."
    Sally "'I was just lookin' for apples, Miss Sally, I swear!'"
    play sound "audio/sfx/laugh04.mp3"
    Sally "Ha, ha, ha, ha, lame."
    Jimmy "I won't deny I looked at you." 
    Jimmy "And I liked what I saw, Sally."
    Jimmy "But don't go lumping me in with every other local yokel who whistles at you from a tractor."
    play sound "audio/sfx/hum01.mp3"
    Sally topless neutral "Oh? Is that so? A 'special' breed of city dog, are ya?"
    "{i}She stepped closer, the smell of lake water and soap drowning out the stench of the rotten apples for a brief, dangerous second.{/i}"
    Sally "You want to prove you're not just lookin' for a trophy to hang on your wall?"
    Sally "You're gonna have to do a lot better than 'getting some apples.'"
    Jimmy "..."
    play sound "audio/sfx/femaleclearthroat.mp3"
    Sally teasing "..."
    "{i}She turned her back making sure [player_name] got a full, final look at her."
    Sally "Don't take too long with those apples..."
    "{i}[player_name] stood there for a minute feeling like he just survived falling from a horse.{/i}"
    Jimmy "Great. Now I'm horny, I smell like shit, and I still have to deliver this to Alice."
    return

image sallylakeanim:
    "sallylakeanim01"
    pause 0.22
    "sallylakeanim02"
    pause 0.21
    "sallylakeanim03"
    pause 0.2
    "sallylakeanim04"
    pause 0.19
    "sallylakeanim05"
    pause 0.18
    "sallylakeanim06"
    pause 0.17
    "sallylakeanim07"
    pause 0.16
    "sallylakeanim08"
    pause 0.15
    "sallylakeanim09"
    pause 0.16
    "sallylakeanim10"
    pause 0.17
    "sallylakeanim11"
    pause 0.18
    "sallylakeanim12"
    pause 0.2
    "sallylakeanim13"
    pause 0.2