label chapterone_start:
    $ prologue.complete = True
    stop music
    play sound "audio/sfx/guitarriff01.ogg"
    show chapteronelabel with fade
    call nextchapter from _call_nextchapter
    pause 1.5
    jump chapterone_garycliquesintro

label chapterone_garycliquesintro:
    scene academygatefallday with fade
    play music MUSIC_UPBEAT
    $ Jimmy.outfit = JIMMY_UNIFORM
    show jimmy smug with dissolve
    "{i}[player_name] arrived at school looking forward to what the week held in store.{/i}"
    "{i}His smile quickly disappeared, however, when he saw Gary Smith, that creepy guy with the scar on his face, approaching him.{/i}"
    show jimmy neutral with dissolve
    play music MUSIC_GARYS_THEME
    show gary uniform neutral with dissolve
    Gary "Hey, new kid."
    Gary "I wasn't expecting you to come back to this hellhole."
    Jimmy talk "What's it to you?"
    Gary "Oh, hostile as ever, I see."
    Gary "I want to be your friend, [player_name]."
    Gary "So, why don't I show you my good faith, and I'll give you some advice to survive this place."
    Jimmy "...I'm listening."
    Gary "Great, come with me to the cafeteria. I'll show you what you need to know."
    hide gary with dissolve
    hide jimmy with dissolve
    "{i}[player_name] followed Gary, not because he trusted him, but because he was curious to hear what this \"survival advice\" was.{/i}"
    $ showscene('mainbuildingcafeteria', transition=fade)
    "{i}The cafeteria was full before classes started, and Gary began his speech.{/i}"
    show jimmy neutral
    show gary uniform neutral
    with dissolve
    Gary "Feeding time at the zoo... Okay, here's the deal."
    scene nerdscliqueintro onlayer cutscene with dissolve
    Gary "Over there we have the nerds."
    Gary "Their turf is the library."
    Gary "Of course, they're complete social rejects."
    Jimmy "Well, they look pretty harmless."
    Gary "They're actually sneaky bastards."
    scene prepscliqueintro onlayer cutscene with dissolve
    Gary "Those are the preps!"
    Gary "They're all money and condescending attitude."
    Jimmy "Yeah, massively inbred and completely brainless."
    Gary "Very observant, [player_name] boy."
    Gary "These pricks have a mansion for themselves in the school's back garden."
    scene greaserscliqueintro onlayer cutscene with dissolve
    Gary "Now, over there are the greasers."
    Gary "They hang by the auto shop."
    Jimmy "Oh, yeah, I saw one of those girls getting weird with a car."
    Gary "They think they're tough."
    Gary "I wouldn't advise messing with them, at least not now..."
    scene jockscliqueintro onlayer cutscene with dissolve
    Gary "And last but not least, the jocks."
    Gary "Their territory is the football field, obviously."
    Gary "These guys rule the school. {i}Definitely{/i} avoid them."
    Jimmy "Whatever, I'm not afraid of some dumb roid monkeys."
    Gary "Don't say I didn't warn you."
    hide jockscliqueintro onlayer cutscene with dissolve
    play sound SOUND_SCHOOL_BELL
    pause 0.5
    Gary "Well, there's the bell."
    Gary "Remember what I told you and you might just survive here."
    hide gary with dissolve
    pause 0.5
    "...Creep."
    hide jimmy with dissolve
    $ showscene('mainbuildingentrance', transition=fade)
    play music MUSIC_UPBEAT
    $ glob.mapUnlocked = True
    show screen freeroamhud(False)
    Developer "{i}Alright player - you're on your own now!{/i}"
    Developer "{i}Attend classes, build relationships with other students, and explore Lustworth, er,{/i} Trustworth {i}Academy.{/i}"
    Developer "{i}If you need to advance time forward, you can do so by sleeping in your bed."
    Developer "{i}Also, now that you know the lay of the land, you can use the map in the lower right to get around campus more quickly.{/i}"
    Developer "{i}If you ever get stuck, check your planner for hints.{/i}"
    Developer "{i}Oh, and one more thing - we're still working on minigames to earn money, but you can earn enough for what you need by working as an assistant for Miss Dawson.{/i}"
    Developer "{i}Okay, good luck and have fun!{/i}"
    # TODO: move this somewhere more sensible
    $ sexscenes.angiesNote = True
    $ chapter1.introCutscene = True
    $ gotoscene('mainbuildingentrance')

