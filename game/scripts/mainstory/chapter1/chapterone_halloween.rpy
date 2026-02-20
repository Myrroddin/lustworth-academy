label halloween_harrisonhousearrival:
    play music MUSIC_HALLOWEEN_THEME
    scene harrisonhouseentrancehalloween with fade
    "{i}It's Halloween night and the full moon illuminates the sky, casting an eerie glow on the landscape.{/i}"
    "{i}Pete, Gary and [player_name], dressed in their particular costumes, are making their way towards the Harrison mansion, where a Halloween party is in full swing.{/i}"
    "{i}As they approach, [player_name] can hear the faint laughter of girls in the distance and wonders who will be there.{/i}"
    "{i}The three friends have an ulterior motive for coming to the party - to pull off the ultimate Halloween prank. Their target? Derby, the leader of the preps."
    "{i}Their goal? To steal the Derby's laptop and pull pranks around the mansion to make the preps look like fools. It's going to be a night that they'll never forget.{/i}"
    "{i}Have fun, have sex, and be scary!{/i}"
    show pete bunny neutral with dissolve
    Pete "Alright, [player_name]. We need to do this like ninjas."
    Pete "First, the preps love drinking cocktails with not that much alcohol." 
    Pete "So, we need to find a way to reach the bar and use the laxative on their drinks without being seen."
    Pete "You are going to help me get close to the bar and I'll do the rest."
    Pete "Second, you see that flag in the ceiling? We need to replace it. That's your deal, here's the replacement."
    play sound "audio/sfx/undress01.ogg"
    call item_pickup(ItemFakeFlag) from _call_item_pickup_15
    Pete "Third, the spray can. Gary wants to leave a message somewhere on the mansion."
    play sound "audio/sfx/slap.ogg"
    if ItemSprayCan not in Jimmy.inventory:
        call item_pickup(ItemSprayCan) from _call_item_pickup_29
    Pete "So, you need to find a good place that's frequently used by the preps."
    Pete "It's tricky because all of the mansion will be full of people."
    $ quests.halloweenFruitPunch = ACTIVE
    $ quests.halloweenFakeFlag = ACTIVE
    $ quests.halloweenGraffitiMessage = ACTIVE
    Pete "And finally, we need to steal Derby's laptop. That's the most important thing."
    Pete "We need to find a way to distract him in order to get in his room."
    show gary nazi neutral with dissolve
    play sound "audio/sfx/clearthroat01.ogg"
    Gary "That's my job. I have a very good idea."
    Gary "So, while you guys have fun in there, I will take care of the distraction and find a way to sneak in."
    Jimmy "Well, this is going to be an interesting night."
    Gary "If everything goes well, we'll be taking over this school before Winter arrives."
    Gary "Happy Halloween, everybody!"
    $ resetHalloweenEvent()
    scene harrisonhouseentrancenight with fade
    $ gotoscene('harrisonhouseentrance', transition=fade)

label halloween_intermission:
    scene laterthatday with fade
    "{i}Some time later...{/i}"
    scene harrisonhouseentrancenight with fade
    show pete bunny neutral with dissolve
    play sound "audio/sfx/heypete01.ogg"
    Pete "[player_name]! Where have you been?"
    Pete "The laxative is working! Did you have luck with your stuff?"
    Jimmy "Well, I've done everything you told me."
    Pete "That's great news! Now we just need to steal Derby's laptop to get out of here."
    Jimmy "Dude, isn't this enough? I mean I've had a good time doing silly stuff, but stealing is a bit much..."
    Pete "Gary doesn't want to leave until he has Derby's laptop."
    Pete "And he wants to talk with you."
    Pete "He's waiting by the pool"
    scene harrisonhousepool with fade
    play music MUSIC_GARYS_THEME
    show gary nazi neutral with dissolve
    play sound "audio/sfx/heygary02.ogg"
    Gary "[player_name], boy! I heard you have been naughty tonight, huh..."
    Gary "I get that you are trying to have some fun, but while you were having fun at the penthouse, you passed the best opportunity of the night."
    Gary "I was watching Derby from a distance and he left his bedroom open because of a sudden urge to go to the bathroom."
    Gary "That was a perfect chance to get his laptop, but you missed it."
    Jimmy "Why didn't you get it yourself?"
    play sound "audio/sfx/clearthroat01.ogg"
    Gary "Because it is not my job, [player_name]. It's your job."
    Gary "I'm the one the one that comes up with the masterplan, and you are the one that gets his hands dirty."
    Gary "You get it?"
    Jimmy "This is fucking stupid."
    Jimmy "So, what are we going to do then?"
    Gary "Well, I DID my job and I came up with a plan B."
    Gary "Here, take this."
    call item_pickup(ItemDogManure) from _call_item_pickup_17
    Jimmy "Holy fuck, man! This stinks!"
    Gary "I know, I know! Hear me out!"
    Gary "Wait for Derby to get inside his room."
    Gary "All you have to do is put this right in front of his door and lure him out just enough to step on it."
    Gary "He'll have to clean himself away from his bedroom."
    Gary "That's the best opportunity you'll have to get the laptop."
    Jimmy "How did you get this?"
    Gary "That is not relevant. Did you get my plan?"
    Jimmy "Yeah, yeah. Make him get full of shit and get the laptop."
    Gary "Don't mess this up, [player_name]."
    Gary "We only have one chance."
    Gary "That dog won't be taking another shit anytime soon."
    Jimmy "What dog? Oh... I don't wanna know."
    jump halloween_violethalloweenincident

