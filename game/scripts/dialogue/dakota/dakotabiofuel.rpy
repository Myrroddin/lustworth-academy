default quests.dakotaBioFuel = LOCKED

label dakotabiofuelintro:
    hide screen freeroamhud
    scene dakotafarmhouselivingroomintro with fade
    __("{i}The air at the ranch that day smelled like hard work, wet hay, and things that had passed through a digestive tract.{/i}")
    __("{i}And that's exactly what [player_name] needed.{/i}")
    show dakota cowgirl neutral with dissolve
    Jimmy "Hey, Dakota. How are you doing this weekend?"
    play sound "audio/sfx/hey04.ogg"
    Dakota "Well, if it ain't my favorite city boy!"
    Dakota "I bet you just miss the sound of my voice tellin' you you're holdin' the shovel on the wrong side?"
    Jimmy "Oh, yeah. I love the sound of your voice, but I wanted to ask your permission on something."
    Dakota teasing "Permission? How can I deny anythin' to that pretty face of yours. What you lookin' for?"
    Jimmy "Manure. Specifically the fresh stuff."
    Jimmy "And maybe some spoiled fruit or compost if you've got it."
    Jimmy "I'm helping Alice, my [roommate_female], to build something that needs... well, let's just say it's a very 'organic' project."
    Dakota "You want to shovel horse pucky? You and your little [roommate_female] got a weird hobby, kid."
    Jimmy "Don't tell me... So, what do you say?"
    Dakota "Tell you what. I'll give you all the pucky you can carry." 
    Dakota neutral "But... I'm lookin' for some young, sturdy backs for the Autumn Harvest Festival in a couple of weeks."
    Jimmy "A festival? The kind where you compete for the size of a cucumber?"
    Dakota "That's right, kiddo. The best festival in Peacock Valley."
    Dakota "It's a whole weekend of chaos, so I need a hand with the heavy liftin'."
    Dakota "And maybe makin' sure the local punks don't tip the port-a-potties."
    Dakota "You agree to show up and sweat, and the manure is yours for the takin'."
    Jimmy "Great. I'll trade my future weekend for horse crap. You've got a deal."
    Dakota cowgirl seductive "Ahh, the things we do for the family."
    Dakota "Now, my daughter Barbara is at the barn checkin' the stalls." 
    Dakota "Go find her. She'll show you which pile is the fresh one."
    Jimmy "Barbara? Right. Thanks, Dakota."
    $ quests.dakotaBioFuel = ACTIVE
    $ gotoscene('dakotasranch')

label barbarabiofuelscene:
    hide screen freeroamhud
    scene dakotafarmbarn01 with fade
    play music MUSIC_BARBARA_THEME
    "{i}[player_name] spotted Barbara near the back stalls with that ponytail that was holding on for dear life.{/i}"
    show barbara casual neutral with dissolve
    Barbara "[player_name]! You're back!"
    Barbara "I thought I heard you coming, or maybe it was just my heart doin' a little line dance."
    Barbara "Did Mama send you back here to help me?"
    Jimmy "Actually, I'm here to get some horse shit, not for free..."
    Jimmy "Dakota already signed me up for your Harvest Festival weekend so I'm part of the crew now."
    Barbara excited "The Festival?! Oh, that's amazing! We can be like... the Dream Team!"
    Barbara "Oh, it's gonna be so cool, you and me working together!"
    scene barbarasexybiofuel01 with fade
    __("{i}Barbara suddenly leaned against a wooden post, trying to look like a calendar model{/i}")
    __("{i}However, she was anything but a model.{/i}")
    Barbara "Hold on, I just need to stretch my back..."
    Barbara "Oh, I think I can see my nose like this..."
    scene barbarasexybiofuel02 with vpunch
    __("{i}She tried doing a pose on a chair and tried to wink, but both eyes closed at the same time.{/i}")
    Barbara "A city boy like you probably likes those skinny girls in the cheerleader outfits at the high school."
    Barbara "I can be 'peppy' too, [player_name]. Watch."
    Jimmy "Look, you're... great, Barbara. Really."
    Jimmy "But right now, I need the horse shit."
    scene barbarasexybiofuel03 with fade
    Barbara "Be patient, cutie. Let me stretch my legs a little bit."
    __("{i}Barbara put herself in an uncomfortable position in front of one of the horses and...{/i}")
    scene barbarasexybiofuel03b with vpunch
    play sound "audio/sfx/horse01.ogg"
    Jimmy "Whoa! Hey there, brother."
    Jimmy "I think your horse just got a little... *too* excited for your routine."
    Barbara "Ha, ha, ha, ha. Oh, hush! That's just Duke."
    Barbara "At least *someone* around here appreciates a hard-working girl."
    Jimmy "Sure..."
    Barbara "Alright, let me help you get the poopoo."
    scene barbarasexybiofuel04 with fade
    __("{i}They spent the next twenty minutes shoveling the manure.{/i}")
    __("{i}Barbara kept 'accidentally' bumping into [player_name]'s shoulder and lingering a little too long when handing over the buckets.{/i}")
    scene barbarasexybiofuel04b with vpunch
    Barbara "Oh, it's so hot in here..."
    Barbara "Let me just, take some air between my..."
    Jimmy "..."
    Jimmy "Okay, that's enough shit."
    scene dakotafarmbarn01 with fade
    show barbara casual neutral with dissolve
    Jimmy "Do you know where I can get some rotten fruit?"
    Barbara thinking "Rotten fruit? The old apple tree down by the lake shore is practically a graveyard for fruit right now."
    Barbara "They've been fallin' and fermentin' in the sun for weeks."
    Jimmy "The lake shore. Got it. Thanks, Barb."
    Jimmy "Try not to pull a muscle doing those *sexy* poses in front of Duke."
    Barbara "I'll be waitin' for you at the festival, [player_name]!"
    Barbara "Don't let the mosquitoes bite that cute little face!"
    $ quests.dakotaBioFuel = SATISFIED
    $ gotoscene('dakotasranch')

label sallybiofuelscene:
    hide screen freeroamhud
    scene ranchlakeshoreday with fade
    play music MUSIC_RANCHLAKE_THEME
    "{i}The air near the lake was cold and fresh. [player_name] spotted the old apple tree drooping over the bank like it had a hangover.{/i}"
    Jimmy "Alright, let's get this over with."
    __("{i}[player_name] started looking for a couple of bruised, brown apples.{/i}")
    __("{i}It felt so peaceful there that for a moment [player_name] forgot about he was looking for, just admiring the view and the sound of nature.{/i}")
    play sound "audio/sfx/watersplash.ogg"
    __("{i}Suddenly a strange sound coming from the lake, put him on alert.{/i}")
    __("{i}It wasn't a fish. Unless the fish in Peacock Valley had well toned arms and shiny blonde hair.{/i}")
    __("{i}[player_name] crept through the tall grass, the lake surface was broken by a figure. It was Sally.{/i}")
    call sally_lakemeeting_scene from _call_sally_lakemeeting_scene
    $ quests.dakotaBioFuel = COMPLETE
    $ quests.aliceScienceProject = SATISFIED
    $ gotoscene('dakotasranch')