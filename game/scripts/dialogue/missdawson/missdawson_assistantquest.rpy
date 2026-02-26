default quests.missdawsonAssistant = LOCKED
default quests.missdawsonAssistantEdna = LOCKED
default quests.missdawsonAssistantMarlon = LOCKED

init python:
    def dawson_memodelivery_iscomplete():
        if not quests.missdawsonAssistantEdna == COMPLETE:
            return False
        if not quests.missdawsonAssistantMarlon == COMPLETE:
            return False
        return True
    def dawson_halloweeninvitations_iscomplete():
        if not quests.missdawsonHalloweenAudrey == COMPLETE:
            return False
        if not quests.missdawsonHalloweenCamembert == COMPLETE:
            return False
        if not quests.missdawsonHalloweenAurora == COMPLETE:
            return False
        return True

label missdawsonassistantquest:
    if quests.missdawsonAssistant == COMPLETE:
        jump .complete
    elif quests.missdawsonAssistant == SATISFIED:
        if dawson_halloweeninvitations_iscomplete():
            jump .satisfied
        else:
            show missdawson neutral with dissolve
            Dawson "Are you done with your tasks?"
            Jimmy "I'm still on it, Miss."
            $ gotoscene('mainbuildingsecretarysoffice')
    elif quests.missdawsonTitShow == COMPLETE:
        jump .active
    elif quests.missdawsonAssistant == LOCKED:
        jump .intro
    elif quests.missdawsonAssistant == ACTIVE:
        if quests.missdawsonTitShow != COMPLETE:
            if dawson_memodelivery_iscomplete():
                jump .titshow
            else:
                show missdawson neutral with dissolve
                Dawson "Are you done with your tasks?"
                Jimmy "I'm still on it, Miss."
                $ gotoscene('mainbuildingsecretarysoffice')
    else:
        show missdawson neutral
        show jimmy neutral
        with dissolve
        Dawson "Hello, Mr. [player_surname]."
        __("I don't require your services today.")
    $ gotoscene('mainbuildingsecretarysoffice')

label .intro:
    show missdawson neutral with dissolve
    show stapleneck talk with dissolve
    play sound "audio/sfx/clearthroat01.ogg"
    play music MUSIC_HEADMASTERS_THEME
    Stapleneck "I'm very sorry for leaving you with this responsability, Miss Dawson."
    Stapleneck arm "But, I'm sure you will be up to the task, as always."
    Stapleneck "I will come back after the festivities, as soon as possible."
    Dawson amazed "Don't you worry about anything, headmaster. I have it under control."
    Stapleneck stern talk "Oh, look who's here! Good evening, Mr. [player_surname]."
    play sound "audio/sfx/frustratedhum.ogg"
    Dawson angry "Oh, good evening."
    Stapleneck arm  "I thought of a great idea!"
    Stapleneck "Let this fine young man help you with the preparations of the festivities."
    play sound "audio/sfx/femaleclearthroat.ogg"
    Dawson "Oh, no, Headmaster. That's not neccesary, I'm sure he is very busy with his schedule."
    Jimmy "I have some free time."
    Dawson "What? Oh, that sounds great. But, I think students should be focused on their studies, don't you agree, Headmaster?"
    play sound "audio/sfx/clearthroat01.ogg"
    Stapleneck smug talk "Nonsense, Miss Dawson. Of course, studies are important..."
    Stapleneck "However, extra curricular activities like this help students develop skills for the future."
    Stapleneck "What do you think about it, Mr. [player_surname]."
    Stapleneck "You think you can assist Miss Dawson?"
    Jimmy "Yeah, no problem, sir."
    Dawson "I can't belive this..."
    Stapleneck talk "What did you say, Miss Dawson?"
    play sound "audio/sfx/hmm02.ogg"
    Dawson amazed "Oh, nothing, just saying it's incredible to find a student so willing to help in that way."
    Stapleneck "That's what I thought! Okay, I'll be going now. I must get ready for my trip."
    play sound "audio/sfx/slap.ogg"
    hide stapleneck with dissolve
    play sound "audio/sfx/mad01.ogg"
    Dawson angry "Don't you even think for a second that this fixes everything that happened."
    Dawson "It's clear that you want to get on my nerves."
    play sound "audio/sfx/frustratedhum.ogg"
    Dawson unamused talk "I can't disobey Dr. Stapleneck, but I don't want to see your face either."
    call item_pickup(ItemMemos01) from _call_item_pickup_22
    Dawson "So, take these memos and deliver them to the cafeteria manager and the concierge at once."
    Dawson "The cafeteria manager is obviously at the cafeteria if your brain hasn't figured it out yet, try the kitchen."
    Dawson "The concierge is in the door to the right of the auditorium."
    Dawson talk point "I will not tolerate mediocrity, so be gone now!"
    $ quests.missdawsonAssistant = ACTIVE
    $ gotoscene('mainbuildingentrance')

