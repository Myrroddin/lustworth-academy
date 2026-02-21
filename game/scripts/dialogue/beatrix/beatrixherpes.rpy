label beatrixherpestreatment:
    if quests.beatrixHerpes == COMPLETE:
        jump .sexscene
    elif quests.beatrixHerpes == SATISFIED:
        jump .satisfied

label .satisfied:
    Jimmy unamused "I got this for you."
    hide beatrixherpes01
    hide beatrix neutral
    show beatrixherpes02
    Beatrix "What is that?"
    Jimmy unamused arm "It's a cream that helps with herpes."
    hide beatrixherpes02
    show beatrixherpes03 with vpunch
    Beatrix "I told you that IS NOT HERPES!"
    Beatrix "It's an allergy."
    Jimmy unamused "Well, in that case. I'll give it to someone else."
    Beatrix "Wait!"
    Jimmy smug "What?"
    Beatrix "Ughh... I hate you. Give me that."
    Beatrix "Thank you."
    Jimmy smug "No problem."
    hide beatrixherpes03
    show beatrixherpes02
    Beatrix "Are we going to study today?"
    Jimmy unamused "Not a chance. Use the cream and I'll see you tomorrow."
    Beatrix "Idiot."
    $ Jimmy.inventory.remove(ItemHerpesCream)
    $ quests.beatrixHerpes = COMPLETE
    $ gotoscene('mainbuildingrighthallway')

label .sexscene:
    Jimmy "I can see you used the cream I gave you."
    Beatrix talk "Yeah, it worked, and that's the end of it."
    Beatrix "I don't want to talk about it, ever again."
    Jimmy "Whatever you say."
    Beatrix "Now that I don't have... that thing in my face."
    Beatrix "I was wondering if..."
    Jimmy "Yeah?"
    Beatrix "We can continue our study sessions?"
    Jimmy "I think that's a good idea, now that you don't look like a sewer monster."
    Beatrix mad "Ugghh, shut up, idiot."
    Beatrix mad arm "Are we going to study today or not?"
    Jimmy "Of course! Let's go to my room."
    scene laterthatday with fade
    pause 1.0
    scene jimmybedroomfallevening with fade
    show jimmy neutral
    show beatrix uniform talk with dissolve
    Beatrix "Alright, we study first and then see what happens."
    Jimmy "Whatever..."
    scene twentyminuteslater with fade
    pause 1.0
    scene jimmybedroomfallevening with fade
    show jimmy neutral
    show beatrix uniform talk with vpunch
    Beatrix talk arm "Of course! That's why I didn't get the same result!"
    Jimmy "See? If you are more open to suggestions, it's easier for both of us."
    Beatrix "Well, you are right this time."
    Jimmy "Right, our session is over for today, time to pay."
    Beatrix "You waited all day for this, don't you?"
    Beatrix "Okay, can I use my mouth this time?"
    Jimmy "Oh, yeah, baby. You can do whatever you want this time."
    call beatrix_beatrixblowjob_scene from _call_beatrix_beatrixblowjob_scene
    scene jimmybedroomfallmidnight with fade
    show jimmy neutral
    show beatrix uniform talk with dissolve
    Beatrix talk "Well, it was fun studying with you."
    Beatrix "You're not such an asshole after all."
    Jimmy "What I can say?"
    Jimmy "You're not such a bitch after all."
    Beatrix "Ha, ha. Funny. Well, see you in class, pervert."
    Jimmy "Oh, you will..."
    $ quests.beatrixHerpes = COMPLETE
    call nexttime from _call_nexttime_6
    hide beatrix uniform talk with dissolve
    call sleep from _call_sleep
    $ gotoscene('boysdormjimmysroom')
