define HUD_PATH = 'gui/hud/'

default hud_expanded = False

#SCREENS
screen freeroamhud(interactable=True, showTray=True):
    zorder 100

    # Day & Time
    use freeroamhud_daytime
    # Money
    if glob.walletUnlocked:
        use freeroamhud_wallet
    if showTray:
        use freeroamhud_icontray(interactable)

transform slide_hud_tray(x):
    linear 0 xpos x

screen freeroamhud_icontray(interactable):
    zorder 100

    $ f = lambda *x: _scale(*x)

    $ icon_spacing = f(30)
    $ inventory_button_width = f(176)
    $ planner_button_width = f(180)
    $ map_button_width = f(192)
    $ hud_tray_width = f(696)

    $ xmin = -hud_tray_width
    $ xmax = xmin + inventory_button_width + icon_spacing + f(44)
    if glob.plannerUnlocked:
        $ xmax += planner_button_width + icon_spacing
    if glob.mapUnlocked:
        $ xmax += map_button_width + icon_spacing
    
    $ hbox_xpos = -xmax + icon_spacing
    $ hbox_ypos = f(16)

    fixed:
        if hud_expanded:
            pos xmin, 0.02
            at slide_hud_tray(xmax)
        else:
            pos xmax, 0.02
            at slide_hud_tray(xmin)

        imagemap:
            idle 'menupanelidle'
            hover 'menupanelhover'

            if interactable:
                hotspot f(696, 48, 44, 136) action ToggleVariable('hud_expanded')

        hbox:
            pos hbox_xpos, hbox_ypos
            spacing icon_spacing

            imagebutton:
                idle 'inventorybuttonidle'
                hover 'inventorybuttonhover'
                if interactable:
                    action Jump('inventory')

            if glob.plannerUnlocked:
                imagebutton:
                    idle 'plannerbuttonidle'
                    hover 'plannerbuttonhover'
                    if interactable:
                        action Jump('freeroamhud_planner')
            
            if glob.mapUnlocked:
                imagebutton:
                    idle 'mapbuttonidle'
                    hover 'mapbuttonhover'
                    if interactable:
                        action Jump('freeroamhud_minimap')

screen freeroamhud_daytime:
    zorder 100
    
    # Time
    $ time = TIME_STRINGS[calendar.when[2] - 1]
    $ time_path = HUD_PATH + 'watch{}.webp'.format(time)
    add time_path:
        pos 0.864, 0.02

    # Day
    $ day = DAY_STRINGS[calendar.when[1] - 1]
    $ day_path = HUD_PATH + 'calendar{}.webp'.format(day)
    add day_path:
        pos 0.897, 0.02

screen freeroamhud_wallet:
    zorder 100
    fixed:
        xsize gui.hud_money_width
        pos 0.897, 0.070
        add (HUD_PATH + 'moneyhud.webp')
        text "[Jimmy.money]":
            xalign 0.5
            font 'fonts/CyborgSister.ttf'
            size gui.hud_money_size
            outlines [ (1, '#000', 0, 0) ]

#LABELS
label freeroamhud_planner:
    # Make free-roam HUD non-interactable
    show screen freeroamhud(False)
    call screen schoolplanner
    # return to current scene on planner close
    $ gotoscene(scenemanager.scene)

label freeroamhud_minimap:
    hide screen freeroamhud
    show schoolminimapfall
    call screen schoolminimap
    # return to current scene on map close
    $ gotoscene(scenemanager.scene)
