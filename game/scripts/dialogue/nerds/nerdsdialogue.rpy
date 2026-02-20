#VARIABLES
default quests.rescueBucky = LOCKED
default quests.slingshotcraft = LOCKED
default quests.RPGcampaign = LOCKED

label melvinherpestalk:
    hide screen freeroamhud with None
    show melvin uniform neutral with dissolve
    Jimmy "Hey, Melvin."
    play sound "audio/sfx/melvinohgreetings.ogg"
    Melvin "Oh, greetings, my friend."
    Jimmy "I'm sorry if it's a bit uncomfortable for you, but..."
    Jimmy "I remember you were talking to Derek about, you know, your problem."
    Melvin "Go on."
    Jimmy "Well, I just wanted to confirm that you were saying the truth."
    Jimmy "I mean, it's okay if you have something going on with Beatrix."
    Jimmy "But, she seems to be having the same problem in her face."
    Melvin "Oh, dear..."
    play sound "audio/sfx/melvinlisten.ogg"
    Melvin "Listen, [player_name]. I'm gonna talk about this, because I'm grateful for your service the last time we met."
    Melvin "So, I owe you one."
    Melvin "I do have a VHS problem, but Beatrix and I have never ever gotten even close."
    Melvin "That is impossible because I'm asexual."
    Jimmy "..."
    Melvin "And I'm very happy of not feeling any kind of sexual attraction to anyone else."
    Jimmy "Right..."
    Melvin "Well, I actually have a inclination for certain fictional characters, most of all the ones depicted in Japanese culture."
    Jimmy "Sure..."
    Melvin "Ahh, those high pitched voices and the expressions on her perfectly cute faces makes me..."
    Jimmy "Uhh, I think I get it..."
    Melvin "So, no. I'm not laid with Beatrix."
    play sound "audio/sfx/melvininfact.ogg"
    Melvin "In fact, I believe I overheard a conversation she had with the girls not long ago."
    Melvin "She was talking about some kind of allergic reaction in her skin... She mentioned a strange medical term, but I don't quite remember it."
    Melvin "You should go to the infirmary. It's on the 2nd floor of the main building to the left hallway."
    Melvin "Maybe the nurse can grant you the knowledge I ignore."
    Jimmy "Okay, thank you, mate."
    Jimmy "I won't bother you with this, again."
    Melvin "No problem, sir."
    $ quests.beatrixHomework = COMPLETE
    $ gotoscene('schoollibrarynerdcliquehq')

#BUCKY RESCUE MISSION

label buckyrescueintro:
    hide screen freeroamhud with None
    scene boysdormtvroomday with fade
    show garypetemess with vpunch
    play music MUSIC_GARYS_THEME
    Pete "Stop, Gary!"
    play sound "audio/sfx/garysorry.ogg"
    Gary "Oh, sorry..."
    Pete "Let me watch this."
    Gary "Ohh, you love to watch girls in swim suits, don't you?"
    Pete "Just get out of the way."
    Gary "Oh no, wait, maybe you like the boys of the team?"
    Pete "Yeah, right, Gary."
    Gary "Which is it, Petey?"
    Jimmy "I see you're getting along as usual."
    hide garypetemess with dissolve
    show gary uniform cocky left with dissolve
    show pete uniform neutral with dissolve
    Gary "I'm just toughening him up, turning him into a man."
    Gary "You know, something my parents didn't even bother to do with me. I wonder why?"
    Gary "Oh, right. They don't exist."
    Gary "What's up, [player_name] boy?"
    hide pete
    show algie uniform neutral with vpunch
    Algie "Hey, [player_name]. Hey Petey!"
    Pete "Hey, Algie..."
    $ Algie.met = True
    show gary uniform neutral left with vpunch
    Gary "Ahhh, piss stain."
    Gary "Good to see you."
    Algie angry "[player_name], we have a crisis."
    Algie "Bucky went to the auto shop to get some parts for his science project."
    Algie "But he hasn't come back yet, I think he might be in trouble."
    play sound "audio/sfx/algiepleaaaase.ogg"
    Algie smug "Can you look for him, pleaaase?"
    Jimmy "Why don't you go there, yourself?"
    Algie "I... I got homework, he he..."
    Jimmy "..."
    Gary "..."
    Algie angry "Okay! I'm frightened! And I have a weak bladder." with vpunch
    Algie neutral "I think the Bullies got Bucky, pleeease I'll pay!"
    play sound "audio/sfx/garydoit.ogg"
    Gary "Hm, I think you should do it."
    Gary "It's a good chance to show Russell who's in charge."
    Jimmy "Who's Russell?"
    Gary "Oh, you'll find out, eventually."
    Gary "We gotta take care of him and his boys..."
    Gary "And then, after that, we'll be able to take care of all the other cliques."
    Gary "Soon, the school will be ours."
    Jimmy "I don't want the school."
    Gary "Well, I do pal! And I intend to get it."
    Algie angry "You're a maniac."
    Gary "Shut up, piss stain."
    Gary "Now you two go do your thing."
    $ quests.rescueBucky = ACTIVE
    $ gotoscene('boysdormhallway')

