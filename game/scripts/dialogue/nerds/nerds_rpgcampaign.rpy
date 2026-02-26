label rpgcampaignintro:
    hide screen freeroamhud with None
    show algie uniform smug with dissolve
    Algie "Ah! The finest marksman of the kingdom is back!"
    Algie "Did you feel the majestic power of the Meteorator?"
    play sound "audio/sfx/clearthroat01.ogg"
    Jimmy "It did the job, I guess. Bucky's back, and nobody lost an ear, which is a win in my book."
    Jimmy "And I managed to scare away a bunch of jerks back there, so yeah, I think so."
    Algie "That's great to hear!"
    Algie "I got great news, the king wants a word with you."
    Jimmy "Why should I talk to him?"
    Algie "Oh, well, because he's the king?"
    Jimmy "I have better things to do."
    play sound "audio/sfx/algiepleaaaase.ogg"
    Algie "Oh, pleaaaaseee!"
    Algie "We need your help one more time."
    Algie "This time it's important and you'll get a big reward."
    Jimmy "Umm, you have my attention now."
    Algie "Let the king explain this to you."
    scene earnestkingintro with fade
    play music MUSIC_NERDSCLIQUE_THEME
    Earnest "Hero of the Hourglass! Approach the Throne of True Valor and give obeisance to the rightful ruler of Cumalot!"
    Jimmy "Uhh, no thanks... Can we skip the royal handshake?"
    Algie "Oh, [player_name]..."
    Earnest "It doesn't matter. Such trifles pale before the magnitude of your achievements." 
    Earnest "[player_name], your... services have been truly invaluable."
    Earnest "For three agonizing years, we have been trapped in the Quest of the Seven Godwokens."
    Earnest "Your recent actions have provided us a crucial component needed to complete the campaign!"
    Earnest "You see, since the start of this school period, Russell goons have tried all kinds of trickery to mess with our goals."
    Earnest "Each time we have tried to finish the campaign, one of them shows up and throws fetid bombs or firecrackers into our headquarters."
    Earnest "So far, this problem has impide us from achieving our goal."
    Earnest "But, with your help, we can turn things around for good."
    Earnest "I hereby bestow upon you the title of Bard of the West Mountains!" with vpunch
    Jimmy "A Bard... Wow, I'm about to cry..."
    Algie "Yes! I told you he was going to love it, my king!"
    Earnest "You shall be granted the honor of playing the campaign's final chapter!"
    Earnest "But, before the grand climax can begin, the sacred regalia must be present."
    Earnest "The very symbol of our divine right!"
    play sound "audio/sfx/clearthroat01.ogg"
    Earnest "Beatrix, custodian of the Crown!"
    show beatrix uniform talk with dissolve
    play sound "audio/sfx/hey03.ogg"
    Beatrix "Hey, [player_name]."
    Earnest "Fetch the Crown of the Gods!"
    Beatrix "..."
    play sound "audio/sfx/earnestohha.ogg"
    Earnest "Oh, ha... please."
    Beatrix "Sure, okay."
    Earnest "Algernon! Send the ravens to call our heroes for duty."
    Algie "At once, my king!"
    Earnest "Tomorrow, we march to meet our destiny!"
    $ showscene('schoollibrarynerdcliquehq', transition=fade)
    show beatrix uniform talk with dissolve
    Beatrix "[player_name], care to join me?"
    Jimmy "Sure, I'll go with you."
    scene laterthatday with fade
    $ renpy.pause()
    $ showscene('schoolgroundssouthplaza', transition=fade)
    play music MUSIC_BEATRIX_THEME
    show beatrix uniform arm with dissolve
    play sound "audio/sfx/giggle01.ogg"
    Beatrix "Thank you again for coming with me."
    Jimmy "No big deal. I see your allergy problem is gone."
    Beatrix talk "That cream really worked wonders."
    Beatrix "Honestly, before you found it, I thought you were just going to avoid me."
    Jimmy "Well, I can't lie telling you that I didn't think about it."
    Jimmy "But, I'm glad I helped. You know, you're not bad when you're not trying to pretend you're above everyone else."
    play sound "audio/sfx/hum01.ogg"
    Beatrix "Well, if you want to survive this place, you'll have to stand up for yourself somehow."
    Beatrix "I'm sorry about how I treated you back then."
    $ showscene('girlsdormfrontgate', transition=fade)
    stop music
    hide fionakioskdialogbutton
    play sound "audio/sfx/girlsigh01.ogg"
    show beatrix uniform arm with dissolve
    Beatrix "Well, this is as far as you can go, Bard of the West Mountains."
    Beatrix smile "I wish you could come up. If there was a way for you to sneak in, like the last time..."
    __("{i}[player_name] leans against the wall, crossing his arms, a smirk playing on his lips.{/i}")
    Jimmy "I don't know what you're talking about."
    play sound "audio/sfx/hmm01.ogg"
    Beatrix "Well, just wait for me here, I guess..."
    __("{i}She's definetely inviting me in, thought [player_name], while Beatrix got inside the building looking back at him several times.{/i}")
    play music MUSIC_SNEAK_THEME
    scene girlsdormpipeclimb with fade
    __("{i}[player_name] reaches the same spot, looking up at the high window near the attic where he snuck in before.{/i}")
    Jimmy "Well, should I do this, again?"
    Jimmy "If I get caught..."
    Jimmy "Fuck it, I'm already here and I won't get another chance like this with Metal Mouth, ha, ha."
    play sound "audio/sfx/big_punch_trimmed.ogg"
    scene girldormattic with vpunch
    Jimmy "Uff, I don't think that pipe will hold off another climb."
    Jimmy "Gonna have to find another way to get out."
    scene girlsdormhallwayfirstfloor01 with fade
    Jimmy "Humm, where is Beatrix's room?"
    scene girlsdormhallwaysecondfloor01 with fade
    Jimmy "Oh, crap. I can't find it."
    play sound "audio/sfx/highheels.ogg"
    Jimmy "Someone is coming up the stairs..."
    play sound "audio/sfx/dooropen01.ogg"
    __("{i}Suddenly, a door opened up next the [player_name] and he felt a hand pulling his arm inside a bedroom.{/i}")
    stop music
    scene beatrixbedroom01 with vpunch
    play sound "audio/sfx/doorclose01.ogg"
    __("{i}The bedroom was meticulously tidy, a faint scent of lavender and something a bit off, like a mix of chemicals.{/i}")
    play sound "audio/sfx/surprisedhum.ogg"
    Beatrix "I thought you weren't going to come in, he, he."
    show beatrix underwear neutral with dissolve
    Jimmy "Well, I wasn't going to miss out on this, right?"
    Beatrix "Good choice of words, but you're totally insane."
    Jimmy "Relax. I'm here to escort you, to the coronation of the King of Fellations."
    play sound "audio/sfx/weirdlaugh.ogg"
    Beatrix smile "HAHAHAHAHA! Oh, right, because now you're the bard of the king."
    Beatrix "But, you didn't bring your lute, where is it?"
    Jimmy "The real question is: Why are you in your underwear?"
    Beatrix "..."
    scene beatrixfirstkiss01 with fade
    play music MUSIC_TENDER01_THEME
    __("{i}[player_name] took a step closer, then another, getting so close to her that he could feel her breath.{/i}")
    Beatrix "You shouldn't be here..."
    __("{i}[player_name] reaches out a hand, not for the crown, but to gently cup her cheek, his thumb brushing over the spot where her allergy had been.{/i}")
    Beatrix "This is..."
    play sound "audio/sfx/kiss01.ogg"
    scene beatrixfirstkiss02 with fade
    __("{i}As he leaned in slowly, her eyes opened wide and their lips met in a soft and hesitant kiss.{/i}")
    __("{i}Time stopped for them, a couple of seconds. At least, that's how it felt for them.{/i}")
    scene beatrixbedroom01 with fade
    show beatrix underwear smile with dissolve
    play sound "audio/sfx/gasp01.ogg"
    Beatrix "Oh, my god."
    Beatrix "We really kissed..."
    Beatrix "I... I have never felt this, before."
    Beatrix "I mean, I kissed someone when I was a child, but..."
    Beatrix "This felt... different."
    Beatrix "I am experiencing an unprecedented physiological response."
    Jimmy "Uhh..."
    play sound "audio/sfx/surprisedhum.ogg"
    Beatrix "The variables are overwhelming. A cascade of neurochemicals currently flooding my central nervous system!"
    Beatrix "Dopamine, oxytocin, vasopressin... I understand the theory. But the application is… chaotic."
    Jimmy "I think that's called liking someone. It messes with the data."
    Beatrix "I think my limbic system is overruling my prefrontal cortex, and for some reason, I don't want to fix this."
    Beatrix "In fact, I want more."
    call beatrix_beatrixblowjob_scene from _call_beatrix_beatrixblowjob_scene_1 
    scene beatrixbedroom01 with fade
    show beatrix underwear cum with dissolve
    play music MUSIC_BEATRIX_THEME
    play sound "audio/sfx/giggle01.ogg"
    Beatrix "I guess you and I crossed the line, now."
    Jimmy "It seems like it."
    Beatrix "I'm not sure how I feel about this."
    Beatrix "You know, I need time to think about it."
    Jimmy "I understand. And I need time to get out of here without being seen."
    play sound "audio/sfx/hum01.ogg"
    Beatrix "How did you get in, in the first place?"
    Jimmy "I climbed a pipe, but it's really rusty and I'm not sure it's going to hold anymore."
    call item_pickup(ItemCrownofGods) from _call_item_pickup_43
    play sound "audio/sfx/alright02.ogg"
    Beatrix "Alright, take the crown to Earnest. I'll give you sheets to make a rope."
    Beatrix "We are going to play the campaign tomorrow night."
    Beatrix "If you don't have a prefect pass, you should go to the headquarters during the evening."
    Jimmy "Alright, got it."
    Beatrix "Now, go. I need to clean this mess."
    stop music
    scene girlsdormhallwaysecondfloor01 with fade
    play music MUSIC_SNEAK_THEME
    Jimmy "I have to get out here, fast."
    scene girldormattic with fade
    play sound "audio/sfx/run01.ogg"
    __("{i}[player_name] made his way up to the attic once again carrying a bunch of bedsheets.{/i}")
    __("{i}He started making the improvised rope, but didn't realized there was someone else there with him.{/i}")
    play sound "audio/sfx/gasp02.ogg"
    Alice "[player_name]?"
    show aliceattictalk with dissolve
    play music MUSIC_ALICES_THEME
    Alice "What are you doing here?"
    play sound "audio/sfx/big_punch_trimmed.ogg"
    Jimmy "Ahhh, you're scared the shit out of me." with vpunch
    Jimmy "Uff, thank god is you."
    Alice "..."
    Jimmy "..."
    Jimmy "Umm..."
    Jimmy "Can I ask you a favor?"
    play sound "audio/sfx/girlsigh01.ogg"
    Alice "Okay..."
    Jimmy "Please, don't say anything."
    Jimmy "Wait..."
    play sound "audio/sfx/clearthroat01.ogg"
    Jimmy "What are you doing here, all alone?"
    play sound "audio/sfx/hmm01.ogg"
    Alice "I... was reading."
    Jimmy "Reading? Humm..."
    Jimmy "Well, can you do that for me, please?"
    Jimmy "I'll make it up to you, I promise."
    play sound "audio/sfx/hmm02.ogg"
    Alice "Okay, [roommate_male]."
    Jimmy "Thanks, little [roommate_female]."
    scene girlsdormsheetsclimb with fade
    __("{i}[player_name] didn't have more time to think about it.{/i}")
    play sound "audio/sfx/undress01.ogg"
    __("{i}Alice waited for him to start climbing down and pulled the rope up when he reached the ground.{/i}")
    show girlsdormpipeclimbbroken with dissolve
    play sound "audio/sfx/run01.ogg"
    __("{i}[player_name] gave her a thumbs up and fled the place to a safe ground as fast as he could.{/i}")
    $ Beatrix.relPoints += 1
    $ quests.beatrixGetlaid = SATISFIED
    $ BeatrixDaylimit = True
    call nexttime from _call_nexttime_54
    $ gotoscene('girlsdormfrontgate')