label halloween_violethalloweenincident:
    play music MUSIC_FUNNY_MOMENT
    scene harrisonhouse2ndfloor with fade
    show derby peterpan with dissolve
    Derby "I'm gonna have a serious talk with that guy in the bunny suit, my princess. I pinky promise."
    show violet tinkerbell neutral with dissolve
    play sound "audio/sfx/giggle01.ogg"
    Violet "Aww, you're so cute my prince."
    Violet "I'm so exhausted. Dealing with the lower class is so tiring."
    Violet "I think I want to sleep in your room, tonight."
    Derby "Do you want to sleep with me tonight, my queen?"
    play sound "audio/sfx/girlsigh01.ogg"
    Violet "Oh, yes, darling."
    Derby "Of course, my love. My room is at your service."
    Violet "Great. You have earned a kiss. {i}*Mwah*{/i}"
    play music "audio/music/sneaking01.ogg"
    hide violet with vpunch
    hide derby with dissolve
    play sound "audio/sfx/doorclose01.ogg"
    $ renpy.pause()
    show jimmy neutral with fade
    Jimmy "Crap, she's inside his room too."
    show dogmanurepositioned with dissolve
    $ Jimmy.inventory.remove(ItemDogManure)
    play sound "audio/sfx/undress01.ogg"
    Jimmy "Let's hope this works."
    hide jimmy
    play sound "audio/sfx/doorknock01.ogg"
    Jimmy "*Knock* *Knock* Derby!! Derby!! The stock market is blowing up!!" with vpunch
    play sound "audio/sfx/dooropen01.ogg"
    Derby "Guys! I'm busy! Violet is my bedroom for the first time in two months!"
    play sound "audio/sfx/big_punch.ogg"
    show derby peterpan dogshit with vpunch
    hide dogmanurepositioned
    Derby "What is the meaning of this!?"
    Derby "Oh my dear lord!"
    Derby "My suit is ruined!"
    Derby "AAAGGGGHHHH!" with vpunch
    play sound "audio/sfx/surprisedhum.ogg"
    Violet "What happened, darling?"
    Derby "Uhh, nothing, my love."
    play sound "audio/sfx/clearthroat01.ogg"
    Derby "I just need to pee!"
    Derby "Give me a second and I'll come back."
    Violet "Okay, my prince!"
    hide derby peterpan dogshit with vpunch
    Jimmy "Can't believe that worked."
    Jimmy "You're are an evil genius, Gary."
    play music MUSIC_SNEAK_THEME
    scene darkderbybedroom with fade
    Jimmy "*She didn't close the door.*"
    Jimmy "*Gotta be quiet or I'll wake her up.*"
    scene derbylaptopfound with fade
    play sound "audio/sfx/undress01.ogg"
    Jimmy "*There it is. This must be Derby's laptop.*"
    Jimmy "*Let's get out of this mad house.*"
    Violet "Derby? Is that you?"
    Jimmy "*Oh, crap.*"
    call violet_halloweenfingering_scene from _call_violet_halloweenfingering_scene
    Jimmy "OH, CRAP!"
    Derby "WHAT IS THE MEANING OF THIS!?"
    Derby "You disgusting peasant, get away from my princess!"
    play sound "audio/sfx/scream01.ogg"
    scene darkderbybedroom with fade
    "{i}[player_name] had two options, taking his clothes and run, or taking Derby's laptop and run.{/i}"
    "{i}As he tried to do both, he realized he was cornered inside the bedroom with the door being held by Derby Harrison.{/i}"
    Jimmy "Think fast, [player_name], think fast!"
    play sound "audio/sfx/big_punch.ogg"
    scene halloweeneventending01 with vpunch
    "{i}In a matter of seconds, [player_name] took Derby's laptop running towards the closest window.{/i}"
    play sound "audio/sfx/run01.ogg"
    "{i}He looked down from the small balcony outside and saw a group of bushes next to the pool.{/i}"
    "{i}There was only one way to get out of there.{/i}"
    play sound "audio/sfx/big_punch.ogg"
    scene halloweeneventending02 with vpunch
    "{i}After throwing the laptop into the bushes, he ran towards the ledge of the balcony and jumped into the pool.{/i}"
    play sound "audio/sfx/crowdshock01.ogg"
    "{i}Being naked in front of the crowd that was about to come out of the building, he got out as fast as he could, fetched the laptop and ran away.{/i}"
    scene halloweeneventending03 with vpunch
    "{i}That was definitely a night he will always remember.{/i}"
    stop music
    call nextday from _call_nextday_7
    call nextday from _call_nextday_8
    call nextday from _call_nextday_9
    $ calendar.event = None
    $ glob.halloweenEventComplete = True
    $ Jimmy.outfit = JIMMY_UNIFORM
    if Violet.relPoints == 0:
        $ Violet.relPoints += 1
    play sound "audio/sfx/guitarriff01.ogg"
    scene chapter3cartel with fade
    $ renpy.pause()
    $ gotoscene('boysdormjimmysroom', transition=fade)

####################################################################################################
## Fiona
####################################################################################################

label halloween_fionabartenderintro:
    $ Fiona.eventMet[HALLOWEEN_EVENT] = True
    scene harrisonbardialog with fade
    show fiona waldo neutral with dissolve
    play sound "audio/sfx/gasp01.ogg"
    Fiona "[player_name]! You came to the party!"
    Fiona "Ooh, that costume looks really good on you."
    Jimmy "I bought it in the best store in town."
    Fiona "Aww, you silly."
    Jimmy "So, you're the bartender?"
    play sound "audio/sfx/femaleclearthroat.ogg"
    Fiona "Oh, yeah, just making some extra money, you know me."
    Fiona "Can I get you something?"
    Jimmy "Well, I want you, but I'm not sure if it's possible."
    Fiona "You already know you can have me whenever you want, handsome."
    Fiona "However, I can't leave the bar right now."
    $ fiona.bartenderIntro = True
    jump fionahalloweendialogue.dialogmenu

label halloween_fionasex:
    $ showscene('harrisonhousebar', transition=fade)
    hide fionawaldodialog01
    show fiona waldo neutral with dissolve
    show pete bunny shy with dissolve
    Jimmy "Hey, Fiona. Turns out my friend here has some bartender skills."
    play sound "audio/sfx/wow01.ogg"
    Fiona "Oh, really?"
    Fiona "Well, good enough for me, I guess."
    Fiona "Just don't mess it up, alright? I'll be back in an hour."
    Pete "No problem, miss."
    Fiona "Aww, your friend is so cute, [player_name]."
    Fiona "Come on, let's get out of here!"
    play music "audio/music/80music.ogg"
    scene fionawaldodancing with vpunch
    "{i}Finally free from the shackles of underpaid labor, Fiona took [player_name]'s hand and led him to the dancing floor.{/i}"
    Fiona "God! You don't know how much I wanted to dance with you!"
    "{i}They both got closer and closer as the music took over their bodies.{/i}"
    "{i}Their skin rubbed together, as the heat of the moment increased, igniting their passion.{/i}"
    Fiona "Let's go to a private place..."
    Jimmy "Of course..."
    scene fewmomentslater with fade
    $ renpy.pause()
    scene harrisonhousebedroom01 with fade
    show fiona waldo neutral
    with dissolve
    Fiona "This is quiet enough, I think."
    Jimmy "Cozy."
    Fiona "My dad doesn't even know I'm here."
    Fiona "He'll eventually find out."
    Fiona "So, before all hell breaks loose, I want to have as much fun as I can tonight with you."
    Jimmy "Anything special in mind?"
    hide fiona with dissolve
    "{i}Fiona hopped on the nearest bed and started taking off her shorts.{/i}"
    "{i}Watching her undress, an aroused [player_name] quickly followed suit and stripped off his clothes.{/i}"
    call fiona_halloweensex_scene from _call_fiona_halloweensex_scene
    stop music
    stop sound
    Jimmy "That was nice, babe."
    Fiona "It was amazing. Nothing will spoiled my night from now on."
    Jimmy "Glad to hear you're happy."
    play sound "audio/sfx/giggle01.ogg"
    Fiona "Being with you is the best feeling ever."
    Fiona "I should go get cleaned. I hope your friend is doing alright at the bar."
    $ quests.fionaBartender = COMPLETE
    if quests.fionaDadTrouble == LOCKED:
        $ quests.fionaDadTrouble = ACTIVE
    $ Fiona.relPoints += 1
    $ gotoscene('harrisonhousefloor2', transition=fade)

####################################################################################################
## Beatrix
####################################################################################################

label halloween_beatrixappleciderintro:
    $ Beatrix.eventMet[HALLOWEEN_EVENT] = True
    show beatrix mavis neutral with dissolve
    Jimmy "Beatrix, is that you?"
    play sound "audio/sfx/surprisedhum.ogg"
    Beatrix "Oh, no. What are you doing here?"
    Jimmy "I could ask you the same thing. I didn't know you were the party kind."
    Beatrix "I'm not. I'm just here because my mom is a member of the honorary league that founded this building." 
    Beatrix "And she asked... no, she ordered me to come."
    play sound "audio/sfx/femaleclearthroat.ogg"
    Beatrix "And I thought this would be the last place on earth I would ever see you."
    Jimmy "Right. So, what's your costume about?"
    Beatrix "Duh, a vampire, obviously..."
    Beatrix "It's an old outfit, that's why it's so tight."
    Jimmy "It suits you well, you know? But, vampires have brackets?"
    play sound "audio/sfx/mad01.ogg"
    Beatrix "Oh, shut up. I feel weird in this costume already."
    Beatrix "By the way, I didn't know the low class of this school was invited."
    Jimmy "Wow, that's a low blow."
    Beatrix "I also saw that psociopath, Gary, walking around outside the mansion. You should be careful with him."
    Jimmy "I can handle him."
    Jimmy "So, can I get you a drink or something?"
    Beatrix "Oh, yes, please! Can you get me an orange juice or something like that? I can't find anything without alcohol around here."
    Jimmy "Well, it won't be easy, but sure, I can try."
    play sound "audio/sfx/giggle01.ogg"
    Beatrix "Nice, thank you, [player_name]."
    $ quests.beatrixAppleCider = ACTIVE
    $ gotoscene('harrisonhousebar')

