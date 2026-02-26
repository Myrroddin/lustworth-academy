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
    __("{i}[player_name] spots Eunice near the decomissioned school bus, talking in a strange manner.{/i}")
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
    Eunice "But it's really hard to get cast because there are a lot of prettier girls for the roles."
    Jimmy suspicious arm "Acting good matters more than the look in the theater, I believe."
    Eunice "Maybe, but Miss Bakshi is the one that makes the decision."
    Jimmy "Have you talked to her, already?"
    play sound "audio/sfx/hum01.ogg"
    Eunice "No, I haven't."
    Jimmy "Well, that might be a problem, don't you think?"
    Eunice "..."
    Jimmy "Tell you what..."
    Jimmy "I'll talk to her. Let's see what she thinks about it and we'll figure out a way to get you the role."
    play sound "audio/sfx/gasp01.ogg"
    Eunice blushed "Seriously? You'd do that?"
    Jimmy smug "Sure, I believe you would make a really good Queen Letticia."
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
    Eunice "I can't believe Miss Bakshi will actually consider me for the role of Queen Letticia!"
    Eunice happy "I'm so excited!"
    Jimmy "Well, let's not get ahead of ourselves."
    Jimmy "We're going to have to find the thing, first."
    Eunice "Right, yeah, the rubber chicken."
    hide eunice with dissolve
    play music "audio/music/mysterytheme.ogg"
    __("{i}The backstage area was a labyrinth of dusty props, coiled ropes, and half-painted sets. A single, bare lightbulb casted long, spooky shadows across everything.{/i}")
    Eunice "[player_name]! Look at the floor."
    show yellowfeather with fade
    __("{i}Eunice pointed dramatically to the floor. Lying on the dusty wood there was a single, pristine, bright yellow feather.{/i}")
    Jimmy "A feather? Isn't the chicken made of rubber?"
    play sound "audio/sfx/hum01.ogg"
    Eunice "Precisely! That's what makes it weird. There are more..."
    __("{i}A few feet away, another yellow feather rested near a stack of wooden crates. And another just beyond that.{/i}")
    Jimmy "It's a trail. A completely illogical feather trail."
    play sound "audio/sfx/femaleclearthroat.ogg"
    Eunice "Come on! The plot chickens! Sorry... thickens!"
    play sound "audio/sfx/sexyintro.ogg"
    scene euniceinvestigating with fade
    __("{i}[player_name] followed the mysterious feather trail, getting distracted a bit by the view.{/i}")
    __("{i}But, in the end, the feathers lead him behind a large, velvet curtain and into a dimly lit corner.{/i}")
    show whiskeybottlemistery with fade
    __("{i}The trail stopped abruptly at a small, overturned table. Lying next to it was an empty bottle of whiskey...{/i}")
    play sound "audio/sfx/whispermale.ogg"
    Jimmy "*Umm, a bottle of whiskey, so the one who took Sir Laughsalot must have been drunk.*"
    play sound "audio/sfx/whisperfemale.ogg"
    Eunice "*That makes sense... But why are there feathers all over the place?*"
    play sound "audio/sfx/whispermale.ogg"
    Jimmy "*This is getting weirder by the minute.*"
    play sound "audio/sfx/whisperfemale.ogg"
    Eunice "*Why are we whispering?*"
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
    __("{i}As they both entered the kitchen, the smell of the food was overwhelming.{/i}")
    __("{i}However, as they got closer to the cook, there was a subtle scent of liquor in the air...{/i}")
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
    Edna daring "What the fuck are you talking about, fatty?"
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
