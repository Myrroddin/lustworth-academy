label cliffcheckfionaintro:
    hide screen freeroamhud with None
    "The cliff's wall is high from this side."
    "There is a way through the rocks that leads to the other side, let's see..."
    $ showscene('seasidecliff', transition=fade)
    "Bingo! I can use these stairs to climb from this side."
    "There is a lower opening I can use to get up there."
    "But, the stairs are broken."
    $ prologue.checkthecliff = True
    Fiona "Need a hand?"
    scene fionabeachintro with fade
    play music MUSIC_FIONAS_THEME
    "Goddamn..."
    Fiona "Wanna climb up there?"
    Fiona "I don't think you should try that."
    Fiona "Those stairs must be rotten and if you reach the top somehow, you'll be entering the mayor's backyard."
    Fiona "That should get you at least 2 years in prison."
    Jimmy "Yeah, well... I was just exploring and I ran into these stuff."
    Fiona "Right... Don't mind me, I'm not a snitch. I'm just warning you."
    Jimmy "Thank you for that, I didn't know there were mermaids around here."
    Fiona "Wow, I hope you're talking about the pretty mermaids, not the ugly ones."
    Fiona "In that case, thank you for the compliment."
    Jimmy "No problem."
    Fiona "Alright, I'll leave to your... exploring activities."
    $ Fiona.met = True
    Fiona "My name is Fiona, by the way."
    Jimmy "[player_name], nice to meet you."
    Fiona "Take care! I hope we see each other another time."
    "I would love that, for sure."
    call nexttime from _call_nexttime_13
    $ showscene('seasidecliff', transition=fade)
    play music MUSIC_HEISTPLAN_THEME
    show wendyplan04 with dissolve
    "Alright, I found a way to reach the mansion."
    show wendyplan05 with dissolve
    "But, I need to find something to fix the stairs, maybe a rope."
    "I'll take look around the house, maybe there is something I can use."
    stop music
    $ gotoscene('seasideareamap')
