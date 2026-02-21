screen christygallery():
    tag menu
    ## Esto asegura que cualquier otra pantalla de menu es remplazada.
    window:
        style "mm_root"

    imagemap:
        idle "images/misc/gallery/christybackground.webp"
        hover "images/misc/gallery/gallerybackgroundhover.webp"

        # This is so that everything transparent is invisible to the cursor.
        alpha False

        hotspot (1611, 144, 63, 63)  action [SetVariable("christygallery", False), ShowMenu('gallery')]

        imagebutton:
            if Toord.met == True:
                xalign 0.122
                yalign 0.26
                idle ('images/misc/gallery/scenesbuttons/christy/showerpeek01button.webp')
                hover ('images/misc/gallery/scenesbuttons/christy/showerpeek01buttonhover.webp')
                action Call('christy_gymshower_scene')
            else:
                xalign 0.122
                yalign 0.26
                idle ('images/misc/gallery/girlbuttons/lockedbutton.webp')

        imagebutton:
            if quests.beatrixDiary == SATISFIED:
                xalign 0.215
                yalign 0.26
                idle ('images/misc/gallery/scenesbuttons/christy/bathtubfightbutton.webp')
                hover ('images/misc/gallery/scenesbuttons/christy/bathtubfightbuttonhover.webp')
                action Call('christy_dildofight_scene')
            elif quests.beatrixDiary == COMPLETE:
                xalign 0.215
                yalign 0.26
                idle ('images/misc/gallery/scenesbuttons/christy/bathtubfightbutton.webp')
                hover ('images/misc/gallery/scenesbuttons/christy/bathtubfightbuttonhover.webp')
                action Call('christy_dildofight_scene')
            else:
                xalign 0.215
                yalign 0.26
                idle ('images/misc/gallery/girlbuttons/lockedbutton.webp')

        imagebutton:
            if quests.christyMandyVoltium == COMPLETE:
                xalign 0.31
                yalign 0.26
                idle ('images/misc/gallery/scenesbuttons/christy/poolfun01button.webp')
                hover ('images/misc/gallery/scenesbuttons/christy/poolfun01buttonhover.webp')
                action Call('christy_halloweenpoolsex_scene')
            else:
                xalign 0.31
                yalign 0.26
                idle ('images/misc/gallery/girlbuttons/lockedbutton.webp')
