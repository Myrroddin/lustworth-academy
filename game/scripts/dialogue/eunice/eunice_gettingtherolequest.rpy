default quests.euniceGettingtherole = LOCKED
default quests.bakshiSirlaughsalot = LOCKED

label eunicegettingtherolequest:
    if quests.euniceGettingtherole == LOCKED:
        jump .intro
    elif quests.euniceGettingtherole == ACTIVE:
        jump .active
        $ gotoscene('schoolgroundsparkinglot')

label .intro:
    play music "audio/music/classicmusic01.ogg"
    scene dramaticpractice01 with fade
    show eunice uniform acting with dissolve
    "{i}[player_name] spots Eunice near the decomissioned school bus, talking in a strange manner.{/i}"
    Eunice "Welcome to the 47th Feast of Purity. May your intestines be clean and your souls flavorless..."
    Jimmy "..."
    Eunice "Silence! Sir Laughsalot, declare this feast a triumph!"
    play sound "audio/sfx/chickensound01.ogg"
    Jimmy "*Where did that come from?*"
    Eunice "[player_name]?"
    show jimmy neutral with dissolve
    Jimmy smug "Hey, so, you're a queen or something?"
    Eunice "Queen Letticia. Sovereign of Sorrow. She rules a kingdom cursed with eternal veganism."
    Jimmy "Interesting..."
    play sound "audio/sfx/giggle01.ogg"
    play music MUSIC_EUNICES_THEME
    Eunice happy "It's good to see you, [player_name]."
    Jimmy smug "Likewise, can I go to see you in the play?"
    Eunice neutral "If I can get the role, yeah."
    Eunice "I've wanted to act in a theater production since middle school."
    play sound "audio/sfx/girlsigh01.ogg"
    Eunice "But it's really hard to get casted because there are a lot of prettier girls for the roles."
    Jimmy suspicious arm "Acting good matters more than the look in the theater, I believe."
    Eunice "Maybe, but Miss Bakshi is the one that makes the decision."
    Jimmy "Have you talk to her, already?"
    play sound "audio/sfx/hum01.ogg"
    Eunice "No, I haven't."
    Jimmy "Well, that might be a problem, don't you think?"
    Eunice "..." 
    Jimmy "Tell you what..."
    Jimmy "I'll talk to her. Let's see what she thinks about it and we'll figure out a way to get you the role."
    play sound "audio/sfx/gasp01.ogg"
    Eunice blushed "Seriously? You'd do that?"
    Jimmy smug "Sure, I believe you would make a real good Queen Letticia."
    Eunice "Oh my god, thank you so much... I don't know what to say."
    Jimmy "Don't worry. I'll handle the politics, you handle the drama."
    $ quests.euniceGettingtherole = ACTIVE
    call nexttime from _call_nexttime_12
    $ gotoscene('schoolgroundsparkinglot')

label .active:
    Jimmy "She's practicing her acting skills."
    Jimmy "I should focus on helping her get the role for the theater play."
    if quests.bakshiSirlaughsalot == ACTIVE:
        Jimmy "Miss Bakshi told me to help her find Sir Laughsalot."
        Jimmy "I should start at the backstage of the Auditorium."
    $ gotoscene('schoolgroundsparkinglot')