label buckyrescuemission:
    if quests.slingshotcraft == COMPLETE:
        jump buckyrescuemission_finale
    elif quests.rescueBucky == SATISFIED:
        jump buckyrescuemission_satisfied
    elif quests.rescueBucky == ACTIVE:
        jump buckyrescuemission_active

label buckyrescuemission_active:
    hide screen freeroamhud with None
    play music "audio/music/sneaking01.ogg"
    scene buckybulliesjunkyard with dissolve
    "[player_name] and Algie arrived at the junkyard and saw a large group of Bullies surrounding a slim guy with glasses."
    Jimmy "There are too many of them."
    Jimmy "We need a plan to get rid of them."
    Jimmy "I don't think punching my way to your friend is the best idea."
    $ showscene('schoolgroundsparkinglot', transition=fade)
    show algie uniform smug with dissolve
    Algie "I think I might have a plan."
    Jimmy "Let's hear it."
    Algie "Well, maybe we can build a weapon that will help us disperse them from a distance."
    Algie "I've been working on a piece of wood for an aerodynamically high-performing slingshot."
    Algie smug "If you find me the materials, I can build it for you."
    Jimmy "That's actually a really good idea!"
    Jimmy "So, what do you need?"
    Algie neutral "The wood piece is inside my locker, in the hallway near the cafeteria."
    Algie "Here's the key."
    Algie "We are also going to need a rubber band."
    Algie "You should be able to find one in the garage."
    Algie "And of course, we are going to need the ammunition, but I will take care of that."
    Jimmy "Alright, I'll get the stuff."
    Algie neutral "Good! Find the pieces and come back once you have them."
    Jimmy "I'm on my way."
    $ quests.rescueBucky = SATISFIED
    $ quests.slingshotcraft = ACTIVE
    $ gotoscene('schoolgroundsparkinglot')

label buckyrescuemission_satisfied:
    hide screen freeroamhud with None
    show buckybulliesjunkyard with dissolve
    Jimmy "I still need to find the pieces for the slingshot."
    if Jimmy.hasItem(ItemRubberBand):
        Jimmy "I already got the rubber band."
        Jimmy "The wooden piece is in Algie's locker at the Main Building."
    elif Jimmy.hasItem(ItemShapedBranch):
        Jimmy "I already got the wooden piece"
        Jimmy "I could find a rubber band at the Shop garage."
    else:
        Jimmy "The wooden piece is in Algie's locker at the Main Building."
        Jimmy "I could find a rubber band at the Shop garage."
    $ gotoscene('schoolgroundsparkinglot')

