label wendygoodbyescene:
    hide screen freeroamhud with None
    scene wendyatwindow with fade
    __("Wendy carefully climbed through the window while the moon shone over her beautiful skin.")
    Wendy "Hey..."
    Jimmy "Wendy? You shouldn't be here."
    Wendy "I know, I know, but I need to talk to you."
    Wendy "Are you going to let me in?"
    __("[player_name] nodded, a small smile playing on his lips as he reached out to take her hand and help her down from the window.")
    scene jimmybedroomfallmidnight with fade
    show wendy goodbye with dissolve
    Wendy "I'm leaving Peacock Valley."
    Jimmy "What? Why?"
    Wendy "My father is trying to avoid gossip, you know. He doesn't want a scandal, so he's sending me away for a while."
    Wendy "He's planning something, something to get revenge on you for disrespecting his name. At least that's what he said."
    Wendy "But, I'm afraid he was scheming everything even before you arrived."
    Wendy "You just pushed him to do whatever he plans to do, before it was intended."
    Wendy "Be careful, okay?"
    Jimmy "It sounds like it is something terrible."
    Wendy "I know my father better than anyone."
    Wendy "He's obssesed with order and morality."
    Wendy "If he can't teach people how to behave, he will make them do what he wants, no matter how."
    Jimmy "Alright, thanks for the heads up, I guess."
    Wendy "Yeah, I didn't came here just to warn you."
    Jimmy "Yeah, I figured you could have done that with a letter or something."
    Wendy "Yeah, hehe."
    Wendy "Do you remember that night?"
    Wendy "The night you infiltrated my father's mansion and entered my room?"
    Jimmy "Well, that's a night I will never forget, princess."
    Wendy "It was so romantic. I felt like I was in a movie."
    Wendy "It was so special. I loved what we did in my bed that night."
    Wendy "I just... I want to make love with you before I go."
    call wendy_analandcreampie_scene from _call_wendy_analandcreampie_scene
    ("{i}The choice you're about to make, will determine the future of Wendy's storyline.{/i}")
    menu:
        __("Wendy gets pregnant"):
            $ pregnancy.Wendy = True
        __("Wendy does not get pregnant"):
            $ pregnancy.Wendy = False
    __("{i}The choice has been made.{/i}")
    scene jimmybedroomfallmidnight with fade
    show wendy goodbye with dissolve
    Wendy "I'll try to help you even if I'm far away."
    Wendy "I discovered something in one of my father's diaries."
    Wendy "They mentioned something about a woman from his past, a woman who died giving birth to a child."
    Wendy "I'm not sure what dark secret my Dad is hiding."
    Wendy "But, I will follow the clues."
    Wendy "When I find something, I'll let you know."
    Jimmy "Thank you for telling me. I appreciate the fact you want to help me."
    Jimmy "But take care of yourself first."
    Wendy "I will miss you."
    Jimmy "I will miss you too, princess, that's for sure."
    __("[player_name] smiled, then leaned in and kissed her gently before saying goodbye.")
    $ quests.goodbyeWendy = COMPLETE
    call sleep from _call_sleep_11
    $ gotoscene('boysdormjimmysroom')

label wendy_analandcreampie_scene:
    Wendy "I wanna feel something I haven't felt before."
    scene wendyanalcreampie01 with fade
    __("She immediately took her clothes off and lay down on the bed, showing her nice round ass.")
    Wendy "Have you ever done anal?"
    Wendy "I'm not sure if your dick will fit in my little hole, but just thinking about it is making me so wet."
    Wendy "I want you to fuck me in the ass, [player_name]."
    Wendy "I want to feel that big cock once more, before I leave!"
    Jimmy "Wish granted, princess."
    scene wendyanalcreampieanim01 with fade
    Wendy "Please, be careful."
    Wendy "Just the tip is making my ass stretch out so much."
    Wendy "I don't think I can take it."
    Wendy "Just push gently..."
    scene wendyanalcreampieanim02 with vpunch
    Wendy "OOHHH MY GOD!"
    Wendy "IT'S SO FUCKING BIG!"
    Wendy "It hurts so much! Please, I can't take it anymore."
    Jimmy "Do you want me to stop?"
    Wendy "Yes! It's too much for me."
    Wendy "I want to feel your cock sliding in and out inside my pussy."
    scene wendyanalcreampieanim03 with fade
    Wendy "Oh, yes! That's the spot!"
    Wendy "Oh my god! It feels so good!"
    Wendy "Keep going! Fuck my little pussy."
    Wendy "YES! YES! YEEEEES!"
    Wendy "You're gonna make me cum!"
    Jimmy "I'm gonna cum too!"
    Wendy "Don't pull it out!"
    Wendy "I want it all!"
    scene wendyanalcreampiecum with vpunch
    Wendy "Uhhh... All that cum inside me."
    Wendy "I feel so full and it feels so warm."
    Wendy "It's flowing inside my belly."
    Wendy "That was a amazing, [player_name]."
    Wendy "I will never forget this, thank you."
    Jimmy "My pleasure, princess."
    if wendygallery == True:
        call screen wendygallery
    return

#Animations

image wendyanalcreampieanim03:
    'wendypussycreampie01'
    pause 0.1
    'wendypussycreampie02'
    pause 0.1
    'wendypussycreampie03'
    pause 0.1
    'wendypussycreampie04'
    pause 0.1
    'wendypussycreampie05'
    pause 0.1
    'wendypussycreampie06'
    pause 0.1
    'wendypussycreampie07'
    pause 0.1
    'wendypussycreampie08'
    pause 0.1
    'wendypussycreampie09'
    pause 0.1
    repeat
