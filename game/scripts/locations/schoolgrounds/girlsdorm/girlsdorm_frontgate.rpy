#VARIABLES
default girlsdormfrontgate.gateClosedComment = False

#SCREENS
init 1 python:
    def girlsdormfrontgate_showif_fiona():
        if quests.fionaPadlock == COMPLETE:
            if not quests.fionaConfrontDerek == COMPLETE:
                return False
        elif calendar.when[0] == PROLOGUE:
            return False
        return True

    scene_defs['girlsdormfrontgate'] = {
        'music': MUSIC_SCHOOLGROUNDSAMBIENCEDAY_THEME,
        'altermusic': MUSIC_SCHOOLGROUNDSAMBIENCENIGHT_THEME,
        'maps': {
            'morning':   ("girlsdormgatefallday", "girlsdormgatefalldayhover"),
            'afternoon': ("girlsdormgatefallafternoon", "girlsdormgatefallafternoonhover"),
            'evening':   ("girlsdormgatefallevening", "girlsdormgatefalleveninghover"),
            'night':     ("girlsdormgatefallnight", "girlsdormgatefallnighthover")
        },
        'hotspots': [
            ('exit', (682, 907, 1234, 170)),
            ('gate', (677, 336, 734, 502)),
            ('kiosk', (-2, 322, 651, 708)),
        ],
        'sprites': [
            Sprite('fiona', 'fionakioskdialogbutton', (539, 713, 306, 372), girlsdormfrontgate_showif_fiona),
        ]
    }

#LABELS
label girlsdormfrontgate:
    $ checkcurfew()
    if quests.fionaHideAndSeek == ACTIVE:
        call girlsdormfrontgatecheckderek from _call_girlsdormfrontgatecheckderek
    elif calendar.when[0] == PROLOGUE and not girlsdormfrontgate.gateClosedComment:
        "The gate to the girl's dorm is closed."
        "I guess they don't like unwanted visitors."
        "There's also some kind of kiosk, but no one is around."
        $ girlsdormfrontgate.gateClosedComment = True
    elif quests.fionaConfrontDerek == LOCKED:
        if quests.fionaPadlock == COMPLETE:
            if FionaDaylimit == False:
                Jimmy "Mhmm... Where is Fiona?"
                Fiona "[player_name]! I really need your help."
                Jimmy "Her voice comes from inside the kiosk."
    jump girlsdormfrontgate_loop

label girlsdormfrontgate_loop:
    $ resetscene()
    call screen map('girlsdormfrontgate')
    jump girlsdormfrontgate_loop

label girlsdormfrontgate_gate:
    "The gate's closed."
    jump girlsdormfrontgate_loop

label girlsdormfrontgate_kiosk:
    if calendar.when[0] == PROLOGUE:
        "There's no one at the kiosk."
    elif quests.fionaHideAndSeek == ACTIVE:
        Jimmy "*Better stay away from Fiona while I deal with this idiot.*"
    elif not quests.fionaConfrontDerek == COMPLETE:
        if quests.fionaPadlock == COMPLETE:
            if FionaDaylimit == False:
                jump fionaconfrontderekquest
    elif quests.fionaPadlock == LOCKED:
        "I should introduce myself to the girl running the stand first."
    else:
        jump fionaskiosk
    jump girlsdormfrontgate_loop

label girlsdormfrontgate_exit:
    $ gotoscene('schoolgroundsentrance')

label girlsdormfrontgate_fiona:
    jump fionadialogue

### Various Labels ####

label girlsdormfrontgatecheckderek:
    if FionaWineFound == False:
        Derek "Very cold"
        return     
    elif FionaDonutFound == False:
        Derek "Very cold"
        return
    else:
        return