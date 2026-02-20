default quests.punnyPrivateLessons = LOCKED
default quests.punnyDatingTeacher = LOCKED

label misspunnyprivatelesson01:
    Jimmy "I'm gonna pay for a private lesson, Miss."
    play sound "audio/sfx/hmm03.ogg"
    Punny "Oh! That's such good news!"
    Punny "Muchas gracias, Mr. [player_surname]."
    $ Jimmy.money -= 100
    Punny desk arm "I have something special for our first lesson."
    Punny "Meet me by the plaza with the golden statue in a couple of hours and we'll start, ¿esta bien?"
    Jimmy "Yeah, alright."
    stop music
    scene laterthatday with fade
    $ renpy.pause()
    $ showscene('schoolgroundspeacockplaza', transition=fade)
    show misspunny teacher neutral with dissolve
    play sound "audio/sfx/hey04.ogg"
    Punny "Mr. [player_surname]! Everything is ready now."
    Punny "Do you like hiking?"
    Jimmy "Well, I don't mind taking a walk from time to time."
    play sound "audio/sfx/giggle01.ogg"
    Punny lean "That's great, because we'll be going up the hill to have a picnic!"
    Jimmy "Oh, food I always like."
    play sound "audio/sfx/giggle02.ogg"
    Punny "Ha, ha, ha, que gracioso."
    Punny "¡Vamos!"
    stop music
    play sound "audio/sfx/20minlater.ogg"
    scene twentyminuteslater with fade
    $ renpy.pause()
    $ showscene('observatoryhillexterior', transition=fade)
    "{i}After walking for a while longer than he expected, [player_name] and Miss Punny arrived to the area near the observatory.{/i}"
    "{i}The sun was shining, and the breeze was gentle.{/i}"
    "{i}A picnic blanket was spread out with various foods: fruits, bread, and juice.{/i}"
    scene misspunnypicnic01 with fade
    play sound "audio/sfx/girlsigh01.ogg"
    play music MUSIC_MISSPUNNY_THEME
    Punny "Alright, I know there is no better motivation for a student than having a full stomach."
    Punny "I hope you like the bread, I made it myself."
    Jimmy "Wow, I didn't expect any of this."
    Jimmy "Gracias, Miss."
    play sound "audio/sfx/gasp01.ogg"
    Punny "Aha! You're eager to talk in Spanish. ¡Eso es muy bueno!"
    Punny "Let's see if you can identify any food in Spanish, alright?"
    Jimmy "Si, ¿dónde está la biblioteca?"
    Jimmy "That's all I know... From a movie."
    play sound "audio/sfx/giggle01.ogg"
    Punny "Ha, ha, ha, you don't want to walk all the way down to the library just now."
    Jimmy "Oh, no, I want to eat first."
    Punny "Sírvase, entonces."
    play sound "audio/sfx/undress01.ogg"
    play music MUSIC_FUNNY_MOMENT
    scene misspunnypicnic02 with fade
    Jimmy "How do you say this in Spanish?"
    Punny "Eso es una manzana. Muy fácil, ¿no?"
    Jimmy "Muy fácil. Manzana. Got it."
    scene misspunnypicnic03 with dissolve
    play sound "audio/sfx/teapour.ogg"
    Jimmy "And what about this one?"
    Punny "Eso es queso. Queso amarillo."
    Jimmy "Queso amareello, right... I’m getting the hang of this."
    scene misspunnypicnic04 with fade
    "{i}The lesson continues and the conversation flows naturally, as well as the food towards the digestive system.{/i}"
    Jimmy "So, Miss, how did you become so good at Spanish?"
    play sound "audio/sfx/femaleclearthroat.ogg"
    Punny "Well, you know, growing up in a Spanish-speaking household helps a lot."
    Jimmy "Interesting. How about this fruit?"
    Jimmy "It has a strange look inside."
    play sound "audio/sfx/surprisedhum.ogg"
    Punny "Oh, I've never seen such a shape. It looks like a..."
    Punny "Nevermind, it's a toronja."
    Jimmy "Toronja, I like it."
    play sound "audio/sfx/girlsigh01.ogg"
    Punny "Deberías chuparla..."
    Jimmy "Sorry?"
    Punny "You should taste it, it's very sweet."
    Jimmy "No doubt about it."
    play sound "audio/sfx/undress01.ogg"
    scene misspunnypicnic05 with fade
    play music MUSIC_TENDER01_THEME
    "{i}For a while, they shared a moment of silence, enjoying the view and the company.{/i}"
    "{i}[player_name] looks at Miss Punny, noticing how the soft sunlight makes her skin glow, realizing how beautiful she was...{/i}"
    scene misspunnypicnic06 with fade
    "{i}And how sexy she was too. That one is called 'banana', by the way.{/i}"
    play sound "audio/sfx/undress01.ogg"
    scene misspunnypicnic07 with fade
    Jimmy "Thank you, Miss."
    Jimmy "I really appreciate the effort. It's not just the lesson, but spending time with you."
    Punny "I've enjoyed it too, Mr. [player_surname]."
    Jimmy "Please, you can call me [player_name], Miss."
    play sound "audio/sfx/hum01.ogg"
    Punny "I shouldn't because I'm your teacher but, alright [player_name]. It's nice to get to know you better outside of the classroom."
    Punny "It must be difficult for you to adapt in a new school, meeting new people and getting used to living in this town."
    Jimmy "Well, it's been strange, but, not that bad. As long as I get to eat queso amareello with you, todo está bien."
    play sound "audio/sfx/giggle01.ogg"
    Punny "Ha, ha, ha, ha! You're so funny."
    Jimmy "I really loved the food, Miss."
    Jimmy "Your husband must be so happy, eating such good bread for breakfast."
    Punny "My husband? Oh..."
    play sound "audio/sfx/girlsigh01.ogg"
    Punny "..."
    "{i}Her expression suddenly changed as [player_name] started questioning if he said something wrong.{/i}"
    "{i}A long silence made things even more uncomfortable.{/i}"
    Punny "Oh, el tiempo vuela! I think it's time to get back."
    call nexttime from _call_nexttime_39
    $ showscene('observatoryhillexterior', transition=fade)
    show misspunny teacher lean with dissolve
    play sound "audio/sfx/giggle02.ogg"
    Punny "That was fun!"
    Punny "I hope you enjoyed your lesson."
    play sound "audio/sfx/femaleclearthroat.ogg"
    Punny suggestive "I'm gonna be busy for now with some stuff I have to do in the Auditorium, so..."
    Punny "We can have our next lesson next week?"
    Jimmy "Sure, Miss. I'll have the money ready for next week."
    Punny "¡Perfecto! Cuídate, [player_name]."
    hide misspunny with dissolve
    Jimmy "Seems like I said something wrong..."
    Jimmy "I think it was when I mentioned her husband."
    Jimmy "Anyways, I got stuff to do."
    $ quests.punnyPrivateLessons = SATISFIED
    $ gotoscene('observatoryhillexterior')

