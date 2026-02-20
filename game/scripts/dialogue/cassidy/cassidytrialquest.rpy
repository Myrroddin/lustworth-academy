default quests.cassidyTrials = LOCKED
default quests.christyPlan = LOCKED

label cassidytrialsquestintro:
    hide screen freeroamhud with None

    "{i}As you entered the gym, you realized there were some girls doing something weird in a corner.{/i}"
    "{i}An opportunity to see girls jumping in short skirts? Of course [player_name] wasn't going to let it pass.{/i}"
    scene cassidytrialsintro01 with fade
    "{i}Getting closer, you could see Cassidy nervously standing in line with a couple other gals.{/i}"
    "{i}A confident redhead girl stood in front of the girls, surveying them with a critical eye.{/i}"
    stop music
    play music MUSIC_CHRISTY_THEME
    scene gymwallbackground with fade
    show christy cheerleader neutral with dissolve
    play sound "audio/sfx/alright02.ogg"
    Christy "Alright, ladies, show me what you've got. Cassidy, you're up first."
    Cassidy "Oh, no..."
    "{i}Cassidy took a deep breath and launched into a dancing routine.{/i}"
    play sound "audio/sfx/big_punch.ogg"
    scene cassidytrialsintro02 with vpunch
    "{i}Her movements were kind of stiff and the uniform she wore was really short.{/i}"
    play sound "audio/sfx/slap.ogg"
    show cassidytrialsintro03 with vpunch
    "{i}The word 'bitch' could be seen on the side of her skirt. [player_name] wondered if that was that the name of the team?{/i}"
    scene gymwallbackground with fade
    show christy cheerleader neutral with dissolve
    show cassidy cheerleader neutral left with dissolve
    play sound "audio/sfx/hum01.ogg"
    Christy mad "Your jump is improving a bit, but your arm movements are so lazy!"
    Christy "We're going to have to work on those."
    Christy sinister "I have the best exercise for it."
    Christy "Are you up for the challenge?"
    play sound "audio/sfx/girlsigh01.ogg"
    Cassidy pleading left "Yes, Christy, I'll do anything."
    Christy "Of course you would, darling."
    Christy "Alright, I'll get everything ready and see you at the library's entrance."
    Cassidy "Okay..."
    hide christy
    Jimmy "Hey, [roommate_female]."
    Cassidy shocked "What are you doing here?" with vpunch
    Jimmy "Ah, just watching you dancing and stuff."
    Cassidy cheerleader soberb "Of course, what else would I expect from a pervert like you."
    Cassidy "Get out of my way, I have more important things to do than talking to you."
    Jimmy "Alright, princess... Are you going to the male's locker room again?"
    play sound "audio/sfx/mad01.ogg"
    Cassidy mad "Uggghh! Shut up, idiot!" with vpunch
    hide cassidy with vpunch
    "{i}Cassidy stormed off clearly mad at [player_name].{/i}"
    "{i}And he wondered if he could see those exercises they talked about at the Library.{/i}"
    $ quests.cassidyTrials = ACTIVE
    return

