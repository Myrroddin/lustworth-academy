label mikuartprojectsceneintro:
    hide screen freeroamhud
    $ showscene('townhousefront', transition=fade)
    show miku casual neutral with dissolve
    play music MUSIC_MIKUS_THEME
    Miku "[player_name]! How are you?"
    Miku happy "Wow, this is such a nice place to live. Near the beach!"
    Miku seductive "You should invite me to swim one of these days!"
    Jimmy "Glad you like it. Please, come in."
    $ showscene('townhouselivingroom', transition=fade)
    stop music
    play sound "audio/sfx/doorclose01.ogg"
    show miku casual neutral with dissolve
    Jimmy "So, did you get lost?"
    Miku "No, I didn't. Turns out I've been here before."
    Jimmy "Oh, I didn't know that."
    play music MUSIC_ALICES_THEME
    show alice casual neutral left with vpunch
    Alice "Miku! I saw you from the window!"
    Alice "What are you doing here?"
    Jimmy "Oh, you two know each other?"
    Miku "Yes! That's what I was trying to say."
    Miku "I didn't know [player_name] was the [roommate_male] you told me about."
    Alice blush "Oh, yeah... Uhh, he is."
    Miku "I'm gonna create an art project with your [roommate_male], if you don't mind."
    Alice "Oh, no, don't mind me. I'll leave you to it."
    Alice "It was nice to see you!"
    Miku "Love you, bye!"
    stop music
    play music MUSIC_MIKUS_THEME
    hide alice with dissolve
    Miku "She's an angel."
    Jimmy "What about your glasses?"
    Miku "Oh, well, contact lenses, he, he. I use them when I'm not in school."
    Jimmy "Cool, your have pretty eyes."
    Miku blush "Aww, thank you, [player_name]"
    Jimmy "Alright, let's go to the backyard."
    scene jimmytownbackyard with fade
    show miku casual neutral with dissolve
    Miku "Oh, yes! This is the perfect place for what I have in mind."
    Miku "Our historical character is an indigenous girl from the colonies period called Moaning Eagle"
    play sound "audio/sfx/stopmusiceffect.ogg"
    play music "audio/music/funnymoment03.ogg"
    Jimmy "Moaning what?" with vpunch
    Miku happy "Ha, ha, ha, ha! I knew you would react like that."
    Miku "Moaning Eagle was her name."
    Miku "There is not much information on why she was named that."
    Jimmy "Well, I can come up with some ideas."
    Miku seductive "Oh, don't you dare... Ha, ha, ha."
    Jimmy "Okay, so what do you need to start?"
    Miku neutral "First, I'm gonna put on the suit and then you're gonna take some pictures with my camera."
    Jimmy "You can change in my room."
    $ showscene('townhousejimmysroom', transition=fade)
    stop music
    play music MUSIC_MIKUS_THEME
    show miku casual neutral with dissolve
    Miku "Aha! So, this is your little fortress."
    Jimmy "Yes, it is."
    Miku "Wow, you have a nice view of the beach from the window!"
    Miku seductive "It must be nice to wake up in that bed and watch the sea first thing in the morning."
    Jimmy "Oh, you should try one day."
    Miku blush "Ha, ha, yeah..."
    Miku "Well, I should get changed!"
    Jimmy "Yeah, I can wait for you outside."
    Miku "It's not necessary."
    play sound "audio/sfx/undress01.ogg"
    Miku undress01 "Just turn around, please."
    Jimmy "Alright."
    hide miku with dissolve
    play sound "audio/sfx/undress01.ogg"
    "{i}At this point, I think you already know what is going to happen next.{/i}"
    "{i}For [player_name], having a girl undressing in his room was a chance that could not go to waste.{/i}"
    "{i}So, naturally, he peeked just a bit.{/i}"
    play sound "audio/sfx/undress01.ogg"
    scene mikuundresspeek with fade
    "{i}Goddamn! Thought [player_name].{/i}" 
    "{i}In order to get some of that at the end of the day, he needed to play his cards right.{/i}"
    "{i}So, he patiently waited for her to be ready.{/i}"
    play sound "audio/sfx/undress01.ogg"
    $ showscene('townhousejimmysroom', transition=fade)
    stop music
    show miku native happy with dissolve
    play music "audio/music/nativeamericantheme.ogg"
    Miku "So, what do you think?"
    Jimmy "Holy crap... You look great!"
    Jimmy "I can even hear music..."
    Miku "Ha, ha, ha, ha, you're silly."
    Miku "I'm glad you like it. I made it myself."
    Jimmy "You have a real talent for this."
    Miku complacent "Alright, here's the camera."
    Miku "I think we should start."
    Jimmy "Say no more..."
    $ showscene('townhousebackyard', transition=fade)
    stop music
    show miku native happy with dissolve
    Miku "Alright, let's see..."
    Miku "I think I can climb that tree."
    Jimmy "Be careful."
    Miku "Don't worry, just make sure to get a nice photo."
    scene mikunativephotobefore with fade
    play music "audio/music/nativeamericantheme.ogg"
    Miku "I THINK THIS IS A GOOD SPOT!"
    Jimmy "YEAH! I CAN HEAR THE NATIVE MUSIC AGAIN!"
    Miku "WHAT MUSIC? HA, HA, HA, HA, YOU'RE SO FUNNY!"
    scene mikunativephotoafter with fade
    "{i}A long time ago, when the land was still mostly untouched by mankind, like an very very ugly woman.{/i}"
    "{i}There was a native girl named Moaning Eagle.{/i}"
    "{i}She loved to climb on big hard poles, also known as trees.{/i}"
    "{i}Maybe that's why she was called Eagle, but not everyone liked her ability to climb huge stiff logs.{/i}"
    "{i}Some of the other natives thought that she would climb just to peek on everyone's business.{/i}"
    scene mikunativephotopeaches with fade
    "{i}First thing in the morning, Moaning Eagle contributed to the wellness of her people by collecting fruit, and by sexually arousing men of the tribe, and some women too.{/i}"
    "{i}Some people questioned her about it.{/i}"
    "{i}They said that she only liked to collect fruits that looked like huge and soft balls.{/i}"
    "{i}However, she never took those words personally. She never stopped being herself.{/i}"
    scene mikunativephotofinal with fade
    "{i}In the end, her skill to climb long and thick staffs, called trees of course... Saved the village from predators more than once.{/i}"
    "{i}She warned the people by watching over the distance, spotting any danger which could approach their territory.{/i}"
    "{i}And sometimes, those big balls she collected were used as projectiles to scare predators away.{/i}"
    "{i}We could say that she was the first CCTV security system in history, but maybe that's an exaggeration.{/i}"
    "{i}Her life went on as she got pregnant twenty-six times, not knowing who the father of each child was, but she sure loved them unconditionally.{/i}"
    "{i}That's the story of Moaning Eagle. A heroic ancester and a powerful woman.{/i}"
    "{i}To this day, it is yet to be determined the origin of 'Moaning' in her name, Moaning Eagle, but I'll leave you that to think about.{/i}"
    $ showscene('townhousebackyard', transition=fade)
    stop music
    call nexttime from _call_nexttime_18
    play music MUSIC_UPBEAT
    show miku native happy with vpunch
    Miku "Wow, those photos look great, [player_name]."
    Miku "We are such a good team!"
    Jimmy "You're right. But, you're the best."
    Miku "I can't wait to show this to my mom."
    Miku "She'll love them!"
    Miku "Alright, let's take a break."
    Miku "My mom should come and pick me up anytime."
    $ showscene('townhousejimmysroom', transition=fade)
    stop music
    play music MUSIC_MIKUS_THEME
    show miku native complacent with dissolve
    Miku "Thank you so much, [player_name]"
    Miku "I had so much fun doing this."
    Jimmy "No problem. You look really nice in that suit. So, that made all the work for me."
    Miku blush "Oh, my... It's getting hot in here, don't you think?"
    Jimmy "Yes, it is..."
    Miku "Do you want to know a secret?"
    Jimmy "Sure..."
    Miku "Moaning Eagle had a third name."
    Jimmy "Did she?"
    Miku "Yes, it was Waterway."
    Jimmy "Oh, I wonder why..."
    Miku "I know why... Let me show you."
    call miku_privatemasturbation_scene from _call_miku_privatemasturbation_scene
    scene jimmytownroomafter01 with fade
    show miku casual blush with dissolve
    Miku "Oh my god, [player_name]. That was so close."
    Miku sad "Oh, no. My camera..."
    Jimmy "Fuck, I'm so sorry, Miku."
    Jimmy "I will find a way to compensate you, I promise."
    Miku "..."
    Miku "I... I should go."
    Jimmy "Let me escort you outside."
    Miku "Okay..."
    stop music
    $ quests.artProject = COMPLETE
    $ showscene('townhousefront', transition=fade)
    stop music
    play music MUSIC_MIKUS_THEME
    show miku casual blush with dissolve
    Miku "Thank you, [player_name]. I had a good time."
    Jimmy "No problem, Miku. Remember this, I will compensate you for the camera. I always keep my word."
    Miku seductive "I believe you, and we are not finished with what we started in your room."
    Jimmy "Of course not..."
    play sound "audio/sfx/carpullin.ogg"
    Miku "Oh, mom's here!"
    stop music
    $ renpy.pause()
    play music MUSIC_IZUMI_THEME
    play sound "audio/sfx/sexyintro.ogg"
    scene izumiintro with fade
    "Heads turned in unison towards the sound of a roaring engine, a blood-red Mustang rolling down the avenue." 
    "In front of it, sat a woman whose presence was as commanding as the machine she controlled." 
    "Her hair was a cascade of dark waves, tamed by a baseball hat perched atop her head."
    "Nothing could consealed the intensity that emanated from her gaze."
    "The combination that was both intimidating and undeniably alluring to [player_name]."
    "The setting sun cast a silhouette that merged with the Mustang and her figure, an embodiment of both beauty and power."
    "[player_name] would never forget that image."
    Izumi "Get in the car, Miku."
    Miku "Yes, mom."
    Miku "Bye, [player_name]!"
    "He could only watch in silence as the woman stepped in the car and left without saying a word."
    "However, she didn't stop looking at [player_name] for more than two seconds until they left, with a gaze both inviting and hair-raising."
    call nexttime from _call_nexttime_49
    $ showscene('townhousejimmysroom', transition=fade)
    Jimmy "That was... intense."
    Jimmy "I should get some rest."
    Jimmy "I gotta plan how to get a new camera for Miku."
    $ quests.mikuPhotoShoot = ACTIVE
    $ fionasKioskItems += [ItemPolaroidCamera]
    call sleep from _call_sleep_3
    $ gotoscene('townhousejimmysroom')