label chapterone_tobecontinued:
    scene tobecontinuedcartel with fade
    play music "audio/music/greasermusic01.ogg"
    pause 1.5
    scene workinprogress with fade
    Developer "{i}This is the end of the current version.{/i}"
    Developer "{i}A new version with new content will come out January 2024.{/i}"
    Developer "{i}Merry Christmas and Happy New Year everyone!{/i}"
    Developer "{i}Many of the features you have seen in this demo will be improved, expanded, and polished.{/i}"
    Developer "{i}If you like this project, consider supporting its development on our Patreon page.{/i}"
    Developer "{i}That way you will get access to the latest edition weeks before the public, in addition to other rewards.{/i}"
    scene lustworthpromo with fade
    Developer "{i}You can continue playing to complete side quests or replay the Halloween event. However, there will be no new story content.{/i}"
    Developer "{i}To replay the Halloween event, go to your closet and select a costume. Each costume unlocks a unique scene during the event.{/i}"
    Developer "{i}Reminder that you can buy costumes you don't already have from Fiona's kiosk. Here's some extra money.{/i}"
    Developer "{i}See ya!{/i}"
    stop music
    # Go to Monday morning
    call nextday from _call_nextday_4
    call nextday from _call_nextday_5
    call nextday from _call_nextday_6
    $ calendar.event = None
    $ glob.halloweenEventComplete = True
    $ Jimmy.outfit = JIMMY_UNIFORM
    $ gotoscene('boysdormjimmysroom', transition=fade)

####################################################################################################
## Beatrix
####################################################################################################

## Diary Quest #####################################################################################

label chapterone_beatrixdiaryintro:
    show jimmy neutral with dissolve
    show beatrix uniform talk with dissolve
    play music MUSIC_BEATRIX_THEME
    Beatrix "Hey, [player_name]."
    Beatrix "Umm... How are you? Um... I hope you're okay."
    Jimmy unamused "Why are you being nice to me?"
    Beatrix "Me? I've always been nice to you..."
    Jimmy "Oh, let me guess, you need something from me."
    Beatrix "Ha, ha... Wow, you're so clever. You have always been so smart, um..."
    Jimmy "Cut the crap. What do you want?"
    Beatrix "Alright, [player_name], can you help me with something?"
    Jimmy "Do I have to?"
    Beatrix "Yes, it's vital."
    Beatrix "Mandy stole my dia... my math notes."
    Beatrix "And without them, I'm gonna fail math, and then I'll never get to work at NASA."
    Beatrix "Which means I won't be able to design a spaceship to help humanity escape Earth when global warming finally starts to kill us all!"
    Beatrix "Basically, the future of the whole world rests on that notebook."
    Jimmy "Riiiiiight."
    Jimmy "What's in it for me?"
    Beatrix "Well... I can, help you with Math!"
    Jimmy "I don't need help with that."
    Beatrix "Ugh, you guys are all the same. What about a kiss?"
    Jimmy "Not enough. The future of the whole world has to be more valuable than that!"
    Beatrix mad arm "Well, if you don't, I'm gonna tell the whole school that you're a pervert who spies on girls in their dorms at night and touches himself!" with vpunch
    Jimmy "Woah, what the fuck?!"
    Jimmy "Relax, okay? I'll get you your damn notes."
    Beatrix talk "Oh, yes! Thank you!"
    Beatrix "But... There's one catch."
    Jimmy "Of course. There's always a catch."
    Beatrix "She took my di... my {i}notebook{/i} to her room."
    Jimmy "Like, in the girls' dorm? How the fuck am I supposed to get in there?"
    Beatrix mad "Figure it out, brainworm! Surely you have at least one brain cell in there."
    Beatrix "Look, I'm not very good at dealing with people. That's why I can't just get the notes myself."
    Jimmy "Wow, and here I thought you were {i}great{/i} with people. Okay, I'll try to get your notebook or whatever."
    Beatrix "Good. And don't you dare read any of it!"
    $ quests.beatrixDiary = ACTIVE
    $ gotoscene('mainbuildingrighthallway')

