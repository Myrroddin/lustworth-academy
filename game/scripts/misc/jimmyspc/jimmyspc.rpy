#VARIABLES
define config.mouse = { }
define config.mouse['jimmyspc'] = [ ( 'images/misc/jimmyspc/jimmyspc_cursor.webp', 0, 0) ]

define jimmyspc.icons = {
    'thispc':        (100,  100),
    'fileexplorer':  (100,  220),
    'chrome':        (100,  340),
    'steam':         (100,  460),
    'discord':       (100,  580),
    'word':          (100,  850),
    'excel':         (220,  850),
    'powerpoint':    (340,  850),
    'scenereplayer': (1560, 100),
    'wallpapers':    (1680, 100),
    'recyclebin':    (1680, 850),
}

default jimmyspc.sceneReplayerActive = False
default jimmyspc.sceneReplayerChar = None

init python:
    def scrollButtonOnClick(id, dir):
        vp = renpy.get_widget(None, id)
        adjustment = vp.yadjustment
        value = adjustment.value
        value += adjustment.step * dir
        adjustment.change(value)

#STYLES
style jimmyspc_text:
    font 'fonts/CyborgSister.ttf'
    color Color("#000000")
    outlines []

style jimmyspc_buttontext is jimmyspc_text:
    size 56

style jimmyspc_windowtitle is jimmyspc_text:
    size 72

style jimmyspc_vscrollbar:
    xsize 56
    ysize 552
    yoffset 56
    base_bar 'jimmyspc_[prefix_]bar'
    thumb Frame('jimmyspc_[prefix_]thumb', Borders(8, 8, 8, 16))
    mouse 'jimmyspc'

style jimmyspc_icon:
    xsize 120
    ysize 120
    mouse 'jimmyspc'

#SCREENS
screen jimmyspc:
    if galleryMode:
        $ jimmyspc.sceneReplayerActive = True
    
    # Captures scrolling to keep from rolling back unintentionally
    viewport:
        area (73, 75, 1770, 920)
        mousewheel True

    imagemap:
        idle 'pcscreennew'
        hover 'pcscreennewhover'

        hotspot (73, 75, 1770, 920) action NullAction() mouse 'jimmyspc'
        hotspot (1679, 1042, 189, 38) action Jump('jimmyspc_exit')

    for icon in jimmyspc.icons:
        $ x, y = jimmyspc.icons[icon]
        $ img = 'jimmyspc_' + icon + '_icon'
        $ isButton = not jimmyspc.sceneReplayerActive
        $ label = 'jimmyspc_' + icon
        use sprite(img, (x, y, 120, 120), isButton=isButton, label=label, mouse='jimmyspc', showHUD=False)

    if jimmyspc.sceneReplayerActive:
        use jimmyspc_scenereplayer(x=560, y=128)

label jimmyspc_showicons:
    python:
        for icon in jimmyspc.icons:
            x, y = jimmyspc.icons[icon]
            img = 'jimmyspc_' + icon + '_icon'
            renpy.show(img, at_list=[Transform(pos=(x, y))])
    return

#LABELS
label jimmyspc:
    hide screen freeroamhud
    jump jimmyspc_loop

label jimmyspc_loop:
    scene pcscreennew
    call jimmyspc_showicons from _call_jimmyspc_showicons
    call screen jimmyspc
    jump jimmyspc_loop

label jimmyspc_thispc:
label jimmyspc_fileexplorer:
label jimmyspc_chrome:
label jimmyspc_steam:
label jimmyspc_discord:
    jump jimmyspc_loop

label jimmyspc_word:
    __("\"Michaelsoft Word\"")
    __("Part of the Michaelsoft Binbows suite.")
    jump jimmyspc_loop

label jimmyspc_excel:
    __("\"Michaelsoft Excel\"")
    __("Part of the Michaelsoft Binbows suite.")
    jump jimmyspc_loop

label jimmyspc_powerpoint:
    __("\"Michaelsoft PowerPoint\"")
    __("Part of the Michaelsoft Binbows suite.")
    jump jimmyspc_loop

label jimmyspc_wallpapers:
    Developer "{i}Wallpapers coming soon!{/i}"
    jump jimmyspc_loop

label jimmyspc_recyclebin:
    if gallerymainmenu:
        $ gallerymainmenu = False
        call screen main_menu()
    else:
        $ jimmyspc.sceneReplayerActive = False
        $ jimmyspc.sceneReplayerChar = None
        return

label jimmyspc_scenereplayer:
    #call screen gallery
    $ jimmyspc.sceneReplayerActive = True
    jump jimmyspc_loop

label jimmyspc_exit:
    $ jimmyspc.sceneReplayerActive = False
    $ jimmyspc.sceneReplayerChar = None
    if gallerymainmenu:
        $ gallerymainmenu = False
        call screen main_menu()
    else:
        # If we were in-game, this returns us to the pause menu/game
        return