label halloween_beatrixapplecidersatisfied:
    show beatrix mavis neutral with dissolve
    Jimmy "Here, I found some apple juice."
    Beatrix "Mm, it smells really good."
    Beatrix "{i}*Glup* *Glup* *Glup*{/i}"
    play sound "audio/sfx/wow01.ogg"
    Beatrix "Ahh, wow. I was thirsty. It's a bit spicy at the end, must be the apple getting a bit of trituonite oxygen..."
    Jimmy "..."
    play sound "audio/sfx/gasp01.ogg"
    Beatrix "Where did you find this? This is so good!"
    Jimmy "Well, there is a study in the 2nd floor, at the end of the hallway."
    Jimmy "I found a lot of bottles in there..."
    Beatrix "Oh, yes! That's the best way to spend the night away from this people."
    play sound "audio/sfx/laugh01.ogg"
    Beatrix "I'm going to that study, if you want to join me, don't... Ha, ha, ha, ha, ha!"
    hide beatrix mavis with dissolve
    Jimmy "Is it me? Or she's kind of drunk?"
    $ quests.beatrixAppleCider = COMPLETE
    $ Jimmy.inventory.remove(ItemAppleCider)
    $ gotoscene('harrisonhousebar')

label halloween_beatrixgrinding:
    Beatrix "[player_name]! Yorr herree..."
    hide screen freeroamhud
    play music MUSIC_FUNNY_MOMENT
    scene beatrixciderdrunk with fade
    Jimmy "Beatrix? How's the night going?"
    play sound "audio/sfx/mh1.ogg"
    Beatrix "I'm jussst feeleeng a litt bit funny."
    "Oh, oh, she's really drunk now."
    Beatrix "You know, I kind og hate you. I mean, I dln't jnow why but you lookm like an asssshole and..."
    Beatrix "I loke you and don't know why. It must be some meethod of reeverrse psychology."
    Beatrix "I can't stip thinling about howw I danssed on yur lap..."
    play sound "audio/sfx/giggle02.ogg"
    Beatrix "It... It felt sooo good. I... I can't beliv I'm fallin forr this kimd of preemal inztincts."
    $ showscene('harrisonhouseoffice')
    show beatrix mavis drunk with dissolve
    play sound "audio/sfx/giggle01.ogg"
    Beatrix "I want to do it agaim. Bur, I wann to feel your peeeenisss." with vpunch
    Jimmy "Wait, do you want to fuck with me?"
    Beatrix "Oh, no. Gross! No seex, just rubbing our recroductice orgzns. Yiu know, friction. Just frictiiom."
    Jimmy "Right, friction."
    Beatrix "Come on, [player_name], I know you want it."
    call beatrix_halloweengrinding_scene from _call_beatrix_halloweengrinding_scene
    $ showscene('harrisonhouseoffice')
    show beatrix mavis cum
    with fade
    Beatrix "Umm, a bit salty and... gross."
    Beatrix "Well, you serrved me well, [player_name]. I shoulld rest now."
    Beatrix "See ya!"
    "{i}She pushed [player_name] outside the office and closed the door.{/i}"
    $ quests.beatrixHalloweenGrinding = COMPLETE
    if quests.beatrixHomework == LOCKED:
        $ quests.beatrixHomework = ACTIVE
    $ Beatrix.relPoints += 1
    $ gotoscene('harrisonhousefloor2', transition=vpunch)

####################################################################################################
## Mandy & Christy
####################################################################################################

label halloween_christyandmandypoolintro:
    scene harrisonhousepool with fade
    Jimmy "Wow... This is a nice goddamn pool."
    Jimmy "After a couple of classes in the day, coming here to swim and relax..."
    Jimmy "Now that would motivate me to study, for sure."
    Jimmy "I can see two girls hanging around the pool."
    Jimmy "Happy Halloween, ladies."
    show mandy supergirl with dissolve
    $ Mandy.eventMet[HALLOWEEN_EVENT] = True
    Mandy "Who... are you?"
    Jimmy "Your new company."
    Mandy "Oh, we're fine alone, thank you."
    show christy pokemon with dissolve
    $ Christy.eventMet[HALLOWEEN_EVENT] = True
    Christy "Oh, don't be so rude, Mandy."
    Christy "I think he is the new guy."
    Christy "You know, the one everyone is talking about."
    Christy "Is it true that you fucked the mayor's daughter?"
    Jimmy "Can't confirm or deny."
    Christy "Uhh, so mysterious. Cut the crap, new guy."
    Christy "Usually I don't talk to anyone who has balls hanging around, unless those balls are huge."
    Christy "And what you did surely took some massive balls."
    Mandy "Christy, I don't like this guy."
    Mandy "I don't care if he fucks the president's son, he looks like a total jerk to me."
    Christy "Mandy, you need to learn to see opportunities when they are presented to you like this."
    Christy "I think our new friend here can help us find some Voltium."
    Mandy "CHRISTY!"
    Jimmy "The what?"
    Christy "Voltium, haven't you heard about it?"
    Christy "Oh, right, I forgot you're new."
    Mandy "Christy, I don't think he should know..."
    Christy "Let me handle it, Mandy."
    Christy "Let's say that Voltium is a sense enhancer."
    Jimmy "Sense enhancer, right. So, it's a drug."
    Christy "Umm, come on! Don't say nasty words in front us ladies."
    Christy "Voltium is actually inoffensive."
    Christy "I'm not sure what it's made of, but it's great for improving our humor and..."
    Christy "Getting some places, wet... If you know what I mean."
    Mandy "Christy!!"
    Jimmy "Um... I'm listening."
    Christy "Get us some Voltium and I'll show you myself what it is capable of."
    Jimmy "Any idea where I can find it?"
    Christy "Look in the bedrooms, Derby's friends must have something."
    Jimmy "Alright, it's a deal."
    Christy "Thank you... Um, what's your name?"
    Jimmy "[player_name]."
    Christy "A pleasure, [player_name]."
    $ quests.christyMandyVoltium = ACTIVE
    $ gotoscene('harrisonhouseentrance', transition=fade)

label halloween_voltiumfound:
    hide screen freeroamhud
    "Seems to be unlocked, let's take a look."
    scene harrisonhousebedroom01 with fade
    "Maybe I can find that Voltium somewhere in here."
    scene twentyminuteslater onlayer cutscene with dissolve
    pause 1.2
    scene onlayer cutscene
    with dissolve
    call item_pickup(ItemVoltium) from _call_item_pickup_18
    "So this is Voltium, huh?"
    "We'll see if it lives up to Christy's hype."
    $ quests.christyMandyVoltium = SATISFIED
    $ gotoscene('harrisonhousefloor2', transition=fade)

