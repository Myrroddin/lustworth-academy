screen wendygallery():
    tag menu
    ## Esto asegura que cualquier otra pantalla de menu es remplazada.
    window:
        style "mm_root"

    imagemap:
        idle "images/misc/gallery/wendybackground.webp"
        hover "images/misc/gallery/gallerybackgroundhover.webp"

        # This is so that everything transparent is invisible to the cursor.
        alpha False

        hotspot (1611, 144, 63, 63)  action [SetVariable("wendygallery", False), ShowMenu('gallery')]

        imagebutton:
            if quests.goodbyeWendy == COMPLETE:
                xalign 0.40
                yalign 0.26
                idle ('images/misc/gallery/scenesbuttons/wendy/goodbyesexbutton.webp')
                hover ('images/misc/gallery/scenesbuttons/wendy/goodbyesexbuttonhover.webp')
                action Call('wendygoodbyescene')
            else:
                xalign 0.40
                yalign 0.26
                idle ('images/misc/gallery/girlbuttons/lockedbutton.webp')

        imagebutton:
            if Jill.met == True:
                xalign 0.31
                yalign 0.26
                idle ('images/misc/gallery/scenesbuttons/wendy/mansionsexbutton.webp')
                hover ('images/misc/gallery/scenesbuttons/wendy/mansionsexbuttonhover.webp')
                action Call('wendy_roominfiltration_scene')
            else:
                xalign 0.31
                yalign 0.26
                idle ('images/misc/gallery/girlbuttons/lockedbutton.webp')

        imagebutton:
            if prologue.secondNight == True:
                xalign 0.215
                yalign 0.26
                idle ('images/misc/gallery/scenesbuttons/wendy/mysterynight02button.webp')
                hover ('images/misc/gallery/scenesbuttons/wendy/mysterynight02buttonhover.webp')
                action Call('wendy_mysterygirlnight2_scene')
            else:
                xalign 0.215
                yalign 0.26
                idle ('images/misc/gallery/girlbuttons/lockedbutton.webp')

        imagebutton:
            if prologue.firstNight == True:
                xalign 0.122
                yalign 0.26
                idle ('images/misc/gallery/scenesbuttons/wendy/mysterynight01button.webp')
                hover ('images/misc/gallery/scenesbuttons/wendy/mysterynight01buttonhover.webp')
                action Call('wendy_mysterygirlnight1_scene')
            else:
                xalign 0.122
                yalign 0.26
                idle ('images/misc/gallery/girlbuttons/lockedbutton.webp')