label misspunnydancinglesson:
    hide screen freeroamhud with None
    $ showscene('mainbuildingauditorium', transition=fade)
    play music "audio/music/salsatheme01.ogg"
    "{i}The auditorium was empty as a soft, golden light cast a warm glow over the scenario.{/i}"
    "{i}Music with a rythmic melody and tropical sounds played softly in the background.{/i}"
    "{i}Miss Punny stood in the middle of the floor, dressed with clothes that make her attributes stand out.{/i}"
    scene misspunnydancinglesson01 with fade
    play sound "audio/sfx/gasp01.ogg"
    Punny "[player_name]! What are you doing here?"
    Jimmy "Hello, Miss. I wanted to stay in school for the weekend to get some work done."
    Jimmy "And I remembered you said something about the auditorium, and I couldn't resist coming to see you."
    play sound "audio/sfx/giggle01.ogg"
    Punny "Oh, that's so cute. Well, come closer, then."
    Punny "Now that you're here. What do think about learning to dance Salsa?"
    Jimmy "Salsa, me gusta. But I warn you, I have two left feet."
    play sound "audio/sfx/laugh03.ogg"
    Punny "Ha, ha, ha, we'll see about that."
    Punny "Just follow my lead. First, let's start with the basic steps."
    scene misspunnydancinglesson02 with fade
    play music "audio/music/salsatheme02.ogg"
    "{i}With fluid and graceful movements, Miss Punny starts moving her feet right and left.{/i}"
    "{i}[player_name] watches intently, trying to mimic her steps.{/i}"
    Punny "You're doing great! Just remember to keep your hips loose and follow the rhythm."
    scene misspunnydancinglesson03 with fade
    play sound "audio/sfx/crowdshock01.ogg"
    "{i}[player_name] fumbles a bit, trying to keep up with Miss Punny's instructions, as she moves closer to him.{/i}"
    "{i}He steps on her foot accidentally and quickly apologizes.{/i}"
    Jimmy "Sorry! I told you, I'm not much of a dancer."
    Punny "You're doing fine! Just relax and enjoy the moment."
    play sound "audio/sfx/alright06.ogg"
    "{i}Gradually [player_name] started to become more comfortable with the steps.{/i}"
    "{i}She took his hand, guiding him through the more complicated movements as there was a growing connection between them.{/i}"
    "{i}There was something about the music and the dance that made them feel closer and closer. Passion brewed inside them.{/i}"
    play sound "audio/sfx/big_punch.ogg"
    scene misspunnydancinglesson04 with fade
    Jimmy "I think I'm getting the hang of it!!"
    play sound "audio/sfx/wow01.ogg"
    Punny "Wow, maybe not that much flair! But I love the enthusiasm."
    "{i}Suddenly, their eyes lock. There's a palpable chemistry between them, and for a brief moment, it felt almost romantic.{/i}"
    play sound "audio/sfx/stopmusiceffect.ogg"
    stop music
    "{i}But then, [player_name] tripped over his own feet, his hands pulling Miss Punny to the ground with him.{/i}"
    play sound "audio/sfx/big_punch_trimmed.ogg"
    scene misspunnydancinglesson05 with vpunch
    play sound "audio/sfx/sexyintro.ogg"
    "{i}They both looked at each other for a while in silence. Neither of them moved, not even an inch.{/i}"
    "{i}He could feel her breathing on his skin and the heat emanating from their sweaty bodies.{/i}"
    play sound "audio/sfx/hmm01.ogg"
    Punny "..."
    Jimmy "..."
    $ showscene('mainbuildingauditorium', transition=fade)
    play music MUSIC_TENDER01_THEME
    show misspunny dancer displeased with dissolve
    Jimmy "Sorry, Miss. That wasn't part of the plan."
    play sound "audio/sfx/femaleclearthroat.ogg"
    Punny "Don't worry, darling."
    Punny "I... I just..."
    Punny "This reminds me of my husband..."
    Punny "You mentioned him the other day and I was kind of rude to you."
    Punny "He was in the army, you know?" 
    play sound "audio/sfx/hum01.ogg"
    Punny "And we used to dance like this whenever he was home."
    Punny "He's... missing in action now."
    Jimmy "I'm so sorry, Miss. I didn't know that."
    Punny "It's okay. Dancing with you tonight brought back some beautiful memories."
    Punny "I felt the same genuine connection I used to feel with him."
    play sound "audio/sfx/girlsigh01.ogg"
    Punny "Thank you for that, [player_name]."
    Jimmy "I'm honored, Miss."
    Punny suggestive "Please, you can call me Lucía."
    Jimmy "Wow, that's a beautiful name."
    play sound "audio/sfx/giggle01.ogg"
    Punny "Thank you, guapo."
    Punny "See you after Halloween for the next lesson?"
    Punny "Of course, Miss... Sorry, Lucía. I'll see you next week."
    hide misspunny with dissolve
    play sound "audio/sfx/highheels.ogg"
    $ quests.punnyPrivateLessons = COMPLETE
    call nexttime from _call_nexttime_40
    stop music
    stop sound
    $ gotoscene('mainbuildingentrance')

