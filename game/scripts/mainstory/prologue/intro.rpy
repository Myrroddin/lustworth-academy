label prologue_intro:
    play music "audio/music/happyrock01.ogg"
    show ontheroad with fade
    pause 2.0
    show impactpresentintro
    pause 1.0
    show presentletter with dissolve
    pause 1.5
    hide impactpresentintro with dissolve
    hide presentletter with dissolve
    __("Last week was my 18th birthday.")
    __("I thought I was finally free to live life by my own rules, but my dad had other plans.")
    scene peacockvalleysignintro with fade
    __("After I got expelled from my last school only a month in, he enrolled me at some preppy boarding school to finish the year.")
    __("Actually, I was expelled from my last {i}five{/i} schools, but my dad just doesn't give up.")
    scene jimmyanddadincarintro with fade
    play sound "audio/sfx/carpassing01.ogg"
    Dad "Say something, [player_name], please."
    Jimmy "..."
    Dad "Come on, you're making this a lot harder than it needs to be."
    Jimmy "Right, because it's so hard for you to go off on a honeymoon with your new wife after you drop me off in another dump."
    Dad "[player_name] [player_surname], watch that mouth. We talked about this."
    Dad "This is an opportunity for both of us to turn over a new leaf."
    Dad "And you won't be alone, you'll be living with Kassandra, remember?"
    Jimmy "Right, a woman I haven't seen since I was four. I'm sure that won't be awkward at all."
    Dad "{i}Sigh.{/i}"
    Dad "Look, [player_name]. I love you. I've dedicated the last 18 years of my life to raising you."
    Dad "But you're an adult now. It's time for you to start taking responsibility for yourself."
    Dad "Please, promise me you'll at least try and make a change for the better."
    Jimmy "..."
    Jimmy "Alright, man. Sure, I'll try."
    Dad "Thank you, [player_name]."
    stop music fadeout 1.0
    play sound "audio/sfx/carpullover.ogg"
    scene academygatefallevening with fade
    show dadcaratgate with dissolve
    Dad "Remember, Kassandra will pick you up after school on Friday, same spot."
    Jimmy "Yeah, I'll be fine."
    jump prologue_start

#ANIMATIONS
image ontheroad:
    'ontheroad01'
    pause 0.4
    repeat

image impactpresentintro:
    'impactpresent01'
    pause 0.2
    'impactpresent02'
    pause 0.2
    'impactpresent03'
    pause 0.2
    'impactpresent04'
    pause 0.2
    'impactpresent05'
    pause 0.2