label halloween_christyandmandypoolsex:
    scene harrisonhousepool with fade
    show christy pokemon
    show mandy supergirl
    with dissolve
    Christy "[player_name]! Please, tell me you have the Voltium."
    Jimmy "Got it right here."
    Christy "See, Mandy? I told you he would get it for us."
    Jimmy "First things first."
    Mandy "Ugh, I told you he was just a pervert."
    Christy "You're right, Mandy. But a deal is a deal."
    Jimmy "That's right, so how are we going to do this?."
    Mandy "Christy?"
    Christy "Hahaha! You think WE are going to have something?"
    Christy "No, my dear. I promised you to show you what the Voltium was capable of, so YOU are just going to watch."
    Mandy "Watch? I don't like this, Christy."
    Christy "Come on, Mandy. We have already done this in front of Teddy."
    Mandy "Yes, but he's my boyfriend. This is different."
    Christy "You said it, YOUR boyfriend, not mine. So, I don't mind."
    Christy "Can you do the same for me this time?"
    Mandy "Ugh... okay."
    Christy "Great, give me the Voltium, [player_name]."
    Christy "Go behind the bushes, it's a good spot to hide. You don't want to be seen spying on us."
    hide christy
    hide mandy
    with dissolve
    "{i}Not much time passed after taking the pills before one of the girls started taking her clothes off.{/i}"
    call christy_halloweenpoolsex_scene from _call_christy_halloweenpoolsex_scene
    Christy "What do you think?"
    Christy "Did we put on a good show?"
    Mandy "What? Oh, shit. I forgot he was here."
    Jimmy "That was hot. That Voltium seems to work well."
    Christy "Oh, it's really good. You should try it sometime. Maybe with one of us..."
    Mandy "Christy!"
    Christy "I'm joking!"
    Christy "Ha, ha! Well, the show is over, new guy."
    $ quests.christyMandyVoltium = COMPLETE
    $ Jimmy.inventory.remove(ItemVoltium)
    $ Christy.relPoints += 1
    $ Mandy.relPoints += 1
    $ gotoscene('harrisonhouseentrance', transition=fade)

####################################################################################################
## Cassidy
####################################################################################################

label halloween_cassidycostumecontest:
    show cassidy daphne neutral with dissolve
    show jimmy smug with dissolve
    play music "audio/music/scoobysong.ogg"
    Jimmy "Well, look who's here..."
    play sound "audio/sfx/hey01.ogg"
    Cassidy "You gotta be fucking kidding me."
    Cassidy "Are we wearing matching costumes?"
    Jimmy "Seems like it, yeah."
    Jimmy "I'm the stoner that likes to get high with his dog..."
    Jimmy "And you're the spoiled brat who likes the jock."
    Jimmy "I believe that's pretty much accurate."
    play sound "audio/sfx/giggle01.ogg"
    Cassidy soberb "Ha, ha, you're an idiot."
    Cassidy "I thought I could get rid of you during Halloween, but here we are."
    Jimmy "Oh, come on! You know you love me."
    Jimmy "You're just afraid to admit it."
    play sound "audio/sfx/hum01.ogg"
    Cassidy neutral "Well, Blair doesn't want to talk to me, which is kind of your fault..."
    Cassidy "And Alice is not allowed to come to this kind of party."
    Cassidy "So, I guess I have to settle with my [roommate_male] tonight."
    Jimmy "I can wear the dog costume if it would make you feel better."
    play sound "audio/sfx/laugh01.ogg"
    Cassidy soberb "HAHAHAHAHAHA!"
    Cassidy "That was really funny."
    Jimmy "You see? We can get along just fine."
    Cassidy neutral "Do you want to sign up for the contest? We are the perfect couple."
    Jimmy "Anything for my dear [roommate_female]."
    jump halloween_costumecontest

