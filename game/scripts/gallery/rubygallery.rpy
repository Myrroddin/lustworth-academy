screen rubygallery():
    tag menu
    ## Esto asegura que cualquier otra pantalla de menu es remplazada.
    window:
        style "mm_root"

    imagemap:
        idle "images/misc/gallery/rubybackground.webp"
        hover "images/misc/gallery/gallerybackgroundhover.webp"

        # This is so that everything transparent is invisible to the cursor.
        alpha False

        hotspot (1611, 144, 63, 63)  action [SetVariable("rubygallery", False), ShowMenu('gallery')]

        imagebutton:
            if Ruby.met == True:
                xalign 0.122
                yalign 0.26
                idle ('images/misc/gallery/scenesbuttons/ruby/superherobutton.webp')
                hover ('images/misc/gallery/scenesbuttons/ruby/superherobuttonhover.webp')
                action Call('ruby_jacuzzisex_scene')
            else:
                xalign 0.122
                yalign 0.26
                idle ('images/misc/gallery/girlbuttons/lockedbutton.webp')