label rpgcampaignpromo:
    hide screen freeroamhud with None
    play music "audio/music/battlebackground02.ogg"
    scene extendededitionpromo with fade
    $ renpy.pause()
    __("{i}You have reached the end of v0.5.4 Standard Edition. Beyond this point, the game hasn't been updated.{/i}")
    scene rpgcampaignpreview with fade
    __("{i}The Extended Edition of v0.5.4 will be available on Patreon on December 21st.{/i}")
    __("{i}That's right, before Jesus Christ is born so he doesn't get to watch you playing this... *wink* *wink*.{/i}")
    __("{i}It features the new fully animated scenes for Fiona and Beatrix as well as the RPG Campaign sequence with the nerds.{/i}")
    __("{i}Happy Holidays, everyone!{/i}")
    $ gotoscene('schoollibrarymainhall')


label rpgcampaignact1:
    hide screen freeroamhud with None
    play music MUSIC_NERDSCLIQUE_THEME
    show algie uniform neutral with dissolve
    Jimmy "Sup, Algie. I brought the crown."
    Jimmy "I really want to see what all the fuss about this campaign is about..."
    Algie "Great, [player_name]! We have everything ready!"
    show earnest king mad with vpunch
    hide algie
    Earnest "Ah! The Crown of the Gods! The final piece of the puzzle! Hand it over, Bard!"
    Earnest "Now we are ready to finish the greatest campaign of Buttos and Vermins, ever!"
    scene laterthatday with fade
    $ renpy.pause()
    scene rpgcampaignact1intro with fade
    Algie "Let's start already! You know my bladder stats are critical."
    Eunice "Och, shut yer gob, ye wee pish-stained coward!"
    Eunice "Oh, hey, [player_name]. I'm glad you're going to play with us."
    Miku "Me too!"
    Beatrix "..."
    Algie "[player_name], you aren't [player_name] right now."
    Algie "You are the Bard of the West Mountains, remember? Here is your character sheet."
    show rpgsheetname01 with dissolve
    Algie "Put your name, here..."
    __("{i}What's your name, Bard of the West Mountains?{/i}")
    $ bard_name = renpy.input("Bard name (default: Spotifus)")
    $ bard_name = bard_name.strip()
    if bard_name == '':
        $ bard_name = "Spotifus"
    play sound "audio/sfx/signature01.ogg"
    show rpgsheetname02 with dissolve
    hide rpgsheetname01
    Algie "Oh, [bard_name], I like it!"
    Algie "Now, your stats are mostly blank except for Charisma: 18 and your weapon called 'The Viol-ence'"
    Jimmy "The Viol-ence? Really?"
    hide rpgsheetname02
    Earnest "Focus! Let's start the recap so we can all be up to date with what's going on."
    stop music
    play music "audio/music/epictheme01.ogg"
    scene rpgpreviously with fade
    Earnest "Previously, on Buttos and Vermins..."
    Earnest "The Kingdom of Cumalot has been ravaged!"
    Earnest "For three years, the Order of the Fellation has journeyed across the land, looking for a way to defeat the Darkness that looms over the known world."
    Earnest "Remember when Bucky summoned a swarm of cockroaches to defile the kitchen of the Cannibal Elves?"
    Algie "Well, technically, the elves weren't cannibals, because they like eating humans, and they are not the same species as us, so..."
    play sound "audio/sfx/algienevermind.ogg"
    Earnest "..."
    Algie "Nevermind..."
    Earnest "Oh, good memories. The Order survived so many adventures together, finally finding the answers they seeked."
    play sound "audio/sfx/crowdshock01.ogg"
    Earnest "Discovering that the true source of the corruption came from the King Earnest himself!"
    Earnest "And now, the Order has arrived at the precipice of destiny!" 
    Earnest "We stand before the capital city: The Citadel of Hardon."
    play sound "audio/sfx/shockeffect01.ogg"
    scene rpgcityofhardon with fade
    Jimmy "Citadel of Hardon? Really?"
    play sound "audio/sfx/melvinlisten.ogg"
    Melvin "Listen, [bard_name], it is named after General Hardon, a conqueror who erected the city in a single night with magic!"
    Jimmy "Look at that map. Look at the shape."
    Earnest "What's wrong with it?"
    Jimmy "It's a dick, Earnest."
    play sound "audio/sfx/weirdlaugh.ogg"
    Beatrix "HAHAHAHAHAHA, sorry I'm not supposed to talk yet."
    Earnest "It is the pinnacle of perfection! The city of white marbles!"
    Jimmy "I can't believe this is my life now."
    scene rpgblackhole with vpunch
    play sound "audio/sfx/metalclang.ogg"
    Earnest "Silence! The situation is dire!" 
    Earnest "A massive Black Hole has opened in the sky above the Palace at the tip of the... uh... Citadel."
    Algie "It's sucking everything in!"
    Jimmy "Oh, god..."
    Earnest "Correct! And sitting on the throne is the corrupted version of myself: King Earnest the Girthy."
    Miku "Yeah, right..."
    play sound "audio/sfx/melvinuponreflection.ogg"
    Melvin "Upon reflection, that name doesn't suit you at all."
    Melvin "So, our objective is simple: Breach the city gates, fight through the demon-infested streets..."
    Melvin "And reach the Palace to insert the 'LE PLUGGE DI BUTTE' into the portal to plug the hole."
    Jimmy "The what? Please, tell me I don't have that."
    Bucky "I have it!"
    play sound "audio/sfx/warhorn01.ogg"
    scene rpgblackholeplug with vpunch
    Jimmy "Okay, that is a... nevermind. I'm not touching that."
    Bucky "Don't worry, is a thing that Miku's mom uses to close wine bottles. Right, Miku?"
    play sound "audio/sfx/giggle01.ogg"
    Miku "Sure... he, he..."
    Earnest "Alright, roll for initiative!"
    stop music
    play music "audio/music/epictheme02.ogg"
    scene hardoncitygates with fade
    Earnest "The party stands at the base of the Citadel."
    Earnest "The gates are smashed open. The air smells of sulfur and burnt flesh."
    Earnest "Suddenly! From the shadows of the shaft... I mean, the ramp... three Tentacle Goblins appear!"
    show algiepaladin with dissolve
    Earnest "ALGIE! Your turn!"
    Algie "I use Shield of Chastity!" with vpunch
    hide algiepaladin
    scene algiepaladincry with vpunch
    play sound "audio/sfx/metalclang.ogg"
    Algie "I curl into a ball and cry!"
    Earnest "Success! The goblins ignore Algie because he looks pathetic."
    Earnest "One of them, starts laughing so hard that he trips and falls on top of a spear of a fallen soldier..."
    Earnest "The first goblin is dead..."
    Jimmy "I can't believe that worked..."
    play sound "audio/sfx/undress01.ogg"
    show melvincleric with vpunch
    Earnest "Melvin!"
    Melvin "I cast 'Calculation of Accuracy.'"
    play sound "audio/sfx/metalclang.ogg"
    show melvinclericmagic with vpunch
    Melvin "Everyone gets a +2 to hit, providing the wind velocity remains constant."
    show eunice barbarian neutral with dissolve
    Earnest "Granted. Eunice?"
    Eunice "I RAGE! I lift me kilt to intimidate the beasties!"
    hide eunice
    show eunicekiltlift with vpunch
    play sound "audio/sfx/crowdshock01.ogg"
    Jimmy "Whoa, wait, is that a combat move?"
    Eunice "In this campaign, yes. Eunice flashes the Scottsman's curse!"
    Eunice "Then I take me club and I bash the slimy fecker right in the nads!"
    Earnest "Critical Hit! He explodes into a pile of blood."
    scene rpggates02 with dissolve
    Bucky "BAZINGA!" with vpunch
    scene rpggates03 with vpunch
    Earnest "The last gobling it's looking at you, [bard_name]. It's charging!"
    Earnest "What do you do?"
    show jimmy bard neutral with dissolve
    menu:
        __("Sing something?"):
            Jimmy "Sing something?"
            Earnest "Uh... okay."
            Earnest "I guess you try to confuse the enemy? Umm, throw a d12"
        __("Kick it in the balls!"):
            Jimmy "Kick it in the balls!"
            Earnest "Tentacle Globins don't have balls, [bard_name]."
            Jimmy "Well, I will kick it on the most sensible part while singing."
            Earnest "Ugh, alright..."
            Earnest "Throw a d16."
    play sound "audio/sfx/diceroll01.ogg"
    __("{i}[bard_name] rolled the dice and it landed on 1.{/i}")
    Jimmy "Aha! I got a 1! Is that good?"
    play sound "audio/sfx/algieno.ogg"
    Algie "No."
    hide jimmy
    Earnest "Critical Fail. You accidentally smack Algie in the balls!"
    Algie "WHAT?" with vpunch
    Earnest "You are curled into a ball, remember?"
    Algie "Oh, crap. You're right."
    play sound "audio/sfx/big_punch.ogg"
    Algie "Ahhh, my lineage!" with vpunch
    Earnest "[bard_name], your singing is horrible. You get emotional damage for the rest of your life."
    Jimmy "Wow, so realistic..."
    Earnest "But wait! As the goblin prepares to strike [bard_name]... a shimmer of magical energy appears on the horizon!"
    Melvin "Reinforcements?"
    show miku necromancer neutral with vpunch
    Miku "HOLD IT RIGHT THERE!"
    Miku "I cast Dance of the Dead-Desu!"
    Earnest "Aha! The ground cracks open! Skeletal hands burst forth!"
    play sound "audio/sfx/animemoan.ogg"
    Miku "Nico Nico NIIIII!"
    play sound "audio/sfx/metalclang.ogg"
    scene rpggates04 with vpunch
    Earnest "All those hands overwhelmed the goblin, touching him everywhere without his consent."
    play sound "audio/sfx/slap.ogg"
    scene rpggates05 with vpunch
    Earnest "It's a massacre. The goblin is defeated."
    Jimmy "That was... disturbing. But, thanks, Miku!"
    show miku necromancer neutral with vpunch
    play sound "audio/sfx/giggle01.ogg"
    Miku "Anytime, handsome bard!"
    Miku "I am the Sexomancer, a necromancer raised in the brothels of the Eastern Plains!"
    Miku "You can ask me about my story, later."
    stop music
    play music "audio/music/destroyedcity.ogg"
    scene rpgpaywallobstacle with fade
    Melvin "Gentlemen, we have a problem. The main gate of the palace is sealed by a high-level magic barrier. It's a Pay-Wall."
    Algie "Oh, no. I hate Patreon suscriptions. Fucking early access."
    Earnest "Well, the kingdom can't survive without taxes."
    Eunice "Aye, we need a back door! A dark, tight passage that no one dares enter!"
    Bucky "Pirate forums?"
    Melvin "No, I have a better idea..."
    Jimmy "Oh, god. Please don't say it..."
    Melvin "The sewers!"
    Jimmy "God dammit."
    jump rpgcampaignact2
    
