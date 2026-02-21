screen jilliangallery():
    tag menu
    ## Esto asegura que cualquier otra pantalla de menu es remplazada.
    window:
        style "mm_root"

    imagemap:
        idle "images/misc/gallery/jillianbackground.webp"
        hover "images/misc/gallery/gallerybackgroundhover.webp"

        # This is so that everything transparent is invisible to the cursor.
        alpha False

        hotspot (1611, 144, 63, 63)  action [SetVariable("jilliangallery", False), ShowMenu('gallery')]

        imagebutton:
            if quests.grantHoboBag == SATISFIED:
                xalign 0.122
                yalign 0.26
                idle ('images/misc/gallery/scenesbuttons/jill/wetdutybutton.webp')
                hover ('images/misc/gallery/scenesbuttons/jill/wetdutybuttonhover.webp')
                action Call('jill_officemasturbation_scene')
            elif quests.grantHoboBag == COMPLETE:
                xalign 0.122
                yalign 0.26
                idle ('images/misc/gallery/scenesbuttons/jill/wetdutybutton.webp')
                hover ('images/misc/gallery/scenesbuttons/jill/wetdutybuttonhover.webp')
                action Call('jill_officemasturbation_scene')
            else:
                xalign 0.122
                yalign 0.26
                idle ('images/misc/gallery/girlbuttons/lockedbutton.webp')
