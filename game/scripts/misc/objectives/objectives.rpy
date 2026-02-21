init python:
    main_objectives = {}
    side_objectives = {}

    def getObjectiveIndex(name):
        objectives = main_objectives[calendar.event]
        for i in range(len(objectives)):
            objective = objectives[i]
            if objective[0] == name:
                return i
        raise Exception('No objective exists with the name "' + name + '".')

    def skipToObjective(name):
        startIdx = getMainObjectiveIndex()
        endIdx = getObjectiveIndex(name)

        objectives = main_objectives[calendar.event]
        if startIdx < endIdx:
            for i in range(startIdx, endIdx):
                objectives[i][3]() # set state
        elif startIdx > endIdx:
            for i in range(startIdx - 1, endIdx - 1, -1):
                objectives[i][3](rollback=True) # set state

    # Finds first incomplete objective for the current event and returns its index
    def getMainObjectiveIndex():
        objectives = main_objectives[calendar.event]
        for i in range(len(objectives)):
            objective = objectives[i]
            # check if objective is (in)complete
            if not objective[2]():
                return i

    def getMainObjective():
        i = getMainObjectiveIndex()
        return main_objectives[calendar.event][i]

    def getSideObjective(girl, keyOnly=False):
        if girl not in side_objectives[calendar.event]:
            return None
        for objective in side_objectives[calendar.event][girl]:
            if not objective[2]():
                if keyOnly:
                    return objective[0]
                return objective
    
    def clearViewedEventObjectives():
        planner.lastViewedObjective = None
        for girl, objectives in side_objectives[calendar.event].items():
            for objective in objectives:
                key = girl + '_' + objective[0]
                if key in planner.viewedObjectives:
                    planner.viewedObjectives.remove(key)

    # def hasUnviewedObjective():
    #     girls = get_girls()
    #     for girl in filter(lambda x: x.met, girls):
    #         objective = getSideObjective(girl.key)
    #         if objective is not None:
    #             key = girl.key + '_' + objective[0]
    #             if key not in planner.viewedObjectives:
    #                 return True
    #     return False
