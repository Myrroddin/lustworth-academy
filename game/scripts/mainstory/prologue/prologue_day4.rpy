label prologue_dakotaranchintro:
    stop music
    scene laterthatday with fade
    $ renpy.pause()
    hide screen freeroamhud
    $ Jimmy.outfit = JIMMY_DEFAULT
    scene dakotafarmgeneralview01 with fade
    play music MUSIC_DAKOTAS_RANCH
    show jimmy neutral with dissolve
    show dakota neutral with dissolve
    Dakota "Here we are, cowboy. Welcome to my humble home. Whaddya think?"
    Jimmy unamused "The view is amazing."
    Dakota happy "It sure is!"
    Dakota "Here, let's go to the house and have some coffee before I show you around."
    Dakota "You were yawning the whole way here."
    scene dakotafarmhouselivingroomintro with fade
    "{i}As they entered the house, two girls came running toward the entrance.{/i}"
    show barbara neutral
    show sally neutral
    with vpunch
    Barbara "Momma!"
    Sally "Is this the boy you told us about?"
    Dakota "Well aren't you two a pair of eager beavers."
    Dakota "Yes, this is [player_name]."
    Dakota "[player_name], these are my girls, Barbara and Sally."
    $ Barbara.met = True
    $ Sally.met = True
    Barbara "Hi, nice to meet you."
    Sally "Oh, Momma, he's so cute."
    Dakota "He's here to help me get some work done, girls."
    Dakota "Please don't bother him. I'm sorry, [player_name]."
    Jimmy "Don't worry, Miss."
    Jimmy "Nice to meet you both."
    Dakota "Oh, you're such a gentlemen."
    Barbara "Can we watch him work, Momma?"
    Sally "Good idea, sis! Please, Momma?"
    Dakota "Girls, I told you to leave him alone."
    Dakota "If you're so eager, go to the lake and get some water for the horses."
    Dakota "And behave in front of [player_name]!"
    Barbara "No problem, Momma!"
    hide barbara
    hide sally
    with vpunch
    pause 0.5
    show jimmy neutral with dissolve
    show dakota neutral with dissolve
    Dakota "Sorry for that, [player_name]."
    Dakota "They're not used to being around men."
    Dakota sexy "I mean, it's the first time a man's come to this ranch in years."
    Dakota "But they'll get used to it."
    Dakota neutral "Well, when you're ready, meet me at the barn."
    Jimmy talk "Alright."
    $ showscene('dakotasranch', transition=fade)
    show jimmy neutral with dissolve
    "I feel like this place is gonna be interesting."
    "If it's true a man hasn't been here in a while..."
    show jimmy smug with dissolve
    "Then maybe this will be an opportunity to get more than just cash."
    hide jimmy with dissolve
    show screen freeroamhud(False)
    Developer "{i}From now on, you'll be able to come the ranch on the weekend and work for Dakota.{/i}"
    $ prologue.dakotaRanchIntro = True
    $ gotoscene('dakotasranch')

label prologue_dakotaranchbarnintro:
    hide screen freeroamhud
    scene dakotafarmbarn01 with fade
    show jimmy neutral with dissolve
    show dakota neutral with dissolve
    Dakota happy "Ah! There you are."
    Dakota "My favorite farmhand."
    Jimmy unamused "Aren't I your {i}only{/i} farmhand?"
    show jimmy neutral with dissolve
    Dakota neutral "You're gonna bale some hay today, alright?"
    Dakota "Don't worry, we're gonna start easy on ya'."
    Dakota "Let me show you how it's done."
    Developer "{i}A minigame will be added here in future updates.{/i}"
    Developer "{i}Until then, enjoy the reward without a drop of sweat.{/i}"
    Dakota "Nice work, [player_name]!"
    Dakota "I knew you were the right man for the job."
    Dakota "Well, here's your pay."
    Dakota "Let me know when you wanna go, and I'll take you back home."
    $ Jimmy.money += 25
    $ Dakota.relPoints += 1
    call nexttime from _call_nexttime_33
    call nexttime from _call_nexttime_34
    $ prologue.ranchMinigameIntro = True
    jump prologue_barbarasallystrapon

label prologue_barbarasallystrapon:
    $ showscene('dakotasranch', transition=fade)
    "...I think I hear voices coming from inside the shed."
    hide screen freeroamhud
    scene farmshedintro with fade
    play music MUSIC_SNEAK_THEME
    "{i}The shed was packed with boxes, shelves, and tools.{/i}"
    "{i}[player_name] followed the voices coming from the back, trying not to be heard.{/i}"
    Barbara "Come on, Sally!"
    Barbara "That cucumber looks so tasty."
    Sally "Don't rush me, Barbara. I'm really tight down there."
    "What are they talking about?"
    "{i}When [player_name] saw them, his eyes opened wide.{/i}"
    play sound SOUND_RECORD_SCRATCH
    call barbara_cucumberstrapon_scene from _call_barbara_cucumberstrapon_scene_1
    "{i}After watching for a few more moments, [player_name] made his way out before they caught him.{/i}"
    $ showscene('dakotasranch', transition=fade)
    show jimmy unamused with dissolve
    "Those girls are nuts!"
    show jimmy smug with dissolve
    "...But they're also really hot."
    "Hopefully that wasn't the last I'll get to see of them."
    $ prologue.barbaraSallyStrapon = True
    jump prologue_leaveranch

label prologue_leaveranch:
    show dakota neutral with dissolve
    Dakota "Howdy partner. Thanks for your help today."
    Dakota "It's gettin' late. Ready to head back?"
    Jimmy unamused "Yeah. I go back to class tomorrow, so I shouldn't stay out too late."
    Dakota "Alright. Hop in my truck and I'll take ya home."
    hide dakota with dissolve
    hide jimmy with dissolve
    stop music
    hide screen freeroamhud
    scene jimmytownhouseday with fade
    pause 0.8
    call nexttime from _call_nexttime_35
    $ showscene('townhouselivingroom', transition=fade)
    show screen freeroamhud(False)
    "I'm beat. I think I'll take a shower and head to bed."
    $ gotoscene('townhouselivingroom')

label prologue_cassidyshower:
    hide screen freeroamhud
    "The door is open..."
    play sound "audio/sfx/showermoans.ogg"
    scene secondfloorbathroom with fade
    "Looks like someone's already taking a shower."
    call cassidy_townhouseshower_scene from _call_cassidy_townhouseshower_scene
    $ showscene('townhousehallway', transition=fade)
    "Oh well. Guess I'll just take a shower in the morning."
    $ prologue.cassidyShower = True
    $ gotoscene('townhousehallway')

label prologue_day4end:
    hide screen freeroamhud
    "Tomorrow is Monday, which means I go back to Trustworth."
    call sleep("I hope I sleep well.") from _call_sleep_8
    $ showscene('townhousejimmysroom', transition=fade)
    play music MUSIC_KASSANDRAS_THEME
    show kassandra pajamas with dissolve
    Kassandra "Good morning [player_name]!"
    Kassandra "Come eat breakfast, and then I'll take you and your [roommate_female]s to the academy."
    jump chapterone_start
