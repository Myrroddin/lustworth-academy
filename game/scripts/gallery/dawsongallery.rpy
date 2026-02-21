screen dawsongallery():
    tag menu
    ## Esto asegura que cualquier otra pantalla de menu es remplazada.
    window:
        style "mm_root"

    imagemap:
        idle "images/misc/gallery/dawsonbackground.webp"
        hover "images/misc/gallery/gallerybackgroundhover.webp"

        # This is so that everything transparent is invisible to the cursor.
        alpha False

        hotspot (1611, 144, 63, 63)  action [SetVariable("dawsongallery", False), ShowMenu('gallery')]

        imagebutton:
            if quests.missdawsonAssistant == ACTIVE:
                xalign 0.122
                yalign 0.26
                idle ('images/misc/gallery/scenesbuttons/dawson/dawsontitbutton.webp')
                hover ('images/misc/gallery/scenesbuttons/dawson/dawsontitbuttonhover.webp')
                action Call('missdawson_underdeskhandjob_scene')
            elif quests.missdawsonAssistant == SATISFIED:
                xalign 0.122
                yalign 0.26
                idle ('images/misc/gallery/scenesbuttons/dawson/dawsontitbutton.webp')
                hover ('images/misc/gallery/scenesbuttons/dawson/dawsontitbuttonhover.webp')
                action Call('missdawson_underdeskhandjob_scene')
            elif quests.missdawsonAssistant == COMPLETE:
                xalign 0.122
                yalign 0.26
                idle ('images/misc/gallery/scenesbuttons/dawson/dawsontitbutton.webp')
                hover ('images/misc/gallery/scenesbuttons/dawson/dawsontitbuttonhover.webp')
                action Call('missdawson_underdeskhandjob_scene')
            else:
                xalign 0.122
                yalign 0.26
                idle ('images/misc/gallery/girlbuttons/lockedbutton.webp')

        imagebutton:
            if quests.missdawsonTitShow == COMPLETE:
                xalign 0.215
                yalign 0.26
                idle ('images/misc/gallery/scenesbuttons/dawson/dawsontit02button.webp')
                hover ('images/misc/gallery/scenesbuttons/dawson/dawsontit02buttonhover.webp')
                action Call('missdawson_titgrope_scene')
            else:
                xalign 0.215
                yalign 0.26
                idle ('images/misc/gallery/girlbuttons/lockedbutton.webp')

        imagebutton:
            if quests.missdawsonAssistant == COMPLETE:
                xalign 0.31
                yalign 0.26
                idle ('images/misc/gallery/scenesbuttons/dawson/underdeskbutton.webp')
                hover ('images/misc/gallery/scenesbuttons/dawson/underdeskbuttonhover.webp')
                action Call('missdawson_oralunderdesk_scene')
            else:
                xalign 0.31
                yalign 0.26
                idle ('images/misc/gallery/girlbuttons/lockedbutton.webp')

        imagebutton:
            if quests.missdawsonAssistant == COMPLETE:
                xalign 0.40
                yalign 0.26
                idle ('images/misc/gallery/scenesbuttons/dawson/deepthroatbutton.webp')
                hover ('images/misc/gallery/scenesbuttons/dawson/deepthroatbuttonhover.webp')
                action Call('missdawson_deepthroat_scene')
            else:
                xalign 0.40
                yalign 0.26
                idle ('images/misc/gallery/girlbuttons/lockedbutton.webp')

        imagebutton:
            if quests.missdawsonHalloweenStaff == COMPLETE:
                xalign 0.49
                yalign 0.26
                idle ('images/misc/gallery/scenesbuttons/dawson/halloweenfuckdawsonbutton.webp')
                hover ('images/misc/gallery/scenesbuttons/dawson/halloweenfuckdawsonhover.webp')
                action Call('missdawson_fucking_scene')
            else:
                xalign 0.49
                yalign 0.26
                idle ('images/misc/gallery/girlbuttons/lockedbutton.webp')