label chapterone_girlsdormsneak:
    scene fewmomentslater with fade
    play sound "audio/sfx/fewmomentslater.ogg"
    $ renpy.pause()
    scene girldormattic with fade
    play music MUSIC_SNEAK_THEME
    "Alright, I'm inside."
    "It smells weird in here."
    "The bedrooms must be down a floor."
    scene girlsdormhallwayfirstfloor01 with fade
    Jimmy "Umm, fancy place..."
    Jimmy "Alright, I have to look for Mandy's room."
    $ Blair.met = False
    Blair "What are you doing here?" with vpunch
    Jimmy "Oh, shit."
    show blair house neutral with dissolve
    show jimmy neutral with dissolve
    $ Blair.met = True
    Jimmy "Blair! Oh, thank God it's you."
    Jimmy "I'm looking for Mandy's room."
    Blair "Wow, you're after the most popular girl in school, way to go perv."
    Jimmy "What? No, she stole something from Beatrix and I'm getting it back."
    Blair "That's very noble of you, but you shouldn't be here."
    Jimmy "I know that, I'll leave as soon as I get the thing, alright?"
    Blair "Well, you are my [roommate_male], so I guess I should help you."
    Blair "Her room is the last door on the right."
    Blair "Be careful though, I saw Cassidy roaming around earlier with one of her friends."
    Blair "She won't be as helpful as me."
    Jimmy "You're the best. I owe you one."
    Blair "Yes, you do."
    hide blair with dissolve
    "Alright, let's see."
    scene girlsdormhallwaysecondfloor01 with fade
    "Wow, lots of doors."
    "Thanks, Blair. I would be lost without you."
    "Last door to the right."
    scene mandyroompreview with dissolve
    "Holy fuck. She really likes pink."
    "Alright, let's look the for the diary."
    "{i}After searching the shelf, [player_name] found a diary with Beatrix's name on it.{/i}"
    "This has to be it."
    call item_pickup(ItemBeatrixDiary) from _call_item_pickup_14
    "{i}[player_name] couldn't resist the urge to take a look inside the diary.{/i}"
    "{i}Beatrix lied to him about it being just math notes.{/i}"
    "{i}He realized that after reading something about a furry friend named Trevor.{/i}"
    Beatrix "{i}Last night I got too excited with Trevor.{/i}"
    Beatrix "{i}We were talking about his life on Galavan-6, how his civilization was so advanced that they could have sexual intercourse using telephatic abilities.{/i}"
    Beatrix "{i}It was so enlightening, I couldn't hold myself to show him how primitive humans do that...{/i}"
    Jimmy "There is a photo here..."
    show beatrixalienphotos with dissolve
    Jimmy "Holy shit! Is that her and... Trevor?"
    Jimmy "This girl is crazy!"
    Jimmy "I'm sure I can do something with this information."
    hide beatrixdiaryfound with dissolve
    $ Christy.met = False
    Christy "You need to get that thing out, now!" with vpunch
    "Oh, shit. Someone's coming!"
    Christy "Wait!"
    $ Cassidy.met = False
    Cassidy "It hurts too much, Christy! Leave me alone!"
    "{i}The sound of a door from another room indicated to [player_name] that this was his chance to escape.{/i}"
    scene girlsdormhallwaysecondfloor01 with fade
    "{i}Making as little noise as possible, he made his way back to the stairs.{/i}"
    scene girlsdormhallwayfirstfloor01 with dissolve
    Dawson "I don't have time for your whinning, girls."
    Dawson "There is nothing in the attic."
    Jimmy "Fuck, she's coming from upstairs..."
    "{i}Making a run for the main entrance was too risky for him, so he looked for a place to hide.{/i}"
    $ Cassidy.met = True
    call christy_dildofight_scene from _call_christy_dildofight_scene
    "{i}Still confused, [player_name] made his way out of the bathroom and up to the attic.{/i}"
    $ quests.beatrixDiary = SATISFIED
    scene fewmomentslater with fade
    play sound "audio/sfx/fewmomentslater.ogg"
    $ renpy.pause()
    $ showscene('girlsdormfrontgate', transition=fade)
    play music MUSIC_FIONAS_THEME
    show fiona clerk neutral with dissolve
    Fiona "[player_name]! You made it out!"
    Jimmy "Not without some close calls."
    Fiona "Well, I'm just glad you didn't get in any trouble."
    $ gotoscene('girlsdormfrontgate')

label chapterone_beatrixlapdance:
    Jimmy talk "You wouldn't believe what I had to do to get this thing."
    Beatrix "OH MY GOD, you found my diary! Thank you!"
    Jimmy "Diary? Weren't these your \"math notes\"?"
    Beatrix "Oh, yes, my math notes, of course..."
    Beatrix arm "Just give it to me, please!"
    Jimmy "Nuh uh. You have to give me something in return."
    Jimmy "I almost got caught in Mandy's room."
    Beatrix "Ugh, take this."
    $ Jimmy.money += 25
    call yougotmoney from _call_yougotmoney_7
    Jimmy "I don't think the money is enough for the trouble."
    Beatrix "What do you want? I have notes from all the classes if you want."
    Jimmy smug "Well, I can think about a lot of things I want, but none of them involve class notes."
    Beatrix "What? I..."
    play sound "audio/sfx/mad01.ogg"
    Beatrix mad arm "Oh my God, [player_name]. Are you thinking about sex?" with vpunch
    Jimmy "Well, now that you mention it..."
    Beatrix "Of course you're thinking about sex. Why do guys always think with their dick?"
    Beatrix "I thought we had a special friendship going on here."
    Jimmy "Friendships should come with some benefits, don't you think?"
    Jimmy "And after what I did for you, I think I deserve some real good benefits."
    Beatrix "I'm not gonna have sex with you, [player_name]."
    Jimmy unamused "That's too bad."
    Jimmy "I don't think Trevor's gonna be happy when he finds out you're ungrateful to your friends."
    Beatrix "..."
    Beatrix "Did you read my diary?"
    Beatrix "You... you..."
    play sound "audio/sfx/mad02.ogg"
    Beatrix mad "AGGGHHHHHH!" with vpunch
    Jimmy "I'm sure you wouldn't want the whole school to know about him."
    Beatrix "I can't believe you're blackmailing me with this..."
    Jimmy smug "Consider it a taste of your own medicine, miss."
    Beatrix "Ugh. Would a lap dance be enough of a reward for you?"
    Jimmy "Well, it's better than nothing."
    Beatrix "I can't believe I'm about to do this..."
    Beatrix mad arm "Come inside the math classroom."
    call beatrix_lapdance_scene from _call_beatrix_lapdance_scene_1
    $ Beatrix.relPoints += 1
    $ quests.beatrixDiary = COMPLETE
    $ Jimmy.inventory.remove(ItemBeatrixDiary)
    call nexttime from _call_nexttime_30
    $ gotoscene('mainbuildingrighthallway', transition=fade)
