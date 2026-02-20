#VARIABLES
default wizardhousepick = 0

label libraryintroscene:
    hide screen freeroamhud with fade
    "The first time [player_name] enters the library, he notices the ominous atmosphere of the place."
    "There are not many students there." 
    "Most usually go to cyber cafes to look for information that would otherwise take much longer to find through books."
    "However, there was a certain charm in the smell of paper and the texture of the cover of an old book, which came to life much more when read within those walls."
    show clarissathelibrarianintro with fade
    "It didn't take long for [player_name] to observe what seemed to be the person in charge of the library." 
    "An attractive woman who projected an aura of pure culture..."
    Jimmy "Good day, Miss. Are you in charge?"
    hide clarissathelibrarianintro with dissolve
    show clarissa office neutral with dissolve
    play sound "audio/sfx/femaleclearthroat.ogg"
    play music MUSIC_CLARISSA_THEME
    Clarissa "Good day, it is a rarity to hear such a polite greeting from a student these days."
    Clarissa "Indeed, I am the one in charge. Clarissa Anderson. How can I serve you, educated young man?"
    $ Clarissa.met = True
    Jimmy "Well, I'm new here, and it's my first time visiting this place."
    Clarissa "Oh, how adorable. Half of the students at this academy don't even set foot in this building all year."
    Jimmy "I can see that it is a quiet place."
    Clarissa mad "If you ask me, it's much better this way."
    Clarissa "The kids who usually spend their time here have a club and they meet in the reading room, on the 2nd floor."
    Clarissa "They keep things in order, so they don't bother me, even though they are kind of nerdy, sometimes."
    Clarissa "Maybe too much when they get together to play those weird fantasy board games."
    Clarissa "But, I prefer that to the scandalous bawling of the athletes who sometimes come out of obligation."
    Clarissa neutral "Anyway, I'm sure I'm bothering you with my banter."
    Clarissa "One of my assistants could give you a little tour of the library, if you want."
    Jimmy "That would be great, thank you very much."
    Clarissa "Do you see that shelf over there? Find a girl with short hair, tell her I sent you."
    Jimmy "I will, thanks. See you later."
    Clarissa "See you later, polite boy."
    $ showscene('schoollibraryshelves', transition=fade)
    stop music
    play music MUSIC_MIKUS_THEME
    show mikulibraryintro with fade
    "In the shelves area, a petite girl with short hair was organizing some books."
    hide mikulibraryintro
    play sound "audio/sfx/big_punch_trimmed.ogg"
    show mikulibraryintro02 with vpunch
    "[player_name] approached cautiously, but the girl got nervous when she saw him and dropped a couple of books on the floor."
    show mikupickingbooks with vpunch
    hide mikulibraryintro02
    hide mikulibraryintro
    play sound "audio/sfx/undress01.ogg"
    "[player_name] quickly set about helping her collect them."
    Jimmy "I'm so sorry if I scared you."
    play sound "audio/sfx/hmm02.ogg"
    Miku "Oh no. Don't worry. I can be very clumsy sometimes."
    "[player_name] caught an eye on a couple of polaroids in the ground that seemed to depict the girl in front of him in less clothes."
    Jimmy "The librarian sent me. She told me you could give me a tour of the place."
    hide mikupickingbooks with dissolve
    show miku uniform complacent with dissolve
    play sound "audio/sfx/hmm03.ogg"
    Miku "So, you are new here? That explains why I don't remember you at all."
    Jimmy "Yes, I just arrived in town and I'm getting familiar with everything."
    if quests.artclassBook == ACTIVE:
        Jimmy "In fact, I'm looking for a book for the art teacher."
    "Even though they picked up all of the stuff that fell down, the girl kept looking down as if something was missing."
    Jimmy "Missing something?"
    Miku "Yeah... No! No, don't worry."
    "She was clearly ashamed and nervious, but the reason was ellusive to [player_name]."
    if quests.artclassBook == ACTIVE:
        Jimmy "Right, so... About the art book."
        Miku "Oh, right! Yes, Miss Bakshi always sends someone to fetch her a book before her class. It's like a ritual of hers."
        Miku "Seems like you were the lucky one, this time. I know exactly what you need."
        Jimmy "Great."
    Miku "Alright, I'll give you a tour of the place, then."
    Miku "Let's start with the archive."
    $ showscene('schoollibraryarchives', transition=fade)
    show miku uniform neutral with dissolve
    Miku "This is the archive!"
    Miku "It's kind of dark and a bit scary, but there are no ghosts, I promise."
    Jimmy "Cool, is there an Elder Scroll hidden here somewhere?"
    play sound "audio/sfx/laugh03.ogg"
    Miku happy "Ha, ha, ha. That's funny! It's actually a boring place."
    Miku "There are old books, but I haven't found anything interesting, yet."
    Jimmy "So, there is hope of finding secrets here."
    Miku "Maybe, ha, ha. They are mostly legal documents and history books about the academy."
    Miku neutral "It's boooooring, believe me."
    Miku "This school wasn't founded by 4 wizards and there isn't a Secret of Cumbers somewhere in the basement, so..."
    Jimmy "Ah, I get that one, Harry Potah. I like the movies."
    play sound "audio/sfx/hmm03.ogg"
    Miku "You do? I totally love the Wizardick World"
    Miku "What house would you be in?"
    menu:
        "Grifingcock":
            $ wizardhousepick = 1
            Jimmy "The red one, I don't remember the name."
            Miku "Grifingcock! So, you're a brave one, huh?"
            Miku "You look like it."
            Miku "I'm a Hafflebutt, love to be with the good guys."
        "Hafflebutt":
            $ wizardhousepick = 2
            Jimmy "The yellow one, I don't remember the name."
            Miku "Hafflebutt! So, you're a kind hearted one, huh?"
            Miku "You look like it."
            Miku "I'm a Hafflebutt too! We are part of the good guys!"
        "Rimjobclaw":
            $ wizardhousepick = 3
            Jimmy "The blue one, I don't remember the name."
            Miku "Rimjobclaw! So, you're a smart one, huh?"
            Miku "You look like it."
            Miku "I'm a Hafflebutt, love to be with the good guys."
        "Sfingering":
            $ wizardhousepick = 4
            Jimmy "The green one, I don't remember the name."
            Miku "Sfingering! So, you're an ambitious one, huh?"
            Miku "You look like it."
            Miku "I'm a Hafflebutt, love to be with the good guys."
    Miku "I went to the theme park last month!"
    Miku seductive "You can buy all types of wands, I like the hard ones."
    Jimmy "I bet you do..."
    play sound "audio/sfx/giggle02.ogg"
    Miku happy "So! Let's keep going with the tour!"
    $ showscene('schoollibrarynerdcliquehq', transition=fade)
    show miku uniform neutral with dissolve
    Miku "Welcome to the Poligonal table of the Ancients."
    Miku "Some of the guys get jealous of who enters this place, but they are not here now, so you can take a look."
    Jimmy "So, this is where the nerds hang out."
    Miku "Yep, this is our stronghold."
    Miku "I love to play role-playing games with them here."
    Miku "It gets really serious sometimes!"
    Miku "You should play with us one day! I think the guys would like you."
    Jimmy "Sure, I want to see what all the fuss is about."
    Miku "Well, that's it."
    Miku "There is not much else to see in the library."
    Miku "You might think is a boring place, like everyone else."
    Miku "But, me and the guys like to have all this space for us."
    Jimmy "Well, your presence actually makes it more interesting."
    play sound "audio/sfx/giggle01.ogg"
    Miku "Oh... ha, ha. That's very... nice of you."
    Miku "Well, let's get out of here before the guys come back."
    $ showscene('schoollibraryshelves', transition=fade)
    stop music
    play music MUSIC_MIKUS_THEME
    show miku uniform complacent with dissolve
    Miku "It was nice talking with you!"
    Miku "Now that I remember, I don't even know your name!"
    $ Miku.met = True
    Miku "I'm so forgetful! My name is Miku Sato, nice to meet you."
    Jimmy "The name is [player_name], is a pleasure."
    Miku "I hope you come back more often."
    Jimmy "I will, thank you, Miku."
    if quests.artclassBook == ACTIVE:
        Jimmy "Now, about that book..."
        call item_pickup(ItemArtBook01) from _call_item_pickup_1
        Miku "Yes, I almost forgot. Take this one. I know exactly what Miss Bakshi likes to read."
        Jimmy "Great, thank you."
        Miku "No problem, see you in class!"
        $ quests.artclassBook = SATISFIED
    show mikumissingphoto with fade
    hide miku uniform complacent with dissolve
    "As [player_name] turns to leave, he notices a polaroid resting under one of the shelves."
    play sound "audio/sfx/undress01.ogg"
    hide mikumissingphoto with dissolve
    show mikupolaroid01 with dissolve
    "After picking it up, he saw a photo that made his jaw open wide."
    Jimmy "Holy..."
    Jimmy "*God damn, she's hot."
    Jimmy "*Nerdy girls can be bad too, huh...*"
    hide mikupolaroid01 with dissolve
    show miku uniform neutral with dissolve
    play sound "audio/sfx/hmm03.ogg"
    Jimmy "Hey, I found this on the floor."
    play sound "audio/sfx/gasp02.ogg"
    Miku blushed photo "..."
    Miku "Oh my... Did you see it?"
    Jimmy "Well, I can't lie, I did."
    Miku "Oh my God, I'm so ashamed..."
    Jimmy "Don't be. You look very nice in that photo."
    Miku "You must think I'm a whore or something."
    Jimmy "It's a private photo, right? What's wrong with that?"
    Jimmy "I just found it by accident, so, it's not up to me to judge you for it."
    Miku "I... Wow, that's nice of you."
    Miku "Could you please not tell anyone?"
    Miku "I mean, yeah... I love to take strange photos, but it's only for my amusement."
    Jimmy "Don't worry, I won't say anything. And if you want me to forget about it, it's gone."
    play sound "audio/sfx/giggle01.ogg"
    Miku seductive "Well, did you really liked it?"
    Jimmy "I did, very much."
    Miku "Ha, ha, thank you."
    Miku "Maybe I can show you more some other time... No, that's a bad idea."
    Jimmy "If you want me to see them, show me. Just make sure you're comfortable with it."
    Miku "I'll think about it, [player_name]."
    $ mikuintro = True
    $ gotoscene('schoollibrarymainhall')