label rpgcampaignact2:
    stop music
    play music "audio/music/epictheme03.ogg"
    scene rpgsewersintro with fade
    __("{i}Making their way through the destroyed streets of the Hardon Citadel, the group finds an entrance to a totally gross sewer tunnel.{/i}")
    Earnest "The party descends into The Rectum of the City."
    Algie "These sewers also got corrupted by the darkness energy."
    Algie "It creates a natural mana hazard. Every turn you spend here, you must roll a Constitution Save or vomit."
    Jimmy "Can I just vomit right away?"
    show rpgsewergolem with vpunch
    play sound "audio/sfx/mrtoordalrightwimps.ogg"
    Earnest "Suddenly! The sewage water ripples! Rising from the muck is a Level 15 Turd Golem, that looks a lot like our gym teacher!"
    Jimmy "..."
    Eunice "I'LL MASH IT BACK INTO PASTE!"
    play sound "audio/sfx/monstergrunt01.ogg"
    Earnest "Eunice charges, but her weapon gets stuck in the golem's... viscosity."
    play sound "audio/sfx/frustratedhum.ogg"
    Earnest "It absorbs the blow! It swings a massive, dripping fist at Miku!"
    play sound "audio/sfx/gasp01.ogg"
    Miku "Kyaaa! Save me! I summon a Bone Wall!"
    Earnest "A wall of ribcages erupts from the ground, blocking the sludge."
    play sound "audio/sfx/monstergrunt02.ogg"
    Earnest "But the Golem is regenerating!"
    Algie "Well, even during the end of the world, people still need to take a shit."
    Bucky "Wait! I have an idea! I call upon the Communist Gators!"
    show rpgsewergolemgators with vpunch
    play sound "audio/sfx/communist01.ogg"
    Earnest "Ah! Three albino alligators burst from the pipes!"
    Bucky "They love eating bullshit from their authoritarian leader, so it should be very effective!"
    Earnest "The Gators tear the Golem apart in a frenzy of feeding."
    Jimmy "Who wrote this?"
    scene rpgdungeonsintro with fade
    Melvin "We have reached the ladder leading up to the Palace Dungeons."
    Earnest "You hear a voice echoing from a cell at the end of the hall."
    play sound "audio/sfx/mad01.ogg"
    Beatrix "You'll never get away with this, you tyrant!"
    Earnest "That's Beatrix!"
    Earnest "She's locked in the Cell of Mansplaining, where a magical voice constantly explains things she already knows!"
    Melvin "That sounds like my dad talking about politics."
    Bucky "That's horrible..."
    show rpgdungeonbeholder with vpunch
    play sound "audio/sfx/monstergrunt03.ogg"
    Algie "Look! The guard! It's a Beholder."
    Jimmy "Okay, how do we kill that?"
    play sound "audio/sfx/melvininfact.ogg"
    Melvin "In fact, we can't fight it head-on."
    Melvin "It's like a Christian sheperd trying to teach you the Bible."
    Melvin "It will paralize you until you turn into an obedient husk."
    play sound "audio/sfx/melvinlisten.ogg"
    Melvin "Listen, we need a distraction!"
    Jimmy "A distraction? I think I got it!"
    Jimmy "Let me use the Chant of the Pale Ale!"
    Earnest "[bard_name], you want to... seduce the floating giant eye?"
    Jimmy "I just want to get this over with so I can see Beatrix's costume."
    Earnest "Roll Charisma."
    play sound "audio/sfx/diceroll01.ogg"
    __("[bard_name] picks up the dice. He shakes them vigorously. He rolls... Natural 20!")
    stop music
    play music "audio/sfx/carelesswhisper.ogg"
    scene rpgdungeonjazzmadness with vpunch
    Jimmy "BOOOM!"
    Jimmy "That's how you do it."
    Jimmy "I play the most sensual solo on my lute."
    Jimmy "{i}We could have been so good together!{/i}" with vpunch
    Jimmy "{i}We could have lived this dance forever!{/i}" with vpunch
    Earnest "Wow..."
    Jimmy "MILFs love that song."
    stop music
    scene rpgdungeoncell with fade
    Earnest "The cell door creaks open."
    Earnest "Beatrix, the Oracle Sorceress, has been freed and joins the group."
    play music MUSIC_BEATRIX_THEME
    show beatrix oracle neutral with dissolve
    Beatrix "Took you long enough."
    Jimmy "Nice to see you."
    Algie "Are you okay?"
    play sound "audio/sfx/girlsigh01.ogg"
    Beatrix "I am at 85%% HP, but my Mana is full."
    Beatrix "King Earnest... the corrupted Earnest... locked me away because I saw the truth."
    Melvin "Tell us, oh, powerful oracle!"
    play sound "audio/sfx/femaleclearthroat.ogg"
    Beatrix "The Black Hole isn't just destroying the city. It's powered by his Virgin Crystal in the throne room."
    Beatrix "As long as he remains... pure... the hole will grow larger and consume the entire world!"
    play sound "audio/sfx/hmm02.ogg"
    Eunice "So we need to... deflower the King?"
    Beatrix "NO! Ew! Gross, Eunice! We just need to smash the Crystal!"
    Miku "Oh, thank god. I don't have spells for that kind of situation."
    Jimmy "Alright, so if we smash the crystal, we save the world."
    Algie "But, the king is guarding it. It won't be that easy."
    play sound "audio/sfx/giggle01.ogg"
    Beatrix "Oh, [bard_name] thanks for... you know, the music. I heard it through the wall."
    Jimmy "At your service, queen."
    Earnest "ALRIGHT, STOP FLIRTING!" with vpunch
    Earnest "The King knows you have escaped! The final battle approaches!"
    stop music
    jump rpgcampaignact3

