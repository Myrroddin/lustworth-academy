screen kassandragallery():
    tag menu
    ## Esto asegura que cualquier otra pantalla de menu es remplazada.
    window:
        style "mm_root"

    imagemap:
        idle "images/misc/gallery/kassandrabackground.webp"
        hover "images/misc/gallery/gallerybackgroundhover.webp"

        # This is so that everything transparent is invisible to the cursor.
        alpha False

        hotspot (1611, 144, 63, 63)  action [SetVariable("kassandragallery", False), ShowMenu('gallery')]

        imagebutton:
            if quests.bathtubclimax == COMPLETE:
                xalign 0.122
                yalign 0.26
                idle ('images/misc/gallery/scenesbuttons/kassandra/bathgasmbutton.webp')
                hover ('images/misc/gallery/scenesbuttons/kassandra/bathgasmbuttonhover.webp')
                action Call('kassandra_bathgasm_scene')
            else:
                xalign 0.122
                yalign 0.26
                idle ('images/misc/gallery/girlbuttons/lockedbutton.webp')
