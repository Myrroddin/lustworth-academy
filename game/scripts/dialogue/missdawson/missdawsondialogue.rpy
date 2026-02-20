#VARIABLES
default quests.missdawsonTitShow = LOCKED
default quests.headmasterSpy = LOCKED
default quests.missdawsonBathroomIncident = LOCKED
default quest.missdawsondeepdone = False

#LABELS
label missdawsondialogue:
    hide screen freeroamhud with None
    play music MUSIC_DAWSONS_THEME
    if quests.missdawsonBathroomIncident == COMPLETE:
        if quests.missdawsonAssistant != COMPLETE:
            jump missdawsonassistantquest
        elif quest.missdawsondeepdone == False:
            jump halloweenreunionstart
    show missdawson neutral
    show jimmy neutral
    with dissolve
    Dawson "Well?"

label .dialogmenu:
    menu:
        "Give headmaster notice" if quests.missdawsonBathroomIncident == ACTIVE:
            jump missdawsonunderthedesk
        "Nevermind":
            pass
    $ gotoscene('mainbuildingsecretarysoffice')

label .headmasterspy:
    hide screen freeroamhud
    play music "audio/music/sneaking01.ogg"
    "{i}As [player_name] got closer to the door, he realized the lock was ancient.{/i}"
    "{i}The key hole was large enough for him to peek through it.{/i}"
    scene headmasterlockpeek01 with dissolve
    "{i}Through the hole, he barely could see the headmaster's office.{/i}"
    "{i}Dr. Stapleneck was sitting in his chair with his head looking up like he was sleeping.{/i}"
    "{i}Suddenly, he percieved a strange movement under the desk as he saw a reddish bush of hair emerging from beneath.{/i}"
    scene headmasterlockpeek02 with dissolve
    play sound "audio/sfx/undress01.ogg"
    "{i}After a couple of seconds, he realized what was actually happening.{/i}"
    "{i}Miss Dawson, the secretary was the one coming out from below the desk.{/i}"
    "{i}What was she doing down there? Was that part of her obligations?{/i}"
    "{i}It wasn't a surprise for [player_name] that the secretary could be having an affair with the headmaster.{/i}"
    "{i}The way she talked about Stapleneck, almost idolizing him, was a clear giveaway.{/i}"
    "{i}Given the ocassion, it was obvious [player_name] had to take advantadge of the situation.{/i}"
    scene headmasterlockpeek03 with vpunch
    play sound "audio/sfx/doorknock01.ogg"
    "{i}The face of the headmaster was hilarious as the secretary started to fix her clothes.{/i}"
    play sound "audio/sfx/whispermale.ogg"
    "{i}The headmaster quickly whispered something to Miss Dawson which [player_name] didn't quite get.{/i}"
    play sound "audio/sfx/hmm02.ogg"
    Dawson "Who is it? The Headmaster is not available right now."
    Jimmy "Sorry, Miss. I just wanted to clear some stuff about my schedule."
    play sound "audio/sfx/whisperfemale.ogg"
    Dawson "It's a student. Very well! Give me a minute!"
    $ showscene('mainbuildingsecretarysoffice', transition=fade)
    play music MUSIC_DAWSONS_THEME
    show missdawson unamused mess with dissolve
    play sound "audio/sfx/femaleclearthroat.ogg"
    Dawson "Be quick about it, I have many things to do."
    Jimmy "Hello, Miss. I just wanted to ask about Astronomy class."
    Jimmy "I don't know where to go for it or who the teacher is."
    Dawson talk mess "Oh, that's very common for new students, my dear."
    Dawson "Astronomy class is taught at the observatory."
    Dawson "I believe you can see the building on top of the hill from outside the boys' dorm."
    Dawson "However, we are still looking for a substitute for Miss Trevelyan, who decided to leave on a trip to Bolivia and didn't return."
    Dawson "It is said that she was involved in some issue with the local natives or something."
    Dawson unamused mess "But, you will be notified once we find a suitable candidate to fulfill the role."
    Jimmy "Right, thank you Miss... I think... I think you have something on your chin."
    play sound "audio/sfx/frustratedhum.ogg"
    Dawson neutral mess "What? Oh... Oh my god... Uh..."
    Dawson "That's... I think I put to much suncream in my face."
    Dawson talk point mess "Anyways, be gone now. I'm busy, and the Headmaster is not available, so don't bother."
    Jimmy "I'll be on my way then."
    $ quests.headmasterSpy = COMPLETE
    call nexttime from _call_nexttime_22
    $ gotoscene('mainbuildingentrance')
