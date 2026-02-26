label fionanightdatequest:
    if quests.fionaNightDate == LOCKED:
        hide fionakioskdialogbutton with dissolve
        show fiona clerk neutral with dissolve
        Fiona "Hey, don't forget about our date at the beach!"
        Fiona "I'll be waiting for you!"
        Jimmy "Someone will have to kill me before I miss that."
        Fiona "Ha, ha, ha, good to hear that!"
        jump fionadialogue.dialogmenu
    
    

## Night Date ######################################################################################

label chapterone_fionanightdateintro:
    hide screen freeroamhud
    show beachpicnicsetupevening with dissolve
    show fiona swimsuit neutral with dissolve
    play sound "audio/sfx/hey02.ogg"
    play music MUSIC_FIONAS_THEME
    Fiona "[player_name]! I'm so happy you came!"
    Fiona "I was so nervous... I... I have everything ready."
    Fiona happy "I brought some beers..."
    Jimmy "Uh, that's nice."
    Fiona "Oh! Thank god you like it, and I also brought..."
    Jimmy "Donuts! Of course, it's perfect, Fiona."
    Jimmy "I really feel guilty now that I didn't bring anything."
    Fiona neutral "Oh, come on. You have done enough for me, [player_name]."
    Fiona "Today, I'll do all the work."
    Fiona "But, now that I think about it..."
    Fiona "I think we need some ice for the beers."
    Jimmy "There is a bar nearby, I can get some and make myself useful."
    Fiona "Good idea! I'll wait for you, here."
    $ quests.fionaNightDate = ACTIVE
    $ gotoscene('seasideareamap')