label cassidytrialsbanana:
    hide screen freeroamhud with None
    stop music
    play music MUSIC_FUNNY_MOMENT
    scene libraryentrancecrowd with fade
    play sound "audio/sfx/crowdlaughclap01.ogg"
    "{i}There was something going on at the entrance of the library that attracted the attention of many students gathering around what looks to be a giant banana.{/i}"
    "{i}Everyone was laughing out loud as the banana moved around making strange moves.{/i}"
    show christy uniform sinister with dissolve
    "{i}Christy was standing close to the banana, with a sinister smile.{/i}"
    "{i}Is that Cassidy, then? [player_name] wondered.{/i}"
    hide christy with dissolve
    scene cassidybanana01 with vpunch
    play sound "audio/sfx/crowdlaugh01.ogg"
    Lola "Hey, look, it's Bananas Cassidy!"
    Algie "Yeah! Who's ready for potassium power?"
    Derek "Shut up, Algie! You're such a nerd, even for jokes."
    Algie "Oh..."
    "{i}At first, [player_name] is amused with the sight of seeing his spoiled [roommate_female] doing ridiculous stuff.{/i}"
    "{i}But, as the seconds went by, he could see the sadness in Cassidy's eyes. At some point, it wasn't funny anymore.{/i}"
    $ showscene('schoollibraryplaza', transition=fade)
    stop music
    play music MUSIC_CHRISTY_THEME
    show christy uniform sinister with dissolve
    play sound "audio/sfx/femaleclearthroat.ogg"
    Christy "Oh, the guy that likes to spy on his [roommate_female]."
    Christy "Do you like the view?"
    Jimmy "I don't."
    Christy "Oh, come on, don't be so boring..."
    Christy "I told you, this is not personal. It's part of the ritual to become a cheerleader."
    Jimmy "Right, stupidity is an important part of being a cheerleader."
    Christy mad "Listen, you idiot. Being a cheerleader in this academy is one of the best privileges a girl could strive for."
    Christy "I'm really sorry that your [roommate_female] here doesn't have what it takes, though."
    play sound "audio/sfx/laugh01.ogg"
    Christy laugh "But, she is good at being a banana, HAHAHAHAHAHAHA!"
    hide christy with dissolve
    stop music
    play sound "audio/sfx/crowdshock01.ogg"
    Jimmy "Well, diplomacy didn't work, so..."
    Jimmy "Let's do some crowd control."
    play sound "audio/sfx/crowdlaugh01.ogg"
    "{i}No one saw [player_name] quietly taking the extinguisher from the wall.{/i}"
    "{i}He just needed to take the lock out and use something to clamp the trigger, like a belt...{/i}"
    play music "audio/music/crazymoment01.ogg"
    scene cassidybanana03 with vpunch
    play sound "audio/sfx/slap.ogg"
    "{i}The masterplan worked, as the extinguisher started to fire the foam while spinning around in the floor.{/i}"
    play sound "audio/sfx/scream01.ogg"
    "{i}[player_name] watched everything from a safe distance, careful to not being seen by the cameras.{/i}"
    play sound "audio/sfx/horrorscream.ogg"
    "{i}The crowd started to run away in all directions and Cassidy found a way to sneak out of Christy's sight.{/i}"
    show algieuniformpantsdown with vpunch
    play sound "audio/sfx/whistle01.ogg"
    Algie "Hey, who took my belt!?"
    $ quests.cassidyTrials = SATISFIED
    play sound "audio/sfx/fewmomentslater.ogg"
    scene fewmomentslater with fade
    $ renpy.pause()
    call nexttime from _call_nexttime_47
    $ showscene('schoollibraryplaza', transition=fade)
    Jimmy "This is getting out of control."
    Jimmy "I need to talk to her, maybe this weekend."
    $ gotoscene('schoollibraryplaza')

