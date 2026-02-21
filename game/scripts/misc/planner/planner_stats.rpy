screen planner_stats:
    # Stats
    use planner_jimmys_stats
    # Objective
    use planner_objective
    # Classes
    use planner_classes

    # Schedule
    add 'planner_schedule':
        xcenter planner_left_center
        ypos gui.planner_schedule_ypos
    
    $ action = SetScreenVariable('page', 'girls')
    use planner_right_arrow(action)

screen planner_jimmys_stats:
    text "[player_name]'s Stats":
        style 'planner_header'
        xcenter planner_left_center
        ypos 0.18
    # Stat names
    vbox:
        xpos gui.planner_stat_label_xpos
        ypos gui.planner_stat_ypos
        spacing gui.planner_stat_label_spacing
        for stat in Jimmy.stats:
            text stat.capitalize() style 'planner_text' size gui.planner_stat_label_size
    # Stat bars
    vbox:
        xpos gui.planner_stat_bar_xpos
        ypos gui.planner_stat_ypos
        spacing gui.planner_stat_bar_spacing
        for stat in Jimmy.stats:
            use planner_statbar(stat)

screen planner_objective:
    text "Objective":
        style 'planner_header_bold'
        xcenter planner_right_center
        ypos 0.18
    
    # Get current objective description
    $ objective = getMainObjective()
    if hasNewObjective():
        $ notif_path = HUD_PATH + 'diarynotif.webp'
        add notif_path:
            pos gui.planner_objective_notif_pos
        # Track most recently viewed objective
        $ planner.lastViewedObjective = objective[0]
    text objective[1]:
        style 'planner_text'
        xcenter planner_right_center
        ypos gui.planner_objective_ypos
        xmaximum gui.planner_objective_width
        text_align 0.5

screen planner_classes:
    text "Classes":
        style 'planner_header'
        xcenter planner_right_center
        ypos 0.34
    grid 2 len(classes):
        xpos gui.planner_classes_xpos
        ypos 0.40
        xspacing gui.planner_classes_xspacing
        yspacing gui.planner_classes_yspacing
        for name, subj in classes.items():
            text name.capitalize() style 'planner_text'
            $ tally = subj.lesson - 1
            text "[tally]/2" style 'planner_text'

screen planner_statbar(stat):
    hbox:
        spacing 6
        for i in range(10):
            if i < Jimmy.stats[stat]:
                add 'stat_frame_full'
            else:
                add 'stat_frame_empty'