label sirlaughsalotsearch01:
    hide screen freeroamhud
    Jimmy "I'm gonna look for Eunice first, I'm sure she'll be happy to help."
    scene laterthatday with fade
    $ renpy.pause()
    scene auditoriumbackstage01 with fade
    show eunice uniform neutral with dissolve
    play sound "audio/sfx/hey01.ogg"
    Eunice "I can't believe Miss Bakshi can actually consider me for the role of Queen Letticia!"
    Eunice happy "I'm so excited!"
    Jimmy "Well, let's not get ahead of ourselves."
    Jimmy "We're going to have to find the thing, first."
    Eunice "Right, yeah, the rubber chicken."
    hide eunice with dissolve
    play music "audio/music/mysterytheme.ogg"
    "{i}The backstage area was a labyrinth of dusty props, coiled ropes, and half-painted sets. A single, bare lightbulb casted long, spooky shadows across everything.{/i}"
    Eunice "[player_name]! Look at the floor."
    show yellowfeather with fade
    "{i}Eunice pointed dramatically to the floor. Lying on the dusty wood there was a single, pristine, bright yellow feather.{/i}"
    Jimmy "A feather? Isn't the chicken made of rubber?"
    play sound "audio/sfx/hum01.ogg"
    Eunice "Precisely! That's what makes it weird. There are more..."
    "{i}A few feet away, another yellow feather rested near a stack of wooden crates. And another just beyond that.{/i}"
    Jimmy "It's a trail. A completely illogical feather trail."
    play sound "audio/sfx/femaleclearthroat.ogg"
    Eunice "Come on! The plot chickens! Sorry... thickens!"
    play sound "audio/sfx/sexyintro.ogg"
    scene euniceinvestigating with fade
    "{i}[player_name] followed the mysterious feather trail, getting distracted a bit by the view.{/i}"
    "{i}But, in the end, the feathers lead him behind a large, velvet curtain and into a dimly lit corner.{/i}"
    show whiskeybottlemistery with fade
    "{i}The trail stopped abruptly at a small, overturned table. Lying next to it was an empty bottle of whiskey...{/i}"
    play sound "audio/sfx/whispermale.ogg"
    Jimmy "{i}*Umm, a bottle of whiskey, so the one who took Sir Laughsalot must have been drunk.*{/i}"
    play sound "audio/sfx/whisperfemale.ogg"
    Eunice "{i}*That makes sense... but why there are feathers all over the place?*{/i}"
    play sound "audio/sfx/whispermale.ogg"
    Jimmy "{i}*This is getting weirder by the minute.*{/i}"
    play sound "audio/sfx/whisperfemale.ogg"
    Eunice "{i}*Why are we whispering?*{/i}"
    play sound "audio/sfx/clearthroat01.ogg"
    Jimmy "I don't know."
    Jimmy "Anyways, I think I have an idea about the culprit..."
    Jimmy "Follow me..."
    $ showscene('mainbuildingcafeteria', transition=fade)
    show eunice uniform neutral with dissolve
    play sound "audio/sfx/hmm01.ogg"
    Eunice "Are you hungry, [player_name]?"
    Eunice "I think I might be, a little bit."
    Jimmy "Oh, well I wasn't thinking about eating... I'm thinking about the case."
    Eunice mad "But, what does the cafeteria have anything to do with Sir Laughsalot?"
    Jimmy "Well, while it seems to be a bad joke, it's obvious that a rubber chicken doesn't have feathers."
    Jimmy "So, what if the feathers didn't come from Sir Laughsalot? What if they came from the kidnapper?"
    play sound "audio/sfx/gasp01.ogg"
    Eunice acting "The kidnapper is a chicken!?" with vpunch
    Jimmy "Not exactly. Think about it: who on campus would have their clothes covered in chicken feathers..."
    Jimmy "... and turns out to have a problem with alcohol?"
    Eunice neutral "Ugh..."
    Jimmy "Can you smell that?"
    play sound "audio/sfx/giggle01.ogg"
    Eunice happy "Oh, yeah! It smells really nice, like roasted chicken..."
    play sound "audio/sfx/surprisedhum.ogg"
    Eunice acting "OOOH!" with vpunch
    Eunice "Oh, you don't think..."
    Jimmy "Let's keep going."
    stop music
    play music "audio/music/mysterytheme.ogg"
    scene schoolkitchendayfall with fade
    "{i}As they both entered the kitchen, the smell of the food was overwhelming.{/i}"
    "{i}However, as they got closer to the cook, there was a subtle scent of licuor in the air...{/i}"
    show edna cook neutral with dissolve
    play sound "audio/sfx/femaleclearthroat.ogg"
    show eunice uniform mad left with vpunch
    Eunice "YOU!"
    play sound "audio/sfx/ednaheykid.ogg"
    Edna "What do you want, kids?"
    Edna "You shouldn't be here..."
    play sound "audio/sfx/gasp01.ogg"
    Eunice acting left "YOU'RE GUILTY!" with vpunch
    play sound "audio/sfx/stopmusiceffect.ogg"
    play music "audio/music/funnymoment04.ogg"
    Edna daring "What the fuck are you talking about, fattie?"
    hide eunice with dissolve
    Eunice "Oh, sorry. I got too excited."
    if Edna.met:
        Jimmy "Sorry to bother you, Edna."
    else:
        Jimmy "Sorry to bother you, Miss."
    Jimmy "But, we are looking for a missing rubber chicken and we want your permission to search in the fridge."
    play sound "audio/sfx/ednalaugh.ogg"
    Edna "And why in the living hell would a rubber chicken be in the fridge?"
    Jimmy "Well, we think you might have confused..."
    Eunice "Just let us take a peek!"
    Eunice "We won't touch anything if it's not in there."
    Edna neutral "Ughhh, you kids are so annoying..."
    Edna "Do whatever you want, don't bother old Edna."
    hide edna with dissolve
    Jimmy "Nice."
    stop music
    play sound "audio/sfx/crowdshock01.ogg"
    scene frozensirlaughsalot with vpunch
    Jimmy "There it is!"
    Eunice "Yes, oh my god! Is he dead!?"
    play sound "audio/sfx/slap.ogg"
    Edna "Stop yelling!"
    Eunice "Oh, sorry."
    Jimmy "Let's just take the chicken and get out of here before we end up in the soup."
    play sound "audio/sfx/dooropen01.ogg"
    scene artclassroomfallday with fade
    "{i}Going back to the Art Classroom, [player_name] realized Miss Bakshi was nowhere to be found.{/i}"
    "{i}However, there was someone else in there...{/i}"
    play music MUSIC_MIKUS_THEME
    show miku uniform neutral with dissolve
    play sound "audio/sfx/hey02.ogg"
    Miku "[player_name]! How's it going?"
    play sound "audio/sfx/gasp01.ogg"
    Miku happy "Ohhhh, Eunice! My beautiful elven mage!"
    show eunice uniform happy left with dissolve
    Eunice "Hey, Miks! I'm so happy to see you."
    Miku neutral "So, you two know each other?"
    Jimmy "We are getting to know each other, yeah."
    Miku "That's great! [player_name], Eunice is my best friend ever, you know?"
    Miku "So, please take care of her. She's a wonderful human being once you get to know her."
    play sound "audio/sfx/girlsigh01.ogg"
    Eunice neutral left "Awww, stop it."
    Miku "So, what are you doing here?"
    Jimmy "We are looking for Miss Bakshi."
    Miku "Oh, Miss Bakshi left just a moment ago. She was talking about a ritual or something..."
    Miku "I'm not sure, but she mentioned the Auditorium."
    Jimmy "Umm, well, let's go to the Auditorium, then."
    play sound "audio/sfx/hum01.ogg"
    Eunice acting left "Oh, [player_name]. I need to talk to Miku about something..."
    Eunice "Can you go and intercede for me?"
    Jimmy "Sure, I'll go."
    Eunice neutral left "Thanks, [player_name]. I owe you big time."
    play sound "audio/sfx/giggle01.ogg"
    Miku seductive "Bye, handsome!"
    $ showscene('mainbuildingauditorium', transition=fade)
    play music "audio/music/sneaking01.ogg"
    show smokeleakbackstage with dissolve
    "{i}As [player_name] entered the auditorium, he immediately got the scent of something strange in the air...{/i}"
    "{i}It was mix of flowers and strong perfumes, maybe some spices...{/i}"
    "{i}A small stream of colored smoke leaked out from the backstage area.{/i}"
    show smokeleakbackstage02 with dissolve
    play music "audio/music/nativeritual01.ogg"
    "{i}The backstage area was transformed.{/i}"
    "{i}Candles flickered in circles on the floor, and thick, sweet-smelling smoke hanged in the air from a brass incense burner.{/i}"
    show missbakshiritual with dissolve
    Jimmy "Miss Bakshi? I..."
    "{i}Aurora was naked right in the middle of the thick layer of smoke.{/i}"
    "{i}[player_name] was hypnotized by the curves of her body dancing and moving gracefully, like the waves of the sea.{/i}"
    Aurora "{i}Melpomene, grant us fire... fill our scenes with heart's desire...{/i}"
    Aurora "{i}Thespis, bless this wooden stage... let our story turn a new page...{/i}"
    Jimmy "..."
    "{i}[player_name] took a step forward, and the smoke billowed around him.{/i}"
    "{i}The scent was strong, like sandalwood, myrrh, and something else he couldn't quite place.{/i}"
    "{i}He took an involuntary breath, and the thick, aromatic smoke filled his lungs... and his mind.{/i}"
    call eunice_fuckvision_scene from _call_eunice_fuckvision_scene
    play sound "audio/sfx/big_punch.ogg"
    $ showscene('mainbuildingbackstage', transition=vpunch)
    stop music
    show aurora jumpsuit crossed with dissolve
    "{i}When he woke up, Aurora was standing there, arms crossed, looking at him with a calm smile. The ritual was over and she was dressed again.{/i}"
    play music MUSIC_AURORA_THEME
    Aurora "Are you alright, Mr. [player_surname]? You look a bit pale."
    Jimmy "I... uh... the smoke. I got to much in my lungs..."
    Aurora "I'm sorry, my boy. But, what smoke? I don't know what you're talking about..."
    Jimmy "There was smoke and you were na..."
    Jimmy "Nevermind..."
    Jimmy "I found it, Miss. Sir Laughsalot, I mean."
    Aurora "Sir Laughsalot! Oh, you clever boy! You've rescued him!"
    show sirlaughsalotthrone02 with fade
    play sound "audio/sfx/chickensound01.ogg"
    "{i}She took the chicken as if it were a holy relic, and placed him back on his tiny throne made of trash.{/i}"
    Aurora "The emotional cornerstone is restored! The cosmic balance of the play is secure!"
    Aurora "You have done me a great service, [player_name]."
    Aurora "I'll go talk to your friend, Eunice, to give her an audition."
    Aurora "Now that Sir Laughsalot is here to witness her rage, Queen Letticia is ready to be casted."
    hide sirlaughsalotthrone02 with dissolve
    Jimmy "That's great! Thank you, Miss Shakti."
    Aurora "Call me Aurora, my sweetu."
    Aurora "And, thank you. You found the chicken, you saved the play."
    $ quests.euniceGettingtherole = COMPLETE
    $ quests.bakshiSirlaughsalot = COMPLETE
    $ Eunice.relPoints += 1
    call nexttime from _call_nexttime_19
    $ gotoscene('mainbuildingauditorium')