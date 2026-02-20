label fionapadlockquest:
    if quests.fionaPadlock == ACTIVE:
        jump .active
    elif quests.fionaPadlock == SATISFIED:
        jump .satisfied

label .active:
    Jimmy "Where did you say Derek took your padlock?"
    Fiona "The boys' dorm."
    Jimmy "Cool, thanks."
    jump fionadialogue.dialogmenu

label .satisfied:
    jump chapterone_fionapadlocksatisfied

## Padlock Quest ###################################################################################

label chapterone_fionaintro:
    hide screen freeroamhud with None
    play music MUSIC_FIONAS_THEME
    show fionaintropeek with dissolve
    "Wow, look at those legs."
    pause 0.8
    $ time = TIME_STRINGS[calendar.when[2] - 1]
    Jimmy "Hey, do you work here?"
    hide fionakioskdialogbutton
    hide fionaintropeek with dissolve
    show fiona clerk neutral with dissolve
    play sound "audio/sfx/hey04.ogg"
    Fiona "Oh, hi."
    Fiona "Sorry, I didn't see you coming. I was lost in my thoughts."
    Fiona happy "Yes! I'm the owner, what do you need?"
    Jimmy "Wait, do I know you?"
    Fiona neutral "Umm, I'm not sure, but you look familiar too."
    show fionabeachmemory with dissolve
    Jimmy "Wait, you are the girl I saw at the beach..."
    Jimmy "Near the cliffs."
    hide fionabeachmemory with dissolve
    play sound "audio/sfx/giggle01.ogg"
    Fiona happy "Oh, right! You're the explorer!"
    Fiona "I'm glad you didn't end up in prison, ha, ha."
    Jimmy "Me too, little mermaid."
    play sound "audio/sfx/hmm01.ogg"
    Fiona neutral "It's nice to get some fresh air between all the assholes that live in this town."
    Jimmy "That's something we have in common."
    Fiona "I used to like it here when I was younger. But then adulthood hits like a fucking truck without breaks..."
    Jimmy "I feel you."
    Jimmy "So, this kiosk is yours?"
    Fiona "Yeah, this is my sad attempt at entrepreneurship."
    Fiona "Just trying to prove my dad that I can take care of myself."
    Jimmy "I'm sure you'll find a way to show him."
    Fiona "Well at least someone believes in me."
    Jimmy "If I can help you with anything, count on me."
    Fiona "Well, actually, there is something you can do for me."
    Jimmy "I got the job? Great!"
    play sound "audio/sfx/giggle02.ogg"
    Fiona happy "Yes, you did, ha, ha, but the payment is kind of non-existant... I hope you are here only to fill your curriculum."
    Jimmy "Sure, that's enough."
    play sound "audio/sfx/alright02.ogg"
    Fiona mad "Alright, so, there is this guy called Derek that stole my minifridge's padlock this morning, and I need it back."
    Fiona "That bastard is always bothering me, asking me for dirty stuff, and obviously I said no."
    Fiona "So he took my padlock and ran away to the boys' dorm."
    Fiona "I can't go in there, because, well, I'm a girl." 
    Jimmy "Oh, good to know."
    Fiona neutral "So, could you please find it for me?"
    Fiona "I'll find a way to repay you, alright?"
    Jimmy "Piece of cake. I'll be back before you know it."
    $ quests.fionaPadlock = ACTIVE
    $ gotoscene('girlsdormfrontgate')

label chapterone_fionapadlocksatisfied:
    Jimmy "Here's your padlock."
    play sound "audio/sfx/gasp01.ogg"
    Fiona happy "Wow, [player_name]. Thank you so much!"
    Fiona "Did you had any problem getting it?"
    Jimmy "Nope, I just found it on a table next to the TV."
    Fiona "Oh, cool, cool. I hope that idiot leaves me alone..."
    play sound "audio/sfx/stopmusiceffect.ogg"
    stop music
    play music "audio/music/crazymoment01.ogg"
    Derek "Hey, sexy boobs! You have a boyfriend now!?" with vpunch
    scene derekthrowingwater with vpunch
    play sound "audio/sfx/big_punch.ogg"
    Derek "I'm the only one that can get you wet!! Ha, ha, ha, ha, ha!"
    play sound "audio/sfx/scream01.ogg"
    Fiona "AAAAAAAAGGHH!" with vpunch
    show derekwaterrun with vpunch
    play sound "audio/sfx/run01.ogg"
    Derek "See you later, bitch!"
    Jimmy "Hey, you piece of shit!"
    Fiona "Don't chase him! Please, just... Stay here with me."
    Jimmy "You sure?"
    Fiona "Yes, please."
    $ showscene('girlsdormfrontgate', transition=fade)
    hide fionakioskdialogbutton with dissolve
    show fiona clerk mad wet with dissolve
    Fiona "Ugh... I'm all soaked..."
    Fiona "Come with me, to the kiosk."
    scene fionastoreshelf with fade
    stop music
    play sound "audio/sfx/doorclose02.ogg"
    show fiona clerk mad wet with dissolve
    Jimmy "How long has he been bothering you?"
    Fiona "A couple of weeks. Not that much."
    play sound "audio/sfx/hmm01.ogg"
    Fiona "He seemed nervous to approach me at first."
    Fiona "But, then I rejected a date proposal and he went crazy."
    Jimmy "Umm, alright."
    Fiona "I could tell one of the monitors, but then my..."
    Fiona "Nevermind. I just want to deal with it, myself."
    Jimmy "Well, I'm not a monitor, but, I will help you."
    play sound "audio/sfx/hmm02.ogg"
    Fiona "Thank you, [player_name]."
    Fiona "I guess I'm gonna get changed."
    Fiona "I wanted to give you something for your trouble."
    $ Jimmy.money += 25
    call yougotmoney from _call_yougotmoney_1
    Fiona "Come by tomorrow, maybe we can have more time to talk."
    Jimmy "Sure, take care."
    $ Fiona.relPoints += 1
    $ FionaDaylimit = True
    $ quests.fionaPadlock = COMPLETE
    $ Jimmy.inventory.remove(ItemFionaPadlock)
    call nexttime from _call_nexttime_28
    $ gotoscene('girlsdormfrontgate', transition=fade)