#VARIABLES
default quests.fionaPadlock = LOCKED
default quests.fionaConfrontDerek = LOCKED
default quests.fionaNightDate = LOCKED
default quests.fionaBartender = LOCKED
default quests.fionaDadTrouble = LOCKED
default quests.fionakioskintro = LOCKED

default fiona.beatrixDiaryIntro = False

#LABELS
label fionadialogue:
    hide screen freeroamhud with None
    play music MUSIC_FIONAS_THEME
    if FionaDaylimit == True:
        hide fionakioskdialogbutton with dissolve
        show fiona clerk neutral with dissolve
        Fiona "[player_name]! I'm a little busy right now."
        Fiona "Another time, maybe."
        $ gotoscene('girlsdormfrontgate')
    $ objective = getSideObjective('fiona', keyOnly=True)
    if quests.fionaPadlock == LOCKED:
        jump chapterone_fionaintro
    elif objective == 'derek_locked':
        jump fionaconfrontderekquest
    elif objective == 'nightdate_locked':
        jump fionanightdatequest
    elif getMainObjective()[0] == 'ch1_fionahalloweenintro':
        jump chapterone_fionahalloweenintro
    elif objective == 'dadtrouble_active':
        jump fionadadtroublequest
    hide fionakioskdialogbutton with dissolve
    show fiona clerk neutral with dissolve
    Fiona "Hey [player_name], what's up?"
    jump .dialogmenu

label .dialogmenu:
    menu:
        "Reset Dad Revenge Quest (v0.5.4)" if quests.fionaDadTrouble == COMPLETE:
            $ quests.fionaDadTrouble = ACTIVE
            $ quest.fionaheadmastertalk = False
            $ prefectpass = False
            $ fionaLoveYou = False
            call item_pickup(ItemHeadmasterKey) from _call_item_pickup_42
            $ Fiona.relPoints -= 2
            jump fionadadtroublequest
        "Headmaster Keys" if quests.fionaDadTrouble == SATISFIED:
            jump fionadadtroublequest
        "Beatrix's diary" if quests.fionaNightDate == COMPLETE and quests.beatrixDiary == ACTIVE:
            jump .beatrixdiary_dialogue
        "Padlock" if quests.fionaPadlock in [ACTIVE, SATISFIED]:
            jump fionapadlockquest
        "Derek" if quests.fionaConfrontDerek in [ACTIVE, SATISFIED]:
            jump fionaconfrontderekquest
        "Night date" if quests.fionaNightDate == ACTIVE:
            jump fionanightdatequest
        "Nevermind":
            pass
    $ gotoscene('girlsdormfrontgate')

label .beatrixdiary_dialogue:
    if not fiona.beatrixDiaryIntro:
        Jimmy "Fiona, I know this is going to sound a bit crazy, but I need to get into the girls' dorm."
        Fiona "What?! Why?"
        Jimmy "I'm trying to help a friend find something that was stolen from her."
        Fiona "But you can't just enter the girls' dorms like that..."
        Jimmy "I know, but I promise my intentions are good."
        Jimmy "I need you to trust me on this one."
        Jimmy "I'm just going to try to get a stolen book and get out as fast as possible."
        Fiona "Oh, [player_name]. Alright, I trust you."
    else:
        Jimmy "Can you help me get into the girls' dorm now?"
    if quests.fionaPadlock != COMPLETE:
        if not fiona.beatrixDiaryIntro:
            Fiona "I don't know, [player_name]. I only just met you."
            Jimmy "If I get you your padlock, will that prove you can trust me?"
            Fiona "Hmmm... Maybe."
            Jimmy "Great, I'm on it."
            $ fiona.beatrixDiaryIntro = True
            $ gotoscene('girlsdormfrontgate')
        else:
            Fiona "Find my padlock first and then maybe."
    else:
        Fiona "Here, I'll open the gate for you, but you can't enter through the main door or someone will catch you."
        Jimmy "Crap, is there any other way I can get in?"
        Fiona "Well, there is a structure on the back of the building that can get you to the attic if you know how to climb."
        Jimmy "Oh, I can do that. "
        Jimmy "Thank you so much, Fiona. I'll make it up to you!"
        Fiona "Just promise me you'll do your stuff fast, okay?"
        Jimmy "I promise."
        jump chapterone_girlsdormsneak
    jump .dialogmenu

