$ quests.bakshiSirlaughsalot = LOCKED

label bakshisirlaughsalotquest:
    if quests.bakshiSirlaughsalot == LOCKED:
        jump .intro
    elif quests.bakshiSirlaughsalot == ACTIVE:
        jump .active
    elif quests.bakshiSirlaughsalot == SATISFIED:
        jump .satisfied
    return

label .intro:
    scene artclassroomfallday with fade
    play music MUSIC_AURORA_THEME
    show aurora jumpsuit crossed with dissolve
    Aurora "Mr. [player_surname]. Have you come do plead for yur muse?"
    Jimmy "Hello, Miss. I have some curiosity about the next teather play you're working on."
    Jimmy "I heard about dit and..."
    Aurora "Oh! Are you interested in a role?"
    play sound "audio/sfx/giggle02.ogg"
    Aurora "I believe you culd be a great royal guard captain for Queen Leddicia."
    Jimmy "Well, I was thinking about a friend of mine, Eunice, that wants to be in the role of Queen Letticia."
    Jimmy "She's been very focused on practicing her acting skills, so I thought I could help her out."
    Aurora "Ah, dhat is so sweet of you, sweetu."
    Aurora "But, dear, Queen Leddicia does nod simply get auditioned. She must be awakened dhrough chaos, commitment, and pouldry."
    Jimmy "Right..."
    Aurora "For example, dhink about Sir Laughsalot." 
    Aurora "He is the emotional cornerstone of the play. Our sacred squeaker!"
    play sound "audio/sfx/chickensound01.ogg"
    show sirlaughsalotthrone01 with fade
    "{i}Suddenly, Miss Shakti pulled out a tiny throne made of recycling materials that was conspicuously empty.{/i}"
    Aurora "I could dalk to Eunice for the role, but as long as Sir Laughsalot is missing, Leddicia's rage feels... emotionally unsupporded."
    Jimmy "What happened to Sir Laughsalot?"
    Aurora "Rumors are dramatic, but he was last seen in the Auditorium backstage."
    hide sirlaughsalotthrone01 with dissolve
    Aurora "Maybe a clever boy like you can help me figure out whad happened to him."
    Aurora "And I can give Eunice a chance..."
    Jimmy "Got it. Find the chicken, save the play."
    $ quests.bakshiSirlaughsalot = ACTIVE
    call nexttime from _call_nexttime_9
    $ gotoscene('mainbuildingrighthallway')
    

label .active:
    scene artclassroomfallday with fade
    play music MUSIC_AURORA_THEME
    show aurora jumpsuit dance with dissolve
    Aurora "Mr. [player_surname]! Have you had any luck finding Sir Laughsalot?"
    Jimmy "Hey, Miss. I'm working on it. You can be sure I'll find it."
    Aurora "I'm sure you will, sweetu."
    $ gotoscene('mainbuildingrighthallway')

label .satisfied: