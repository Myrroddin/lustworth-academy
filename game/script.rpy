define config.layers = ['master', 'cutscene', 'transient', 'screens', 'overlay']
default save_version = 'v0.40.5'

default persistent.sexscenes = set()
default persistent.metGirls = set()
default galleryMode = False

init -1 python:
    import pygame

    def _scale(*args):
        if len(args) == 0:
            return
        scale = config.screen_width / 1920
        if len(args) == 1:
            return round(args[0] * scale)
        return tuple(round(x * scale) for x in args)

#NEW VARIABLES (TEMPORARY)
default quick_menu = True
define derbylaptopfound = False
default jimmynewuniform = False
default gallerymainmenu = False

#CONSTANTS
# Strings
define DAY_STRINGS  = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']
define TIME_STRINGS = ['morning', 'afternoon', 'evening', 'night']
# Chapters
define PROLOGUE  = 0
define CHAPTER_1 = 1
define CHAPTER_2 = 2
define CHAPTER_3 = 3
# Days
define MONDAY    = 1
define TUESDAY   = 2
define WEDNESDAY = 3
define THURSDAY  = 4
define FRIDAY    = 5
define SATURDAY  = 6
define SUNDAY    = 7
# Times
define MORNING   = 1
define AFTERNOON = 2
define EVENING   = 3
define NIGHT     = 4
# Quest states
define LOCKED    =  0  # the quest has not yet been received
define ACTIVE    =  1  # the quest has been started
define SATISFIED =  2  # the quest's requirements have been met
define COMPLETE  =  3  # the quest has been turned in
define FAILED    = -1  # the quest was failed and cannot be completed
# Events
define HALLOWEEN_EVENT   = 'halloween'
define CHRISTMAS_EVENT   = 'christmas'
define SPRINGBREAK_EVENT = 'springbreak'
# Outfits
define JIMMY_DEFAULT = 'casual'
define JIMMY_UNIFORM = 'uniform'
define JIMMY_STEALTH = 'stealth'
define JIMMY_SHAGGY  = 'shaggy'
define JIMMY_PIRATE  = 'pirate'
define JIMMY_HOMELANDER  = 'homelander'

#VARIABLES
default classes = {
    'geography': Subject(Jones,     (), MUSIC_GEOGRAPHY_CLASS),
    'biology':   Subject(DrLed,     (), MUSIC_BIOLOGY_CLASS),
    'art':       Subject(Aurora,    'charisma', MUSIC_ART_CLASS),
    'music':     Subject(Dewey,     (), MUSIC_MUSIC_CLASS),
    'chemistry': Subject(Argon,     (), None),
    'astronomy': Subject(Dyson,     (), None),
    'spanish':   Subject(Punny,     (), MUSIC_SPANISH_CLASS),
    'gym':       Subject(Toord,     'guts', None),
    'math':      Subject(Camembert, 'wits', None),
    'shop':      Subject(Audrey,    'endurance', None),
}
define class_max_lessons = {
    'geography': 2,
    'biology':   2,
    'art':       2,
    'music':     2,
    'chemistry': 2,
    'astronomy': 1,
    'spanish':   2,
    'gym':       2,
    'math':      2,
    'shop':      2,
}
# Global
default glob.plannerUnlocked = False
default glob.walletUnlocked = False
default glob.mapUnlocked = False
default glob.halloweenEventComplete = False
# Scene management
default scenemanager.scene = None
default scenemanager.sceneGround = None
default scenemanager.sceneHover = None
default scenemanager.bgMusic = None
default inclass = False
# Calendar
default calendar.when = (0, 0, 0) # (Chapter, Day, Time)
default calendar.season = 'fall'
default calendar.dayNum = 0
default calendar.event = None
# Quests
default quests.cassidyDildo = LOCKED
default quests.grantHoboBag = LOCKED
default quests.blairUSB = LOCKED
default quests.halloweenCostume = LOCKED
default quests.halloweenFruitPunch = LOCKED
default quests.halloweenFakeFlag = LOCKED
default quests.halloweenGraffitiMessage = LOCKED

