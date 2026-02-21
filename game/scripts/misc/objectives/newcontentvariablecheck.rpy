#v0.50.2
default newcontentskipactive = False

label newcontentvariablecheck:
    $ prologue.finishIntro = True
    $ prologue.findJimmysRoom = True
    ## Day 1
    $ prologue.firstNight = True
    $ prologue.spanishIntro = True
    $ prologue.gymIntro = True
    ## Day 2
    $ prologue.secondNight = True
    $ prologue.mathIntro = True
    $ prologue.shopIntro = True
    $ prologue.mayorsSpeech = True
    $ prologue.kassandraIntro = True
    $ prologue.cassidyPeephole = True
    $ prologue.sneakOutTownhouse = True
    ## Day 3
    $ prologue.visitthebeach = True
    $ prologue.checkthecliff = True
    $ prologue.findtherope = True
    $ prologue.awkwardBreakfast = True
    $ prologue.afternoonNap = True
    $ prologue.dakotaJobOffer = True
    $ prologue.ranchMinigameIntro = True
    $ alice_breakfastwarning = True
    $ breakfast_ready = True
    ## Day 4
    $ prologue.dakotaRanchIntro = True
    $ prologue.barbaraSallyStrapon = True
    $ prologue.cassidyShower = True
    $ prologue.complete = True
    $ Stapleneck.met = True
    $ Dawson.met = True
    $ Beatrix.met = True
    $ prologue.finishIntro = True
    $ prologue.findJimmysRoom = True
    $ Pete.met = True
    $ glob.plannerUnlocked = True
    $ prologue.firstNight = True
    $ Mandy.met = True
    $ Violet.met = True
    $ Punny.met = True
    $ prologue.spanishIntro = True
    $ Christy.met = True
    $ Toord.met = True
    $ Cassidy.met = True
    $ prologue.gymIntro = True
    $ Wendy.met = True
    $ Gary.met = True
    $ prologue.secondNight = True
    $ Camembert.met = True
    $ prologue.mathIntro = True
    $ Lola.met = True
    $ Blair.met = True
    $ Audrey.met = True
    $ prologue.shopIntro = True
    $ Donaguy.met = True
    $ prologue.mayorsSpeech = True
    $ Kassandra.met = True
    $ Alice.met = True
    $ prologue.kassandraIntro = True
    $ quests.cassidyDildo = COMPLETE
    $ prologue.cassidyPeephole = True
    $ prologue.sneakOutTownhouse = True
    $ Jill.met = True
    $ Grant.met = True
    $ quests.grantHoboBag = COMPLETE
    $ quests.blairUSB = COMPLETE
    $ glob.walletUnlocked = True
    $ prologue.awkwardBreakfast = True
    $ prologue.afternoonNap = True
    $ Antonella.met = True
    $ Dakota.met = True
    $ prologue.dakotaJobOffer = True
    $ Barbara.met = True
    $ Sally.met = True
    $ prologue.dakotaRanchIntro = True
    $ Jimmy.money += 50
    $ prologue.ranchMinigameIntro = True
    $ prologue.barbaraSallyStrapon = True
    $ prologue.cassidyShower = True
    $ prologue.complete = True
    $ chapter1.introCutscene = True
    $ glob.mapUnlocked = True
    $ sexscenes.angiesNote = True
    $ chapter1.introCutscene = True
    $ Fiona.met = True
    $ Derek.met = True
    # Fiona quests
    $ quests.fionaPadlock = COMPLETE
    $ quests.fionaConfrontDerek = COMPLETE
    $ quests.fionaNightDate = COMPLETE
    # Beatrix quests
    $ quests.beatrixDiary = COMPLETE
    $ Miku.met = True
    $ quests.artProject = COMPLETE
    $ quests.mikuPhotoShoot = COMPLETE
    $ quests.mikuStorypartone = COMPLETE
    # Miss Dawson quests
    $ quests.headmasterSpy = COMPLETE
    $ quests.missdawsonBathroomIncident = COMPLETE
    $ quests.missdawsonAssistantEdna = COMPLETE
    $ quests.missdawsonAssistantMarlon = COMPLETE
    $ quests.missdawsonTitShow = COMPLETE
    $ quests.missdawsonHalloweenAurora = COMPLETE
    $ quests.missdawsonHalloweenAudrey = COMPLETE
    $ quests.missdawsonHalloweenCamembert = COMPLETE
    $ quests.missdawsonAssistant = COMPLETE
    $ quests.missdawsonHalloweenStaff = COMPLETE
    $ quest.missdawsondeepdone = True
    $ Jimmy.money += 1000
    # Cassidy quests
    $ quests.cassidyTrials = COMPLETE
    $ quests.cassidyFirstFuck = COMPLETE
    # Bakshi quests
    $ quests.bakshiSirlaughsalot = COMPLETE
    # Christy quests
    $ quests.christyPlan = COMPLETE
