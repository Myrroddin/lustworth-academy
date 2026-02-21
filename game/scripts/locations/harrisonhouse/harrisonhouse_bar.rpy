#SCREENS
init 1 python:
    def harrisonhousebar_showif_cassidy():
        if Jimmy.outfit != JIMMY_SHAGGY:
            return False
        if getMainObjective()[0] != 'halloween_costumecontest':
            return False
        return True

    def harrisonhousebar_showif_tatiana():
        if Jimmy.outfit != JIMMY_PIRATE:
            return False
        if getMainObjective()[0] != 'halloween_costumecontest':
            return False
        return True

    def harrisonhousebar_showif_ruby():
        if Jimmy.outfit != JIMMY_HOMELANDER:
            return False
        if getMainObjective()[0] != 'halloween_costumecontest':
            return False
        return True

    scene_defs['harrisonhousebar'] = {
        'music': MUSIC_HARRISONBAR_THEME,
        'altermusic': MUSIC_HARRISONBAR_THEME,
        'maps': {
            'default': ('harrisonhousebarnight', 'harrisonhousebarnighthover'),
        },
        'hotspots': [
            ('toentrance', (0, 951, 1918, 129)),
        ],
        'sprites': [
            Sprite('fiona',   'fionawaldodialog01',     (1574, 468, 197, 287), lambda: quests.fionaBartender != COMPLETE),
            Sprite('beatrix', 'beatrixmavisdialog01',   (96,   356, 207, 695), lambda: quests.beatrixAppleCider != COMPLETE),
            Sprite('cassidy', 'cassidydaphnedialog01',  (96,   432, 249, 543), harrisonhousebar_showif_cassidy),
            Sprite('tatiana', 'tatiandialogbuttonidle', (245,  450, 249, 543), harrisonhousebar_showif_tatiana),
            Sprite('ruby',    'rubydialogbuttonidle',   (245,  450, 249, 543), harrisonhousebar_showif_ruby),
        ]
    }

#LABELS
label harrisonhousebar:
    jump harrisonhousebar_loop

label harrisonhousebar_loop:
    $ resetscene()
    call screen map('harrisonhousebar')
    jump harrisonhousebar_loop

label harrisonhousebar_toentrance:
    $ gotoscene('harrisonhouseentrance')

label harrisonhousebar_fiona:
    hide fionawaldodialog01
    jump fionahalloweendialogue

label harrisonhousebar_beatrix:
    hide beatrixmavisdialog01
    jump beatrixhalloweendialogue

label harrisonhousebar_cassidy:
    hide cassidydaphnedialog01
    jump cassidyhalloweendialogue

label harrisonhousebar_tatiana:
    hide tatiandialogbuttonidle
    jump tatianahalloweendialogue

label harrisonhousebar_ruby:
    hide rubydialogbuttonidle
    jump rubyhalloweendialogue