label buckyrescuemission_finale:
    hide screen freeroamhud with None
    show algie uniform neutral with dissolve
    stop music
    play music "audio/music/funnymoment.ogg"
    Algie "Did you get the pieces?"
    Jimmy "Yeah, here the wooden piece and the rubber band."
    Algie "Great, let me assemble the contraption."
    call item_pickup(ItemStonesAmmo) from _call_item_pickup_7
    $ Jimmy.inventory.remove(ItemRubberBand)
    $ Jimmy.inventory.remove(ItemShapedBranch)
    Algie "I managed to gather some stones that are aerodynamically perfect for the slingshot."
    "{i}[player_name] was surprised and impressed at Algie's handy skills, and how helpful he could be in those situtations.{/i}"
    Jimmy "I didn't know you were so good with this kind of stuff."
    Algie "Well, maybe you can consider being my friend now that you know I can be useful."
    Algie angry "Here you have it! A mighty weapon! I CALL IT THE METEORATOR!"
    call item_pickup(ItemSlingshot) from _call_item_pickup_8
    $ Jimmy.inventory.remove(ItemStonesAmmo)
    Jimmy "The meteorator, alright."
    Jimmy "Let's get to higher ground then."
    play sound "audio/sfx/undress01.ogg"
    scene buckybulliesjunkyard with dissolve
    "{i}The two of them got into a perfect position, hidden from view.{/i}"
    "{i}[player_name] loaded the slingshot with stones, and after measuring the power of it with some bushes in the distance...{/i}"
    call start_buckyrescue_slingshot from _call_start_buckyrescue_slingshot
    show bucky uniform neutral with dissolve
    $ Algie.met = True
    $ Bucky.met = True
    hide slingshot_gun with dissolve
    stop music
    play music MUSIC_FUNNY_MOMENT
    Bucky bazinga "BAZINGA!!" with vpunch
    Jimmy "What?"
    Algie "I don't know why he says that."
    Bucky neutral "Thank you. You saved me!"
    Jimmy "We both did."
    Jimmy "Your friend, Algie, came up with the plan."
    Algie "Oh, it was nothing, he, he. *blushes*"
    "Bucky looked at Algie and gave him an appreciative nod."
    Bucky neutral "Thank you both. I owe you guys."
    Bucky "I'm gonna be able to finish working on the science project."
    Bucky "How are the preparations for the campaign going?"
    Algie "We are almost done, our friend here helped us recover the scroll and I believe he can help us with the campaign itself."
    Bucky "Ahh, maybe he could take the place of the bard."
    Algie "Yes, that's a possibility."
    Bucky "Well, I'm ready to take my place, whenever the kingdom calls."
    Algie "Great, Earnest will be pleased."
    play sound "audio/sfx/slap.ogg"
    Bucky bazinga "It's gonna be amazing!" with vpunch
    $ quests.rescueBucky = COMPLETE
    Jimmy "Let's get out of here, then."
    stop music
    hide bucky with dissolve
    call nexttime from _call_nexttime_26
    scene laterthatday with fade
    $ renpy.pause()
    play music "audio/music/persecution01.ogg"
    scene russellintro03 with vpunch
    Russell "..."
    Russell "Russell is angry..."
    Russell "Russell with get his hands on the new guy very soon!"
    $ quests.beatrixGetlaid = ACTIVE
    $ quests.Buckyrescue = COMPLETE
    stop music
    $ gotoscene('schoolgroundsparkinglot')

#SLINGSHOTPIECESRECOVERY

label rubberbandscene:
    hide screen freeroamhud with None
    scene audreysexymechanic with fade
    play music MUSIC_AUDREY_THEME
    "{i}As [player_name] opened the door to the Garage, the smell of engine oil and the sound of a cool music hit his senses.{/i}"
    "{i}The substitute teacher was in there, working on a car with her toned and sweaty body.{/i}"
    "{i}[player_name] couldn't help thinking on that Halloween night where he almost got to bang her.{/i}"
    "{i}Did she remember anything? thought [player_name].{/i}"
    play sound "audio/sfx/clearthroat01.ogg"
    Jimmy "Excuse me, Miss."
    play sound "audio/sfx/hey01.ogg"
    Audrey "Hey, kiddo! Do we have a class now?"
    Jimmy "No, Miss. I'm here for something else."
    Audrey "Oh, okay. I thought I forgot about the schedule again."
    Audrey "Give me a second to get out of here."
    play sound "audio/sfx/undress01.ogg"
    $ showscene('schoolgarage', transition=fade)
    play music MUSIC_AUDREY_THEME
    show audrey mechanic arms with dissolve
    Audrey "So, what do you need?"
    Jimmy "Do you happen to have a rubber band I could borrow? Something around this size?"
    play sound "audio/sfx/hum01.ogg"
    "{i}Audrey looked at [player_name] like she was trying to figure out who he was.{/i}"
    "{i}After a couple of seconds, she realized how awkward the situation was and smiled.{/i}"
    Audrey "Sorry, I just... I lingered for a moment."
    Audrey "So, a rubber band..."
    Audrey "Umm, I see what you're doing."
    Audrey "You want to make a slingshot, right?"
    Jimmy "Well..."
    play sound "audio/sfx/laugh04.ogg"
    Audrey "Ha, ha, ha, ha, don't worry, that's not of my business."
    Audrey "I still got a bit of that young rebel spirit in me, you know?"
    "{i}Audrey reached into her pocket and handed [player_name] a rubber band.{/i}"
    call item_pickup(ItemRubberBand) from _call_item_pickup_9
    Audrey "Here you go. Good luck with your slingshot."
    Jimmy "Thanks, Miss."
    Audrey "Oh, you can call me Audrey."
    Jimmy "Okay, Audrey. Thank you for being so cool."
    play sound "audio/sfx/surprisedhum.ogg"
    Audrey "Aww, that's cute. By the way, your face really is very familiar to me somehow, but I can't figure out why."
    Jimmy "Oh... Well, I'm in your class and..."
    Jimmy "We also met at the teacher's Halloween reunion."
    Audrey "Oh, right! I remember you were there, yeah... Well, I was really drunk, and I don't remember much."
    play sound "audio/sfx/femaleclearthroat.ogg"
    Audrey "I... Do you remember why I woke up at the concierge room?"
    Audrey "I managed to get out of there before the old man arrived, lucky me, he, he."
    Jimmy "Umm, you were very drunk as you said and..."
    Audrey "Nah, don't worry. I'm sure I just landed there, looking for a place to sleep."
    play sound "audio/sfx/mh1.ogg"
    Audrey "Even though, I was naked and... wet, down there."
    Audrey "I shouldn't be talking like this in front of a student."
    Audrey "I'm really sorry."
    Jimmy "Don't worry, Audrey. I owe you a secret. {i}*shows her the rubber band*{/i}"
    play sound "audio/sfx/laugh01.ogg"
    Audrey "Cool! Ha, ha, ha, well, go on now, I got stuff to do."
    if quests.slingshotcraft == ACTIVE:
        $ quests.slingshotcraft = SATISFIED
        Jimmy "Alright, now I just need to get the wooden piece. Algie mentioned his locker near the cafeteria."
    elif quests.slingshotcraft == SATISFIED:
        $ quests.slingshotcraft = COMPLETE
        Jimmy "This is it, I should go back to the junkyard."
    $ gotoscene('schoolgroundsparkinglot')

