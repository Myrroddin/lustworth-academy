# Checkpoints
## Day 0
default prologue.finishIntro = False
default prologue.findJimmysRoom = False
## Day 1
default prologue.firstNight = False
default prologue.spanishIntro = False
default prologue.gymIntro = False
## Day 2
default prologue.secondNight = False
default prologue.mathIntro = False
default prologue.shopIntro = False
default prologue.mayorsSpeech = False
default prologue.kassandraIntro = False
default prologue.cassidyPeephole = False
default prologue.sneakOutTownhouse = False
## Day 3
default prologue.visitthebeach = False
default prologue.checkthecliff = False
default prologue.findtherope = False
default prologue.awkwardBreakfast = False
default prologue.afternoonNap = False
default prologue.dakotaJobOffer = False
default prologue.ranchMinigameIntro = False
default alice_breakfastwarning = False
default breakfast_ready = False
## Day 4
default prologue.dakotaRanchIntro = False
default prologue.barbaraSallyStrapon = False
default prologue.cassidyShower = False
default prologue.complete = False

# Callbacks
init python:
    def ch0_finishintro_setstate(rollback=False):
        Stapleneck.met = not rollback
        Dawson.met = not rollback
        Beatrix.met = not rollback
        prologue.finishIntro = not rollback

    def ch0_findjimmysroom_setstate(rollback=False):
        prologue.findJimmysRoom = not rollback

    def ch0_firstnight_setstate(rollback=False):
        sexscenedict['wendy']['mysterygirlnight1'].seen = not rollback
        Pete.met = not rollback
        glob.plannerUnlocked = not rollback
        prologue.firstNight = not rollback

    def ch0_spanishclassintro_setstate(rollback=False):
        Mandy.met = not rollback
        Violet.met = not rollback
        Punny.met = not rollback
        prologue.spanishIntro = not rollback

    def ch0_gymclassintro_setstate(rollback=False):
        Christy.met = not rollback
        sexscenedict['christy']['gymshower'].seen = not rollback
        Toord.met = not rollback
        Cassidy.met = not rollback
        sexscenedict['cassidy']['lockerroomdildo'].seen = not rollback
        prologue.gymIntro = not rollback

    def ch0_secondnight_setstate(rollback=False):
        sexscenedict['wendy']['mysterygirlnight2'].seen = not rollback
        Wendy.met = not rollback
        Gary.met = not rollback
        prologue.secondNight = not rollback

    def ch0_mathclassintro_setstate(rollback=False):
        Camembert.met = not rollback
        prologue.mathIntro = not rollback

    def ch0_shopclassintro_setstate(rollback=False):
        sexscenedict['lola']['carmasturbation'].seen = not rollback
        Lola.met = not rollback
        Blair.met = not rollback
        Audrey.met = not rollback
        prologue.shopIntro = not rollback

    def ch0_mayorsspeech_setstate(rollback=False):
        Donaguy.met = not rollback
        prologue.mayorsSpeech = not rollback

    def ch0_kassandraintro_setstate(rollback=False):
        Kassandra.met = not rollback
        Alice.met = not rollback
        prologue.kassandraIntro = not rollback

    def ch0_townhousecaught_setstate(rollback=False):
        quests.cassidyDildo = ACTIVE if not rollback else LOCKED

    def ch0_findcassidysdildo_setstate(rollback=False):
        quests.cassidyDildo = COMPLETE if not rollback else ACTIVE # SATISFIED?

    def ch0_cassidypeephole_setstate(rollback=False):
        sexscenedict['cassidy']['townhousepeephole'].seen = not rollback
        prologue.cassidyPeephole = not rollback

    def ch0_townhousesneak_setstate(rollback=False):
        prologue.sneakOutTownhouse = not rollback

    def ch0_wendysroom_setstate(rollback=False):
        sexscenedict['wendy']['roominfiltration'].seen = not rollback
        Jill.met = not rollback
        Grant.met = not rollback
        quests.grantHoboBag = ACTIVE if not rollback else LOCKED

    def ch0_grantsbagfetch_setstate(rollback=False):
        sexscenedict['jill']['officemasturbation'].seen = not rollback
        quests.grantHoboBag = SATISFIED if not rollback else ACTIVE

    def ch0_grantsbagreturn_setstate(rollback=False):
        quests.grantHoboBag = COMPLETE if not rollback else SATISFIED
        quests.blairUSB = ACTIVE if not rollback else LOCKED

    def ch0_blairusb_setstate(rollback=False):
        sexscenedict['blair']['opheliascissoring'].seen = not rollback
        quests.blairUSB = COMPLETE if not rollback else ACTIVE # SATISFIED?

    def ch0_awkwardbreakfast_setstate(rollback=False):
        glob.walletUnlocked = not rollback
        prologue.awkwardBreakfast = not rollback

    def ch0_afternoonnap_setstate(rollback=False):
        prologue.afternoonNap = not rollback

    def ch0_dakotajoboffer_setstate(rollback=False):
        Antonella.met = not rollback
        Dakota.met = not rollback
        prologue.dakotaJobOffer = not rollback

    def ch0_dakotaranchintro_setstate(rollback=False):
        Barbara.met = not rollback
        Sally.met = not rollback
        prologue.dakotaRanchIntro = not rollback

    def ch0_ranchminigameintro_setstate(rollback=False):
        Jimmy.money += 50 if not rollback else -50
        Dakota.relPoints += 1 if not rollback else -1
        prologue.ranchMinigameIntro = not rollback

    def ch0_barbarasallystrapon_setstate(rollback=False):
        sexscenedict['barbara']['cucumberstrapon'].seen = not rollback
        sexscenedict['sally']['cucumberstrapon'].seen = not rollback
        prologue.barbaraSallyStrapon = not rollback

    def ch0_takeshower_setstate(rollback=False):
        sexscenedict['cassidy']['townhouseshower'].seen = not rollback
        prologue.cassidyShower = not rollback

    def ch0_endofprologue_setstate(rollback=False):
        prologue.complete = not rollback