label halloween_costumecontest:
    if Jimmy.outfit == JIMMY_SHAGGY:
        scene harrisonbarstage with fade
        show serenity halloween presenter with dissolve
        play music MUSIC_HALLOWEEN_THEME
        Serenity "Alright, ladies and gentlemen, welcome to the annual Halloween costume gala."
        Serenity "A contest to admire the creativity of the outfits being worn by our distinguished guests."
        Serenity "Tonight, we have a special prize for the winners."
        Serenity "That's right, guurl. This time there will be two winners because we are going to judge costume couples!"
        Serenity "Isn't that exciting?"
        play sound "audio/sfx/weirdlaugh.ogg"
        Serenity "HAHAHAHAHAHAHAHAHAHAHAHAHA!" with vpunch
        Jimmy "Wow, what an awful laugh..."
        Serenity "Anyways, let's start with our first couple of contestants."
        scene violetderbyhalloweencontest with fade
        Serenity "Oh, the King and the Queen of the Harrison House!"
        Jimmy "*Wow, she's so hot...*"
        Serenity "Please, give a big round of applause to Violet and Derby!"
        $ Violet.met = True
        $ Derby.met = True
        Serenity "WOOOOOHHH!"
        Derek "Oh, look at those tight pants, Derby. Seems like you skip leg day! Ha, ha, ha, ha!"
        Derby "Shut up, Derek. Who let you in here?"
        scene violetderbyhalloweencontest02 with vpunch
        play sound "audio/sfx/loudfart01.ogg"
        Derby "Oh, shit... I don't feel so good."
        Violet "Derby, oh my god!"
        Derby "I'm sorry babe, I think I drank too much."
        Derek "Goddamn it, Derby! You're dead inside!"
        scene violetderbyhalloweencontest with dissolve
        Violet "Ugh..."
        Serenity "Wow, look at that beautiful dress! Violet, you always shine above the rest, yasss queeeeen!"
        Violet "Thanks, Sery..."
        $ Serenity.met = True
        Serenity "Give it up for Pedro Pan and Stinker Bell! Such a perfect match for this contest!"
        Serenity "I'm sure you two will win this year again!"
        Derek "Boooooring!"
        scene rubyalgiehalloweencontest with fade
        play music MUSIC_FUNNY_MOMENT
        Serenity "Ruby! My girl, you look so cool tonight!"
        Serenity "But, your companion seems to be having a little bit of trouble fitting in his costume."
        Ruby "Ughh, don't tell me about it."
        Algie "Come on, girls, Ruby is a superhero and I'm a villain, don't you see?"
        Algie "It's a good match!"
        Ruby "Ugh... Can somebody please kill me?"
        Serenity "Well, give it up for Queen Maybe and uh... Whatever Algie is wearing!!"
        play sound "audio/sfx/crowdlaughclap01.ogg"
        Derek "Pisstain Man!"
        Algie "Shut up, Derek!"
        scene tatianaderekhalloweencontest with fade
        Serenity "Is that you, Tatiana?"
        Serenity "Wow, I never thought I would see you here."
        Tatiana "Well, I'm just paying a stupid debt to my brother..."
        Serenity "Your costume is really nice."
        Derek "What about me?"
        Serenity "You don't even exist for me, Derek. Get lost."
        Derek "Oh, come on! This is a great costume!"
        Tatiana "This is so stupid, I love it, ha, ha, ha, ha."
        Serenity "Well, give it up for Tatiana and his mentally ill friend!"
        play sound "audio/sfx/crowdlaughclap01.ogg"
        Serenity "Next!"
        scene cassidyjimmyhalloweencontest with fade
        play music "audio/music/scoobysong.ogg"
        Serenity "Oh, here's a surprise!"
        Serenity "This is a last minute entry, fellas."
        Serenity "Oh, blondie! You look so cute tonight!"
        Cassidy "Thank you!"
        Serenity "And who is your hot companion?"
        Serenity "Oh my god! It's the new guy!"
        Jimmy "Sup."
        Serenity "Wow, I love those costumes. Where's the dog? Where's Scrooby Dude?"
        Jimmy "Smoking pot, somewhere..."
        Serenity "Ha, ha, ha, that's funny!"
        play sound "audio/sfx/crowdlaughclap01.ogg"
        Serenity "Alright, let's give it up for our last couple!"
        scene finalhalloweencontest01 with fade
        stop music
        Serenity "Alright, ladies and gentlemen, according to the judges we have a DRAAAAW!"
        Serenity "So, we are going to make a final decision between these two couples, with a special question."
        Serenity "Let's start with Violet, the beloved queen of the Harrison House."
        Serenity "Alright, queen. What do you think about the disparity of social classes that keeps rising in the world year after year?"
        Violet "Thank you, Sery."
        play sound "audio/sfx/stopmusiceffect.ogg"
        play music MUSIC_FUNNY_MOMENT
        Violet "A lot of people have created this idea of a wealth-gap just to justify their own mediocrity."
        Violet "I don't understand why people don't just work harder. I mean, when I need something, I just ask my daddy or my boyfriend, and they solve my problem." 
        Violet "I just read somewhere that some people live in houses with less than seven bathrooms. Seven! Like, how do they even function?"
        Violet "I have a bathroom for each day of the week, each one decorated with stuff from different cultures around the world..."
        Violet "Today I used the Uganda themed bathroom, and while sitting on the toilet lined with leopard furr, I could enjoy a live safari on a wall-sized screen."
        Violet "It is such a rich experience for the senses."
        Violet "Honestly, if people want more money, they should just... what's the word? Manifest it or something."
        stop music
        play sound "audio/sfx/crickets01.ogg"
        Jimmy "..."
        Serenity "Oh... my... god..."
        Serenity "That was an amazing answer, Violet!"
        Violet "Thank you so much, people!"
        play sound "audio/sfx/crowdlaugh01.ogg"
        Serenity "Wow, thinking like that you might become a future president of this country."
        Jimmy "God save us all..."
        Serenity "What did you say?"
        Jimmy "..."
        Serenity "Well, let's go with Cassidy."
        Serenity "If there is one thing about the world you could change what would it be?"
        Cassidy "Umm..."
        Jimmy "Come on, I believe in you."
        play music "audio/music/sadmoment01.ogg"
        Cassidy "I... I think I'd make it easier for family to truly understand each other."
        Cassidy "Not just the surface-level understanding—like knowing your dad's favorite meal or your sibling's weird obsession with that one TV show—but the real understanding."
        Cassidy "The kind where people could talk openly without fear of judgment."
        Cassidy "And siblings don't grow apart because of misunderstandings."
        Jimmy "..."
        Cassidy "Because no matter how much the world changes, family will always be the first place we learn how to love—or how to hurt."
        Jimmy "Wow..."
        Serenity "..."
        play sound "audio/sfx/stopmusiceffect.ogg"
        play music "audio/music/crazymoment01.ogg"
        Serenity "Uhh, cheeesy aleeeeeert!"
        play sound "audio/sfx/weirdlaugh.ogg"
        Serenity "HAHAHAHAHAHAHHAHAHAHHAHAHA!"
        Serenity "Girl, we preps already have perfect families and that is thanks to money, honey."
        Serenity "So, that answer is not good enough for..."
        play sound "audio/sfx/loudfart01.ogg"
        scene finalhalloweencontestfart01 with vpunch
        Derby "Oh fuck... I think I..."
        Derby "I gotta go... Sorry, babe."
        Violet "Derby!!"
        scene cassidyjimmyhalloweencontest with vpunch
        Serenity "..."
        Derek "Did he shit himself?"
        Serenity "..."
        Serenity "ALRIGHT!!!"
        Serenity "Ummm, well... Our beloved king and queen, Violet and Derby, have decided to be so humble to let this new contestants win this time!"
        Serenity "So, congratulations!"
        Serenity "You have won an exclusive our of leisure in the penthouse jacuzzi of the Harrison House."
        Serenity "Enjoy this once in a lifetime privilegue, peasants!"
        jump halloween_cassidyjacuzzi
    elif Jimmy.outfit == JIMMY_PIRATE:
        scene harrisonbarstage with fade
        show serenity halloween presenter with dissolve
        Serenity "Alright, ladies and gentlemen, welcome to the annual Halloween costume gala."
        Serenity "A contest to admire the creativity of the outfits being worn by our distinguished guests."
        Serenity "Tonight, we have a special prize for the winners."
        Serenity "That's right, guurl. This time there will be two winners because we are going to judge costume couples!"
        Serenity "Isn't that exciting?"
        Serenity "HAHAHAHAHAHAHAHAHAHAHAHAHA!" with vpunch
        Jimmy "Wow, what an awful laugh..."
        Serenity "Anyways, let's start with our first couple of contestants."
        scene violetderbyhalloweencontest with fade
        Serenity "Oh, the King and the Queen of the Harrison House!"
        Jimmy "*Wow, she's so hot...*"
        Serenity "Please, give a big round of applause to Violet and Derby!"
        $ Violet.met = True
        $ Derby.met = True
        Serenity "WOOOOOHHH!"
        Derek "Oh, look at those tight pants, Derby. Seems like you skip leg day! Ha, ha, ha, ha!"
        Derby "Shut up, Derek. Who let you in here?"
        scene violetderbyhalloweencontest02 with vpunch
        play sound "audio/sfx/loudfart01.ogg"
        Derby "Oh, shit... I don't feel so good."
        Violet "Derby, oh my god!"
        Derby "I'm sorry babe, I think I drank too much."
        Derek "Goddamn it, Derby! You're dead inside!"
        scene violetderbyhalloweencontest with dissolve
        Violet "Ugh..."
        Serenity "Wow, look at that beautiful dress! Violet, you always shine above the rest, yasss queeeeen!"
        Violet "Thanks, Sery..."
        $ Serenity.met = True
        Serenity "Give it up for Pedro Pan and Stinker Bell! Such a perfect match for this contest!"
        Serenity "I'm sure you two will win this year again!"
        Derek "Boooooring!"
        scene rubyalgiehalloweencontest with fade
        Serenity "Ruby! My girl, you look so cool tonight!"
        Serenity "But, your companion seems to be having a little bit of trouble fitting in his costume."
        Ruby "Ughh, don't tell me about it."
        Algie "Come on, girls, Ruby is a superhero and I'm a villain, don't you see?"
        Algie "It's a good match!"
        Ruby "Ugh... Can somebody please kill me?"
        Serenity "Well, give it up for Queen Maybe and uh... Whatever Algie is wearing!!"
        Derek "Pisstain Man!"
        Algie "Shut up, Derek!"
        scene tatianajimmyhalloweencontest with fade
        Serenity "Is that you, Tatiana?"
        Serenity "Wow, I never thought I would see you here."
        Tatiana "Well, I'm just paying a stupid debt to my brother..."
        Serenity "Your costume is really nice."
        Serenity "And who is your hot companion?"
        Serenity "Oh my god! It's the new guy!"
        Jimmy "Sup."
        Serenity "Wow, I love those costumes. Arrrrgh! Give me some grog! Where did you leave your pirate ship?"
        Jimmy "In the Monkey Island..."
        Serenity "Ha, ha, ha, that's funny! I don't know what that is, but monkeys are always funny."
        Serenity "Alright, let's give it up for our last couple!"
        scene finalhalloweencontest02 with fade
        Serenity "Alright, ladies and gentlemen, according to the judges we have a DRAAAAW!"
        Serenity "So, we are going to make a final decision between these two couples, with a special question."
        Serenity "Let's start with Violet, the beloved queen of the Harrison House."
        Serenity "Alright, queen. What do you think about the disparity of social classes that keeps rising in the world year after year?"
        Violet "Thank you, Sery."
        Violet "A lot of people have created this idea of a wealth-gap just to justify their own mediocrity."
        Violet "I don't understand why people don't just work harder. I mean, when I need something, I just ask my daddy or my boyfriend, and they solve my problem." 
        Violet "I just read somewhere that some people live in houses with less than seven bathrooms. Seven! Like, how do they even function?"
        Violet "I have a bathroom for each day of the week, each one decorated with stuff from different cultures around the world..."
        Violet "Today I used the Uganda themed bathroom, and while sitting on the toilet lined with leopard furr, I could enjoy a live safari on a wall-sized screen."
        Violet "It is such a rich experience for the senses."
        Violet "Honestly, if people want more money, they should just... what's the word? Manifest it or something."
        play sound "audio/sfx/crickets01.ogg"
        Jimmy "..."
        Serenity "Oh... my... god..."
        Serenity "That was an amazing answer, Violet!"
        Violet "Thank you so much, people!"
        Serenity "Wow, thinking like that you might become a future president of this country."
        Jimmy "God save us all..."
        Serenity "What did you say?"
        Jimmy "..."
        Serenity "Well, let's go with Tatiana."
        Serenity "If there is one thing about the world you could change what would it be?"
        Tatiana "Umm..."
        Jimmy "You got this..."
        Tatiana "I think I would change the roles of humans in the world."
        Tatiana "Maybe we are just here to protect and nurture what was already here before we showed up."
        Tatiana "In the vastness of the known universe, we don't know how many planets are able to be as beautiful as ours is."
        Tatiana "Whoever created this, created humans to take care of it; protect this small rounded paradise in the middle of nowhere."
        Jimmy "..."
        Tatiana "I don't know, this is so stupid."
        Jimmy "No, that was great..."
        Serenity "..."
        Serenity "Uhh, hippieeeee aleeeeeert!"
        Serenity "HAHAHAHAHAHAHHAHAHAHHAHAHA!"
        Serenity "Girl, the only thing humans are here for is to make money, honey."
        Serenity "So, that answer is not good enough for..."
        play sound "audio/sfx/loudfart01.ogg"
        scene finalhalloweencontestfart02 with vpunch
        Derby "Oh fuck... I think I..."
        Derby "I gotta go... Sorry, babe."
        Violet "Derby!!"
        scene tatianajimmyhalloweencontest with vpunch
        Serenity "..."
        Derek "Did he shit himself?"
        Serenity "..."
        Serenity "ALRIGHT!!!"
        Serenity "Ummm, well... Our beloved king and queen, Violet and Derby, have decided to be so humble to let this other contestants win this time!"
        Serenity "So, congratulations!"
        Serenity "You have won an exclusive our of leisure in the penthouse jacuzzi of the Harrison House."
        Serenity "Enjoy this once in a lifetime privilegue, peasants!"
        jump halloween_tatianajacuzzi
    elif Jimmy.outfit == JIMMY_HOMELANDER:
        scene harrisonbarstage with fade
        show serenity halloween presenter with dissolve
        Serenity "Alright, ladies and gentlemen, welcome to the annual Halloween costume gala."
        Serenity "A contest to admire the creativity of the outfits being worn by our distinguished guests."
        Serenity "Tonight, we have a special prize for the winners."
        Serenity "That's right, guurl. This time there will be two winners because we are going to judge costume couples!"
        Serenity "Isn't that exciting?"
        Serenity "HAHAHAHAHAHAHAHAHAHAHAHAHA!" with vpunch
        Jimmy "Wow, what an awful laugh..."
        Serenity "Anyways, let's start with our first couple of contestants."
        scene violetderbyhalloweencontest with fade
        Serenity "Oh, the King and the Queen of the Harrison House!"
        Jimmy "*Wow, she's so hot...*"
        Serenity "Please, give a big round of applause to Violet and Derby!"
        $ Violet.met = True
        $ Derby.met = True
        Serenity "WOOOOOHHH!"
        Derek "Oh, look at those tight pants, Derby. Seems like you skip leg day! Ha, ha, ha, ha!"
        Derby "Shut up, Derek. Who let you in here?"
        scene violetderbyhalloweencontest02 with vpunch
        play sound "audio/sfx/loudfart01.ogg"
        Derby "Oh, shit... I don't feel so good."
        Violet "Derby, oh my god!"
        Derby "I'm sorry babe, I think I drank too much."
        Derek "Goddamn it, Derby! You're dead inside!"
        scene violetderbyhalloweencontest with dissolve
        Violet "Ugh..."
        Serenity "Wow, look at that beautiful dress! Violet, you always shine above the rest, yasss queeeeen!"
        Violet "Thanks, Sery..."
        $ Serenity.met = True
        Serenity "Give it up for Pedro Pan and Stinker Bell! Such a perfect match for this contest!"
        Serenity "I'm sure you two will win this year again!"
        Derek "Boooooring!"
        scene tatianajimmyhalloweencontest with fade
        Serenity "Is that you, Tatiana?"
        Serenity "Wow, I never thought I would see you here."
        Tatiana "Well, I'm just paying a stupid debt to my brother..."
        Serenity "Your costume is really nice."
        Derek "What about me?"
        Serenity "You don't even exist for me, Derek. Get lost."
        Derek "Oh, come on! This is a great costume!"
        Tatiana "This is so stupid, I love it, ha, ha, ha, ha."
        Serenity "Well, give it up for Tatiana and his mentally ill friend!"
        Serenity "Next!"
        scene rubyjimmyhalloweencontest with fade
        Serenity "Ruby! My girl, you look so cool tonight!"
        Ruby "Ughh, don't tell me about it."
        Serenity "And who is your hot companion?"
        Serenity "Oh my god! It's the new guy!"
        Jimmy "Sup."
        Serenity "Wow, I love those costumes. What is your group of superheros called?"
        Jimmy "The Offenders..."
        Ruby "Ugh... Can somebody please kill me?"
        Serenity "Ha, ha, ha, you're so funny, Ruby!"
        Serenity "Alright, let's give it up for our last couple!"
        scene finalhalloweencontest03 with fade
        Serenity "Alright, ladies and gentlemen, according to the judges we have a DRAAAAW!"
        Serenity "So, we are going to make a final decision between these two couples, with a special question."
        Serenity "Let's start with Violet, the beloved queen of the Harrison House."
        Serenity "Alright, queen. What do you think about the disparity of social classes that keeps rising in the world year after year?"
        Violet "Thank you, Sery."
        Violet "A lot of people have created this idea of a wealth-gap just to justify their own mediocrity."
        Violet "I don't understand why people don't just work harder. I mean, when I need something, I just ask my daddy or my boyfriend, and they solve my problem." 
        Violet "I just read somewhere that some people live in houses with less than seven bathrooms. Seven! Like, how do they even function?"
        Violet "I have a bathroom for each day of the week, each one decorated with stuff from different cultures around the world..."
        Violet "Today I used the Uganda themed bathroom, and while sitting on the toilet lined with leopard furr, I could enjoy a live safari on a wall-sized screen."
        Violet "It is such a rich experience for the senses."
        Violet "Honestly, if people want more money, they should just... what's the word? Manifest it or something."
        play sound "audio/sfx/crickets01.ogg"
        Jimmy "..."
        Serenity "Oh... my... god..."
        Serenity "That was an amazing answer, Violet!"
        Violet "Thank you so much, people!"
        Serenity "Wow, thinking like that you might become a future president of this country."
        Jimmy "God save us all..."
        Serenity "What did you say?"
        Jimmy "..."
        Serenity "Well, let's go with Tatiana."
        Serenity "If there is one thing about the world you could change what would it be?"
        Ruby "Umm..."
        Jimmy "You got this."
        Ruby "Maybe I would make it easier for kids to choose what they want to do with their lives."
        Ruby "Not be so dependant on what their parents want from them. Just help them become capable enough of choosing their own path..."
        Tatiana "Uhhh, Ruby... Are you okay?"
        Ruby "..."
        Ruby "You know what? I would take care of the tragic injustice of running out of battery at 1%%." 
        Ruby "Like, seriously, why does my flip phone die right when I need to send the most life-changing text?"
        Ruby "Scientists should really stop wasting time on boring things like saving the planet and focus on infinite battery life." 
        Ruby "Priorities, people."
        Jimmy "..."
        Serenity "Wow, that's such a great idea!"
        Jimmy "Mhmm, I see what you mean about meeting other people's expectations, Ruby."
        Ruby "Shut up, that's not your business."
        play sound "audio/sfx/loudfart01.ogg"
        scene finalhalloweencontestfart03 with vpunch
        Derby "Oh fuck... I think I..."
        Derby "I gotta go... Sorry, babe."
        Violet "Derby!!"
        scene tatianajimmyhalloweencontest with vpunch
        Serenity "..."
        Derek "Did he shit himself?"
        Serenity "..."
        Serenity "ALRIGHT!!!"
        Serenity "Ummm, well... Our beloved king and queen, Violet and Derby, have decided to be so humble to let this new contestants win this time!"
        Serenity "So, congratulations!"
        Serenity "You have won an exclusive our of leisure in the penthouse jacuzzi of the Harrison House."
        Serenity "Enjoy this once in a lifetime privilegue, peasant!"
        jump halloween_rubyjacuzzi