#LABELS
# Entry point
label start:
    scene adultwarning with fade
    pause 2.0
    call namesigning from _call_namesigning
    menu:
        __("Play new content v0.5.4"):
            call housematesnaming from _call_housematesnaming
            call newcontentvariablecheck from _call_newcontentvariablecheck
            $ Jimmy.outfit = JIMMY_UNIFORM
            $ calendar.when = (CHAPTER_3, MONDAY, MORNING)
            $ newcontentskipactive = True
            $ showscene('boysdormhallway', transition=fade)
            Jimmy __("So, what am I doing here?")
            Jimmy __("Right, I gotta go talk to Pete at the TV room.")
            $ gotoscene('boysdormhallway')
        __("Continue New Game"):
            jump prologue_intro

label namesigning:
    stop music
    scene namesigning01 with fade
    __("{i}What's your name, new guy?{/i}")
    $ player_name = renpy.input(__("First name (default: Jimmy)"))
    $ player_name = player_name.strip()
    if player_name == '':
        $ player_name = "Jimmy"
    play sound "audio/sfx/signature01.ogg"
    scene namesigning02 with dissolve
    $ player_surname = renpy.input(__("Last name (default: Napkins)"))
    $ player_surname = player_surname.strip()
    if player_surname == '':
        $ player_surname = "Napkins"
    play sound "audio/sfx/signature02.ogg"
    scene namesigning03 with dissolve
    __("{i}Welcome to Trustworth, [player_name] [player_surname].{/i}")
    return

label housematesnaming:
    play music "audio/music/happyrock01.ogg"
    scene jimmytownhouseday with fade
    __("{i}Before we get started, I need to introduce you to a few characters.{i}")
    # Kassandra
    show kassandra neutral with dissolve
    __("{i}This is Kassandra. You live with her on the weekends.{/i}")
    $ landlady_name = renpy.input(__("Kassandra is your... (default: landlady)"))
    $ landlady_name = landlady_name.strip()
    if landlady_name == "":
        $ landlady_name = "landlady"
    # Cassidy/Blair/Alice
    hide kassandra with dissolve
    show cassidy pajama neutral
    show blair roommate intro
    show alice roommate intro
    with dissolve
    __("{i}These are Kassandra's daughters, Cassidy, Blair, and Alice.{/i}")
    $ roommate_female = renpy.input(__("Cassidy/Blair/Alice is your... (default: roommate)"))
    $ roommate_female = roommate_female.strip()
    if roommate_female == "":
        $ roommate_female = "roommate"
    $ roommate_male = renpy.input(__("And you are their... (default: roommate)"))
    $ roommate_male = roommate_male.strip()
    if roommate_male == "":
        $ roommate_male = "roommate"
    hide cassidy
    hide blair
    hide alice
    with dissolve
    __("{i}Alright, thanks. Now, on with the show!{/i}")
    return

label halloweencostumeselection:
    stop music
    $ fionasKioskItems += [ItemShaggyCostume, ItemPirateCostume, ItemHeroCostume]
    show screen freeroamhud(showTray=False)
    call fionaskiosk_showscene from _call_fionaskiosk_showscene
    __("What costume do you want to wear to the party?")
    call screen fionaskiosk(halloweenSkip=True)
    $ item = _return
    call fionaskiosk_onclick(item) from _call_fionaskiosk_onclick
    if item == ItemShaggyCostume:
        $ Jimmy.outfit = JIMMY_SHAGGY
    elif item == ItemPirateCostume:
        $ Jimmy.outfit = JIMMY_PIRATE
    elif item == ItemHeroCostume:
        $ Jimmy.outfit = JIMMY_HOMELANDER
    return

#MONEY
label yougotmoney:
    play sound "audio/sfx/purchasesound.ogg"
    show screen money_pickup with dissolve
    pause 1.5
    hide screen money_pickup with dissolve
    return

screen money_pickup:
    fixed:
        xysize 700, 480
        xalign 0.5
        yanchor 0.5
        ypos 0.45

        # add Solid('#000b')
        add Frame('gui/nvl.webp', Borders(0, 0, 0, 0))

        $ img = Transform('images/sprites/inventory/money01_sprite.webp', zoom=1.5)
        add img:
            xalign 0.5
            yanchor 0.5
            ypos 0.37

        $ msg = __("You got money!")
        text msg:
            style 'item_pickup_text'
            yoffset -40

#SCRIPTS
label nexttime:
    $ renpy.pause()
    $ chapter, day, time = calendar.when
    # intentionally not supporting rollover from night
    # to morning; nextday should be used instead
    if time < 4:
        $ time += 1
    $ calendar.when = (chapter, day, time)
    return