label rpgcampaignact3:
    play music "audio/music/epictheme01.ogg"
    scene rpgthroneroom with fade
    Earnest "You kick open the doors to the Throne Room!"
    Earnest "There it is, floating above the Golden Throne..."
    Earnest "The Virginity Crystal! It pulses with the raw, chaotic energy of the dark hole in the sky."
    Melvin "The energy readings are off the charts! It's vibrating!"
    Eunice "Aye! It's shakin' like a dog passin' a peach pit!"
    show lepluggedibutte with vpunch
    play sound "audio/sfx/warhorn01.ogg"
    Bucky "The time has come! I present... 'LE PLUGGE DI BUTTE'!"
    Bucky "I just need to... insert it... into the hole... of the crystal."
    Jimmy "Please stop..."
    Bucky "Now that I think about it, this is a really weird shape for a bottle tap."
    hide lepluggedibutte
    show earnestking with vpunch
    Earnest "HALT!"
    Earnest "You think you can simply close the vortex?"
    Earnest "You fools! Real power is having the ability to destroy the world... and choosing to edge it instead!"
    Jimmy "That's a weird choice of words..."
    Earnest "ENOUGH! Behold my true form!"
    play sound "audio/sfx/monstergrunt01.ogg"
    scene rpgthroneroomdragon with vpunch
    play sound "audio/sfx/crowdshock01.ogg"
    Earnest "I consume the energy of the crystal and become... A level 50 Void Dragon!"
    Algie "Oh, no. This is going to be an impossible battle!"
    play sound "audio/sfx/melvinimdistraught.ogg"
    Melvin "I'm distraught!"
    Bucky "BAZINGA!"
    Miku "What is that coming down from the sky!!?"
    play sound "audio/sfx/swordslash01.ogg"
    scene rpgthroneroomslayer with vpunch
    __("{i}The roof of the throne room ilumminates! A celestial figure descends!{/i}")
    __("{i}Everyone is confused. Earnest, the Game Master, lays down on the ground as the mysterious figure shows himself.{/i}")
    play sound "audio/sfx/stopmusiceffect.ogg"
    play music "audio/music/funnymoment03.ogg"
    show derek arms with vpunch
    Derek "Sup, losers!"
    Algie "Hey! Derek! You can't be up here!"
    Derek "Shut up, dork. I've been spying on the new guy and found out you were going to play this game for virgins, again."
    Jimmy "Derek. Leave. Now."
    Derek "Or what? I'm fucking tired of you, new kid."
    Derek "So, game over, bitches. I win. Now, give me your lunch money, Earnest."
    Melvin "Listen, friend. We spent four hours getting here, and we would like to politely ask you to leave."
    Derek "Oh, too bad. The campaign's over, freaks."
    show jimmy bard neutral with vpunch
    play sound "audio/sfx/clearthroat01.ogg"
    Jimmy "You know what? The campaign will end when I kick your ass out of here."
    Derek "You think you're tough, Hopkins? Come on!"
    call start_battlederekfinal from _call_start_battlederekfinal
    jump derekdefeatedrpgending