label cassidytrialbedroomtalk:
    hide screen freeroamhud with None
    stop music
    scene cassidycrossedlegs with fade
    play sound "audio/sfx/doorclose01.ogg"
    play music MUSIC_CASSIDY_THEME
    "{i}As [player_name] entered the bedroom, he saw Cassidy sitting cross-legged on her bed, looking utterly dejected.{/i}"
    "{i}Her room was filled with posters of inspirational quotes and pictures of her on family trips.{/i}"
    Jimmy "Banana emergency? Or just looking a-peel-ing?"
    play sound "audio/sfx/hum01.ogg"
    Cassidy "Not in the mood for your stupid jokes, [player_name]."
    Jimmy "Ah, come on. It's always fun when you treat me like shit and then I get back at you with something clever."
    play sound "audio/sfx/girlsigh01.ogg"
    Cassidy "*Sigh*..."
    Jimmy "What's going on?"
    Cassidy "Christy. She's making me do these ridiculous tasks just to get on the cheerleading team."
    Cassidy "You saw me dressed like a giant banana, dancing in front of the entire school!"
    Jimmy "Please tell me the security cameras got that on video, because I will find a way to get my hands on it."
    play sound "audio/sfx/frustratedhum.ogg"
    Cassidy "Not helping, [player_name]."
    Jimmy "Alright, alright... The question is, why you're going along with it?"
    Cassidy "I don't know. I guess I just really want to be on the team."
    Cassidy "Cheerleading's supposed to be fun and... I thought it'd make me feel more confident."
    Cassidy "I don't know why I'm talking about this with you..."
    Jimmy "Well, even though we don't get along most of the time, you're still my [roommate_female]."
    Jimmy "So, does it feel fun? Or you're just doing what other people told you to do for their amusement?"
    play sound "audio/sfx/hmm01.ogg"
    Cassidy "I guess I feel used."
    Jimmy "Then, let's fix it."
    Cassidy "Fix what?"
    Jimmy "Your confidence problem."
    Jimmy "Forget Christy and her stupid rituals."
    Jimmy "If you want to feel confident, you need to stand up for yourself."
    Jimmy "Prove that bitch what you're made of. Prove her that you can be a better leader that she is."
    "{i}Cassidy looked at him with a hopeful expression.{/i}"
    play sound "audio/sfx/giggle01.ogg"
    Cassidy "I thought you were a total asshole."
    Jimmy "Well, it depends on the situation."
    Cassidy "Do you remember when we were kids?"
    Jimmy "To be honest, I don't remember much."
    Cassidy "Look..."
    "{i}Cassidy pointed at a picture hanging on the wall and [player_name] took it in his hands.{/i}"
    play music "audio/music/tendertheme02.ogg"
    scene woodstripphoto with fade
    Cassidy "That's the last trip to the woods we made before you left."
    Jimmy "A camping trip... Is that the time you got lost looking for 'fairy dust'?"
    play sound "audio/sfx/hum01.ogg"
    Cassidy "What? I wasn't looking for 'fairy dust', I was just exploring."
    Jimmy "Right, exploring... You almost got us grounded for life."
    Cassidy "You found me, remember?"
    play sound "audio/sfx/giggle02.ogg"
    Cassidy "I was crying and then you distracted me with some ridiculous story about trolls being turned to stone with the sunlight."
    Jimmy "That story is a masterpiece, and it worked, didn't it?"
    scene cassidybedroomnight with fade
    show cassidy pajama neutral with dissolve
    "Cassidy looked at him with a smile."
    play sound "audio/sfx/girlsigh01.ogg"
    Cassidy "You did it, again."
    Cassidy "I saw you firing the extinguisher that day."
    Jimmy "Well, that dance was horrible, so..."
    play sound "audio/sfx/laugh03.ogg"
    Cassidy laugh "Ha, ha, ha, ha! You idiot."
    Cassidy "I just wanted to thank you."
    Cassidy "I know you have been watching me doing strange stuff with my toys."
    Cassidy "And even though I've been a little bit rough with you, you haven't said anything to anyone."
    Jimmy "Yeah, well, we all have our hobbies."
    play sound "audio/sfx/hmm02.ogg"
    Cassidy horny "Is it your hobby peeking at me while I shower?"
    Jimmy "I was going to take a shower after a tough day at the ranch, and you were there."
    Cassidy "Of course, and you stayed for a while..."
    Cassidy "I'm not judging you."
    Cassidy "I mean, it felt kind of weird to be seen like that by your [roommate_male]."
    Cassidy "But, I get that you're a curious. I am too, you know?"
    play sound "audio/sfx/undress01.ogg"
    call cassidy_titsout_scene from _call_cassidy_titsout_scene
    scene cassidybedroomnight with fade
    show cassidy topless pleading with dissolve
    Cassidy pleading "I'll try my best to stand up for myself."
    Jimmy "That's a start."
    Cassidy "By the way, are you going to the Halloween party?"
    Jimmy "Halloween party? I'm not sure."
    play sound "audio/sfx/hum01.ogg"
    Cassidy neutral "You need an invitation. I'm sure you can get one somehow."
    Cassidy "If you happen to go to the party, maybe we can hang out."
    Jimmy "Sure, I'll see what I can do."
    $ quests.cassidyTrials = COMPLETE
    $ Cassidy.relPoints += 1
    $ gotoscene('townhousehallway')