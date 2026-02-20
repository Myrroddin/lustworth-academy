label missdawsonunderthedesk:
    hide screen freeroamhud
    Jimmy "Hello, Miss."
    show missdawson neutral with dissolve
    Dawson "Oh, it's you. Today I don't have time for students."
    Dawson "I have an important meeting with the Headmaster, so, off with you."
    "{i}[player_name] immediately thought about what he saw the last time he came to the office.{/i}"
    "{i}Maybe their 'meeting' could have something to do with the naughty business he witnessed last time?{/i}"
    "{i}There was a way of taking advantage of the situation for [player_name].{/i}"
    "{i}It was risky, for sure, but no risk, no fun, right? He thought.{/i}"
    Jimmy unamused arm "Yeah, about that. The Headmaster told me to give you a message."
    Jimmy "There was an incident in one of the bathrooms downstairs, and he wanted to let you know that he will return a bit later than usual."
    Dawson amazed  "Did he? Oh, and did he say anything else?"
    Jimmy "He said that you should wait for him in his office."
    Dawson "Ahh, that's good to hear. Thank you, dear. You did good."
    Dawson talk point "Now, please leave. I have to prepare for the meeting."
    Jimmy smug "Sure, Miss. Good evening."
    hide missdawson with dissolve
    hide jimmy with dissolve
    stop music
    play music MUSIC_SNEAK_THEME
    scene missdawsonlubeenter01 with fade
    "{i}[player_name] walked towards the exit making it look like he was leaving.{/i}"
    play sound "audio/sfx/highheels.ogg"
    "{i}He listened carefully as Miss Dawson seemed to look for something in the drawers and then stood up walking to the back.{/i}"
    scene missdawsonlubeenter02 with fade
    play sound "audio/sfx/dooropen01.ogg"
    "{i}At the exit's threshold, [player_name] heard the sound of the headmaster's door opening.{/i}"
    play sound "audio/sfx/highheels.ogg"
    "{i}The secretary was eagerly entering the office with some kind of bottle in her hand.{/i}"
    scene secretaryoffice01night with fade
    play sound "audio/sfx/doorclose02.ogg"
    "{i}Once she entered, [player_name] came back in and shut the door behind him.{/i}"
    scene missdawsonhandjoblockpeek with fade
    "{i}He then peeked through the lock and saw exactly what he expected to see.{/i}"
    "{i}Behind the desk, Miss Dawson seemed to be trying to get under it.{/i}"
    "{i}The plan was working so far; the only thing left to do was practice his throat clearing.{/i}"
    play sound "audio/sfx/dooropen01.ogg"
    scene headmasterstudyfallevening with fade
    play sound "audio/sfx/clearthroat01.ogg"
    "{i}After a couple of minutes, he opened the door and cleared his throat imitating Dr. Stapleneck the best he could.{/i}"
    play sound "audio/sfx/femaleclearthroat.ogg"
    "{i}Right away, he heard Miss Dawson also clearing her throat like a sign of approval.{/i}"
    play sound "audio/sfx/undress01.ogg"
    scene missdawsonhandjobintro01 with dissolve
    "{i}[player_name] approached the desk and took off his sleeveless jumper, hoping that Miss Dawson wouldn't recognize his uniform from the waist down.{/i}"
    scene missdawsonhandjobintro02 with fade
    play sound "audio/sfx/slap.ogg"
    "{i}As quickly as possible, [player_name] snuck his way to the headmaster's chair, trying his best to hide his face.{/i}"
    play sound "audio/sfx/whisperfemale.ogg"
    Dawson "{i}*whisper*{/i} I'm so glad you're finally here, Headmaster. {i}*whisper*{/i}"
    play sound "audio/sfx/clearthroat01.ogg"
    Dawson "{i}*whisper*{/i} Oh, you don't want to talk, I understand. {i}*whisper*{/i}"
    play sound "audio/sfx/hmm01.ogg"
    play sound "audio/sfx/undress01.ogg"
    Dawson "{i}*whisper*{/i} Don't be mad at me, Headmaster. I promise I will make you happy. {i}*whisper*{/i}"
    call missdawson_underdeskhandjob_scene from _call_missdawson_underdeskhandjob_scene
    scene headmasterstudyfallevening with vpunch
    show missdawson angry cum with vpunch
    play sound "audio/sfx/big_punch_trimmed.ogg"
    play music "audio/music/crazymoment01.ogg"
    Dawson "WHAT!?"
    play sound "audio/sfx/mad01.ogg"
    Dawson "What is the meaning of this!?"
    Jimmy "Ummm, I don't know, you tell me..."
    Dawson "You, the new student! I knew you would be trouble the moment I saw you."
    Dawson "The Headmaster will know about this!"
    Jimmy "Really? What will you tell him?"
    play sound "audio/sfx/frustratedhum.ogg"
    Dawson "I... I will... Oh, my god... He can't know anything about this!"
    Dawson "What am I going to do?"
    Jimmy "That's a nice skill you have with your hands. The Headmaster must be pleased."
    play sound "audio/sfx/frustratedhum.ogg"
    Dawson "Oh, shut up, you little punk."
    Dawson "Get out of here before Dr. Stapleneck shows up or we will both be in trouble!"
    Jimmy "You don't need to tell me twice!"
    play sound "audio/sfx/mad01.ogg"
    call nexttime from _call_nexttime_24
    $ quests.missdawsonBathroomIncident = COMPLETE
    $ gotoscene('mainbuildingentrance')