label beatrixbiologyessay:
    hide screen freeroamhud
    play music MUSIC_BEATRIX_THEME
    show beatrix herpes talk with dissolve
    Jimmy "Hey, Beatrix."
    play sound "audio/sfx/hey01.ogg"
    Beatrix "Oh, hey."
    "{i}He's eyes immediately fell on the faint, reddish rash on the side of her mouth."
    "{i}'It looks an awful lot like cold sores.' [player_name] kept the thought to himself.{/i}"
    play sound "audio/sfx/frustratedhum.ogg"
    Beatrix "Look, about Halloween... I need to be clear about something."
    Beatrix "I was pretty drunk, alright? Like, seriously tipsy."
    play sound "audio/sfx/femaleclearthroat.ogg"
    Beatrix "I get the joke, that you tried to make me drink alcohol, but it's not funny."
    Jimmy "What?"
    play sound "audio/sfx/mad01.ogg"
    Beatrix mad "Don't get your hopes up that anything like that is going to, you know, *repeat* itself."
    Jimmy "First of all, I didn't know it had alcohol."
    Beatrix "Well, I guess you don't know how to read, but whatever..."
    "{i}Before [player_name] could start a round of insults to shut her down, a familiar, crisp voice cuts the air.{/i}"
    play sound "audio/sfx/stopmusiceffect.ogg"
    play music MUSIC_DAWSONS_THEME
    show missdawson neutral left with dissolve
    play sound "audio/sfx/femaleclearthroat.ogg"
    Dawson "Beatrix! There you are. I was just looking for you."
    Beatrix talk "Miss Dawson. Is everything alright?"
    play sound "audio/sfx/hmm01.ogg"
    Dawson "Well, not exactly. I'm afraid your last biology test score has given your teacher, a bit of a fright."
    Dawson "You know we want you to succeed, especially with your aspirations."
    Dawson "Mr. Vivisect has agreed to let you write a detailed essay on the human reproductive system, as an opportunity to raise your grade."
    play sound "audio/sfx/frustratedhum.ogg"
    Beatrix talk arm "The human reproductive system? Ugh..."
    Beatrix "I guess if I really want to be the one who discovers the cure for cancer, I can't be squeamish."
    Beatrix talk "Fine. I'll do it. No problem."
    hide beatrix with dissolve
    Dawson "That's the spirit. Now, Mr. [player_surname]."
    Dawson talk arm left "The Headmaster is due back next week."
    Dawson "And he wants to have a very serious conversation with you about your... antics on Halloween night."
    Dawson "However, if you can help Beatrix with this essay, I will personally vouch for your good intentions when he returns."
    Jimmy "Seriously? Thank you. I'll do it. Absolutely."
    play sound "audio/sfx/alright01.ogg"
    Dawson "Alright, that's it for now."
    hide missdawson with dissolve
    show beatrix herpes mad arm with dissolve
    Beatrix "You see? I can't even get rid of you!"
    Beatrix mad "You better not ruin this for me."
    Jimmy "Come on, you know you like me to be around..."
    Beatrix "Ugh, meet me in the Biology Lab in a couple of days. I need to gather some books and information first."
    Jimmy "Alright, sure."
    call nexttime from _call_nexttime_7
    $ quests.beatrixHomework = SATISFIED
    $ gotoscene('mainbuildingrighthallway')

