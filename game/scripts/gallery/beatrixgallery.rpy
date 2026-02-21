screen beatrixgallery():
    tag menu
    ## Esto asegura que cualquier otra pantalla de menu es remplazada.
    window:
        style "mm_root"

    imagemap:
        idle "images/misc/gallery/beatrixbackground.webp"
        hover "images/misc/gallery/gallerybackgroundhover.webp"

        # This is so that everything transparent is invisible to the cursor.
        alpha False

        hotspot (1611, 144, 63, 63)  action [SetVariable("beatrixgallery", False), ShowMenu('gallery')]

        imagebutton:
            if quests.beatrixDiary == COMPLETE:
                xalign 0.122
                yalign 0.26
                idle ('images/misc/gallery/scenesbuttons/beatrix/lapdancebutton.webp')
                hover ('images/misc/gallery/scenesbuttons/beatrix/lapdancebuttonhover.webp')
                action Call('beatrix_lapdance_scene')
            else:
                xalign 0.122
                yalign 0.26
                idle ('images/misc/gallery/girlbuttons/lockedbutton.webp')

        imagebutton:
            if quests.beatrixHalloweenGrinding == COMPLETE:
                xalign 0.215
                yalign 0.26
                idle ('images/misc/gallery/scenesbuttons/beatrix/applepiebutton.webp')
                hover ('images/misc/gallery/scenesbuttons/beatrix/applepiebuttonhover.webp')
                action Call('beatrix_halloweengrinding_scene')
            else:
                xalign 0.215
                yalign 0.26
                idle ('images/misc/gallery/girlbuttons/lockedbutton.webp')

        imagebutton:
            if quests.beatrixHomework == COMPLETE:
                xalign 0.31
                yalign 0.26
                idle ('images/misc/gallery/scenesbuttons/beatrix/studyfeetjobbutton.webp')
                hover ('images/misc/gallery/scenesbuttons/beatrix/studyfeetjobbuttonhover.webp')
                action Call('beatrix_beatrixfootjob_scene')
            else:
                xalign 0.31
                yalign 0.26
                idle ('images/misc/gallery/girlbuttons/lockedbutton.webp')

        imagebutton:
            if quests.beatrixHerpes == COMPLETE:
                xalign 0.40
                yalign 0.26
                idle ('images/misc/gallery/scenesbuttons/beatrix/studyblowjobbutton.webp')
                hover ('images/misc/gallery/scenesbuttons/beatrix/studyblowjobbuttonhover.webp')
                action Call('beatrix_beatrixblowjob_scene')
            else:
                xalign 0.40
                yalign 0.26
                idle ('images/misc/gallery/girlbuttons/lockedbutton.webp')