label nextday:
    $ chapter, day, time = calendar.when
    $ day = day % 7 + 1
    $ calendar.when = (chapter, day, MORNING)
    # $ calendar.dayNum += 1
    return

label nextchapter:
    $ chapter, day, time = calendar.when
    $ chapter += 1
    $ calendar.when = (chapter, day, time)
    return

label nap(until):
    hide screen freeroamhud
    stop music
    scene black with fade
    pause 0.6
    $ current = calendar.when[2]
    # Kinda ugly but no for loops
    if until - current >= 3:
        call nexttime from _call_nexttime
    if until - current >= 2:
        call nexttime from _call_nexttime_1
    call nexttime from _call_nexttime_2
    return

label nap_menu:
    $ scene = scenemanager.scene
    menu:
        __("How long should I rest?")

        __("Afternoon") if time < AFTERNOON:
            call nap(AFTERNOON) from _call_nap
        __("Evening") if time < EVENING:
            call nap(EVENING) from _call_nap_1
        __("Night") if time < NIGHT:
            call nap(NIGHT) from _call_nap_2
        __("Nevermind"):
            jump expression (scene + '_bed')
    $ gotoscene(scene, transition=fade)

label sleep(comment=None):
    if quests.mikuPhotoShoot == COMPLETE:
        $ miku.nextdayflag01 = True
    call chardaylimitreset from _call_chardaylimitreset
    hide screen freeroamhud
    $ renpy.say(None, comment if comment is not None else __("Time to hit the sack."))
    stop music
    scene nightsky with fade
    pause 0.8
    call nextday from _call_nextday
    return