label beatrixbiologyessay02:
    hide screen freeroamhud
    stop music
    scene chemistrylab01 with fade
    "{i}The Biology Lab had an old air conditioner that clacked once in a while but kept the room fresh.{/i}"
    play music MUSIC_BEATRIX_THEME
    show beatrix herpes mad with dissolve
    play sound "audio/sfx/mad01.ogg"
    Beatrix "I was hoping you forgot to show up."
    Beatrix "But, then again, having someone to test my theories on, it's a good idea."
    Jimmy "Hey! Good to see you, Beatrix. You look great today, by the way."
    Beatrix "Oh, so you know how to use sarcasm, huh..."
    Beatrix talk "Let's cut to important stuff. I have been here for one hour and I believe I have five pages written."
    Beatrix "Of course, it's just a draft, but it's a good introduction."
    Jimmy "Five pages for an introduction? Wow, you're good."
    Beatrix talk arm "Alright, so the essay needs to cover the entire male reproductive system."
    Beatrix "Structure, function, hormones... the works."
    Jimmy "Right... Well, we got two balls and a stick, what else?"
    play sound "audio/sfx/frustratedhum.ogg"
    Beatrix "Oh my god... This is going to be really hard."
    Jimmy "Oh, yeah. It gets hard, depending if you're naked or not."
    play sound "audio/sfx/mad02.ogg"
    Beatrix mad "AAAGGHH! Can you just be serious for a minute?"
    Jimmy "Alright, alright... Jesus..."
    Jimmy "There is something I want to ask before we start."
    Beatrix herpes talk "I'm listening."
    Jimmy "About that... rash thing. On your mouth."
    "{i}Beatrix's head snaped up, her eyes narrowing. She instinctively touched the side of her mouth.{/i}"
    play sound "audio/sfx/hmm02.ogg"
    Beatrix "What about it? Don't worry, it's not contagious, if that's what you're worried about."
    Jimmy "I know it's probably none of my business, but I wanted to make sure you're okay."
    Jimmy "A friend of mine has those things and they can be uncomfortable."
    Beatrix "Those 'things'?"
    "{i}Her voice got dangerously quiet, laced with an accusation that hanged heavy in the air.{/i}"
    play sound "audio/sfx/mad01.ogg"
    Beatrix mad arm "Are you seriously implying I have herpes?"
    Jimmy "Well, that looks like a cold sore, from a distance."
    "{i}Beatrix stares at him, her anger slowly giving way to a frustrated sigh. She rubs the affected area gently.{/i}"
    play sound "audio/sfx/frustratedhum.ogg"
    Beatrix herpes talk "It's called Perioral dermatitis"
    Beatrix "It's a skin condition. It's not contagious, and it's definitely not from... kissing someone else."
    "{i}She casts her eyes down, then looks back up at him, a flicker of something softer in her gaze.{/i}"
    Beatrix "And for the record... the only person I've been THAT close to, is you."
    "{i}A beat of surprised silence hangs between them, the fluorescent lights of the lab buzzing overhead.{/i}"
    Jimmy "I'm sorry, Beatrix."
    Beatrix "Whatever."
    "{i}She sighs, picking up her pen and tapping it against the textbook.{/i}"
    Jimmy "Alright, let's just do the homework."
    Beatrix "Yes, please."
    play music MUSIC_FUNNY_MOMENT
    scene malereproductivediagram with fade
    Beatrix "So, here's the male reproductive system."
    Jimmy "..."
    play sound "audio/sfx/hum01.ogg"
    Beatrix "Of course, from the outside it looks diferent. But, here we can see the shape of it and start identifying more or less where is everything."
    Jimmy "He, he, he, he..."
    Beatrix "..."
    Beatrix "Ummm, it's interesting how the prostate it's so problematic for men, at least in the latest stages of age."
    Jimmy "He, he, he..."
    Beatrix "Oh, my god."
    Beatrix "Do you want to say something?"
    Jimmy "..."
    play sound "audio/sfx/girlsigh01.ogg"
    Beatrix "I know it will be stupid, just say it."
    Jimmy "Mine is bigger, ha, ha, ha, ha!"
    Beatrix "..."
    Beatrix "You guys really think with your cocks, don't you?"
    Jimmy "HAHAHAHAHAHAHAHA! I'm sorry, I had to say it." with vpunch
    play sound "audio/sfx/femaleclearthroat.ogg"
    Beatrix "Well, you know what's funny about that?"
    Jimmy "What?"
    Beatrix "It's true, yours is bigger."
    Jimmy "Aha! You still remember, don't you?"
    Beatrix "Ha, ha, ha, ha, yes, idiot."
    play music "audio/music/tendertheme02.ogg"
    scene chemistrylab01 with fade
    show beatrix herpes talk with dissolve
    Beatrix "Can I tell you, something?"
    Jimmy "Sure."
    play sound "audio/sfx/girlsigh01.ogg"
    Beatrix "It was kind of cute that you cared about my... problem."
    Jimmy "Well, that's what friends are for."
    play sound "audio/sfx/hmm03.ogg"
    Beatrix "Really? We are friends?"
    Jimmy "Of course, you were basically the first student I met when I got here."
    Jimmy "And, I risked my skin for you to get your diary back."
    Jimmy "And, you gave me a lap dance. It was really good, by the way."
    Beatrix "Ugh..."
    Jimmy "I won't talk about Halloween, because you already told me not to."
    play sound "audio/sfx/frustratedhum.ogg"
    Beatrix "I guess you're right."
    Beatrix "I have an idea."
    Jimmy "What do you have in mind?"
    Beatrix "Well, know that we are studying the male reproductive system."
    Beatrix "I was thinking that maybe we could study a real specimen."
    Jimmy "Ummm, I like where you're going..."
    Beatrix "What are you waiting for, then."
    call beatrix_beatrixfootjob_scene from _call_beatrix_beatrixfootjob_scene
    stop music
    scene chemistrylab01 with fade
    show beatrix herpes talk with dissolve
    play sound "audio/sfx/frustratedhum.ogg"
    Beatrix "Ugh, I'm gonna have to clean this mess, now."
    Beatrix "Anyways, I'll see you tomorrow to finish the rest of the essay."
    Jimmy "I'll be here."
    $ BeatrixDaylimit = True
    $ quests.beatrixHerpes = ACTIVE
    call nexttime from _call_nexttime_8
    $ gotoscene('mainbuildinglefthallway')

