#VARIABLES
default quests.drunkblair = LOCKED

#LABELS

label blairdrunkscene:
    hide screen freeroamhud
    stop music
    scene jimmytownbedroomnight with fade
    Jimmy "What is that sound?"
    scene blairrocktrow02 with vpunch
    Jimmy "What the..."
    scene blairrocktrow03 with fade
    __("It was Blair throwing rocks at his window, she was holding a bottle of liquor in her hand and wearing very short clothes which wasn't usual for her.")
    Jimmy "What the hell, Blair? It's 2 am..."
    __("[player_name] whispered. Blair was making signs for him to come down and meet her outside.")
    __("[player_name] replied with another sign for her to wait for him.")
    scene townhousehallwayfallnight with fade
    $ renpy.pause()
    scene jimmyhouselivingroomnight with fade
    $ renpy.pause()
    scene jimmytownhousenight with fade
    show blair drunk with dissolve
    Blair "I'm sorry, [player_name], but I needed your help to get in the house."
    __("[player_name] could smell the alcohol in her breath, she was very drunk but was able to talk very clearly.")
    Jimmy "Why are you drinking? It's really late for you to come home."
    Blair "Oh, come on, mom. Is that you? Ha, ha!"
    Jimmy "I just think it might be dangerous, you know."
    Blair "I was in a party at Olivia's house, and we had a fight..."
    Blair "*Sip of the bottle* And I didn't wanted to stay there anymore."
    Jimmy "Umm, sorry to hear that."
    Blair "I'm sorry too."
    __("Blair was struggling to stand on her feet, so [player_name] had an idea.")
    Jimmy "You can't even walk in this state."
    Jimmy "Hop on my back. I'll take you to your room quietly."
    __("A pretty smile formed in Blair's face, who's clear skin was even more bright with the moonlight.")
    Blair "Alright, [player_name]."
    scene blairtransport01 with fade
    __("The house was very quiet. [player_name] already had some experience sneaking in places, so the way to Blair's room was easy enough.")
    scene blairtransport02 with fade
    __("Upon reaching her bedroom, [player_name] was starting to struggle with her weight.")
    scene blairtransport03 with fade
    __("But being so close to her bed, he put her down and she woke up from her short slumber.")
    call blair_drunknight_scene from _call_blair_drunknight_scene
    $ quests.drunkblair = COMPLETE
    $ gotoscene('townhousejimmysroom')