label shapedbranchscene:
    hide screen freeroamhud with None
    scene algielocker01 with fade
    Jimmy "Algernon P, this is it."
    play sound "audio/sfx/slap.ogg"
    show algielocker02 with dissolve
    Jimmy "This must be the wood piece."
    call item_pickup(ItemShapedBranch) from _call_item_pickup_10
    show algielocker03 with dissolve
    play sound "audio/sfx/crowdshock01.ogg"
    Unk "AGHHHH! Leave me alone, Russell!" with vpunch
    Unk "I don't have money today."
    Jimmy "What's going on?"
    scene russellintro01 with fade
    play music MUSIC_RUSSELL_THEME
    "{i}As [player_name] turn his head, he heard a loud growl and saw at the end of the hallway a huge guy messing with a nerd.{/i}"
    "{i}The man was almost seven feet tall and pulled the other poor guy's trousers lifting his feet from the floor.{/i}"
    "{i}That intimidating fella was Russell, the leader of the Bullies.{/i}"
    "{i}[player_name] understood why Derek mentioned Russell everytime they had a problem.{/i}"
    $ Russell.met = True
    Russell "NO MONEY, NO PANTIES! HAHAHAHAHAHAHA"
    Unk "AAAAHHHHH! That hurts!"
    "{i}When Russell finished the wedgie, he turned his head and met [player_name] gaze.{/i}"
    play sound "audio/sfx/giantsteps.ogg"
    "{i}It was too late to walk away, [player_name] knew that showing cowardice in front of that mole wasn't an option.{/i}"
    show russellintro02 with vpunch
    "{i}[player_name] kept his nerve and met Russell's gaze head on.{/i}"
    "{i}He wasn't going to let him know that he was intimidated.{/i}"
    Russell "I'm watching you, new guy..."
    Russell "Derek is scared of you. I'm not..."
    Jimmy "..."
    play sound "audio/sfx/russellgrunt.ogg"
    "{i}Russell glared at [player_name] for a few moments before finally letting out a gruff chuckle.{/i}"
    Russell "Don't look for more trouble, or you'll have to deal with me."
    Jimmy "Whatever, big foot..."
    Russell "..."
    play sound "audio/sfx/giantsteps.ogg"
    "{i}With his heart still racing, [player_name] saw Russell walking away thinking that maybe a confrontation with the giant was inevitable.{/i}"
    scene algielocker01 with fade
    if quests.slingshotcraft == ACTIVE:
        Jimmy "Alright, I got the wooden piece. Now I need the rubber band, Algie said something about the garage."
        $ quests.slingshotcraft = SATISFIED
    elif quests.slingshotcraft == SATISFIED:
        Jimmy "This is it, I should go back to the junkyard."
        $ quests.slingshotcraft = COMPLETE
    $ gotoscene('mainbuildingentrance')
