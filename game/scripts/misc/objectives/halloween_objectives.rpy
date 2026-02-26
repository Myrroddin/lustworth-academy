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
        ('halloween_fruitpunch_active',     __("Find out the location of the Fruit Punch"),   lambda: quests.halloweenFruitPunch >= SATISFIED                  ),
        ('halloween_fruitpunch_satisfied',     __("Tell Pete that you found the Fruit Punch"),lambda: quests.halloweenFruitPunch == COMPLETE                   ),
        ('halloween_fakeflag_active',     __("Replace the flag in the mansion's roof"),       lambda: quests.halloweenFakeFlag == COMPLETE                     ),
        ('halloween_freeroam',       __("Explore the Harrison House and talk to the guests"), halloween_freeroam_iscomplete, halloween_freeroam_setstate       ),
        ('halloween_costumecontest', __("Go to the lounge for the costume contest"),          lambda: False,                 halloween_costumecontest_setstate ),
        #('', "", lambda: , ),
    ]

    side_objectives[HALLOWEEN_EVENT] = {
        'beatrix': [
            ('halloween_cider_locked',    __("Find her in the lounge"),                         lambda: quests.beatrixAppleCider >= ACTIVE           ),
            ('halloween_cider_active',    __("Search the house for something non-alcoholic"),   lambda: quests.beatrixAppleCider >= SATISFIED        ),
            ('halloween_cider_satisfied', __("Give her the juice you found"),                   lambda: quests.beatrixAppleCider == COMPLETE         ),
            ('halloween_grinding_locked', __("Go back and check the juice you found"),       lambda: quests.beatrixHalloweenGrinding >= SATISFIED ),
            #('', "", lambda: ),
        ],
        'cassidy': [
            ('halloween_start',          __("Replay the event while wearing the Shaggy costume"), lambda: Jimmy.outfit == JIMMY_SHAGGY ),
            ('halloween_freeroam',       __("Help the party-goers around the mansion"),           halloween_freeroam_iscomplete        ),
            ('halloween_costumecontest', __("Go to the lounge for the costume contest"),          lambda: False                        ),
            #('', "", lambda: ),
        ],
        'christy': [
            ('halloween_voltium_locked',    __("Find her at the pool"),                lambda: quests.christyMandyVoltium >= ACTIVE    ),
            ('halloween_voltium_active',    __("Search the mansion for some Voltium"), lambda: quests.christyMandyVoltium >= SATISFIED ),
            ('halloween_voltium_satisfied', __("Take the Voltium back to the pool"),   lambda: quests.christyMandyVoltium == COMPLETE  ),
            #('', "", lambda: ),
        ],
        'fiona': [
            ('halloween_bartender_locked', __("Talk to her at the bar"),                       lambda: quests.fionaBartender >= ACTIVE    ),
            ('halloween_bartender_active', __("Find someone to take over for her at the bar"), lambda: quests.fionaBartender >= SATISFIED ),
            #('', "", lambda: ),
        ],
        'mandy': [
            ('halloween_voltium_locked',    __("Find her at the pool"),                lambda: quests.christyMandyVoltium >= ACTIVE    ),
            ('halloween_voltium_active',    __("Search the mansion for some Voltium"), lambda: quests.christyMandyVoltium >= SATISFIED ),
            ('halloween_voltium_satisfied', __("Take the Voltium back to the pool"),   lambda: quests.christyMandyVoltium == COMPLETE  ),
            #('', "", lambda: ),
        ],
        'miku': [
            ('halloween_start',   __("Improve your relationship with her, then replay the event"), lambda: quests.mikuPhotoShoot == COMPLETE ),
            ('halloween_jacuzzi', __("Talk to her on the second floor"),                           lambda: quests.mikuJacuzzi == COMPLETE    ),
            #('', "", lambda: ),
        ],
        'ruby': [
            ('halloween_start',          __("Replay the event while wearing the Superhero costume"), lambda: Jimmy.outfit == JIMMY_HOMELANDER ),
            ('halloween_freeroam',       __("Help the party-goers around the mansion"),              halloween_freeroam_iscomplete            ),
            ('halloween_costumecontest', __("Go to the lounge for the costume contest"),             lambda: False                            ),
            #('', "", lambda: ),
        ],
        'tatiana': [
            ('halloween_start',          __("Replay the event while wearing the Pirate costume"), lambda: Jimmy.outfit == JIMMY_PIRATE ),
            ('halloween_freeroam',       __("Help the party-goers around the mansion"),           halloween_freeroam_iscomplete        ),
            ('halloween_costumecontest', __("Go to the lounge for the costume contest"),          lambda: False                        ),
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