label chapterone_fionasurfinglesson:
    hide screen freeroamhud
    $ showscene('seasideareamap', transition=fade)
    $ renpy.pause()
    $ showscene('seasidecliff', transition=fade)
    show beachpicnicsetupevening
    show fiona swimsuit neutral with dissolve
    Jimmy "Here's some ice, my lady."
    Fiona "Oh, thank so much, sir."
    $ Jimmy.inventory.remove(ItemIceBag)
    play music MUSIC_FIONAS_THEME
    Fiona happy "I got something fun for us to do! Have you ever surfed before?"
    Jimmy "Ummm... no."
    play sound "audio/sfx/giggle01.ogg"
    Fiona "Aha! This is gonna be fun! Come here, I'm gonna teach you."
    Jimmy "I don't think that's a good idea..."
    Fiona "Oh, come on, don't be a coward."
    play music "audio/music/funnymoment04.ogg"
    scene fionasurfinglesson01 with fade
    Fiona "Alright, here's the deal."
    Fiona "First you find the wave while laying down on the board."
    Fiona "Then, you push your chest up with your arms."
    Fiona "Put your right feet where your left knee is..."
    Fiona "And then the left feet between your hands."
    Fiona "That will make it easier for you to stand while in movement."
    Fiona "You need to keep your knees flexed and your hands above your hips."
    play sound "audio/sfx/giggle01.ogg"
    scene fionasurfinglesson02 with fade
    Jimmy "Wow, wow, wow, that's a lottt of information."
    Jimmy "Wait a minute..."
    Jimmy "Push up... Right knee..."
    Jimmy "Wait, left knee... okey, let's see."
    scene fionasurfinglesson03 with vpunch
    play sound "audio/sfx/gasp01.ogg"
    Jimmy "Ahhh, crap!"
    play sound "audio/sfx/laugh04.ogg"
    Fiona "HAHAHAHAHAHAHAHAHAHAHA!"
    Jimmy "Hey don't lau... Augh!"
    $ showscene('seasidecliff', transition=fade)
    show beachpicnicsetupevening with dissolve
    show fiona swimsuit neutral with dissolve
    Jimmy "This is definetely not my thing..."
    Fiona happy "Ha, ha, ha, don't be so hard on yourself."
    Fiona "You just need some practice."
    Fiona neutral "Oh my god, look!"
    play music "audio/music/sadmoment02.ogg"
    scene fionasunsetkiss01 with fade
    play sound "audio/sfx/girlsigh01.ogg"
    Fiona "Told you the sunset was beautiful."
    Jimmy "You're right, it's beautiful."
    Jimmy "But, I'm not sure if that view can compete with the way YOU look."
    play sound "audio/sfx/giggle01.ogg"
    Fiona "Ah, that's so cheesy... I love it."
    Fiona "I haven't had this much fun in a long time."
    Jimmy "Well, now that I'm here, we can have all the fun you want."
    Fiona "Thank you, [player_name]."
    Fiona "I... I need to tell you something..."
    Jimmy "Hold on."
    scene fionasunsetkiss02 with vpunch
    play sound "audio/sfx/surprisedhum.ogg"
    Fiona "..."
    Jimmy "..."
    __("{i}The weird silence was only interrupted by the sound of the waves and the seagulls.{/i}")
    __("{i}Even though it took her by surprise, Fiona didn't back away from the kiss, she embraced it.{/i}")
    call nexttime from _call_nexttime_15
    $ showscene('seasidecliff', transition=fade)
    show beachpicnicsetupnight with dissolve
    show fiona swimsuit neutral with dissolve
    Fiona "That was..."
    Fiona "I never even dreamed of kissing someone during such a beautiful sunset."
    Fiona "And yet, it felt like I waited for something like that all my life."
    Jimmy "I'm sorry, I just couldn't control myself."
    Fiona aroused "It was perfect, [player_name]."
    Fiona "I... I like you [player_name], a lot."
    scene fionabeachteasing with fade
    play sound "audio/sfx/sexyintro.ogg"
    Fiona "I don't want this evening to end..."
    Fiona "See this? I'm getting wet for you..."
    Jimmy "Well, we are both wet, we were swimming ha, ha, ha." with vpunch
    play sound "audio/sfx/giggle01.ogg"
    Fiona "Ha, ha, ha, shut up."
    Fiona "Please, [player_name], I want you."
    Jimmy "You're so sexy, Fiona. I want you too."
    Fiona "It's just so perfect that we met here, and now..."
    Fiona "Let's get you hard, baby."
    call fiona_nightdate_scene from _call_fiona_nightdate_scene_1
    scene fionabeachending with fade
    Fiona "That was amazing, [player_name]."
    Fiona "It has been the best week of my life."
    Fiona "Thank you so much."
    Jimmy "No problem. But, I also have to thank you for this."
    Jimmy "I'm not sure about the surfing thing, but we can hang out whenever you feel like."
    Fiona "Ha, ha, ha, you can surf me instead."
    Jimmy "Oh, yeah, I love that."
    Fiona "[player_name], there is something I wanted to tell you."
    Jimmy "Oh, yeah, I interrupted you."
    Jimmy "What is it?"
    Fiona "I think is important for you to know who is my father..."
    Jimmy "Oh, you want me to meet your family, already?"
    Jimmy "I mean, I'm not against it, but maybe we should take it easy..."
    Fiona "No, silly. That's not what I meant... It's just that..."
    Fiona "Well, I will just say it because I can't keep this anymore and it's killing my brain."
    Fiona "My dad is the Headmaster."
    stop music
    play sound "audio/sfx/stopmusiceffect.ogg"
    Jimmy "What?!" with vpunch
    $ showscene('seasidecliff', transition=fade)
    show beachpicnicsetupnight with dissolve
    show fiona naked mad with dissolve
    Jimmy "Your dad is Stapleneck?"
    Fiona "Yes, I'm Fiona Layla Stapleneck Davis."
    Fiona "Nice to meet you?"
    Jimmy "..."
    Fiona "..."
    Fiona "Say something at least."
    Jimmy "Wow, I... I don't know about this."
    Jimmy "It's just that, you could've mentioned it before, y'know..."
    Fiona "Does it change anything?"
    Fiona "I don't have to ask my dad for permission to be with anyone, I'm an adult."
    Jimmy "Fiona, your dad has his eyes on me, alright?"
    Jimmy "I'm the new guy in the academy, hell, I'm the new guy in town."
    Jimmy "I gotta watch my back, and dating the headmaster's daughter can draw a target on my head."
    Jimmy "This is my last chance to get my degree, and... I can't mess this up."
    Fiona "Wow, I thought you would at least stand up to him."
    Fiona "But like everyone else, my dad just can't help to scare everyone away from me."
    Jimmy "Fiona, I've been expelled from a ton of places and your dad thinks I'm a menace."
    Jimmy "You know he's not gonna take it lightly when he finds out I'm getting intimate with you."
    Fiona "I don't give a damn about what my dad thinks!" with vpunch
    Fiona "I'm an adult, and I can make my own decisions."
    Jimmy "I don't know, Fiona."
    Jimmy "Maybe... maybe we can try something else."
    Fiona "What do you have in mind?"
    Jimmy "Maybe we can hang out, but not in public, y'know?"
    Jimmy "I'm sure there are a bunch of snitches all over the school."
    Jimmy "If they even see us talking, they'll come up with some bullshit to tell your dad."
    Fiona "{i}Sigh.{/i} I guess you're right."
    Fiona "I mean, it could be exciting, right?"
    Jimmy "I was thinking just that."
    Jimmy "Come on, don't be mad. We'll figure it out, alright?"
    Fiona "Oh, [player_name]..."
    Jimmy "Let's not think about that now, we gotta take care of those donuts!"
    Fiona "And the beers! Ha, ha, you're right, let's enjoy the night."
    $ Fiona.relPoints += 1
    $ quests.fionaNightDate = COMPLETE
    scene nightsky with fade
    __("{i}After a good night of laughs and some more failed surfing practice, [player_name] and Fiona parted ways.{/i}")
    __("{i}Who knows what destiny was planned for those two, but one thing was for sure, and it's that it was going to be dangerous.{/i}")
    call nexttime from _call_nexttime_16
    $ gotoscene('townhousejimmysroom')