label .titshow:
    hide screen freeroamhud
    show missdawson neutral
    Dawson "So, you've finally returned."
    Jimmy "Yes, Miss. The concierge got the memo and said that he was going to work on it as soon as possible."
    Jimmy "As for the cook, well... She told me she won't do what you asked."
    Jimmy "She will be taking some days off during that weekend."
    play sound "audio/sfx/frustratedhum.ogg"
    Dawson angry "What? But, she's not allowed to..."
    Dawson "Ughh... I'm gonna have to talk to her myself about this."
    Dawson unamused talk "Wait for me here, Mr. [player_surname]."
    play sound "audio/sfx/highheels.ogg"
    hide missdawson with dissolve
    Jimmy "Sure."
    scene twentyminuteslater with dissolve
    play sound "audio/sfx/20minlater.ogg"
    pause 1.0
    scene secretaryoffice01 with fade
    play music "audio/music/persecution01.ogg"
    show missdawson angry goo with vpunch
    Dawson "This is outrageous!"
    Dawson "How could she do this to me?"
    Dawson "I swear she forced my hand!"
    Jimmy "Wow, what the hell?"
    Jimmy "Wait, DID YOU KILL HER!?" with vpunch
    play sound SOUND_RECORD_SCRATCH
    stop music
    play music "audio/music/funnymoment03.ogg"
    Dawson "What? Of course not, you silly boy."
    Dawson "We had a serious discussion about the memo and as usual..."
    Dawson "She insulted me, so I had to suspend her wages for the days she will be going 'on vacation'."
    Dawson "She got so mad, she threw stew on me."
    Dawson "Luckily it was cold!"
    Jimmy "Wow, that's the best story I've heard in a while, ha, ha, ha, ha."
    Dawson "Shut up, this is not funny."
    Jimmy "So, what about the food you need?"
    Dawson "About that... After I got soaked with the stew she laughed out loud and told she was going to make the food."
    Dawson "She said that seeing me like this was better than some days off at the beach."
    Jimmy "Well... I'm sorry about that."
    stop music
    play music "audio/music/sadmoment01.ogg"
    scene dawsontitshowsad with fade
    play sound "audio/sfx/womansobbing01.ogg"
    Dawson "..."
    Jimmy "..."
    __("{i}'Oh, shit. This got serious', thought [player_name] as he saw the woman sobbing in front of him.{/i}")
    Dawson "Sometimes it's so hard to... to do this job..."
    Dawson "And he... he left me alone with all the responsability this time..."
    Dawson "It's not fair..."
    Jimmy "..."
    Dawson "I'm sorry, you shouldn't see me like this."
    Jimmy "I don't mind... Can I help in some way?"
    Dawson "Please, close the door."
    Jimmy "Alright."
    play sound "audio/sfx/doorclose02.ogg"
    scene dawsontitshowintro with fade
    Dawson "Can I ask you a question?"
    __("{i}The headmaster's assistant sat on the desk in a very suggestive pose.{/i}")
    __("{i}She looked at [player_name] with tears drying on her beautiful face.{/i}")
    Dawson "Would you marry a woman like me?"
    __("{i}'Wow, that's scalated quickly', thought [player_name].{/i}")
    Jimmy "Uhmmm... I think I would, yes."
    play sound "audio/sfx/femaleclearthroat.ogg"
    Dawson "Really? I mean, it's just that sometimes I feel that I'm not enough."
    Dawson "Maybe I need to do more, or maybe I'm just not wife material, just a sexual toy."
    Jimmy "Well, is hard to give you my opinion after what happened, you know..."
    Jimmy "But, I think you're being too hard on yourself."
    Jimmy "I think you're trying to meet expectations from another person, and that's not what you should aim for."
    Jimmy "My dad told me that, right before he told me he was going to leave me at Trustworth Academy."
    Jimmy "So, I don't know, either."
    stop music
    Dawson "Thank you for saying that."
    call missdawson_titgrope_scene from _call_missdawson_titgrope_scene
    play music MUSIC_DAWSONS_THEME
    scene secretaryoffice01 with fade
    show missdawson seductive with dissolve
    Dawson "You have to earn this."
    Dawson "I was thinking you could do some more assistant work for me."
    Dawson "You can come next week during office hours. Of course, I will pay you for your help."
    Dawson "Here's some cash in advance, as motivation."
    $ Jimmy.money += 50
    call yougotmoney from _call_yougotmoney_2
    Dawson "I may even grant you a prefect pass, if your behavior pleases me."
    Dawson "Now, go on. It's getting late. You should go to your dorm."
    $ Dawson.relPoints += 1
    call nexttime from _call_nexttime_20
    $ showscene('mainbuildingentrance', transition=fade)
    show jimmy smug with dissolve
    __("Damn, that was hot!")
    __("I hope I get to see more of those \"juicy\" tits in the future...")
    $ quests.missdawsonTitShow = COMPLETE
    $ gotoscene('mainbuildingentrance')

