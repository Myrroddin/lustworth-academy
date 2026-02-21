screen eunicegallery():
    tag menu
    ## Esto asegura que cualquier otra pantalla de menu es remplazada.
    window:
        style "mm_root"

    imagemap:
        idle "images/misc/gallery/eunicebackground.webp"
        hover "images/misc/gallery/gallerybackgroundhover.webp"

        # This is so that everything transparent is invisible to the cursor.
        alpha False

        hotspot (1611, 144, 63, 63)  action [SetVariable("eunicegallery", False), ShowMenu('gallery')]

        imagebutton:
            if quests.euniceBreastSize == COMPLETE:
                xalign 0.122
                yalign 0.26
                idle ('images/misc/gallery/scenesbuttons/eunice/chocolatesbutton.webp')
                hover ('images/misc/gallery/scenesbuttons/eunice/chocolatesbuttonhover.webp')
                action Call('eunice_gymtitjob_scene')
            else:
                xalign 0.122
                yalign 0.26
                idle ('images/misc/gallery/girlbuttons/lockedbutton.webp')

        imagebutton:
            if quests.euniceSexDate == COMPLETE:
                xalign 0.215
                yalign 0.26
                idle ('images/misc/gallery/scenesbuttons/eunice/biggerbetterbutton.webp')
                hover ('images/misc/gallery/scenesbuttons/eunice/biggerbetterbuttonhover.webp')
                action Call('eunice_gymsex_scene')
            else:
                xalign 0.215
                yalign 0.26
                idle ('images/misc/gallery/girlbuttons/lockedbutton.webp')