label halloween_cassidyjacuzzi:
    scene laterthatday with fade
    $ renpy.pause()
    stop music
    scene harrisonhousejacuzzi with fade
    play music "audio/music/happyrock02.ogg" volume 0.5
    Jimmy "Holy shit, what a view!"
    Cassidy "..."
    Jimmy "Wanna take a dip?"
    play sound "audio/sfx/hum01.ogg"
    Cassidy "No. That's weird."
    Jimmy "Well, what do you want to do?"
    Cassidy "Let's just drink some wine..."
    Jimmy "Alright."
    show twentyminuteslater with fade
    pause 1.0
    hide twentyminuteslater with fade
    show cassidy daphne neutral
    with dissolve
    play sound "audio/sfx/frustratedhum.ogg"
    Cassidy "This is so fucking boring. The wine is good though."
    Jimmy "Wow, thanks."
    Cassidy "I mean, it's not because of you..."
    Cassidy "It's just... It would have been better if you weren't my [roommate_male], you know?"
    Jimmy "Let's play a game."
    Cassidy "Yes, please. What do you want to play?"
    Jimmy "Let's play 2 truths, 1 lie."
    Cassidy "Alright, but we have to swear that anything we say will not get out of here."
    Jimmy "I promise."
    Cassidy "Alright. You start."
    Jimmy "Okay, let me think."
    Jimmy "I... caught a fly with my bare hands."
    play sound "audio/sfx/frustratedhum.ogg"
    Cassidy "Oh, come on! That's boring. You have to say daring things, like... You fucked someone or masturbated in a public place."
    Jimmy "Oh, come on, you're the expert on doing weird shit on public places."
    Cassidy "Yes, and you already know that, so..."
    Jimmy "Alright, first, I snuck into the girl's dorm..."
    Cassidy "Are you serious? You really are a pervert if this is true."
    Jimmy "Two, I fucked the mayor's daughter."
    Cassidy "What the fuck? That's not possible..."
    Jimmy "And, I think one of my [roommate_female]s is hot as fuck."
    Cassidy "..."
    Cassidy blush "Can I ask who?"
    Jimmy "Nope."
    play sound "audio/sfx/mad01.ogg"
    Cassidy "Okay... Um... This is too hard."
    Cassidy "You must be lying about all of them."
    Jimmy "Just one, I swear."
    Cassidy "Did you really fuck Wendy Donaguy?."
    Cassidy "Nah, that's bullshit."
    Jimmy "Did you ever wonder what I did that night when I went out of the house through the window?"
    Cassidy "Wait... I saw you in the morning getting out of a police car."
    play sound "audio/sfx/gasp01.ogg"
    Cassidy "No fucking way! You're fucking nuts!"
    Cassidy "How did that happen?"
    Jimmy "Explanations are not part of the game."
    Cassidy "Ughh... Alright, the lie is that you snuck into the girl's dorm."
    Jimmy "Yes, that's the lie."
    Cassidy "Oh, so you really think one of your [roommate_female]s is hot."
    Jimmy "Yeah."
    Cassidy "..."
    Jimmy "Your turn."
    stop music
    Cassidy "Alright..."
    play sound "audio/sfx/hum01.ogg"
    Cassidy "One, I have never had sex in my life."
    Jimmy "Umm..."
    play sound "audio/sfx/hmm03.ogg"
    Cassidy "Two, I make webcam porn for money."
    Jimmy "Right..."
    play sound "audio/sfx/femaleclearthroat.ogg"
    Cassidy "And... I want to see my [roommate_male]'s dick."
    Jimmy "Wow! That came outta left field."
    Cassidy "Just play."
    Jimmy "Alright..."
    menu:
        "What's the lie?"

        "I've never had sex in my life.":
            Jimmy "I don't believe you're a virgin."
            Jimmy "You must be a nymphomaniac."
            play sound "audio/sfx/wrongfx.ogg"
            Cassidy "Wrong!"
            Cassidy "I am actually a virgin."
            Jimmy "Really? Wow, but you have some kind of addiction to dildos."
            Cassidy "I do have a problem with dildos..."
            Cassidy "It's the only way I can know how a dick feels inside me, kind of."
            Cassidy "Christy says a dick feels ten times better."
            Jimmy "She must already know how every dick in town feels inside her."
            Cassidy soberb "HAHAHAHAHA! You're so mean."
            Cassidy "But, you lost..."
        "I make webcam porn for money.":
            Jimmy "Webcam? Bullshit."
            play sound "audio/sfx/correctfx.ogg"
            Cassidy "Ding, ding. We have a winner!"
        "I want to see your dick.":
            Jimmy "You don't want to see my dick, do you?"
            Cassidy "..."
            play sound "audio/sfx/wrongfx.ogg"
            Cassidy "You lost."
    Cassidy "The webcam porn. That's the lie."
    Jimmy "So, that means..."
    play sound "audio/sfx/hum01.ogg"
    Jimmy "Do you actually want to see my dick?"
    Cassidy "I'm just curious, [player_name]."
    Cassidy "I showed you my boobs that night in my bedroom."
    play sound "audio/sfx/girlsigh01.ogg"
    Cassidy "Since you came home, I can't stop thinking that maybe you could show me your dick."
    Cassidy "I just want to feel a real dick near me."
    Jimmy "Are you sure?"
    Cassidy "Yeah, just a peek."
    Jimmy "Alright."
    call cassidy_halloweenblowjob_scene from _call_cassidy_halloweenblowjob_scene
    scene harrisonhousejacuzzi with fade
    show cassidy daphne neutral with dissolve
    play sound "audio/sfx/girlsigh01.ogg"
    Cassidy "Fuck, I can't... I need to use my toys."
    Jimmy "Wait, you can't leave me like this!"
    Cassidy "Just masturbate or something, that's not my problem."
    hide cassidy
    play sound "audio/sfx/run01.ogg"
    Jimmy "..."
    play sound "audio/sfx/fewmomentslater.ogg"
    scene fewmomentslater with fade
    $ quests.cassidyFirstFuck = ACTIVE
    $ quests.christyPlan = ACTIVE
    $ Cassidy.relPoints += 1
    if quests.halloweenGraffitiMessage == ACTIVE:
        "{i}After having fun in the jacuzzi, [player_name]'s head was clearer than ever.{/i}"
        "{i}He realized the jacuzzi had to be one of the preps' favorite places to hang out.{/i}"
        "{i}So, it was the perfect place to leave a message.{/i}"
        play sound "audio/sfx/guitarriff01.ogg"
        scene prepprankgraffiti with fade
        $ quests.halloweenGraffitiMessage = COMPLETE
        Jimmy "Perfect."
        $ Jimmy.inventory.remove(ItemSprayCan)
    jump halloween_intermission

