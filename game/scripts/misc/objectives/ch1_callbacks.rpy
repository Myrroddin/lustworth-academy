# Checkpoints
default chapter1.introCutscene = False
default chapter1.nerdsIntro = False

# Callbacks
init python:
    def ch1_introcutscene_setstate(rollback=False):
        glob.mapUnlocked = not rollback
        sexscenes.angiesNote = not rollback
        chapter1.introCutscene = not rollback

    def ch1_freeroam_setstate(rollback=False):
        Fiona.met = not rollback
        Derek.met = not rollback
        # Fiona padlock quest
        Fiona.relPoints += 1 if not rollback else -1
        sexscenedict['fiona']['kiosktitflash'].seen = not rollback
        quests.fionaPadlock = COMPLETE if not rollback else LOCKED
        # Fiona Derek quest
        sexscenedict['fiona']['kioskblowjob'].seen = not rollback
        quests.fionaConfrontDerek = COMPLETE if not rollback else LOCKED
        # Fiona night date quest
        Fiona.relPoints += 1 if not rollback else -1
        sexscenedict['fiona']['nightdate'].seen = not rollback
        quests.fionaNightDate = COMPLETE if not rollback else LOCKED
        # Beatrix diary quest
        Beatrix.relPoints += 1 if not rollback else -1
        sexscenedict['beatrix']['lapdance'].seen = not rollback
        quests.beatrixDiary = COMPLETE if not rollback else LOCKED

    def ch1_fionahalloweenintro_setstate(rollback=False):
        quests.halloweenCostume = ACTIVE if not rollback else LOCKED

    def ch1_halloweencostume_setstate(rollback=False):
        quests.halloweenCostume = SATISFIED if not rollback else ACTIVE

    def ch1_halloweenevent_setstate(rollback=False):
        # Call set-state callback for all Halloween objectives
        for objective in main_objectives[HALLOWEEN_EVENT]:
            objective[3](rollback)
        glob.halloweenEventComplete = not rollback

    def ch1_nerdsIntro_setstate(rollback=False):
        chapter1.nerdsIntro = not rollback