label misspunnyprivatelesson02:
    Jimmy "Hey, Lucía. I'm here for our next lesson."
    play sound "audio/sfx/alright01.ogg"
    Punny "Alright! Let's get started, then. Today, we're going to learn some anatomy terms in Spanish."
    Punny "I'm sure you'll love this lesson..."
    scene laterthatday with dissolve
    if calendar.when[2] == MORNING:
        call nexttime from _call_nexttime_41
        call nexttime from _call_nexttime_42
        call nexttime from _call_nexttime_43
    elif calendar.when[2] == AFTERNOON:
        call nexttime from _call_nexttime_44
        call nexttime from _call_nexttime_45
    elif calendar.when[2] == EVENING:
        call nexttime from _call_nexttime_46
    "{i}They spent the rest of the day practicing what [player_name] learned in the last lesson, and getting the basics of anatomy in Spanish.{/i}"
    play sound "audio/sfx/laugh01.ogg"
    Punny "HA, HA, HA! It's not cerveza! It's CABEZA! HA HA HA!" with vpunch
    play music MUSIC_FUNNY_MOMENT
    scene spanishclassroomfallnight with fade
    show misspunny teacher neutral with dissolve
    Punny "Alright, we're going to do something different now. I'll use my body to point to some parts of it and you must name them in Spanish."
    Jimmy "Cool, cool, I'm ready."
    scene misspunnyanatomy01 with fade
    Punny "Let's start with the head..."
    menu:
        "Pierna":
            play sound "audio/sfx/wrongfx.ogg"
            Jimmy "La pierna?"
            Punny "Oh, no... It's Cabeza."
        "Cabeza":
            play sound "audio/sfx/correctfx.ogg"
            Jimmy "La cerve... La cabeza!"
            Punny "Good job!"
        "Mano":
            play sound "audio/sfx/wrongfx.ogg"
            Jimmy "La mano?"
            Punny "Oh, no... It's Cabeza."
    scene misspunnyanatomy02 with fade
    Punny "What about these..."
    menu:
        "Pierna":
            play sound "audio/sfx/wrongfx.ogg"
            Jimmy "La pierna?"
            Punny "Oh, no... It's los ojos."
        "Cuello":
            play sound "audio/sfx/wrongfx.ogg"
            Jimmy "El cuello?"
            Punny "Oh, no... It's los ojos."
        "Los ojos":
            play sound "audio/sfx/correctfx.ogg"
            Jimmy "Los ojos."
            Punny "Good job!"
            Jimmy "Muy bonitos."
            play sound "audio/sfx/giggle01.ogg"
            Punny "Ha, ha, ha, thank you so much..."
    scene misspunnyanatomy03 with fade
    Punny "And these..."
    menu:
        "Piernas":
            play sound "audio/sfx/correctfx.ogg"
            Jimmy "Las piernas?"
            Punny "Good job!"
        "Los brazos":
            play sound "audio/sfx/wrongfx.ogg"
            Jimmy "Los brazos?"
            Punny "Oh, no... It's las piernas."
        "Corazón":
            play sound "audio/sfx/wrongfx.ogg"
            Jimmy "El corazón?"
            Punny "Oh, no... It's las piernas."
    scene misspunnyanatomy04 with fade
    Punny "Next, we have..."
    menu:
        "Pecho":
            play sound "audio/sfx/wrongfx.ogg"
            Jimmy "El pecho?"
            Punny "Oh, no... It's los pies."
        "Pies":
            play sound "audio/sfx/correctfx.ogg"
            Jimmy "Los pies!"
            Punny "Good job!"
            Jimmy "Muy bonitos too."
            play sound "audio/sfx/giggle02.ogg"
            Punny "Ha, ha, ha, stop it..."
        "Dedos":
            play sound "audio/sfx/wrongfx.ogg"
            Jimmy "Los dedos?"
            Punny "Oh, no... It's los pies."
    scene misspunnyanatomy05 with fade
    Punny "And lastly..."
    menu:
        "Tetas":
            play sound "audio/sfx/wrongfx.ogg"
            Jimmy "Las tetas?"
            play sound "audio/sfx/laugh03.ogg"
            Punny "HA HA HA HA HA HA HA HA HA!"
            Punny "Oh, my god! [player_name]! No!"
            Punny "It's el corazón!"
            Jimmy "Oh, I'm sorry, Lucía."
        "Corazón":
            play sound "audio/sfx/correctfx.ogg"
            Jimmy "El corazón!"
            Punny "Good job!"
        "Nalgas":
            play sound "audio/sfx/wrongfx.ogg"
            Jimmy "Las nalgas?"
            play sound "audio/sfx/laugh01.ogg"
            Punny "HA HA HA HA HA HA HA HA HA!"
            Punny "Oh, my god! [player_name]! No!"
            Punny "It's el corazón!"
            Jimmy "Oh, I'm sorry, Lucía."
    scene spanishclassroomfallnight with fade
    show misspunny teacher neutral with dissolve
    play music MUSIC_TENDER01_THEME
    Jimmy "Ugh... How did I do?"
    play sound "audio/sfx/surprisedhum.ogg"
    Punny "Don't worry, darling. You're doing great!"
    Punny "Now, I know we are adults, so I would like to show you a couple of things to finish off this lesson."
    play sound "audio/sfx/alright02.ogg"
    Punny "It's about genitals, alright?"
    Punny "It's important to know them in Spanish, too."
    Jimmy "Right..."
    Punny surprised "Oh, my god! It's so late! I'm so sorry for this."
    Jimmy "No problem, Miss. I like to spend my time learning with you."
    play sound "audio/sfx/giggle01.ogg"
    Punny lean "Awww, thank you so much, I'm so glad you're here."
    Punny "I... I don't know about you, but..."
    Punny "I've felt a connection since we started with these lessons."
    Punny "That day we danced in the auditorium, it felt amazing..."
    Jimmy "Lucía, every moment with you has been special."
    Jimmy "Your husband is a lucky man, because your heart belongs to him..."
    play sound "audio/sfx/hum01.ogg"
    Punny displeased "It's has been so long..."
    Punny "He went missing almost three years ago."
    Punny "I've have felt so lonely, trying to grasp some kind of hope of him to coming back."
    Punny "But, I don't know anymore..."
    Jimmy "Wow, that's a long time."
    Punny suggestive "Yes, too long since I feel something like what I felt with you when we danced."
    play sound "audio/sfx/femaleclearthroat.ogg"
    Punny "I felt alive again. I felt like there was someone having my back again."
    Jimmy "You don't have to be alone, anymore, Lucía."
    Jimmy "I'm here for you, if it means anything."
    Punny "Oh, [player_name]. You're so guapo and gentle."
    Punny "You know how to make a girl blush..."
    call punny_69lesson_scene from _call_punny_69lesson_scene
    scene spanishclassroomfallnight with fade
    show misspunny topless cum with dissolve
    stop music
    play sound "audio/sfx/mh1.ogg"
    Punny "Me encantó, papi."
    Jimmy "A mi también..."
    Punny "Mhm, you learn so fast."
    Punny "It's such a great feeling to be desired once again."
    Punny "Oh, [player_name]. I want to do this again, soon."
    Jimmy "I would love that, Lucía."
    play sound "audio/sfx/hmm02.ogg"
    Punny "¿Quieres ir a mi casa?"
    Jimmy "Ummm, casa?"
    play sound "audio/sfx/giggle01.ogg"
    Punny "Ha, ha, ha, you cute little devil..."
    Punny "I'm gonna invite you for dinner at my house."
    Punny "Here's the adress."
    play sound "audio/sfx/undress01.ogg"
    show misspunnyaddress with dissolve
    Jimmy "Humm, that's..."
    Jimmy "I think that's on the same street I live now!"
    play sound "audio/sfx/undress01.ogg"
    hide misspunnyaddress with dissolve
    Punny "Oh, that's even better! We're neighbors!"
    Punny "Please, come by Saturday night."
    Punny "I know you like my food, so I'm gonna cook something good for you."
    Jimmy "Oh, yeah, and now I like your toronja as well."
    play sound "audio/sfx/laugh02.ogg"
    Punny "HA HA HA HA HA, you're silly."
    Punny "You should get dressed and go back to the dorm."
    Punny "It's too late for you to be here."
    Jimmy "Alright, Lucía, I'll see you this weekend."
    play sound "audio/sfx/girlsigh01.ogg"
    Punny "Te espero, guapo."
    $ quests.punnyDatingTeacher = ACTIVE
    $ gotoscene('mainbuildingentrance')