####################################################################################################
## Tatiana
####################################################################################################

label halloween_tatianacostumecontest:
    scene notcanonwarning with fade
    $ renpy.pause()
    show jimmy smug with dissolve
    show tatiana pirate with dissolve
    Jimmy "Hello, beautiful. I don't think we've met before."
    Tatiana "Mm, yes. You're right. What's your name?"
    Jimmy "[player_name] [player_surname], at your serivice."
    Tatiana "Tatiana Flores. It's a pleasure"
    $ Tatiana.met = True
    Jimmy "Oh, so you're Hispanic."
    Tatiana "Have a problem with that, cariño?"
    Jimmy "Oh, no, señorita. No problema. I like your accent."
    Tatiana "My family is from South America, our accent is not the only exotic thing about us."
    Jimmy "I can see that. That costume looks great on you."
    Tatiana "Gracias! You're the first one to give me a compliment."
    Tatiana "These rich boys are so full of themselves that they just look at expensive costumes."
    Tatiana "I think we look good together. I mean, our costumes match a la perfección."
    Jimmy "Oh, yeah, I see that now. I'm glad I made the right choice."
    Tatiana "Me too, guapo."
    Jimmy "That means handsome, right?"
    Jimmy "Miss Punny uses that word a lot."
    Tatiana "Oh, so you actually pay attention in class."
    Tatiana "Hmm. I could give you some private language lessons tonight."
    Jimmy "I'm listening."
    Tatiana "But, you have to sign up for the contest with me. I want to see these spoiled brats looking at me winning this thing."
    Jimmy "Done."
    jump halloween_costumecontest

