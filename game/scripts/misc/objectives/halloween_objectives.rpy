# (name, description, iscompletecallback, setstatecallback)
init 1 python:
    def halloween_freeroam_iscomplete():
        if quests.fionaBartender != COMPLETE:
            return False
        if quests.beatrixHalloweenGrinding != COMPLETE:
            return False
        if quests.christyMandyVoltium != COMPLETE:
            return False
        if quests.mikuJacuzzi != COMPLETE:
            return False
        return True

    main_objectives[HALLOWEEN_EVENT] = [
        ('halloween_fruitpunch_active',     "Find out the location of the Fruit Punch",   lambda: quests.halloweenFruitPunch >= SATISFIED                  ),
        ('halloween_fruitpunch_satisfied',     "Tell Pete that you found the Fruit Punch",lambda: quests.halloweenFruitPunch == COMPLETE                   ),
        ('halloween_fakeflag_active',     "Replace the flag in the mansion's roof",       lambda: quests.halloweenFakeFlag == COMPLETE                     ),
        ('halloween_freeroam',       "Explore the Harrison House and talk to the guests", halloween_freeroam_iscomplete, halloween_freeroam_setstate       ),
        ('halloween_costumecontest', "Go to the lounge for the costume contest",          lambda: False,                 halloween_costumecontest_setstate ),
        #('', "", lambda: , ),
    ]

    side_objectives[HALLOWEEN_EVENT] = {
        'beatrix': [
            ('halloween_cider_locked',    "Find her in the lounge",                         lambda: quests.beatrixAppleCider >= ACTIVE           ),
            ('halloween_cider_active',    "Search the house for something non-alcoholic",   lambda: quests.beatrixAppleCider >= SATISFIED        ),
            ('halloween_cider_satisfied', "Give her the juice you found",                   lambda: quests.beatrixAppleCider == COMPLETE         ),
            ('halloween_grinding_locked', "Go back and check the juice you found",       lambda: quests.beatrixHalloweenGrinding >= SATISFIED ),
            #('', "", lambda: ),
        ],
        'cassidy': [
            ('halloween_start',          "Replay the event while wearing the Shaggy costume", lambda: Jimmy.outfit == JIMMY_SHAGGY ),
            ('halloween_freeroam',       "Help the party-goers around the mansion",           halloween_freeroam_iscomplete        ),
            ('halloween_costumecontest', "Go to the lounge for the costume contest",          lambda: False                        ),
            #('', "", lambda: ),
        ],
        'christy': [
            ('halloween_voltium_locked',    "Find her at the pool",                lambda: quests.christyMandyVoltium >= ACTIVE    ),
            ('halloween_voltium_active',    "Search the mansion for some Voltium", lambda: quests.christyMandyVoltium >= SATISFIED ),
            ('halloween_voltium_satisfied', "Take the Voltium back to the pool",   lambda: quests.christyMandyVoltium == COMPLETE  ),
            #('', "", lambda: ),
        ],
        'fiona': [
            ('halloween_bartender_locked', "Talk to her at the bar",                       lambda: quests.fionaBartender >= ACTIVE    ),
            ('halloween_bartender_active', "Find someone to take over for her at the bar", lambda: quests.fionaBartender >= SATISFIED ),
            #('', "", lambda: ),
        ],
        'mandy': [
            ('halloween_voltium_locked',    "Find her at the pool",                lambda: quests.christyMandyVoltium >= ACTIVE    ),
            ('halloween_voltium_active',    "Search the mansion for some Voltium", lambda: quests.christyMandyVoltium >= SATISFIED ),
            ('halloween_voltium_satisfied', "Take the Voltium back to the pool",   lambda: quests.christyMandyVoltium == COMPLETE  ),
            #('', "", lambda: ),
        ],
        'miku': [
            ('halloween_start',   "Improve your relationship with her, then replay the event", lambda: quests.mikuPhotoShoot == COMPLETE ),
            ('halloween_jacuzzi', "Talk to her on the second floor",                           lambda: quests.mikuJacuzzi == COMPLETE    ),
            #('', "", lambda: ),
        ],
        'ruby': [
            ('halloween_start',          "Replay the event while wearing the Superhero costume", lambda: Jimmy.outfit == JIMMY_HOMELANDER ),
            ('halloween_freeroam',       "Help the party-goers around the mansion",              halloween_freeroam_iscomplete            ),
            ('halloween_costumecontest', "Go to the lounge for the costume contest",             lambda: False                            ),
            #('', "", lambda: ),
        ],
        'tatiana': [
            ('halloween_start',          "Replay the event while wearing the Pirate costume", lambda: Jimmy.outfit == JIMMY_PIRATE ),
            ('halloween_freeroam',       "Help the party-goers around the mansion",           halloween_freeroam_iscomplete        ),
            ('halloween_costumecontest', "Go to the lounge for the costume contest",          lambda: False                        ),
            #('', "", lambda: ),
        ],
    }

    def resetHalloweenEvent():
        calendar.event = HALLOWEEN_EVENT
        clearViewedEventObjectives()
        quests.beatrixAppleCider = LOCKED
        quests.beatrixHalloweenGrinding = LOCKED
        quests.fionaBartender = LOCKED
        quests.mikuJacuzzi = LOCKED
        quests.christyMandyVoltium = LOCKED

# Callbacks
init python:
    def halloween_freeroam_setstate(rollback=False):
        # Fiona bartender quest
        Fiona.eventMet[HALLOWEEN_EVENT] = not rollback
        sexscenedict['fiona']['halloweensex'].seen = not rollback
        quests.fionaBartender = COMPLETE if not rollback else LOCKED
        # Beatrix apple cider quest
        Beatrix.eventMet[HALLOWEEN_EVENT] = not rollback
        quests.beatrixAppleCider = COMPLETE if not rollback else LOCKED
        quests.beatrixHalloweenGrinding = COMPLETE if not rollback else LOCKED
        sexscenedict['beatrix']['halloweengrinding'].seen = not rollback
        # Christy & Mandy Voltium quest
        Christy.eventMet[HALLOWEEN_EVENT] = not rollback
        Mandy.eventMet[HALLOWEEN_EVENT] = not rollback
        sexscenedict['christy']['halloweenpoolsex'].seen = not rollback
        sexscenedict['mandy']['halloweenpoolsex'].seen = not rollback
        quests.christyMandyVoltium = COMPLETE if not rollback else LOCKED
        # Miku Jacuzzi quest
        Miku.eventMet[HALLOWEEN_EVENT] = not rollback
        sexscenedict['miku']['halloweeensex'].seen = not rollback
        quests.mikuJacuzzi = COMPLETE if not rollback else LOCKED

    def halloween_costumecontest_setstate(rollback=False):
        return