label punnyromanticdinner:
    play music MUSIC_TENDER01_THEME
    scene punnyhouselivingroomnight with fade
    play sound "audio/sfx/highheels.ogg"
    "{i}The aroma of freshly cooked paella filled the cozy, dimly lit dining room.{/i}"
    "{i}[player_name] could hear the faint notes of a soft melody playing in the background.{/i}"
    show misspunny gala talk with dissolve
    play sound "audio/sfx/doorclose01.ogg"
    "{i}Lucía, draped in a stunning red dress that accentuated her graceful figure, moved with elegant ease as she already had the table ready for two.{/i}"
    "{i}As she heard the door knocking sound, a smile played on her lips, a blend of anticipation and nervous excitement.{/i}"
    "{i}She opened the door to find [player_name] standing there, and her eyes lit up.{/i}"
    play sound "audio/sfx/gasp02.ogg"
    Punny suggestive "[player_name]! Estás aquí!"
    Jimmy "You look breathtaking, Lucía."
    Punny "Thank you so much, entra, por favor."
    Punny talk "You came just in time."
    Punny "Dinner is ready, are you hungry?"
    Jimmy "Oh, yes, I'm starving."
    play sound "audio/sfx/giggle01.ogg"
    Punny "I like your jacket! You look manly in it."
    Jimmy "Thanks, ha, ha. I'm really sorry I didn't bring something more adequate."
    Jimmy "Seeing you in that dress, makes me feel like an idiot."
    play sound "audio/sfx/femaleclearthroat.ogg"
    Punny suggestive "Ahh, don't worry. You're so young and handsome, anything you wear suits you."
    Jimmy "You're too kind."
    Punny "Well, let's stop talking and let's get to the important stuff."
    Jimmy "Yes, ma'am!"
    scene punnyromanticdinner01 with fade
    "{i}They settled at the table, and the little amount of conversation that wasn't interrumpted by chewing, flowed effortlesly.{/i}"
    play sound "audio/sfx/giggle02.ogg"
    "{i}There was an undoubtable growing connection between them, nurtured through those private lessons that ended up with a such a climatic scene.{/i}"
    play sound "audio/sfx/teapour.ogg"
    "{i}As they sipped on a rich red wine, Lucía felt a sense of joy she hadn't experienced in a long time, since her husband dissapeared.{/i}"
    "{i}Yet, there was doubt clouding her mind, a feeling of sadness that refused to be silenced.{/i}"
    scene punnyhouselivingroomnight with fade
    show misspunny gala talk with dissolve
    Punny "[player_name], I've been meaning to tell you something."
    Jimmy "What is it?"
    play sound "audio/sfx/girlsigh01.ogg"
    Punny displeased "It's just... Sharing this time with you has brought so much joy into my life, again."
    Punny "More than I ever thought possible after everything that's happened." 
    Punny "But there's something I need you to understand."
    Jimmy "You can tell me anything."
    play music "audio/music/sadmoment01.ogg"
    Punny "It's about my husband..."
    Punny "You already know I haven't had any news of his whereabouts in years."
    Punny "I don't even know if he's still alive." 
    play sound "audio/sfx/frustratedhum.ogg"
    Punny "It's been so hard to move on, to find happiness again."
    Punny "But being with you... It feels strange but, so right, so natural."
    play sound "audio/sfx/hum01.ogg"
    Punny "And yet, there's this part of me that feels guilty for allowing myself to feel this way."
    Jimmy "Lucía, you deserve to be happy."
    Jimmy "Life has a way of taking unexpected turns."
    Jimmy "But right now, in this moment, I am here with you."
    Jimmy "That's all that matters."
    play sound "audio/sfx/girlsigh01.ogg"
    Punny "Thank you, [player_name]. For everything."
    "{i}They finished the bottle of wine, their conversation meandering through memories and shared dreams.{/i}"
    "{i}As the night grew darker, Lucía felt a desire she could no longer ignore.{/i}"
    Punny "Would you like to come to my bedroom?"
    Jimmy "I'd love to."
    Jimmy "But, I need to go to the bathroom, first."
    Punny "Alright, I'll be waiting for you there..."
    stop music
    play sound "audio/sfx/doorclose01.ogg"
    scene punnyhousebathroomnight with fade
    Jimmy "Holy shit, this is happening."
    Jimmy "I feel bad for her... All the stuff about her husband."
    Jimmy "But, we're not doing anything bad, right?"
    Jimmy "It's been a long time, so..."
    Jimmy "Stop thinking stupid shit, [player_name]."
    Jimmy "Let's do this!"
    play music "audio/music/sensualtrap.ogg"
    scene punnyhousebedroomnight with fade
    Jimmy "Lucía?"
    show misspunny lingerie suggestive with dissolve
    Punny "Yes, [player_name]?"
    Jimmy "Wow..."
    play sound "audio/sfx/girlsigh01.ogg"
    Punny "Come to me, I want to enjoy this moment with you..."
    call punny_dinnersex_scene from _call_punny_dinnersex_scene
    play sound "audio/sfx/undress01.ogg"
    scene punnyhousebedroomnight with fade
    show misspunny naked cum
    Punny "Will I see you next week?"
    Jimmy "Of course, we haven't finished with my lessons."
    play sound "audio/sfx/giggle01.ogg"
    Punny "Tell you what, because of the way you made me scream tonight, the next class will be for free."
    Jimmy "Nice, now we're talking."
    Jimmy "If you want me to make you scream again, just let me know."
    Punny "Ha, ha, ha, por supuesto, así será."
    Punny "Let me accompany you."
    play sound "audio/sfx/hmm01.ogg"
    Punny "Uh, I'm so full of cum... I can't walk like this."
    Jimmy "Don't worry, I can walk a couple of houses, he, he."
    Punny "Alright, good night, [player_name]."
    Jimmy "Good night, Lucía."
    scene nightsky with fade
    $ quests.punnyDatingTeacher = SATISFIED
    call nextday from _call_nextday_1
    $ renpy.pause()
    $ gotoscene('townhousejimmysroom')

label punnyhusbandarrival:
    show misspunny teacher neutral with dissolve
    Punny "Good day, [player_name]."
    Punny "Thank you so much for that dinner."
    Punny "It was such a great night."
    Jimmy "It was amazing."
    Punny lean "Are you here for our next lesson?"
    Jimmy "Yes, I mean, it's free, right?"
    play sound "audio/sfx/giggle01.ogg"
    Punny "Yeah, I keep my word, ha, ha, ha..."
    Punny "Alright, let's..."
    play sound "audio/sfx/dooropen01.ogg"
    stop music
    play music MUSIC_TENDER01_THEME
    show jakesarrival with dissolve
    Jake "Lucía?"
    play sound "audio/sfx/gasp01.ogg"
    Punny "..."
    play sound "audio/sfx/doorclose01.ogg"
    "{i}After hearing that voice, Lucía froze and couldn't move for a moment.{/i}"
    "{i}A man wearing a military uniform was standing near the door of the classroom.{/i}"
    "{i}[player_name] already figured out who he was...{/i}"
    $ quests.punnyDatingTeacher = COMPLETE
    $ gotoscene('mainbuildingrighthallway')