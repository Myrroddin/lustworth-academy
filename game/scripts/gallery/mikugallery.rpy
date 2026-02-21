screen mikugallery():
    tag menu
    ## Esto asegura que cualquier otra pantalla de menu es remplazada.
    window:
        style "mm_root"

    imagemap:
        idle "images/misc/gallery/mikubackground.webp"
        hover "images/misc/gallery/gallerybackgroundhover.webp"

        # This is so that everything transparent is invisible to the cursor.
        alpha False

        hotspot (1611, 144, 63, 63)  action [SetVariable("mikugallery", False), ShowMenu('gallery')]

        imagebutton:
            if quests.mikuPhotoShoot == COMPLETE:
                xalign 0.310
                yalign 0.26
                idle ('images/misc/gallery/scenesbuttons/miku/archivebjbutton.webp')
                hover ('images/misc/gallery/scenesbuttons/miku/archivebjbuttonhover.webp')
                action Call('miku_photoshootblowjob_scene')
            else:
                xalign 0.310
                yalign 0.26
                idle ('images/misc/gallery/girlbuttons/lockedbutton.webp')

        imagebutton:
            if quests.mikuJacuzzi == COMPLETE:
                xalign 0.400
                yalign 0.26
                idle ('images/misc/gallery/scenesbuttons/miku/pottersexbutton.webp')
                hover ('images/misc/gallery/scenesbuttons/miku/pottersexbuttonhover.webp')
                action Call('miku_halloweensex_scene')
            else:
                xalign 0.400
                yalign 0.26
                idle ('images/misc/gallery/girlbuttons/lockedbutton.webp')

        imagebutton:
            if quests.artProject == COMPLETE:
                xalign 0.215
                yalign 0.26
                idle ('images/misc/gallery/scenesbuttons/miku/privmastbutton.webp')
                hover ('images/misc/gallery/scenesbuttons/miku/privmastbuttonhover.webp')
                action Call('miku_privatemasturbation_scene')
            else:
                xalign 0.215
                yalign 0.26
                idle ('images/misc/gallery/girlbuttons/lockedbutton.webp')
        
        imagebutton:
            if mikutitshake01 == True:
                xalign 0.122
                yalign 0.26
                idle ('images/misc/gallery/scenesbuttons/miku/titshakebutton.webp')
                hover ('images/misc/gallery/scenesbuttons/miku/titshakebuttonhover.webp')
                action Call('miku_titshake_scene')
            else:
                xalign 0.122
                yalign 0.26
                idle ('images/misc/gallery/girlbuttons/lockedbutton.webp')