label halloween_tatianajacuzzi:
    scene harrisonhousejacuzzi with fade
    show jimmy smug with dissolve
    show tatiana pirate with dissolve
    Tatiana "YES! That was great!"
    Tatiana "Did you see the look on their faces? Increíble!"
    Tatiana "Oh my god. If only Lola could see this."
    Tatiana "I asked her to come, but Vincent wouldn't let her."
    Tatiana "Ese idiota es tan... ugh, so possessive."
    Jimmy "That was fun. First contest I've ever won."
    Tatiana "Me too, ha, ha."
    Tatiana "Well, we have the jacuzzi for an hour, so I don't know about you but..."
    call tatiana_jacuzzisex_scene from _call_tatiana_jacuzzisex_scene
    $ Tatiana.relPoints += 1
    if quests.halloweenGraffitiMessage == ACTIVE:
        scene harrisonhousejacuzzi with fade
        "{i}After having fun in the jacuzzi, [player_name]'s head was clearer than ever.{/i}"
        "{i}He realized the jacuzzi had to be one of the preps' favorite places to hang out.{/i}"
        "{i}So, it was the perfect place to leave a message.{/i}"
        scene prepprankgraffiti with fade
        $ quests.halloweenGraffitiMessage = COMPLETE
        Jimmy "Perfect."
        $ Jimmy.inventory.remove(ItemSprayCan)
    jump halloween_intermission

####################################################################################################
## Ruby
####################################################################################################

label halloween_rubycostumecontest:
    scene notcanonwarning with fade
    $ renpy.pause()
    show jimmy neutral with dissolve
    show ruby maeve with dissolve
    Ruby "Hey! I like your suit."
    Jimmy "Thanks, yours is pretty cool too."
    Ruby "My name is Ruby, Ruby Myers."
    $ Ruby.met = True
    Jimmy "[player_name], it's a pleasure."
    Ruby "Oh, such a gentlemen. That's rare to see these days."
    Jimmy "I like your accent. Where are you from?"
    Ruby "Oh, my family is from the UK. We are actually distantly related to the monarchy."
    Jimmy "Oh, pardon me, my lady."
    Ruby "Ha, ha! You're funny. So, are you a friend of Derby? Is your family part of the Honorary League?"
    Jimmy "Not sure what you're talking about, but no, I'm not a friend of Derby. I don't even know him."
    Ruby "Oh, then you're a commoner."
    Jimmy "If that means I'm as normal as anyone, then yeah, I am."
    Ruby "Don't get me wrong, it's just that here in the Harrison House we are not used to sharing time with people outside of our house."
    Ruby "But... I think you're interesting enough to earn my time."
    Jimmy "I feel honored, your highness."
    Ruby "Awww, you're so cute."
    "I guess she doesn't understand the concept of sarcasm."
    Ruby "It's a change of pace not talking to one of Derby's friends."
    Ruby "Sometimes they get on my nerves."
    Ruby "Did you heard about the costume contest?"
    Jimmy "Kind of, I'm not sure how it works."
    Ruby "This time is a couple's contest. To participate we need to have matching costumes."
    Jimmy "What do you think about us?"
    Ruby "We look really nice together. I would love to win this contest at least once."
    Jimmy "Well, my lady, I'm at your service."
    jump halloween_costumecontest

label halloween_rubyjacuzzi:
    scene harrisonhousejacuzzi with fade
    show jimmy neutral
    show ruby maeve
    with dissolve
    Ruby "Well, I didn't expect this to be the prize."
    Ruby "The water seems warm though, so we might as well take a dip."
    Jimmy "Sure thing, I've never used a jacuzzi in my life."
    Ruby "Oh, so this is your first time, that's so cute."
    Ruby "I guess you're used to common showers and stuff like that, right?"
    Jimmy "Well, I sometimes have to take a bath under the rain, you know, 'cause it's free."
    Ruby "Oh, that's so sad..."
    "Did she seriously just believe that?"
    Ruby "Well, in a jacuzzi the water is warm and really enticing."
    Jimmy "Alright, so, do we take our clothes off? Or..."
    Ruby "Yes, of course, we can go in in our underwear."
    call ruby_jacuzzisex_scene from _call_ruby_jacuzzisex_scene
    $ Ruby.relPoints += 1
    if quests.halloweenGraffitiMessage == ACTIVE:
        scene harrisonhousejacuzzi with fade
        "{i}After having fun in the jacuzzi, [player_name]'s head was clearer than ever.{/i}"
        "{i}He realized the jacuzzi had to be one of the preps' favorite places to hang out.{/i}"
        "{i}So, it was the perfect place to leave a message.{/i}"
        scene prepprankgraffiti with fade
        $ quests.halloweenGraffitiMessage = COMPLETE
        Jimmy "Perfect."
        $ Jimmy.inventory.remove(ItemSprayCan)
    jump halloween_intermission
