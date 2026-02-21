#VARIABLES

#LABELS
label eunicedialogue:
    hide screen freeroamhud with None
    play music MUSIC_EUNICES_THEME
    $ objective = getSideObjective('eunice', keyOnly=True)
    if objective == 'chocolates_locked':
        jump eunicechocolatesquest
    elif objective == 'gettingtherole_locked':
        jump eunicegettingtherolequest
    elif objective == 'gettingtherole_miku':
        jump eunicegettingtherolequest
    elif objective == 'gettingtherole_active':
        jump eunicegettingtherolequest
    elif objective == 'theaterpractice_locked':
        jump eunicetheater_practiceintro
    elif objective == 'theaterpractice_active':
        Jimmy "I should get the book for Eunice from the library."
        return
    elif objective == 'theaterpractice_satisfied':
        jump eunicetheater_bookfetch
    elif objective == 'theaterpractice_complete':
        Jimmy "Nothing to do here."
        return
    elif objective == 'theaterpractice_active':
        Jimmy "I should look for Eunice's book at the library."
        return
    elif objective == 'theaterpractice_complete':
        Jimmy "Eunice isn't here, maybe she's practicing at the Auditorium."
        return
    show jimmy neutral
    show eunice uniform neutral
    with dissolve
    Eunice "[player_name]! What can I do for you?"
    jump .dialogmenu

label .dialogmenu:
    menu:
        "Nevermind":
            pass
    $ gotoscene('mainbuildingcafeteria')