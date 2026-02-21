screen cassidygallery():
    tag menu
    ## Esto asegura que cualquier otra pantalla de menu es remplazada.
    window:
        style "mm_root"

    imagemap:
        idle "images/misc/gallery/cassidybackground.webp"
        hover "images/misc/gallery/gallerybackgroundhover.webp"

        # This is so that everything transparent is invisible to the cursor.
        alpha False

        hotspot (1611, 144, 63, 63)  action [SetVariable("cassidygallery", False), ShowMenu('gallery')]

        imagebutton:
            if Cassidy.met == True:
                xalign 0.122
                yalign 0.26
                idle ('images/misc/gallery/scenesbuttons/cassidy/dildo01button.webp')
                hover ('images/misc/gallery/scenesbuttons/cassidy/dildo01buttonhover.webp')
                action Call('cassidy_lockerroomdildo_scene')
            else:
                xalign 0.122
                yalign 0.26
                idle ('images/misc/gallery/girlbuttons/lockedbutton.webp')

        imagebutton:
            if prologue.cassidyPeephole == True:
                xalign 0.215
                yalign 0.26
                idle ('images/misc/gallery/scenesbuttons/cassidy/dildo02button.webp')
                hover ('images/misc/gallery/scenesbuttons/cassidy/dildo02buttonhover.webp')
                action Call('cassidy_townhousepeephole_scene')
            else:
                xalign 0.215
                yalign 0.26
                idle ('images/misc/gallery/girlbuttons/lockedbutton.webp')

        imagebutton:
            if prologue.cassidyShower == True:
                xalign 0.31
                yalign 0.26
                idle ('images/misc/gallery/scenesbuttons/cassidy/dildo03button.webp')
                hover ('images/misc/gallery/scenesbuttons/cassidy/dildo03buttonhover.webp')
                action Call('cassidy_townhouseshower_scene')
            else:
                xalign 0.31
                yalign 0.26
                idle ('images/misc/gallery/girlbuttons/lockedbutton.webp')

        imagebutton:
            if quests.cassidyFirstFuck == ACTIVE:
                xalign 0.40
                yalign 0.26
                idle ('images/misc/gallery/scenesbuttons/cassidy/halloweenbjbutton.webp')
                hover ('images/misc/gallery/scenesbuttons/cassidy/halloweenbjbuttonhover.webp')
                action Call('cassidy_halloweenblowjob_scene')
            elif quests.cassidyFirstFuck == COMPLETE:
                xalign 0.40
                yalign 0.26
                idle ('images/misc/gallery/scenesbuttons/cassidy/halloweenbjbutton.webp')
                hover ('images/misc/gallery/scenesbuttons/cassidy/halloweenbjbuttonhover.webp')
                action Call('cassidy_halloweenblowjob_scene')
            else:
                xalign 0.40
                yalign 0.26
                idle ('images/misc/gallery/girlbuttons/lockedbutton.webp')

        imagebutton:
            if quests.cassidyFirstFuck == COMPLETE:
                xalign 0.49
                yalign 0.26
                idle ('images/misc/gallery/scenesbuttons/cassidy/cowgirlcassbutton.webp')
                hover ('images/misc/gallery/scenesbuttons/cassidy/cowgirlcassbuttonhover.webp')
                action Call('cassidy_cassidycowgirl_scene')
            else:
                xalign 0.49
                yalign 0.26
                idle ('images/misc/gallery/girlbuttons/lockedbutton.webp')