label beatrixbiologyessay03:
    hide screen freeroamhud
    stop music
    scene chemistrylab01 with fade
    "{i}Beatrix was already seated near another poster of the female reproductive system propped up on the wall beside her.{/i}"
    "{i}Her mood seems markedly better than yesterday.{/i}"
    play music MUSIC_BEATRIX_THEME
    show beatrix herpes talk with dissolve
    Jimmy "Hey!"
    play sound "audio/sfx/hey01.ogg"
    Beatrix talk arm "Oh, hey, [player_name]. You made it."
    Beatrix "Ready to delve into the fascinating world of estrogen and oocytes?"
    Jimmy "Whatever that is, sure."
    scene femalereproductivediagram with fade
    Jimmy "With all this tubes and weird stuff we have inside, this looks more like a plumbing exam."
    play sound "audio/sfx/giggle01.ogg"
    "{i}Beatrix lets out a small, unexpected laugh, then gives him a playful glare.{/i}"
    Beatrix "Okay, bad joke, but I'll allow it."
    Jimmy "And talking about plumbing..."
    Jimmy "Here's a tube that will help you."
    "{i}[player_name] reached into his pocket and pulls out a small, white tube."
    Beatrix "What's that?"
    play music "audio/music/tendertheme02.ogg"
    Jimmy "I know I put my foot in my mouth, last time. So, I stopped by the Nurse's office after school."
    $ Jimmy.inventory.remove(ItemDermatitisCream)
    "{i}He gently slides the tube across the table towards her.{/i}"
    Jimmy "She said it might help with your problem."
    play sound "audio/sfx/gasp01.ogg"
    Beatrix "Oh my god... you didn't have to do that."
    "Beatrix picks up the tube, her fingers brushing against the label while her cheeks were blushing."
    Beatrix "You're... actually not an idiot, are you?"
    Jimmy "Only when it comes to the concept of personal space."
    play sound "audio/sfx/girlsigh01.ogg"
    Beatrix "Thank you, [player_name]. Seriously. That's really sweet."
    Jimmy "Anytime."
    Beatrix "Okay. The essay. Let's finish up the female hormones before the day is over."
    Jimmy "I have an idea."
    play sound "audio/sfx/hmm02.ogg"
    Beatrix "Oh, oh..."
    Jimmy "Last time, we made sure to study my real specimen."
    Beatrix "I was thinking that maybe we could study a real specimen."
    Beatrix "Oh, god..."
    Jimmy "So, why don't you show me yours?"
    Beatrix "..."
    Beatrix "Fair enough..."
    call beatrix_beatrixboobjob_scene from _call_beatrix_beatrixboobjob_scene
    stop music
    scene chemistrylab01 with fade
    show beatrix herpes talk with dissolve
    play sound "audio/sfx/hum01.ogg"
    Beatrix "This is getting out of hand."
    Beatrix "At least, we're almost finished."
    Jimmy "Thank you for helping me with this."
    Beatrix "Thank you, for the cream."
    Jimmy "Which one? The one from my cock or..."
    play sound "audio/sfx/laugh02.ogg"
    Beatrix "HAHAHAHAHAHA! Get out of here!" with vpunch
    $ BeatrixDaylimit = True
    $ quests.beatrixHerpes = COMPLETE
    call nexttime from _call_nexttime_50
    $ gotoscene('mainbuildinglefthallway')