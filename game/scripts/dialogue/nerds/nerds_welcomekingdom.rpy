label welcometothekingdom:
    hide screen freeroamhud with None
    scene librarynerdcliquehq with fade
    play music MUSIC_NERDSCLIQUE_THEME
    __("{i}The heavy oak door creaked open, groaning like an entrance to a forgotten crypt.{/i}")
    __("{i}Jimmy stepped inside, and the world shifted.{/i}")
    __("{i}It wasn't just a room; it was a testament to dedication and nerdiness.{/i}")
    __("{i}Candles flickered, casting dancing shadows on medieval shields hanging beside faded band posters.{/i}")
    __("{i}A beautiful, stained-glass window depicted an ancient, glowing elven tree.{/i}")
    __("{i}The air was thick with the scent of old paper, cheap energy drinks, and... was that ozone? Or just body sweat?{/i}")
    __("{i}A massive, faded tapestry on the far wall depicted a sprawling continent, labeled in elegant script: 'The Glorious Kingdom of Cumalot.'{/i}")
    __("{i}The sound of a throat clearing, wet and dramatic, echoed from the back of the room.{/i}")
    scene earnestkingintro with fade
    play sound "audio/sfx/clearthroat01.ogg"
    $ renpy.pause()
    show algie uniform neutral with dissolve
    Algie "Hark! Ye, who hath defiled the sacred waters of the autumn revelry! Approach, O' Naked Leaper of the Second Storey!"
    Jimmy "*Da fuck?*"
    Algie "Present thyself before His Most Righteous, His Most Punctual, Sovereign of The Cumalot Kingdom, Protector of the Order of the Libidae, and Overlord of the Spire of Fellations!"
    Algie "The King, Earnest the Great!"
    $ Earnest.met = True
    __("{i}Algie paused, taking a deep, satisfied breath.{/i}")
    Jimmy "Uh... fellation?"
    Algie smug "It's a fancy word for 'fellas', you know, 'a group of friends', like us..."
    Jimmy "Right..."
    Jimmy "So, does he talk?"
    play sound "audio/sfx/whispermale.ogg"
    __("{i}Algie whispered something urgent to the King, whose face tried to look menacing, failing miserably.{/i}")
    Earnest "{i}How dare you...{/i}"
    __("{i}A high-pitched, almost squeaky voice came out of the King's mouth, who tried to speak in a grave, solemn voice.{/i}")
    Earnest "How dare you talk like that to me, mortal?"
    scene earnestkingfall with vpunch
    play sound "audio/sfx/big_punch.ogg"
    __("{i}He took a majestic step forward, his foot catching on the very edge of his ridiculously long bear fur cape.{/i}")
    __("{i}He tumbled from the throne with a surprisingly undignified yelp, landing in the wooden floor.{/i}")
    Jimmy "You okay there, Overlord of Fellation?"
    Algie "My liege!"
    scene librarynerdcliquehq with fade
    show earnest king neutral with dissolve
    Earnest "A mere... strategic repositioning, Algernon! Now, you, the one known as [player_name]"
    $ Algie.met = True
    Earnest "Your recent... exploits have reached the hallowed halls of our academy's most discerning minds."
    Algie "That's right, we heard about what happened at the Harrison house."
    Earnest "Indeed. The reports of your... apparent lack of self-preservation have piqued my interest."
    __("{i}The King gestured dramatically at the RPG map on the table, then the continent map on the wall.{/i}")
    Earnest mad "The final chapter, the confrontation with the Shadow Lord, approaches! But, alas, a great misfortune has befallen us."
    Earnest "Brainless Globins from the real world have hindered our progress, and our most vital artifact, the 'Scroll of the Ancients', has been..."
    Algie "Stolen! By the brutish, uncultured troglodytes under Russell's command!"
    Jimmy "Russell? I've heard that name before."
    Earnest "Precisely! We need your help to recover the Scroll of the Ancients, and a couple more things we need as well."
    Jimmy "And what's in it for me?"
    Earnest explain "Well, you shall have access to our vast repository of theoretical knowledge!"
    Algie "That means we can help you with your homework."
    Jimmy "No offense, your Majesty, but I'm pretty capable of taking care of my homework."
    Earnest "Hmm. A formidable negotiator, it seems. Very well."
    Algie "What of... coin? Gold? The shiny stuff that makes the mundane world go round?"
    $ Jimmy.money += 25
    call yougotmoney from _call_yougotmoney_4
    Jimmy "Now you're speaking my language."
    Earnest "If you recover the scroll, you can become a member of the Order of the Libidae."
    scene nerdscliquegirlsintro with fade
    Earnest "Which grants you permission to approach the beautiful women of the court."
    Earnest "I'm sure you are dazzled by their beauty..."
    play sound "audio/sfx/whisperfemale.ogg"
    Jimmy "..."
    play sound "audio/sfx/giggle01.ogg"
    __("{i}The girls were whispering to each other, giggling and glancing at [player_name].{/i}")
    Jimmy "Alright, King of Fellation. Where do I start?"
    scene librarynerdcliquehq with fade
    show earnest king neutral with dissolve
    Earnest "Look for our Sage, Melvin. He's is the one in charge of guarding the Scroll of the Elders."
    Earnest "One of our ravens came with a message earlier today, telling us that he might be in trouble."
    Earnest "He's in one of the bathrooms inside the Main building."
    Jimmy "Got it, I'll look for him."
    $ quests.algieScroll = ACTIVE
    __("{i}As [player_name] made his way out, Eunice called him before he could completely exit the hallway.{/i}")
    $ showscene('schoollibrarymainhall', transition=fade)
    show eunice uniform happy with dissolve
    Eunice "Oh, hey, [player_name]!"
    Jimmy "Hey, lady of the court of Fellation."
    play sound "audio/sfx/laugh01.ogg"
    Eunice "Ha, ha, ha, ha, what an awful name, right?"
    Eunice "I told them, but you know how stubborn you guys are."
    Eunice neutral "I wanted to thank you for helping me with the teather play."
    Eunice "Miss Bakshi, said I will have an audition next week."
    Eunice "I'm so excited!"
    Jimmy "Wow, that's great news."
    Jimmy "I'm sure you'll get the role."
    play sound "audio/sfx/hmm01.ogg"
    Eunice "Yeah, I..."
    Eunice blushed "I want to compensate you, and... you told me the other day that I looked good and huggable."
    Jimmy "Oh, yeah, I remember."
    __("{i}The memory of that strange vision came back to [player_name] as his skin shivered thinking about the babies.{/i}")
    Eunice seductive "What do you think about meeting in the gym's storage room after class?"
    Eunice "I will thank you for being so nice to me."
    Jimmy "Well... Sure, I guess."
    play sound "audio/sfx/alright01.ogg"
    Eunice "Alright, see you soon..."
    __("{i}As he walked out of the hallway, [player_name] saw Eunice excitedly whispering something to Miku while she looked at him with a mischievous smile.{/i}")
    __("{i}*What are they plotting?*, thought [player_name] going back to business.{/i}")
    $ quests.euniceBoobytrap = ACTIVE
    $ gotoscene('schoollibrarymainhall')
