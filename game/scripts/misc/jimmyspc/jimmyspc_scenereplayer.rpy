screen jimmyspc_scenereplayer(x, y):
    zorder 100

    $ girl = jimmyspc.sceneReplayerChar

    imagemap:
        pos x, y

        idle 'jimmyspc_window'
        hover 'jimmyspc_windowhover'

        hotspot (0, 0, 808, 808) action NullAction() mouse 'jimmyspc'

        if girl is not None:
            hotspot (640, 24, 56, 56) action SetVariable('jimmyspc.sceneReplayerChar', None) mouse 'jimmyspc'
        else:
            hotspot (640, 24, 56, 56)
        
        if galleryMode:
            hotspot (712, 24, 56, 56) action Jump('jimmyspc_exit') mouse 'jimmyspc'
        else:
            hotspot (712, 24, 56, 56) action SetVariable('jimmyspc.sceneReplayerActive', False) mouse 'jimmyspc'

        hotspot (712, 104, 56, 56) action Function(scrollButtonOnClick, 'scenereplayer', -1) mouse 'jimmyspc'
        hotspot (712, 712, 56, 56) action Function(scrollButtonOnClick, 'scenereplayer', 1) mouse 'jimmyspc'

    $ title = girl.name if girl is not None else "Scene Replayer"
    text title:
        style 'jimmyspc_windowtitle'
        pos x + 40, y + 16

    side 'c r':
        area (x + 40, y + 104, 728, 664)

        if girl is None:
            use jimmyspc_scenereplayer_girlselect()
        else:
            use jimmyspc_scenereplayer_sceneselect(girl)

        vbar value YScrollValue('scenereplayer'):
            style 'jimmyspc_vscrollbar'

screen jimmyspc_scenereplayer_girlselect():
    viewport id 'scenereplayer':
        mousewheel True

        vbox:
            null width 728 height 24

            hbox:
                xoffset 44

                spacing 32
                box_wrap True
                box_wrap_spacing 24

                $ girls = get_girls()
                for i in range(len(girls)):
                    use jimmyspc_scenereplayer_icon(i, girls[i])

            null width 728 height 24

screen jimmyspc_scenereplayer_sceneselect(char):
    viewport id 'scenereplayer':
        mousewheel True

        vbox:
            $ scenes = sexSceneDict[char.key]
            for sceneID, sceneData in scenes.items():
                $ seen = sceneID in persistent.sexscenes
                use jimmyspc_scenereplayer_button(char.key, sceneID, sceneData, locked=not seen)

screen jimmyspc_scenereplayer_icon(i, girl):
    $ met = girlMet(girl) if not galleryMode else girl.key in persistent.metGirls
    $ img = '{}_portrait'.format(girl.key) if met else 'lockedscene_thumbnail'
    vbox:
        fixed:
            xysize 120, 120
            add img:
                align 0.5, 0.5
            imagebutton:
                idle Null(
                    height=gui.planner_portrait_size,
                    width=gui.planner_portrait_size)
                hover AlphaMask(Solid('#fff3'), img)
                tooltip i
                if met:
                    action SetVariable('jimmyspc.sceneReplayerChar', girl)
                else:
                    action NullAction()
                mouse 'jimmyspc'
            add 'jimmyspc_icon_frame1'
        text girl.name:
            style 'jimmyspc_text'
            xalign 0.5

screen jimmyspc_scenereplayer_button(girl, sceneLabel, sceneData, locked=True):
    fixed:
        xysize 664, 136

        imagebutton:
            idle 'jimmyspc_listbutton_idle'
            hover 'jimmyspc_listbutton_hover'
            if not locked:
                action Hide(), Call('jimmyspc_replayscene', girl, sceneLabel)
            else:
                action NullAction()
            mouse 'jimmyspc'

        $ thumbnail = sceneData['thumbnail'] if not locked else 'lockedscene_thumbnail'
        add thumbnail:
            xoffset 24
            yoffset 8
        add 'jimmyspc_icon_frame2':
            xoffset 24
            yoffset 8

        $ title = sceneData['title'] if not locked else "???"
        text title:
            style 'jimmyspc_buttontext'
            yanchor 0.5
            xoffset 152
            yoffset 60

label jimmyspc_replayscene(girl, sceneLabel):
    stop music
    scene black with fade
    # call sexscene(girl, sceneLabel) from _call_sexscene
    if galleryMode:
        $ player_name = "Jimmy"
    call expression sceneLabel from _call_expression_9
    scene black with fade
    play music scenemanager.bgMusic
    return
