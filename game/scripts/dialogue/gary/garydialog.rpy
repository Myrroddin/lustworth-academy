default quests.garyHalloweenHeist = LOCKED

label garyhalloweenheistintro:
    hide screen freeroamhud with None
    #stop music
    show pete uniform neutral
    with dissolve
    play sound "audio/sfx/heypete01.ogg"
    Pete "Hey [player_name]!"
    Pete "I need to talk to you about something."
    Jimmy "Right, what is it?"
    Pete "It's about Gary..."
    Pete "He's coming up with a plan for Halloween."
    Jimmy "Oh, is he planning a girls sleepover?"
    play sound "audio/sfx/heygary02.ogg"
    Gary "Ha, ha, ha, very funny, [player_name] boy!" with vpunch
    play music MUSIC_GARYS_THEME
    show gary uniform neutral left with dissolve
    Gary "Fucking hilarious..."
    Jimmy "Thanks."
    Gary "Halloween is coming, [player_name]."
    Gary "And our fellow preps are getting ready for a party at their castle."
    Gary "Those spoiled brats with an abandonment trauma always get the best piece of the cake."
    Gary "While we, the people, get dressed in our cheap costumes and roam scared around the schoolgrounds while dealing with Russell's goons."
    Gary thinking left "Do you think that's fair, little Pete?"
    Pete "Umm... No, Gary."
    Gary "Of course not, Pete."
    Gary "So, I have a plan to ruin their night for once and give them what they deserve."
    Jimmy "Well, good luck with that."
    Gary cocky left "Oh, [player_name], I can tell you like to be begged, don't you?"
    Gary "Why do you think I'm telling this to you?"
    play sound "audio/sfx/clearthroat01.ogg"
    Jimmy "To fill your megalomaniacal ego?"
    Gary "Oh, yes, that's right, but we also need your help, my friend."
    Gary thinking left "I know you have... resources."
    Gary "Sneaking into the girls' dorm is not an easy feat, am I right?"
    Jimmy "That's none of your business, Gary."
    Gary "Of course not, [player_name] boy. But, you need to understand that I'm the one that needs your wits."
    Gary pointing left "Put yourself in my shoes, and you'll see that my intention is not to reveal your secrets..."
    Gary "Because, we are friends, right? And, as friends, we should be able to trust each other."
    Jimmy "..."
    Gary "So, I'm going to make you a deal."
    Gary "If you help me with this, you'll get to sit by my side once I take over the school."
    Gary "No one and nothing will stand against us."
    Gary cocky left "Look at little Pete, he accepted to join me because he believes in this cause."
    Gary "He might be a coward, but he's smart..."
    Pete "Gary..."
    play sound "audio/sfx/whispermale.ogg"
    Gary thinking left "Shushhh! So, [player_name], I just need you to get something for us."
    Gary "The only thing we need is a can of spray paint."
    Gary "And you need to get yourself an invitation for the Halloween party."
    Gary neutral left "Pete, go ahead."
    Pete "Alright, [player_name]. We'll explain everything once you get those two things."
    Pete "You can find a can of spray paint in the Garage backyard. The Greasers have a hidden storage somewhere..."
    Pete "If you can find it, you'll be able to get the can."
    Pete "And, about the invitation, I'm still figuring out how to get you one."
    Pete "I already got Gary his invitation from Eunice, don't ask what I had to do."
    Pete "And I have a clue of where to find one for me."
    Pete shy "I have an idea, but it's a bit dangerous."
    Gary cocky left "Just tell him, Pete!"
    Gary "Our friend here is a man who doesn't fear danger."
    Pete neutral "Right, I heard that Miss Dawson confiscated an invitation recently, so maybe you can find it in her office."
    Jimmy "Umm... Alright."
    Jimmy "I might be interested in going to that party, anyways, so..."
    Gary neutral left"I knew you were smart, my friend."
    Gary "Let me know when you are ready and, obviously, get yourself a costume..."
    Gary "You can't enjoy Halloween without a costume, am I right?"
    Gary "It will be a night to remember, [player_name]. You can be sure of that."
    Jimmy "Yeah, right."
    hide pete
    hide gary
    stop music
    play sound "audio/sfx/signature01.ogg"
    show halloweenheistplans01 with dissolve
    Jimmy "Let's see what I need for this plan..."
    play sound "audio/sfx/signature01.ogg"
    show halloweenheistplans02 with dissolve
    Jimmy "I need to find a spray paint can."
    play sound "audio/sfx/signature01.ogg"
    show halloweenheistplans03 with dissolve
    Jimmy "Get myself an invitation for the party."
    play sound "audio/sfx/signature01.ogg"
    show halloweenheistplans04 with dissolve
    Jimmy "And... a costume, obviously."
    Jimmy "Well, I think I'll start with the spray paint."
    if quests.missdawsonHalloweenStaff == COMPLETE:
        show halloweenheistplansinvitation with dissolve
        Jimmy "I already got the invitation from Miss Dawson."
    Jimmy "I'll figure out the rest later."
    $ quests.garyHalloweenHeist = ACTIVE
    $ gotoscene('boysdormtvroom')

label chapterone_garyhalloweenintro:
    hide screen freeroamhud
    play music MUSIC_GARYS_THEME
    show gary nazi neutral with dissolve
    Jimmy neutral "Hey! What are you doing in my room?"
    play sound "audio/sfx/heygary02.ogg"
    Gary "Not much, just laying here, wishing I could be more like you."
    Jimmy "..."
    Gary "But, I'm cursed."
    Jimmy "..."
    Gary "Cursed by brains."
    Gary thinking "You don't have any idea what torture it is to be thinking all the time."
    Jimmy "Oh, and what do you think about? Torturing people?"
    Gary "Even better, have you ever heard about Machiavelli? That guy was cold blooded."
    Jimmy "What do you want, Gary? Get to the point."
    Gary "Well, you know I've been planning this for weeks..."
    Gary "All the prefects are at out in town."
    Gary "And the teachers are entertaining - I use that word loosely - the kids."
    Gary "I think the opportunities for fun are pretty much nil."
    Jimmy "So, what do you have in mind?"
    Gary pointing "Well, the stupid leader of the preps banned me from entering the Harrison House a long a time ago..."
    Gary "So, having an invitation is useless for me."
    Jimmy "Wonder why..."
    play sound "audio/sfx/clearthroat01.ogg"
    Gary "But, I have a plan to humiliate him..."
    Gary "Our companion in crime will give you the details, my friend."
    Jimmy "Companion?"
    Gary cocky "Pete! Come here!"
    Gary "You'll love the costume I got him."
    hide jimmy with dissolve
    show pete bunny neutral with dissolve
    play music MUSIC_FUNNY_MOMENT
    play sound "audio/sfx/heypete01.ogg"
    Pete "Hey, [player_name]."
    Pete "Gary, this suit is ridiculous."
    Gary neutral "Oh, come on, Pete! It's genius. No one will suspect that the guy in the pink bunny costume is a big time prankster."
    Pete "Ugh..."
    Gary "You look fine, Pete. Now, fill our friend [player_name] with the details while we make our way to the mansion."
    Pete "Alright..."
    jump halloween_harrisonhousearrival