label clairesecretscene:
    hide screen freeroamhud
    play music MUSIC_SEXY_THEME
    $ entry = True
    jump clairesecretscene_menu

label clairesecretscene_menu:
    scene claireintro with fade
    if entry:
        Claire "Hey, I really needed this break."
        Claire "You don't know how messy it gets being around zombies."
        $ entry = False
    menu:
        __("Side fuck"):
            jump clairesecretscene_sidefuck
        __("Anal on bike"):
            jump clairesecretscene_anal
        __("Leave"):
            return

label clairesecretscene_sidefuck:
    Jimmy "Your body is amazing."
    Claire "Mmm, what do you want to do with it?"
    Jimmy "I have an idea."
    scene clairesidefuck1 with fade
    Claire "Oh my god! I feel the tip of your cock pushing hard inside me."
    scene clairesidefuck2
    Claire "Finally I can have a nice fuck."
    Claire "COME ON! YES! Drill that pussy!"
    $ renpy.pause()
    scene clairesidefuckcum with vpunch
    Claire "Wow, I feel so much cum flowing inside me..."
    jump clairesecretscene_menu

label clairesecretscene_anal:
    Jimmy "That bike looks cool."
    Claire "And it's really comfy too..."
    Jimmy "Wanna know what's better than riding that bike?"
    Claire "What are you thinking, you little..."
    scene claireanal1 with fade
    Claire "AHH, fuck! Be careful with my ass."
    scene claireanal2
    Claire "Uff, my hole is stretching so much!"
    Claire "Yes, fuck me in the ass! JUST LIKE THAT!"
    $ renpy.pause()
    scene claireanalcum with vpunch
    Claire "Oh, that was a good ride, baby..."
    jump clairesecretscene_menu

#ANIMATIONS
image claireanal1:
    'claireanal01'
    pause 0.3
    'claireanal02'
    pause 0.3
    'claireanal03'
    pause 0.3
    'claireanal04'
    pause 0.3
    'claireanal05'
    pause 0.3
    'claireanal06'
    pause 0.3
    'claireanal07'
    pause 0.3
    'claireanal08'
    pause 0.3
    'claireanal09'
    pause 0.3
    repeat

image claireanal2:
    'claireanal01'
    pause 0.1
    'claireanal02'
    pause 0.1
    'claireanal03'
    pause 0.1
    'claireanal04'
    pause 0.1
    'claireanal05'
    pause 0.1
    'claireanal06'
    pause 0.1
    'claireanal07'
    pause 0.1
    'claireanal08'
    pause 0.1
    'claireanal09'
    pause 0.1
    repeat

image clairesidefuck1:
    'clairesidefuck01'
    pause 0.3
    'clairesidefuck02'
    pause 0.3
    'clairesidefuck03'
    pause 0.3
    'clairesidefuck04'
    pause 0.3
    'clairesidefuck05'
    pause 0.3
    'clairesidefuck06'
    pause 0.3
    'clairesidefuck07'
    pause 0.3
    'clairesidefuck08'
    pause 0.3
    repeat

image clairesidefuck2:
    'clairesidefuck01'
    pause 0.1
    'clairesidefuck02'
    pause 0.1
    'clairesidefuck03'
    pause 0.1
    'clairesidefuck04'
    pause 0.1
    'clairesidefuck05'
    pause 0.1
    'clairesidefuck06'
    pause 0.1
    'clairesidefuck07'
    pause 0.1
    'clairesidefuck08'
    pause 0.1
    repeat
