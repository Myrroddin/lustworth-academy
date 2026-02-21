screen blairgallery():
    tag menu
    ## Esto asegura que cualquier otra pantalla de menu es remplazada.
    window:
        style "mm_root"

    imagemap:
        idle "images/misc/gallery/blairbackground.webp"
        hover "images/misc/gallery/gallerybackgroundhover.webp"

        # This is so that everything transparent is invisible to the cursor.
        alpha False

        hotspot (1611, 144, 63, 63)  action [SetVariable("blairgallery", False), ShowMenu('gallery')]

        imagebutton:
            if quests.blairUSB == COMPLETE:
                xalign 0.122
                yalign 0.26
                idle ('images/misc/gallery/scenesbuttons/blair/opheliamp4button.webp')
                hover ('images/misc/gallery/scenesbuttons/blair/opheliamp4buttonhover.webp')
                action Call('blair_opheliascissoring_scene')
            else:
                xalign 0.122
                yalign 0.26
                idle ('images/misc/gallery/girlbuttons/lockedbutton.webp')

        imagebutton:
            if quests.drunkblair == COMPLETE:
                xalign 0.215
                yalign 0.26
                idle ('images/misc/gallery/scenesbuttons/blair/drunkblairbutton.webp')
                hover ('images/misc/gallery/scenesbuttons/blair/drunkblairbuttonhover.webp')
                action Call('blair_drunknight_scene')
            else:
                xalign 0.215
                yalign 0.26
                idle ('images/misc/gallery/girlbuttons/lockedbutton.webp')
