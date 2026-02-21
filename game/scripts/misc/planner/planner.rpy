#VARIABLES
default planner.viewedObjectives = set()
default planner.lastViewedObjective = None

init python:
    def girlMet(girl):
        return girl.met if calendar.event is None else girl.eventMet[calendar.event]

    def girlHasEventContent(girl):
        return calendar.event is None or girl.key in side_objectives[calendar.event]
    
    def hasNewObjective():
        objective = getMainObjective()[0]
        return objective != 'endofcontent' and objective != planner.lastViewedObjective

#STYLES
define planner_left_center = 0.31
define planner_right_center = 0.69

style planner_text:
    font 'fonts/Calibri.ttf'
    color Color("#94745A")
    outlines []

style planner_text_bold is planner_text:
    font 'fonts/Calibri Bold.ttf'

style planner_header is planner_text:
    size 48

style planner_header_bold is planner_header:
    font 'fonts/Calibri Bold.ttf'

#SCREENS
screen schoolplanner:
    zorder 150
    add 'planner_template'

    default page = 'stats'

    if page == 'stats':
        use planner_stats
    elif page == 'girls':
        use planner_girls
    # use planner_girls
    # use planner_profile(Ruby)

    ## Exit ribbon
    use sprite('planner_exit_ribbon', (0.81, 0.112, 55, 90), action=Return())

screen planner_left_arrow(action):
    imagebutton:
        idle 'planner_arrow_left'
        hover 'planner_arrow_left_hover'
        xalign 0.191
        yalign 0.864
        action action

screen planner_right_arrow(action):
    imagebutton:
        idle 'planner_arrow_right'
        hover 'planner_arrow_right_hover'
        xalign 0.8095
        yalign 0.864
        action action

#LABELS
label schoolplanner_exit:
    # return to current scene
    $ gotoscene(scenemanager.scene)
