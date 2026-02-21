# (name, description, iscompletecallback, setstatecallback)
init 1 python:
    def chapter1_freeroam_iscomplete():
        if quests.beatrixDiary != COMPLETE:
            return False
        if quests.fionaNightDate != COMPLETE:
            return False
        return True

    def chapter1_freeroam2_iscomplete():
        if quests.cassidyTrials != COMPLETE:
            return False
        if quests.mikuStorypartone != COMPLETE:
            return False
        if quests.euniceGettingtherole != COMPLETE:
            return False
        return True

    def chapter1_hallowenheist_iscomplete():
        if quests.missdawsonHalloweenStaff != COMPLETE:
            return False
        if quests.cassidyTrials != COMPLETE:
            return False
        if quests.mikuStorypartone != COMPLETE:
            return False
        if quests.garyHalloweenHeist != COMPLETE:
            return False
        return True

    main_objectives[None] = [
        # PROLOGUE
        ('ch0_finishintro',         "",                                                                     lambda: prologue.finishIntro,               ch0_finishintro_setstate       ),
        ('ch0_findjimmysroom',      "Find [player_name]'s dorm room",                                       lambda: prologue.findJimmysRoom,            ch0_findjimmysroom_setstate      ),
        ('ch0_firstnight',          "Go to sleep",                                                          lambda: prologue.firstNight,                ch0_firstnight_setstate      ),
        ('ch0_spanishclassintro',   "Change into your school uniform and head to Spanish class",            lambda: prologue.spanishIntro,              ch0_spanishclassintro_setstate      ),
        ('ch0_gymclassintro',       "Go to the Gym to meet Pete",                                           lambda: prologue.gymIntro,                  ch0_gymclassintro_setstate      ),
        ('ch0_secondnight',         "Go to sleep",                                                          lambda: prologue.secondNight,               ch0_secondnight_setstate      ),
        ('ch0_mathclassintro',      "Go to Math class",                                                     lambda: prologue.mathIntro,                 ch0_mathclassintro_setstate      ),
        ('ch0_shopclassintro',      "Go to the garage in the parking lot for Shop class",                   lambda: prologue.shopIntro,                 ch0_shopclassintro_setstate      ),
        ('ch0_mayorsspeech',        "Go the auditorium for the mayor's assembly",                           lambda: prologue.mayorsSpeech,              ch0_mayorsspeech_setstate      ),
        ('ch0_kassandraintro',      "Change out of your uniform and meet Kassandra at the front entrance",  lambda: prologue.kassandraIntro,            ch0_kassandraintro_setstate      ),
        ('ch0_blairusb',            "Get your USB from downstairs and finish setting up your PC",           lambda: quests.blairUSB == COMPLETE,        ch0_blairusb_setstate      ),
        ('ch0_awkwardbreakfast',    "Go downstairs for breakfast",                                          lambda: prologue.awkwardBreakfast,          ch0_awkwardbreakfast_setstate      ),
        ('ch0_visitthebeach',       "Go out to the beach to check for ways to get into the mansion.",       lambda: prologue.visitthebeach,               ),
        ('ch0_checkthecliff',       "Check the cliff near the mansion.",                                    lambda: prologue.checkthecliff,               ),
        ('ch0_findarope',           "Find something to fix the stair in the house.",                        lambda: prologue.findtherope,                 ),
        ('ch0_dakotajoboffer',      "Go see what Kassandra wants in the kitchen",                           lambda: prologue.dakotaJobOffer,            ch0_dakotajoboffer_setstate      ),
        ('ch0_afternoonnap',        "Take a nap until midnight.",                                           lambda: prologue.afternoonNap,              ch0_afternoonnap_setstate      ),
        ('ch0_townhousecaught',     "Find a way to sneak out of the house without anyone noticing",         lambda: quests.cassidyDildo >= ACTIVE,      ch0_townhousecaught_setstate      ),
        ('ch0_findcassidysdildo',   "Find and return Cassidy's \"toy\"",                                    lambda: quests.cassidyDildo == COMPLETE,    ch0_findcassidysdildo_setstate      ),
        ('ch0_cassidypeephole',     "Check to make sure Cassidy is asleep {i}*wink, wink*{/i}",             lambda: prologue.cassidyPeephole,           ch0_cassidypeephole_setstate      ),
        ('ch0_townhousesneak',      "Sneak out of the house now that Cassidy is asleep",                    lambda: prologue.sneakOutTownhouse,         ch0_townhousesneak_setstate      ),
        ('ch0_wendysroom',          "Find a way into Wendy's room",                                         lambda: quests.grantHoboBag >= ACTIVE,      ch0_wendysroom_setstate      ),
        ('ch0_grantsbagfetch',      "Sneak into Jillian's office on the second floor to retrieve Grant's bag", lambda: quests.grantHoboBag >= SATISFIED,ch0_grantsbagfetch_setstate  ),
        ('ch0_grantsbagreturn',     "Give Grant his bag",                                                   lambda: quests.grantHoboBag == COMPLETE,    ch0_grantsbagreturn_setstate  ),
        ('ch0_dakotaranchintro',    "Go to sleep",                                                          lambda: prologue.dakotaRanchIntro,          ch0_dakotaranchintro_setstate  ),
        ('ch0_ranchminigameintro',  "Meet Dakota in the barn so you can start working",                     lambda: prologue.ranchMinigameIntro,        ch0_ranchminigameintro_setstate  ),
        ('ch0_barbarasallystrapon', "Investigate the noises coming from the shed",                          lambda: prologue.barbaraSallyStrapon,       ch0_barbarasallystrapon_setstate  ),
        ('ch0_takeshower',          "Take a shower",                                                        lambda: prologue.cassidyShower,             ch0_takeshower_setstate  ),
        ('ch0_endofprologue',       "Go to sleep",                                                          lambda: prologue.complete,                  ch0_endofprologue_setstate  ),
        # CHAPTER 1
        ('ch1_introcutscene',       "",                                                                     lambda: chapter1.introCutscene,             ch1_introcutscene_setstate  ),
        ('ch1_freeroam',            "Complete quests for Fiona and Beatrix",                                chapter1_freeroam_iscomplete,               ch1_freeroam_setstate  ),
        ('ch1_halloweenheist',      "Talk to Pete at the Boys Dorm",                                        lambda: quests.garyHalloweenHeist >= ACTIVE,  ),
        ('ch1_halloweenheist',      "Look for spray paint at the Junkyard",                                 lambda: quests.garyHalloweenHeist >= SATISFIED,  ),
        ('ch1_halloweenheist',      "Complete quests for Cassidy, Miku and Eunice",                         chapter1_freeroam2_iscomplete,                ),
        ('ch1_halloweeninvitation', "Get an invitation to the Halloween party",                             lambda: quests.missdawsonHalloweenStaff == COMPLETE,),
        ('ch1_fionahalloweenintro', "Talk to Fiona",                                                        lambda: quests.halloweenCostume >= ACTIVE,  ch1_fionahalloweenintro_setstate  ),
        ('ch1_halloweencostume',    "Buy a Halloween costume from Fiona",                                   lambda: quests.garyHalloweenHeist >= COMPLETE, ch1_halloweencostume_setstate ),
        ('ch1_halloweenevent',      "Change into your costume for the Halloween party",                     lambda: glob.halloweenEventComplete,        ch1_halloweenevent_setstate  ),
        # CHAPTER 2
        ('ch1_nerdsintro',                 "Go to the library and talk to the Nerds",                       lambda: quests.algieScroll >= ACTIVE,         ),
        ('ch1_algiescrollquest_active',    "Find Algie's scroll in a bathroom (Main building)",             lambda: quests.algieScroll >= SATISFIED,      ),
        ('ch1_algiescrollquest_satisfied', "Bring the Scroll of The Ancients to Algie",                     lambda: quests.algieScroll == COMPLETE,       ),
        ('ch2_buckyrescue_locked',         "Go to the Boysdorm TV Room",                                    lambda: quests.rescueBucky >= ACTIVE          ),
        ('ch2_buckyrescue_active',         "Go to the Junkyard",                                            lambda: quests.rescueBucky >= SATISFIED       ),
        ('ch2_buckyrescue_satisfied',      "Find the Parts to Create the Slingshot",                        lambda: quests.slingshotcraft == COMPLETE     ),
        ('ch2_buckyrescue_complete',       "Rescue Bucky from the Bullies at the Junkyard",                 lambda: quests.rescueBucky == COMPLETE        ),
        ('ch2_beatrix_complete',           "Help Beatrix with her Biology Essay",                           lambda: quests.beatrixHerpes == COMPLETE),
        ('ch2_RPGCampaign_locked',         "Go to the Nerds HQ",                                            lambda: quests.beatrixGetlaid >= SATISFIED    ),
        ('ch2_RPGCampaign_active',         "Deliver the crown to finish the RPG Campaign (Extended Edition)",lambda: quests.RPGcampaign >= ACTIVE          ),
        ('ch2_RPGCampaign_satisfied',      "Help the Order of Fellation save the city",                     lambda: quests.RPGcampaign >= SATISFIED       ),
        ('ch2_RPGCampaign_complete',       "Defeat Derek once and for all",                                 lambda: quests.RPGcampaign == COMPLETE        ),
        ('endofcontent',                   "{i}More story content coming soon{/i}",                         lambda: False, lambda: None                   )
        #('', "", lambda: , ),
    ]

    side_objectives[None] = {
        'alice': [
            #('', "", lambda: ),
        ],
        'antonella': [
            #('', "", lambda: ),
        ],
        'audrey': [
            #('', "", lambda: ),
        ],
        'aurora': [
            ('meet', "Attend art class for the first time", lambda: quests.artclassBook >= ACTIVE),
            ('booksearch_active', "Go to the Library to search the book", lambda: quests.artclassBook >= SATISFIED),
            ('booksearch_satisfied', "Go to the Art classroom to deliver the book", lambda: quests.artclassBook == COMPLETE),
            ('gettingtherole_locked', "Talk to Eunice at the Parking Lot", lambda: quests.euniceGettingtherole >= ACTIVE),
            ('sirlaughsalot_active', "Talk to Miss Bakshi about Eunice's role", lambda: quests.bakshiSirlaughsalot >= ACTIVE),
            ('sirlaughsalot_complete', "Find Sir Laughsalot", lambda: quests.bakshiSirlaughsalot == COMPLETE),
            #('', "", lambda: ),
        ],
        'barbara': [
            #('', "", lambda: ),
        ],
        'beatrix': [
            ('diary_locked', "Talk to her outside the Math classroom", lambda: quests.beatrixDiary >= ACTIVE),
            ('diary_fiona_unmet', "Find a way into the girl's dorm", lambda: Fiona.met),
            ('diary_active', "Convince Fiona to help you get into the girl's dorm", lambda: quests.beatrixDiary >= SATISFIED),
            ('diary_satisfied', "Give her back her \"math notes\"", lambda: quests.beatrixDiary == COMPLETE),
            ('homework_locked', "Complete the Halloween Event", lambda: glob.halloweenEventComplete),
            ('homework_satisfied', "Talk to her outside the Math Classroom", lambda: quests.beatrixHomework >= SATISFIED),
            ('herpes_locked', "Complete some missions for the Nerds", lambda: quests.algieScroll == COMPLETE),
            ('homework_complete', "Talk to Melvin about his Herpes problem", lambda: quests.beatrixHomework == COMPLETE),
            ('herpes_active', "Go to the Biology Lab", lambda: quests.beatrixHerpes >= ACTIVE),
            ('herpes_satisfied', "Go to the Infirmary (2nd floor Left - Main Building)", lambda: quests.beatrixHerpes >= SATISFIED),
            ('herpes_complete', "Give the Medicine to Beatrix at the Biology Lab", lambda: quests.beatrixHerpes == COMPLETE),
            ('getlaid_active', "Rescue Bucky from the Bullies (Nerd's Quest)", lambda: quests.beatrixGetlaid >= ACTIVE),
            ('getlaid_satisfied', "Talk to her at the Nerds HQ", lambda: quests.beatrixGetlaid >= SATISFIED),
            ('getlaid_complete', "Complete the RPG Campaign with the Nerds (Extended Edition)", lambda: quests.beatrixGetlaid == COMPLETE),
            #('', "", lambda: ),
        ],
        'blair': [
            ('drunkblair_locked', "Complete the Halloween Event", lambda: glob.halloweenEventComplete),
            ('drunkblair_active', "Go to your town house on the weekend", lambda: quests.drunkblair >= SATISFIED),
            ('drunkblair_satisfied', "Go to bed at night", lambda: quests.drunkblair == COMPLETE),
            #('', "", lambda: ),
        ],
        'cassidy': [
            ('cassidyquests_locked', "Complete Beatrix's Diary quest", lambda: quests.beatrixDiary == COMPLETE),
            ('cassidytrials_locked', "Go to the Gym", lambda: quests.cassidyTrials >= ACTIVE),
            ('cassidytrials_active', "Go to the Library Plaza", lambda: quests.cassidyTrials >= SATISFIED),
            ('cassidytrials_satisfied', "Talk to Cassidy in her room during the weekend at Night", lambda: quests.cassidyTrials >= COMPLETE),
            ('firstfuck_locked', "Complete the Halloween Event (Shaggy's costume)", lambda: quests.cassidyFirstFuck >= ACTIVE),
            ('firstfuck_active', "Go to the boys locker room at the Gym", lambda: quests.cassidyFirstFuck >= SATISFIED),
            ('firstfuck_satisfied', "Talk to Cassidy in her room during the weekend at Night", lambda: quests.cassidyFirstFuck == COMPLETE),
            #('', "", lambda: ),
        ],
        'christy': [
            ('christyplan_locked', "Complete the Halloween event", lambda: quests.christyPlan >= ACTIVE),
            ('christyplan_active', "Go to the boys locker room at the Gym", lambda: quests.christyPlan >= SATISFIED),
            ('christyplan_satisfied', "Talk to Cassidy in her room during the weekend at Night", lambda: quests.christyPlan == COMPLETE),
        ],
        'clarissa': [
            #('', "", lambda: ),
        ],
        'dakota': [
            #('', "", lambda: ),
        ],
        'eunice': [
            ('chocolates_locked', "Meet her in the cafeteria", lambda: Eunice.met),
            ('gettingtherole_locked', "Talk to her at the Parking Lot", lambda: quests.euniceGettingtherole >= ACTIVE),
            ('gettingtherole_miku', "Go to Art Class and help Miku with her Art Project", lambda: quests.artProject >= COMPLETE),
            ('gettingtherole_active', "Talk to Miss Bakshi in the Art Classroom", lambda: quests.euniceGettingtherole >= SATISFIED),
            ('gettingtherole_satisfied', "Find Sir Laughsalot, investigate the Auditorium backstage", lambda: quests.euniceGettingtherole >= COMPLETE),
            ('gettingtherole_complete', "Complete the Halloween Event", lambda: glob.halloweenEventComplete),
            ('boobytrap_locked', "Talk to Algie at the Library", lambda: quests.euniceBoobytrap >= ACTIVE),
            ('boobytrap_complete', "Meet her in the Gym storage room in the Evening", lambda: quests.euniceBoobytrap == COMPLETE),
            ('theaterpractice_locked', "Go to the Art Classroom", lambda: quests.euniceTheaterpractice >= ACTIVE),
            ('theaterpractice_active', "Go to the Library and ask Miku about the book", lambda: libraryeunicebookintro == True),
            ('theaterpractice_satisfied', "Bring the right book to the Art Classroom", lambda: quests.euniceTheaterpractice >= SATISFIED),
            ('theaterpractice_complete', "Go to the Auditorium during the Evening", lambda: quests.euniceTheaterpractice == COMPLETE),
            #('', "", lambda: ),
        ],
        'fiona': [
            ('meet', "Meet her at the kiosk in front of the girl's dorm", lambda: quests.fionaPadlock >= ACTIVE),
            ('padlock_active', "Find the padlock Derek stole from her", lambda: quests.fionaPadlock >= SATISFIED),
            ('padlock_satisfied', "Return the padlock to her", lambda: quests.fionaPadlock == COMPLETE),
            ('derek_locked', "Talk to her at the kiosk", lambda: quests.fionaConfrontDerek >= ACTIVE),
            ('derek_active', "Find Derek and make sure he stops bothering her", lambda: quests.fionaConfrontDerek >= SATISFIED),
            ('derek_satisfied', "Find Fiona's stolen goods", lambda: quests.fionaConfrontDerek == COMPLETE),
            ('nightdate_locked', "Go to the beach on Saturday evening", lambda: quests.fionaNightDate >= ACTIVE),
            ('nightdate_active', "Get some ice from the Tiki bar", lambda: quests.fionaNightDate >= SATISFIED),
            ('dadtrouble_locked', "Complete the Halloween Event", lambda: glob.halloweenEventComplete),
            ('dadtrouble_active', "Talk to Fiona at her kiosk", lambda: quests.fionaDadTrouble >= SATISFIED),
            ('dadtrouble_satisfied', "Get the key from Miss Dawson", lambda: quests.missdawsonAssistant == COMPLETE),
            ('dadtrouble_complete', "Hide inside Fiona's kiosk until Night time", lambda: quests.fionaDadTrouble == COMPLETE),
            #('', "", lambda: ),
        ],
        'jill': [
            #('', "", lambda: ),
        ],
        'kassandra': [
            ('bathtubclimax_locked', "Complete the Halloween Event", lambda: glob.halloweenEventComplete),
            ('bathtubclimax_active', "Go to the town house on the weekend", lambda: quests.bathtubclimax >= ACTIVE),
            ('bathtubclimax_satisfied', "Talk to Kassandra in the backyard", lambda: quests.bathtubclimax >= SATISFIED),
            ('bathtubclimax_complete', "At night, go downstairs and take a peek at Kassandra's door", lambda: quests.bathtubclimax == COMPLETE),
            #('', "", lambda: ),
        ],
        'lola': [
            #('', "", lambda: ),
        ],
        'mandy': [
            #('', "", lambda: ),
        ],
        'miku': [
            ('meet', "Meet her in the library", lambda: Miku.met),
            ('artproject_locked', "Go to Art Class and approve the 1st lesson", lambda: quests.artProject >= ACTIVE),
            ('artproject_active', "Meet Miku at the front of the Town House for the Art project", lambda: quests.artProject >= SATISFIED),
            ('artproject_satisfied', "Go to the backyard to finish the Art project", lambda: quests.artProject >= COMPLETE),
            ('photoshoot_active', "Save up enough money to purchase a camera for Miku", lambda: quests.mikuPhotoShoot >= SATISFIED),
            ('photoshoot_satisfied', "Show her the camera you bought", lambda: quests.mikuPhotoShoot == COMPLETE),
            ('photoshoot_complete', "Talk to her in the library archive at evening", lambda: quests.mikuStorypartone == COMPLETE),
            ('mikuhalloween_complete', "Complete the Halloween Event", lambda: glob.halloweenEventComplete),
            ('theaterpracticem_locked', "Go to the Art Classroom", lambda: quests.euniceTheaterpractice >= ACTIVE),
            ('theaterpracticem_active', "Go to the Library and ask Miku about the book", lambda: quests.euniceTheaterpractice >= SATISFIED),
            ('theaterpracticem_complete', "Go to the Auditorium during the Evening", lambda: quests.euniceTheaterpractice == COMPLETE),
            #('', "", lambda: ),
        ],
        'missdawson': [
            ('headmasterspy', "Visit the headmaster's office", lambda: quests.headmasterSpy == COMPLETE),
            ('bathroomincident_active', "Go to the Cafeteria hallway", lambda: quests.missdawsonBathroomIncident >= ACTIVE), 
            ('bathroomincident_complete', "Give the notice to Miss Dawson at her office", lambda: quests.missdawsonBathroomIncident == COMPLETE),
            ('assistant_locked', "Talk to Miss Dawson during office hours", lambda: quests.missdawsonAssistant >= ACTIVE),
            ('assistant_edna', "Give the notice to the Cafeteria manager", lambda: quests.missdawsonAssistantEdna == COMPLETE),
            ('assistant_marlon', "Give the notice to the Concierge", lambda: quests.missdawsonAssistantMarlon == COMPLETE),
            ('titshow', "Deliver the news to Miss Dawson", lambda: quests.missdawsonTitShow == COMPLETE),
            ('assistant_active', "Talk to Miss Dawson during office hours", lambda: quests.missdawsonAssistant >= SATISFIED),
            ('halloweenstaff_aurora', "Ask the Art Class teacher about the reunion", lambda: quests.missdawsonHalloweenAurora == COMPLETE),
            ('halloweenstaff_audrey', "Ask the Shop Class teacher about the reunion", lambda: quests.missdawsonHalloweenAudrey == COMPLETE),
            ('halloweenstaff_camembert', "Ask the Math Class teacher about the reunion", lambda: quests.missdawsonHalloweenCamembert == COMPLETE),
            ('assistant_complete', "Deliver the news to Miss Dawson", lambda: quests.missdawsonAssistant == COMPLETE),
            ('halloweenstaff_active', "Talk to Miss Dawson to start the Halloween Reunion", lambda: quests.missdawsonHalloweenStaff >= ACTIVE),
            ('halloweenstaff_complete', "Discover who is Miss Dawson's secret ghost", lambda: quests.missdawsonHalloweenStaff == COMPLETE),
            #('', "", lambda: ),
        ],
        'missjones': [
            ('meet', "Attend geography class for the first time", lambda: Jones.met),
            #('', "", lambda: ),
        ],
        'misspunny': [
            ('privatelessons_locked', "Complete Spanish class 2nd lesson", lambda: quests.punnyPrivateLessons >= ACTIVE),
            ('privatelessons_active', "Pay 100$ for the 1st private lesson", lambda: quests.punnyPrivateLessons >= SATISFIED),
            ('privatelessons_satisfied', "Go to the Auditorium on Friday at evening", lambda: quests.punnyPrivateLessons >= COMPLETE),
            ('punnyhalloween_complete', "Complete the Halloween Event", lambda: glob.halloweenEventComplete),
            ('datingtheteacher_locked', "Pay 100$ for the 2nd private lesson", lambda: quests.punnyDatingTeacher >= ACTIVE),
            ('datingtheteacher_active', "Go to Miss Punny's house at night", lambda: quests.punnyDatingTeacher >= SATISFIED),
            ('datingtheteacher_satisfied', "Talk to Miss Punny in her classroom", lambda: quests.punnyDatingTeacher >= COMPLETE),
            #('', "", lambda: ),
        ],
        'ruby': [
            #('', "", lambda: ),
        ],
        'sally': [
            #('', "", lambda: ),
        ],
        'tatiana': [
            #('', "", lambda: ),
        ],
        'violet': [
            #('', "", lambda: ),
        ],
        'wendy': [
            #('', "", lambda: ),
        ],
    }