# Save compatibility
init python:
    def v0_30_1_saveupdate():
        # De-coupled prologue objectives from the calendar
        prologue.firstNight = calendar.when > (PROLOGUE, WEDNESDAY, NIGHT)
        prologue.spanishIntro = calendar.when > (PROLOGUE, THURSDAY, MORNING)
        prologue.gymIntro = calendar.when > (PROLOGUE, THURSDAY, AFTERNOON)
        prologue.secondNight = calendar.when > (PROLOGUE, THURSDAY, NIGHT)
        prologue.mathIntro = calendar.when > (PROLOGUE, FRIDAY, MORNING)
        prologue.shopIntro = calendar.when > (PROLOGUE, FRIDAY, AFTERNOON)
        prologue.afternoonNap = calendar.when > (PROLOGUE, SATURDAY, MORNING)
        prologue.dakotaRanchIntro = calendar.when > (PROLOGUE, SATURDAY, NIGHT)
        prologue.complete = calendar.when > (PROLOGUE, SUNDAY, NIGHT)
    
    def update_unlocked_sexscenes():
        for girl in get_girls():
            if girl.met:
                persistent.metGirls.add(girl.key)
        # Antonella
        if prologue.dakotaJobOffer:
            persistent.sexscenes.add('antonella_titshow_scene')
        # Barbara
        if prologue.barbaraSallyStrapon:
            persistent.sexscenes.add('barbara_cucumberstrapon_scene')
        # Beatrix
        if quests.beatrixDiary == COMPLETE:
            persistent.sexscenes.add('beatrix_lapdance_scene')
        if quests.beatrixHalloweenGrinding == COMPLETE:
            persistent.sexscenes.add('beatrix_halloweengrinding_scene')
        if quests.beatrixHomework == COMPLETE:
            persistent.sexscenes.add('beatrix_beatrixfootjob_scene')
        if quests.beatrixHerpes == COMPLETE:
            persistent.sexscenes.add('beatrix_beatrixboobjob_scene')
        if quests.beatrixHerpes >= SATISFIED:
            persistent.sexscenes.add('beatrix_beatrixblowjob_scene')
        # Blair
        if quests.blairUSB == COMPLETE:
            persistent.sexscenes.add('blair_opheliascissoring_scene')
        if quests.drunkblair == COMPLETE:
            persistent.sexscenes.add('blair_drunknight_scene')
        # Cassidy
        if Cassidy.met:
            persistent.sexscenes.add('cassidy_lockerroomdildo_scene')
        if prologue.cassidyPeephole:
            persistent.sexscenes.add('cassidy_townhousepeephole_scene')
        if prologue.cassidyShower:
            persistent.sexscenes.add('cassidy_townhouseshower_scene')
        if quests.cassidyTrials == COMPLETE:
            persistent.sexscenes.add('cassidy_titsout_scene')
        if quests.cassidyFirstFuck >= ACTIVE:
            persistent.sexscenes.add('cassidy_halloweenblowjob_scene')
        if quests.cassidyFirstFuck == COMPLETE:
            persistent.sexscenes.add('cassidy_cassidycowgirl_scene')
        # Christy
        if Toord.met:
            persistent.sexscenes.add('christy_gymshower_scene')
        if quests.beatrixDiary >= SATISFIED:
            persistent.sexscenes.add('christy_dildofight_scene')
        if quests.christyMandyVoltium == COMPLETE:
            persistent.sexscenes.add('christy_halloweenpoolsex_scene')
        if quests.christyPlan == COMPLETE:
            persistent.sexscenes.add('christy_blowjob_scene')
        # Eunice
        if quests.euniceGettingtherole == COMPLETE:
            persistent.sexscenes.add('eunice_fuckvision_scene')
        if quests.euniceBoobytrap == COMPLETE:
            persistent.sexscenes.add('eunice_gymsex_scene')
        if quests.euniceTheaterpractice == COMPLETE:
            persistent.sexscenes.add('miku_queenrescue3some_scene')
        # Fiona
        if quests.fionaPadlock == COMPLETE:
            persistent.sexscenes.add('fiona_kiosktitflash_scene')
        if quests.fionaConfrontDerek == COMPLETE:
            persistent.sexscenes.add('fiona_kioskblowjob_scene')
        if quests.fionaNightDate == COMPLETE:
            persistent.sexscenes.add('fiona_nightdate_scene')
        if quests.fionaBartender == COMPLETE:
            persistent.sexscenes.add('fiona_halloweensex_scene')
        if quests.fionaDadTrouble == COMPLETE:
            persistent.sexscenes.add('fiona_dadrevenge_scene')
        # Jillian
        if quests.grantHoboBag >= SATISFIED:
            persistent.sexscenes.add('jill_officemasturbation_scene')
        # Kassandra
        if quests.bathtubclimax == COMPLETE:
            persistent.sexscenes.add('kassandra_bathgasm_scene')
        # Lola
        if Lola.met == True:
            persistent.sexscenes.add('lola_carmasturbation_scene')
        # Mandy
        if quests.christyMandyVoltium == COMPLETE:
            persistent.sexscenes.add('mandy_halloweenpoolsex_scene')
        # Miku
        if quests.mikuPhotoShoot == COMPLETE:
            persistent.sexscenes.add('miku_photoshootblowjob_scene')
        if quests.mikuJacuzzi == COMPLETE:
            persistent.sexscenes.add('miku_halloweensex_scene')
        if quests.artProject == COMPLETE:
            persistent.sexscenes.add('miku_privatemasturbation_scene')
        if mikutitshake01:
            persistent.sexscenes.add('miku_titshake_scene')
        if quests.euniceTheaterpractice == COMPLETE:
            persistent.sexscenes.add('miku_queenrescue3some_scene')
        # Miss Dawson
        if quests.missdawsonTitShow == COMPLETE:
            persistent.sexscenes.add('missdawson_titgrope_scene')
        if quests.missdawsonAssistant >= ACTIVE:
            persistent.sexscenes.add('missdawson_underdeskhandjob_scene')
        if quests.missdawsonAssistant == COMPLETE:
            persistent.sexscenes.add('missdawson_oralunderdesk_scene')
            persistent.sexscenes.add('missdawson_deepthroat_scene')
        if quests.missdawsonHalloweenStaff == COMPLETE:
            persistent.sexscenes.add('missdawson_fucking_scene')
        # Ruby
        if Ruby.met:
            persistent.sexscenes.add('ruby_jacuzzisex_scene')
        # Miss Punny
        if quests.punnyDatingTeacher >= ACTIVE:
            persistent.sexscenes.add('punny_69lesson_scene')
        if quests.punnyDatingTeacher >= SATISFIED:
            persistent.sexscenes.add('punny_dinnersex_scene')
        # Sally
        if prologue.barbaraSallyStrapon:
            persistent.sexscenes.add('sally_cucumberstrapon_scene')
        # Tatiana
        if Tatiana.met:
            persistent.sexscenes.add('tatiana_jacuzzisex_scene')
        # Violet
        if glob.halloweenEventComplete:
            persistent.sexscenes.add('violet_halloweenfingering_scene')
        # Wendy
        if prologue.firstNight:
            persistent.sexscenes.add('wendy_mysterygirlnight1_scene')
        if prologue.secondNight:
            persistent.sexscenes.add('wendy_mysterygirlnight2_scene')
        if Jill.met:
            persistent.sexscenes.add('wendy_roominfiltration_scene')
        if quests.goodbyeWendy == COMPLETE:
            persistent.sexscenes.add('wendygoodbyescene')
        
