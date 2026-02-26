screen planner_girls:
    default char = None

    if char is not None:
        use planner_profile(char)
    else:
        use planner_girls_select

    if char is None:
        $ action = SetScreenVariable('page', 'stats')
    else:
        $ action = SetScreenVariable('char', None)
    use planner_left_arrow(action)

screen planner_girls_select:
    $ girls = get_girls()

    text __("The Girls"):
        style 'planner_header'
        underline True
        xcenter planner_left_center
        ypos 0.18

    # Portraits
    grid 4 4:
        xcenter planner_left_center
        ypos 0.25
        xspacing gui.planner_girls_xspacing
        yspacing gui.planner_girls_yspacing
        for i in range(16):
            if i < len(girls):
                use planner_portrait(i, girls[i])
            else:
                use planner_portrait(i)
    grid 4 4:
        xcenter planner_right_center
        ypos 0.25
        xspacing gui.planner_girls_xspacing
        yspacing gui.planner_girls_yspacing
        for i in range(16, 32):
            if i < len(girls):
                use planner_portrait(i, girls[i])
            else:
                use planner_portrait(i)

    # Name on hover
    $ index = GetTooltip()
    if index is not None:
        $ girl = girls[index]
        $ hasEventContent = girlHasEventContent(girl)
        $ name = girl.name if girl.met else '???'
        $ c = girl.color if (girl.met and hasEventContent) else Color("#ccc")
        text name:
            style 'planner_text_bold'
            xcenter (planner_left_center if index < 16 else planner_right_center)
            ypos gui.planner_girls_tooltip_ypos
            size gui.planner_girls_tooltip_size
            color c
            outlines [(1, "#000", 0, 0)]

screen planner_portrait(i, char=None):
    fixed:
        xmaximum gui.planner_portrait_size
        ymaximum gui.planner_portrait_size
        add 'planner_portrait_frame'
        if char != None:
            $ hasEventContent = girlHasEventContent(char)
            if calendar.event is not None and hasEventContent:
                $ img = '{}_{}_portrait'.format(char.key, calendar.event)
            else:
                $ img = '{}_portrait'.format(char.key)

            if not hasEventContent:
                $ img = AlphaMask(Solid('#333'), img)
            elif not girlMet(char):
                # Gray-out characters that have not been met
                $ img = AlphaMask(Solid('#666'), img)
            
            add img
            imagebutton:
                idle Null(
                    height=gui.planner_portrait_size, 
                    width=gui.planner_portrait_size)
                hover AlphaMask(Solid('#fff3'), img)
                tooltip i
                if hasEventContent:
                    action SetScreenVariable('char', char)
                else:
                    action NullAction()
            
            # Only show quest bubbles after the prologue
            if calendar.when[0] != PROLOGUE:
                $ objective = getSideObjective(char.key)
                if objective is not None:
                    $ key = char.key + '_' + objective[0]
                    if key not in planner.viewedObjectives:
                        add 'quest_notif_new'
                    else:
                        add 'quest_notif'

screen planner_profile(char):
    $ name = char.name if char.met else '???'
    text name:
        style 'planner_profile_header'
    
    use expression ('planner_' + char.key + '_profile')

    text __("Current Objective"):
        style 'planner_text_bold'
        xcenter planner_left_center
        ypos 0.25

    if calendar.when[0] == PROLOGUE:
        $ objective = ("{i}" + __("Complete the prologue to unlock quest hints") + "{/i}")
    else:
        $ objective = getSideObjective(char.key)
        if objective is not None:
            # Mark viewed
            $ planner.viewedObjectives.add(char.key + '_' + objective[0])
            $ objective = objective[1]
        elif calendar.event is not None:
            $ objective = "{i}" + __("No more event content") + "{/i}"
        else:
            $ objective = "{i}" + __("More content coming soon") + "{/i}"
    
    text objective:
        style 'planner_text'
        xcenter planner_left_center
        ypos 0.29
        xmaximum gui.planner_objective_width
        text_align 0.5
    
    text __("Relationship Status"):
        style 'planner_text_bold'
        xcenter planner_left_center
        ypos 0.39
    
    # TODO: dynamic relationship status titles
    # text __("Acquaintances"):
    #     style 'planner_text'
    #     xcenter planner_left_center
    #     ypos 0.48
    #     size 30

    $ relBarPos = (0.19, 0.435)
    add Solid('#dddddd', xsize=gui.planner_relationship_bar_width, ysize=gui.planner_relationship_bar_height):
        pos relBarPos
    $ w = char.relPoints * 50
    add Solid('#ff0000', xsize=w, ysize=gui.planner_relationship_bar_height):
        pos relBarPos
    
    text __("About"):
        style 'planner_text_bold'
        xcenter planner_left_center
        ypos gui.planner_profile_about_label_ypos
