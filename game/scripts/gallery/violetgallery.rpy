screen violetgallery():
    tag menu
    ## Esto asegura que cualquier otra pantalla de menu es remplazada.
    window:
        style "mm_root"

    imagemap:
        idle "images/misc/gallery/violetbackground.webp"
        hover "images/misc/gallery/gallerybackgroundhover.webp"

        # This is so that everything transparent is invisible to the cursor.
        alpha False

        hotspot (1611, 144, 63, 63)  action [SetVariable("violetgallery", False), ShowMenu('gallery')]

        imagebutton:
            if glob.halloweenEventComplete == True:
                xalign 0.122
                yalign 0.26
                idle ('images/misc/gallery/scenesbuttons/violet/undercoverbutton.webp')
                hover ('images/misc/gallery/scenesbuttons/violet/undercoverbuttonhover.webp')
                action Call('violet_halloweenfingering_scene')
            else:
                xalign 0.122
                yalign 0.26
                idle ('images/misc/gallery/girlbuttons/lockedbutton.webp')