label after_load:
    # if save_version == config.version:
    #     return
    # $ v0_30_1_saveupdate()
    # $ save_version = config.version
    # $ renpy.block_rollback()
    $ update_unlocked_sexscenes()
    return

# Classes
init python:
    class Subject:
        def __init__(self, teacher, stat, music):
            self.teacher = teacher
            self.stat = stat
            self.music = music
            self.lesson = 1
            self.lessonFailed = False

label subject(name):
    $ subject = classes[name]
    $ n = subject.lesson
    # Music
    if subject.music is not None:
        play music subject.music
    else:
        stop music
    # Intro
    $ maxLesson = class_max_lessons[name]
    if subject.lesson > maxLesson:
        "{i}Time passes and you finish class without any novelty.{/i}"
        call nexttime from _call_nexttime_3
        return
    elif subject.lessonFailed:
        call expression (name + '_failintro') from _call_expression
    else:
        call expression ('{}_lesson{}intro'.format(name, n)) from _call_expression_1
    # Minigame
    $ quick_menu = False
    call expression (name + '_minigame') from _call_expression_2
    $ quick_menu = True
    $ subject.lessonFailed = not _return
    # Outro
    if subject.lessonFailed:
        call expression (name + '_failoutro') from _call_expression_3
    else:
        call expression ('{}_lesson{}outro'.format(name, n)) from _call_expression_4
        python:
            subject.lesson += 1
            if type(subject.stat) is tuple:
                for stat in subject.stat:
                    Jimmy.stats[stat] += 1
            else:
                Jimmy.stats[subject.stat] += 1
            subject.teacher.relPoints += 1
    call nexttime from _call_nexttime_4
    return

# Item pick-ups
style item_pickup_text is text:
    xalign 0.5
    yalign 1.0
    size 48
    text_align 0.5

screen item_pickup(item):
    fixed:
        xysize 700, 480
        xalign 0.5
        yanchor 0.5
        ypos 0.45

        # add Solid('#000b')
        add Frame('gui/nvl.webp', Borders(0, 0, 0, 0))

        $ img = Transform(item.image, zoom=1.5)
        add img:
            xalign 0.5
            yanchor 0.5
            ypos 0.37

        $ msg = __("You got\n{}!").format(item.name)
        text msg:
            style 'item_pickup_text'
            yoffset -40

label item_pickup(item):
    show screen item_pickup(item) with dissolve
    pause 1.5
    hide screen item_pickup with dissolve
    $ Jimmy.inventory.append(item)
    return

# Scene-related functions
init python:
    scene_defs = {}

    def checkcurfew():
        # TODO: add prefect pass check once prefect pass added
        if calendar.when[2] == NIGHT:
            if prefectpass == True:
                return
            else:
                renpy.pause(0.4)
                renpy.show_screen('freeroamhud', interactable=False)
                renpy.say(None, __("It's getting late. I should head back to my dorm if I don't want detention."))
                gotoscene('boysdormjimmysroom', transition=fade)

    def showscene(scene_name, transition=None, playMusic=True):
        # clear the scene
        renpy.scene()
        # show the new scene
        ground, _ = _get_image_maps(scene_name)
        renpy.show(ground)
        sprites = scene_defs[scene_name]['sprites']
        # add sprites
        for sprite in filter(lambda x: x.showif(), sprites):
            x, y = sprite.bounds[:2]
            renpy.show(sprite.image, at_list=[Transform(pos=(x, y))])
        if transition is not None:
            renpy.with_statement(transition)
        # update music
        if playMusic:
            if calendar.when[2] == NIGHT:
                _play_altermusic(scene_name)
            else:
                _play_music(scene_name)
        return

    def gotoscene(scene_name, transition=False):
        # update scene variables
        ground, hover = _get_image_maps(scene_name)
        scenemanager.scene = scene_name
        scenemanager.sceneGround = ground
        scenemanager.sceneHover = hover
        scenemanager.bgMusic = scene_defs[scene_name]['music']
        # set scene
        showscene(scenemanager.scene, transition)
        # (re-)display HUD
        renpy.show_screen('freeroamhud')
        # jump to scene
        renpy.jump(scene_name)
        return

    def resetscene():
        # set scene
        showscene(scenemanager.scene)
        # (re-)display HUD
        if inclass == False:
            renpy.show_screen('freeroamhud')
        return
        

    def _play_music(scene_name):
        music = scene_defs[scene_name]['music']
        if music is not None:
            renpy.music.play(music, if_changed=True)
        else:
            renpy.music.stop()
        return

    def _play_altermusic(scene_name):
        music = scene_defs[scene_name]['altermusic']
        if music is not None:
            renpy.music.play(music, if_changed=True)
        else:
            renpy.music.stop()
        return

    # Returns the ground & hover images for a scene in scene_defs
    def _get_image_maps(scene_name):
        backgrounds = scene_defs[scene_name]['maps']
        time_key = TIME_STRINGS[calendar.when[2] - 1]
        season_key = calendar.season
        combo_key = season_key + time_key
        # time + season
        if combo_key in backgrounds:
            imgs = backgrounds[combo_key]
        # time only
        elif time_key in backgrounds:
            imgs = backgrounds[time_key]
        # season only
        elif season_key in backgrounds:
            imgs = backgrounds[season_key]
        # default
        else:
            imgs = backgrounds['default']
        return imgs

