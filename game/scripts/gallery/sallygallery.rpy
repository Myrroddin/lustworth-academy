screen sallygallery():
    tag menu
    ## Esto asegura que cualquier otra pantalla de menu es remplazada.
    window:
        style "mm_root"

    imagemap:
        idle "images/misc/gallery/sallybackground.webp"
        hover "images/misc/gallery/gallerybackgroundhover.webp"

        # This is so that everything transparent is invisible to the cursor.
        alpha False

        hotspot (1611, 144, 63, 63)  action [SetVariable("sallygallery", False), ShowMenu('gallery')]

        imagebutton:
            if prologue.barbaraSallyStrapon == True:
                xalign 0.122
                yalign 0.26
                idle ('images/misc/gallery/scenesbuttons/sally/cucumberbutton.webp')
                hover ('images/misc/gallery/scenesbuttons/sally/cucumberbuttonhover.webp')
                action Call('sally_cucumberstrapon_scene')
            else:
                xalign 0.122
                yalign 0.26
                idle ('images/misc/gallery/girlbuttons/lockedbutton.webp')