##################### CHAPTER 2 ############################

    call item_pickup(ItemShaggyCostume) from _call_item_pickup_33
    call item_pickup(ItemPirateCostume) from _call_item_pickup_34
    call item_pickup(ItemHeroCostume) from _call_item_pickup_35
    call item_pickup(ItemPartyInvitation) from _call_item_pickup_31
    call item_pickup(ItemHeadmasterKey) from _call_item_pickup_32
    # Halloween quests
    $ quests.halloweenCostume = COMPLETE
    $ quests.garyHalloweenHeist = COMPLETE
    $ glob.halloweenEventComplete = True
    $ quests.beatrixAppleCider = COMPLETE
    $ quests.beatrixHalloweenGrinding = COMPLETE
    $ quests.fionaBartender = COMPLETE
    $ quests.mikuJacuzzi = COMPLETE
    $ quests.christyMandyVoltium = COMPLETE

    ####### CLASSES AND STATS #########
    $ classes['spanish'].lesson = 3
    $ Jimmy.stats['charisma'] += 2
    $ classes['art'].lesson = 3
    $ classes['biology'].lesson = 3
    $ classes['geography'].lesson = 3
    $ classes['music'].lesson = 3
    $ classes['chemistry'].lesson = 3
    $ classes['gym'].lesson = 3
    $ Jimmy.stats['guts'] += 2
    $ classes['shop'].lesson = 3
    $ Jimmy.stats['endurance'] += 2
    $ classes['math'].lesson = 3
    $ Jimmy.stats['wits'] += 2
    $ Jones.met = True
    $ Matunga.met = True
    $ Marlon.met = True
    $ Earnest.met = True
    $ Melvin.met = True
    $ Algie.met = True
    $ Derek.met = True

    ######### MISS PUNNY ############
    $ quests.punnyPrivateLessons = COMPLETE
    $ quests.punnyDatingTeacher = COMPLETE

    ############# CHAPTER 3 ###########
    $ quests.artclassBook = COMPLETE
    $ Aurora.met = True
    $ quests.drunkblair = COMPLETE
    $ quests.bathtubclimax = COMPLETE
    $ quests.euniceGettingtherole = COMPLETE
    $ quests.euniceBoobytrap = COMPLETE
    $ quests.algieScroll = COMPLETE
    $ Eunice.met = True
    $ libraryeunicebookintro = True 
    $ quests.euniceTheaterpractice = COMPLETE
    $ quests.beatrixHomework = COMPLETE
    $ quests.beatrixHerpes = COMPLETE

    ############ RELATIONSHIP POINTS ############
    $ Antonella.relPoints += 1
    $ Audrey.relPoints += 1
    $ Barbara.relPoints += 3
    $ Sally.relPoints += 3
    $ Dakota.relPoints += 1
    $ Blair.relPoints += 1
    $ Cassidy.relPoints += 3
    $ Christy.relPoints += 2
    $ Eunice.relPoints += 2
    $ Fiona.relPoints += 4
    $ Miku.relPoints += 5
    $ Dawson.relPoints += 5
    $ Punny.relPoints += 4
    $ Violet.relPoints += 1
    $ Wendy.relPoints += 3

############################## LATEST CONTENT VARIABLE SETUP ###########################################
    $ quests.fionaDadTrouble = ACTIVE 
    return