# Scenes
screen map(scene_name):
    imagemap:
        ground scenemanager.sceneGround
        hover scenemanager.sceneHover

        $ hotspots = scene_defs[scene_name]['hotspots']
        for hotspot in hotspots:
            $ tag, bounds = hotspot[:2]
            if len(hotspot) == 2 or hotspot[2]():
                hotspot bounds clicked Show('freeroamhud', interactable=False), Jump(scene_name + '_' + tag)

    $ sprites = scene_defs[scene_name]['sprites']
    for sprite in filter(lambda x: x.showif(), sprites):
        if sprite.isButton:
            $ label = scene_name + '_' + sprite.key
            use sprite(sprite.image, sprite.bounds, hover=sprite.hover, label=label)
        else:
            use sprite(sprite.image, sprite.bounds, hover=sprite.hover, isButton=False)

screen sprite(
        name,
        bounds,
        isButton=True,
        hover=None,
        label=None,
        action=None,
        focusMask=True,
        mouse=None,
        showHUD=True):
    $ x, y, w, h = bounds
    if action is None:
        $ action = Jump(label) if label is not None else NullAction()
    if showHUD:
        $ action = (Show('freeroamhud', interactable=False), action)

    if not isButton:
        add name:
            pos x, y
    elif hover is None:
        add name:
            pos x, y
        $ fillRect = Fixed(Solid('#fff3'), xsize=w, ysize=h)
        imagebutton:
            idle Null(width=w, height=h)
            hover AlphaMask(fillRect, name)
            pos x, y
            if focusMask:
                focus_mask name
            action action
            if mouse is not None:
                mouse mouse
    else:
        imagebutton:
            idle name
            hover hover
            pos x, y
            focus_mask focusMask
            action action
            if mouse is not None:
                mouse mouse

init python:
    class Sprite:
        def __init__(self, key, image, bounds, showif, hover=None, isButton=True):
            self.key = key
            self.image = image
            self.hover = hover
            self.bounds = bounds
            self.showif = showif
            self.isButton = isButton

label chardaylimitreset:
    $ AliceDaylimit = False
    $ AntonellaDaylimit = False
    $ AudreyDaylimit = False
    $ FionaDaylimit = False
    $ WorkDaylimit = False
    $ PunnyDaylimit = False
    $ MikuDaylimit = False
    $ EuniceDaylimit = False
    $ BeatrixDaylimit = False
    $ ChristyDaylimit = False
    $ BlairDaylimit = False
    $ CassidyDaylimit = False
    $ SallyDaylimit = False
    $ RubyDaylimit = False
    $ TatianaDaylimit = False
    $ VioletDaylimit = False
    $ WendyDaylimit = False
    $ JillianDaylimit = False
    $ LolaDaylimit = False
    $ MandyDaylimit = False
    $ DawsonDaylimit = False
    $ PunnyDaylimit = False
    $ JonesDaylimit = False
    $ BarbaraDaylimit = False
    $ ClarissaDaylimit = False
    $ DakotaDaylimit = False
    $ SerenityDaylimit = False
    $ KassandraDaylimit = False
    return