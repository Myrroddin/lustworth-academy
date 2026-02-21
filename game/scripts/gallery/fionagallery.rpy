screen fionagallery():
    tag menu
    ## Esto asegura que cualquier otra pantalla de menu es remplazada.
    window:
        style "mm_root"

    imagemap:
        idle "images/misc/gallery/fionabackground.webp"
        hover "images/misc/gallery/gallerybackgroundhover.webp"

        # This is so that everything transparent is invisible to the cursor.
        alpha False

        hotspot (1611, 144, 63, 63)  action [SetVariable("fionagallery", False), ShowMenu('gallery')]

        imagebutton:
            if quests.fionaPadlock == COMPLETE:
                xalign 0.122
                yalign 0.26
                idle ('images/misc/gallery/scenesbuttons/fiona/titshowbutton.webp')
                hover ('images/misc/gallery/scenesbuttons/fiona/titshowbuttonhover.webp')
                action Call('fiona_kiosktitflash_scene')
            else:
                xalign 0.122
                yalign 0.26
                idle ('images/misc/gallery/girlbuttons/lockedbutton.webp')

        imagebutton:
            if quests.fionaConfrontDerek == COMPLETE:
                xalign 0.215
                yalign 0.26
                idle ('images/misc/gallery/scenesbuttons/fiona/kioskblowjobbutton.webp')
                hover ('images/misc/gallery/scenesbuttons/fiona/kioskblowjobbuttonhover.webp')
                action Call('fiona_kioskblowjob_scene')
            else:
                xalign 0.215
                yalign 0.26
                idle ('images/misc/gallery/girlbuttons/lockedbutton.webp')

        imagebutton:
            if quests.fionaNightDate == COMPLETE:
                xalign 0.31
                yalign 0.26
                idle ('images/misc/gallery/scenesbuttons/fiona/nightdatebutton.webp')
                hover ('images/misc/gallery/scenesbuttons/fiona/nightdatebuttonhover.webp')
                action Call('fiona_nightdate_scene')
            else:
                xalign 0.31
                yalign 0.26
                idle ('images/misc/gallery/girlbuttons/lockedbutton.webp')

        imagebutton:
            if quests.fionaBartender == COMPLETE:
                xalign 0.40
                yalign 0.26
                idle ('images/misc/gallery/scenesbuttons/fiona/waldobutton.webp')
                hover ('images/misc/gallery/scenesbuttons/fiona/waldobuttonhover.webp')
                action Call('fiona_halloweensex_scene')
            else:
                xalign 0.40
                yalign 0.26
                idle ('images/misc/gallery/girlbuttons/lockedbutton.webp')

        imagebutton:
            if quests.fionaDadTrouble == COMPLETE:
                xalign 0.49
                yalign 0.26
                idle ('images/misc/gallery/scenesbuttons/fiona/dadrevengebutton.webp')
                hover ('images/misc/gallery/scenesbuttons/fiona/dadrevengebuttonhover.webp')
                action Call('fiona_dadrevenge_scene')
            else:
                xalign 0.49
                yalign 0.26
                idle ('images/misc/gallery/girlbuttons/lockedbutton.webp')