label .active:
    show missdawson neutral
    show jimmy neutral
    with dissolve
    Dawson amazed "Mr. [player_surname]! It's a good thing you're here."
    Dawson "The preparations for the Halloween reunion are almost done."
    Dawson talk arm "However, while I take care of one final detail..."
    Dawson "I need you to confirm the assistance of a couple of teachers and Mr. Neil's substitute."
    Dawson "Please, find Mr. Camembert, Miss Bakshi and... I don't remember the name of the Shop class substitute, sorry."
    Dawson "Anyways! They all should be in their classrooms."
    Jimmy talk "Alright, I'm on it."
    Jimmy "Oh, and, about the payment..."
    Dawson "Yes, yes, just do what I asked and you'll get the money."
    Jimmy "Right away, boss."
    Dawson "Thank you, Mr. [player_surname]."
    $ quests.missdawsonAssistant = SATISFIED
    $ gotoscene('mainbuildingentrance')

label .satisfied:
    show missdawson neutral with dissolve
    play music MUSIC_HEADMASTERS_THEME
    show stapleneck smug talk with dissolve
    play sound "audio/sfx/clearthroat01.ogg"
    Stapleneck "So, I trust you have everything under control, Miss Dawson?"
    play sound "audio/sfx/giggle01.ogg"
    Dawson amazed "Oh, yes, Headmaster! The reunion will be a success."
    Stapleneck "Excellent, there is nothing for me to do here for now."
    Stapleneck "I will return after Halloween, Miss Dawson."
    Stapleneck "Have a nice weekend."
    Dawson "Very well, Headmaster! Have a good trip!"
    play sound "audio/sfx/clearthroat01.ogg"
    Stapleneck "Greetings, Mr. [player_surname]."
    Jimmy "Sir..."
    play sound "audio/sfx/highheels.ogg"
    hide stapleneck with dissolve
    play music MUSIC_DAWSONS_THEME
    play sound "audio/sfx/frustratedhum.ogg"
    Dawson angry "Ughh... Thank god he left."
    Dawson "I don't care what he says, I know he's lying and he will be going to see his ex-wife."
    Dawson "Do you know what he asked me to do?"
    Dawson "To go under his desk one last time before the trip."
    Jimmy "And what did you do?"
    Dawson "Nothing, I avoided him as much as I could until he forgot about it."
    Dawson talk arm "Anyways, any news?"
    Jimmy "Oh, yeah. Mr. Camembert says he doesn't have a costume yet. He hasn't found anything his size and I believe him."
    Jimmy "Miss Bakshi and Audrey will totally come to the reunion. Audrey was eager to know if there was going to be any alcohol."
    play sound "audio/sfx/hmm01.ogg"
    Dawson "Dear god... Well, you did good. Thank you."
    Dawson "Here's the money I promised."
    $ Jimmy.money += 200
    call yougotmoney from _call_yougotmoney_3
    Jimmy "Thank you, Miss."
    Dawson blush "Before you leave..."
    Jimmy "Yeah?"
    Dawson "Follow me."
    play sound "audio/sfx/highheels.ogg"
    scene headmasterstudyfallevening with fade
    show missdawson blush with dissolve
    stop music
    play sound "audio/sfx/dooropen01.ogg"
    Dawson neutral "I want to ask you something."
    play sound "audio/sfx/doorclose02.ogg"
    Jimmy "Sure, what is it?"
    Dawson "Did you like what I did to you under the Headmaster's desk?"
    Jimmy "I think the mess I left on your face gave it away."
    Dawson "Good one."
    play sound "audio/sfx/femaleclearthroat.ogg"
    Dawson unamused talk "Alright, Mr. [player_surname]."
    Dawson "Since that happened, I've been fantazising about doing it again..."
    Dawson "But, with me sitting on the chair."
    Jimmy "Oh, I can see what you mean."
    play sound "audio/sfx/giggle02.ogg"
    Dawson happy "You're a smart guy."
    call missdawson_oralunderdesk_scene from _call_missdawson_oralunderdesk_scene
    scene headmasterstudyfallevening with fade
    show missdawson amazed with dissolve
    show jimmy uniform fluid with dissolve
    play music MUSIC_DAWSONS_THEME
    Jimmy "Well, you got me this time."
    play sound "audio/sfx/giggle01.ogg"
    Dawson happy "Ha, ha, ha, ha! Yes, I did."
    Dawson amazed "That was amazing, Mr. [player_surname]."
    Jimmy "I think that now that I have your pussy juice on my face, you can call me [player_name]."
    Dawson "You're right, [player_name]. Thank you so much for this."
    Dawson "Will you come to the Halloween reunion with me?"
    Jimmy "If you want me to, I will."
    play sound "audio/sfx/hmm01.ogg"
    Dawson "Yes, that's great!"
    Dawson "I have an awesome gift for you after the reunion."
    Jimmy "Can't wait..."
    $ quests.missdawsonAssistant = COMPLETE
    $ Dawson.relPoints += 1
    play sound "audio/sfx/guitarriff01.ogg"
    scene chapter2cartel with fade
    $ renpy.pause()
    call nexttime from _call_nexttime_21
    $ gotoscene('mainbuildingentrance')


