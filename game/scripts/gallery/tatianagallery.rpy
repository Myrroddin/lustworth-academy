screen tatianagallery():
    tag menu
    ## Esto asegura que cualquier otra pantalla de menu es remplazada.
    window:
        style "mm_root"

    imagemap:
        idle "images/misc/gallery/tatianabackground.webp"
        hover "images/misc/gallery/gallerybackgroundhover.webp"

        # This is so that everything transparent is invisible to the cursor.
        alpha False

        hotspot (1611, 144, 63, 63)  action [SetVariable("tatianagallery", False), ShowMenu('gallery')]

        imagebutton:
            if Tatiana.met == True:
                xalign 0.122
                yalign 0.26
                idle ('images/misc/gallery/scenesbuttons/tatiana/piratewannabebutton.webp')
                hover ('images/misc/gallery/scenesbuttons/tatiana/piratewannabebuttonhover.webp')
                action Call('tatiana_jacuzzisex_scene')
            else:
                xalign 0.122
                yalign 0.26
                idle ('images/misc/gallery/girlbuttons/lockedbutton.webp')