#HALLOWEEN
default fiona.bartenderIntro = False

label chapterone_fionahalloweenintro:
    hide fionakioskdialogbutton
    show fiona clerk neutral with dissolve
    Fiona "Hey [player_name]!"
    Fiona "Good to see you!"
    Jimmy "Likewise!"
    Fiona happy "Are you going to the Halloween party at Harrison House?"
    Jimmy "Harrison House?"
    Fiona "It's the mansion at the base of Observatory Hill."
    Jimmy "Oh, fancy."
    Fiona "I'm so excited. I love Halloween. You should come!"
    Fiona "You need a costume? Here, come with me."
    $ oldItems = fionasKioskItems
    $ fionasKioskItems = [ItemShaggyCostume, ItemPirateCostume, ItemHeroCostume]
    call fionaskiosk_showscene from _call_fionaskiosk_showscene_1
    $ fionasKioskItems += oldItems
    Fiona "It's a costume party, so you'll need a one if you want to get in."
    Fiona "I'm selling some if you need one."
    Fiona "Special prices for my man."
    Jimmy "Thanks, I'll take a look."
    Fiona "Great! I really hope you go to the party so we can have some fun away from prying eyes..."
    Fiona "And speaking about that..."
    Fiona "I can't stop thinking about your dick, [player_name]."
    Jimmy "Oh, baby, I can't stop thinking about your pussy either."
    Fiona "Gosh, I don't have much time now, but... I really wanted you to come."
    Jimmy "Well, I'm here, babe."
    play sound "audio/sfx/giggle01.ogg"
    Fiona "Ah, fuck it."
    Fiona aroused tits "Come on, I want to see your cock." with vpunch
    Jimmy "Okay..."
    call fiona_kioskblowjob_scene from _call_fiona_kioskblowjob_scene_1
    scene fionastoreshelf with fade
    show fiona clerk tits cum with dissolve
    play music MUSIC_FIONAS_THEME
    play sound "audio/sfx/wow01.ogg"
    Fiona "Wow, that was really fun..."
    Jimmy "Oh, yeah, I loved it."
    Fiona "I'm gonna get cleaned now."
    Fiona "Remember I have those costumes available, [player_name]."
    Fiona "See you around!"
    $ quests.halloweenCostume = ACTIVE
    $ gotoscene('girlsdormfrontgate')

label fionahalloweendialogue:
    hide screen freeroamhud with None
    if not fiona.bartenderIntro:
        jump halloween_fionabartenderintro
    show fiona waldo neutral
    with dissolve
    play sound "audio/sfx/hey02.ogg"
    Fiona "Hey [player_name]. Can I get you anything?"
    jump .dialogmenu

label .dialogmenu:
    menu:
        "Ask about the drinks" if quests.fionaBartender != COMPLETE:
            Jimmy "You know, I've been wondering what these kind of people drink."
            Jimmy "I mean, the people who live in a place like this."
            Fiona "Oh, well. They usually like cocktails with fruit juice or something sweet."
            Fiona "But, to make my job easier, I made a bowl full of a special Fruit Punch."
            Fiona "Though, I recommend you drink something more traditional if you want to get hammered."
            Fiona "This thing is really soft."
            Jimmy "Umm, okay. Thanks for the tip."
            $ quests.halloweenFruitPunch = SATISFIED
            jump .dialogmenu
        "Ask for a drink for Beatrix" if quests.beatrixAppleCider == ACTIVE:
            Jimmy "Do you have anything without alcohol?"
            Fiona "Hmm, short answer, no."
            Fiona "Water? Maybe?"
            Fiona "At this point, I think even the water has alcohol."
            Jimmy "Nah, I'm looking for a fruit juice or something like that."
            Fiona "Sorry, I don't have anything left. Used everything on the cocktails."
            Jimmy "Alright, no worries."
            jump .dialogmenu
        "Hang out" if quests.fionaBartender == LOCKED:
            jump fionabartenderquest
        "Nevermind":
            $ gotoscene('harrisonhousebar')