label derekdefeatedrpgending:
    play sound "audio/sfx/big_punch_trimmed.ogg"
    scene derekdefeated with vpunch
    Derek "OW! My eye! You crazy jerk!"
    Jimmy "I don't want to see you near this place, again."
    Eunice "AYE! SCRAM, YE DAFT CUNT! BEFORE I SIT ON YE!"
    Jimmy "You're really good with that accent, Eunice."
    play sound "audio/sfx/giggle01.ogg"
    Eunice "Ha, ha, thanks!"
    Bucky "Can the rats eat him now?"
    Derek "WHAT!?" with vpunch
    Derek "You're all fucking crazy, I'm out of here..."
    play sound "audio/sfx/crowdlaughclap01.ogg"
    scene rpgcampaignact1intro with vpunch
    Earnest "AND THE BEAST IS VANQUISHED!"
    Earnest "A fitting end. The Corrupted King fell, but the Party united to defeat the True Evil."
    Earnest "The Kingdom of Cumalot is saved!"
    Algie "I need to pee. Like, right now..."
    Earnest "Session dismissed! Good game, everyone!"
    stop music
    show librarynerdcliquehq with fade
    __("{i}The nerds started packing up as Algie ran to the bathroom.{/i}")
    __("{i}Slowly, they all filter out of the library basement, leaving only the mess of chips, dice, and...{/i}")
    scene rpgthroneroomempty with fade
    show beatrix oracle neutral with dissolve
    play music "audio/music/tendertheme02.ogg"
    Beatrix "You know... technically, that was against the rules."
    Beatrix "You can't use physical violence in a tabletop RPG."
    Jimmy "Sometimes we need a more... realistic combat system."
    play sound "audio/sfx/giggle01.ogg"
    Beatrix "Well, it worked. The probability of Derek returning is zero."
    Jimmy "So. Did you have fun?"
    Beatrix "It was... tolerable."
    Beatrix "You defended us. That is something I will never forget."
    play sound "audio/sfx/girlsigh01.ogg"
    __("{i}She looks up at him revealing a genuine, slightly nervous smile.{/i}")
    call beatrix_beatrixfinalreward_scene from _call_beatrix_beatrixfinalreward_scene
    $ quests.beatrixGetlaid = COMPLETE
    hide screen freeroamhud with None
    play music "audio/music/epictheme01.ogg"
    scene v0_5_5preview with fade
    $ renpy.pause()
    __("{i}You have reached the end of v0.5.4 Extended Edition. Beyond this point, the game hasn't been updated.{/i}")
    __("{i}v0.5.5 will be launching February 20th.{/i}")
    __("{i}The new update is set to include new sequences and sex scenes with your [landlady_name] and [roommate_female]s during the weekend at the Town House.{/i}")
    __("{i}Cheers, everyone!{/i}")
    call nexttime from _call_nexttime_55
    $ gotoscene('schoollibrarymainhall')
