default quests.euniceTheaterpractice = LOCKED
default eunicewrongbook = False
default eunicecorrectbook = False
default libraryeunicebookintro = False
default consolingpalading = False
default eunicebookfetch = False
default mikuauditoriumnote = False

label eunicetheater_practiceintro:
    hide screen freeroamhud with None
    stop music
    scene artclassroomfallday with fade
    __("{i}The art classroom was quiet, smelling faintly of turpentine and clay.{/i}")
    __("{i}In the center of the room, Eunice stood talking in a strange manner towards the sunlight leaking through the windows.{/i}")
    play music "audio/music/classicmusic01.ogg"
    show eunice uniform acting with dissolve
    Eunice "How dare you! You bring this... this peasant's trifle before me and call it tribute? Your insolence is a stain upon this court!"
    play sound "audio/sfx/frustratedhum.ogg"
    Eunice "Guards! Seize him! Let him contemplate his failure in the deepest, darkest... uh... pencil-sharpening closet!"
    Jimmy "Oh, no! My queen! I promise I will bring vanilla icecream on top of a piece of brownie."
    play music MUSIC_EUNICES_THEME
    play sound "audio/sfx/laugh01.ogg"
    Eunice happy "That's sound delicious, ha, ha, ha, ha."
    Eunice "It's good to see you, [player_name]."
    Eunice "What do you think about the mindset of the Queen. Do you see some regal fury, righteous indignation or what?"
    Jimmy "I see copious amounts of curves waiting for me to get lost in them."
    play sound "audio/sfx/giggle01.ogg"
    Eunice blushed "Oh, my..."
    Eunice "I can't thank you enough for getting me this chance."
    Eunice "I've been reading the script nonstop! But it's hard to practice a dialogue by yourself."
    Jimmy "Well, destiny brought me here for a reason."
    play sound "audio/sfx/alright01.ogg"
    Eunice "Really? That's great! You could read the lines for the Royal Guard Captain. It's not many!"
    Jimmy "Sure, I can do that. What's the scene?"
    Eunice "The Captain is reporting to the Queen about a baker who used cow milk instead of almond milk."
    Eunice acting "Okay, I'm ready. Get into character!"
    play music "audio/music/classicmusic01.ogg"
    __("{i}Eunice takes a deep breath, her entire demeanor shifting into one of regal fury. It might be a good idea to remember her lines...{/i}")
    play sound "audio/sfx/clearthroat01.ogg"
    Jimmy "Your Majesty, the baker has been apprehended. He claims it was a... a simple mistake."
    play sound "audio/sfx/hum01.ogg"
    Eunice "A mistake? {b}Treason tastes like bitter herbs on a coward's tongue!{/b} A mistake does not curdle the royal cream!"
    Jimmy "He begs for your mercy, my Queen. He says he was distracted by the beauty of one of your portraits."
    play sound "audio/sfx/femaleclearthroat.ogg"
    Eunice "Distracted? Mercy is a luxury this kingdom cannot afford, but I sure understand that my presence might be too dazzling for some."
    Jimmy "Your Majesty, he is the only one who knows the royal gingerbread recipe..."
    Eunice "Silence! What do you think about this, Sir Laughsalot?"
    play sound "audio/sfx/chickensound01.ogg"
    $ renpy.pause()
    Eunice "And... scene..."
    play sound "audio/sfx/wow01.ogg"
    play music MUSIC_EUNICES_THEME
    Eunice happy "Wow! That felt... really good! Having someone to play off of makes all the difference. Thanks, [player_name]!"
    Jimmy "No problem. You've definitely got the 'furious queen' part down."
    Eunice neutral "Thanks. I'm trying to find her softer side, too. Her motivation."
    Eunice "I believe her hard rule over the fact that veganism has to be obligatory for the kingdom might be a metaphor, I think."
    Eunice "Which reminds me... I need to do some character research. Could you do me a huge favor?"
    Eunice "Could you go to the library and find a book for me? It's called '{i}The Compassionate Palate: A Vegan's Guide to Friendly Cuisine.{/i}'"
    play sound "audio/sfx/giggle02.ogg"
    Eunice "Maybe our mutual friend, Miku, can help you get it."
    Jimmy "Find a book on vegan cooking to help you play a furious queen. Got it."
    Jimmy "I'll be back soon."
    Eunice "Thanks, [player_name]! You're the best!"
    $ quests.euniceTheaterpractice = ACTIVE
    $ gotoscene('mainbuildingrighthallway', transition=fade)

label eunicetheater_bookfetch:
    if eunicebookfetch == False:
        hide screen freeroamhud with None
        stop music
        play sound "audio/sfx/doorknock01.ogg"
        __("{i}The door to the Art classroom was locked, but [player_name] could hear the voice of Eunice laughing and talking to another girl.{/i}")
        __("{i}What's going on? Thought [player_name], before knocking on the door.{/i}")
        play sound "audio/sfx/gasp01.ogg"
        Eunice "Coming!"
        Eunice "*whispers* He's here. *whispers*"
        play sound "audio/sfx/giggle01.ogg"
        Unk "*whispers* He, he, he. *whispers*"
        __("{i}[player_name] heard the steps getting closer to the door, but the when it opened he couldn't hide the shock on his face.{/i}")
        play sound "audio/sfx/dooropen01.ogg"
        scene eunicedoorkeep01 with vpunch
        play sound "audio/sfx/sexyintro.ogg"
        Jimmy "WOW! What the..?"
        Eunice "Shhh... Be quiet. Here, stand here so you can cover me."
        play sound "audio/sfx/giggle02.ogg"
        Eunice "This is kind of... embarrasing... he, he."
        play sound "audio/sfx/clearthroat01.ogg"
        Jimmy "What are you doing in there?"
        Eunice "I'm helping Miku with a photoshoot session."
        Jimmy "Miku, huh..."
        play sound "audio/sfx/hey02.ogg"
        Miku "Hey, do you want to help us?"
        Jimmy "If you need me, I'm available."
        play sound "audio/sfx/hmm01.ogg"
        Eunice "Well, we can let you in, but did you get the book I asked?"
        Jimmy "Is it this one?"
        $ eunicebookfetch = True
        if Jimmy.hasItem(ItemArtBook02):
            Eunice "The Contemplative Palette..."
            Eunice "This is a book about the theory of color, [player_name]."
            play sound "audio/sfx/girlsigh01.ogg"
            Eunice "This is not the one I need."
            Eunice "It's the 'The Compassionate Palate: A Vegan's Guide to Friendly Cuisine.'"
            Jimmy "Shit, I'm sorry. I sounded similar."
            Jimmy "I'll get you the right one."
            Miku "Hurry up! We're waiting for you!"
            play sound "audio/sfx/doorclose01.ogg"
            $ gotoscene('mainbuildingrighthallway', transition=fade)
        elif Jimmy.hasItem(ItemArtBook03):
            Eunice "The Companionable Plate..."
            Eunice "This is a book about house decoration, [player_name]."
            play sound "audio/sfx/girlsigh01.ogg"
            Eunice "This is not the one I need."
            Eunice "It's the 'The Compassionate Palate: A Vegan's Guide to Friendly Cuisine.'"
            Jimmy "Shit, I'm sorry. I sounded similar."
            Jimmy "I'll get you the right one."
            Miku "Hurry up! We're waiting for you!"
            play sound "audio/sfx/doorclose01.ogg"
            $ gotoscene('mainbuildingrighthallway', transition=fade)
        elif Jimmy.hasItem(ItemArtBook04):
            Eunice "The Consoling Paladin..."
            Eunice "This is an erotic novel, [player_name]."
            play sound "audio/sfx/girlsigh01.ogg"
            Eunice "This is not the one I need, even though I think I want to read it now."
            Eunice "I need the 'The Compassionate Palate: A Vegan's Guide to Friendly Cuisine.'"
            Jimmy "Shit, I'm sorry. I sounded similar."
            Jimmy "I'll get you the right one."
            Miku "Hurry up! We're waiting for you!"
            play sound "audio/sfx/doorclose01.ogg"
            $ gotoscene('mainbuildingrighthallway', transition=fade)
        elif Jimmy.hasItem(ItemArtBook05):
            Eunice "The Compassionate Palate..."
            play sound "audio/sfx/gasp02.ogg"
            Eunice "This is it, [player_name]!"
            Eunice "Thank you so much, you're so good to me."
            Miku "Hurry up! Come in already!"
            play sound "audio/sfx/doorclose01.ogg"
            jump eunicemikuartworkintro
    elif eunicebookfetch == True:
        hide screen freeroamhud with None
        play sound "audio/sfx/doorknock01.ogg"
        Eunice "Coming!"
        scene eunicedoorkeep01 with fade
        Jimmy "Is it this one?"
        $ eunicebookfetch = True
        if Jimmy.hasItem(ItemArtBook02):
            Eunice "The Contemplative Palette..."
            Eunice "This is a book about the theory of color, [player_name]."
            play sound "audio/sfx/girlsigh01.ogg"
            Eunice "This is not the one I need."
            Eunice "It's the 'The Compassionate Palate: A Vegan's Guide to Friendly Cuisine.'"
            Jimmy "Shit, I'm sorry. It sounded similar."
            Jimmy "I'll get you the right one."
            Miku "Hurry up! We're waiting for you!"
            play sound "audio/sfx/doorclose01.ogg"
            $ gotoscene('mainbuildingrighthallway', transition=fade)
        elif Jimmy.hasItem(ItemArtBook03):
            Eunice "The Companionable Plate..."
            Eunice "This is a book about house decoration, [player_name]."
            play sound "audio/sfx/girlsigh01.ogg"
            Eunice "This is not the one I need."
            Eunice "It's the 'The Compassionate Palate: A Vegan's Guide to Friendly Cuisine.'"
            Jimmy "Shit, I'm sorry. It sounded similar."
            Jimmy "I'll get you the right one."
            Miku "Hurry up! We're waiting for you!"
            play sound "audio/sfx/doorclose01.ogg"
            $ gotoscene('mainbuildingrighthallway', transition=fade)
        elif Jimmy.hasItem(ItemArtBook04):
            Eunice "The Consoling Paladin..."
            Eunice "This is an erotic novel, [player_name]."
            play sound "audio/sfx/girlsigh01.ogg"
            Eunice "This is not the one I need, even though I think I want to read it now."
            Eunice "I need the 'The Compassionate Palate: A Vegan's Guide to Friendly Cuisine.'"
            Jimmy "Shit, I'm sorry. It sounded similar."
            Jimmy "I'll get you the right one."
            Miku "Hurry up! We're waiting for you!"
            play sound "audio/sfx/doorclose01.ogg"
            $ gotoscene('mainbuildingrighthallway', transition=fade)
        elif Jimmy.hasItem(ItemArtBook05):
            Eunice "The Compassionate Palate..."
            play sound "audio/sfx/gasp02.ogg"
            Eunice "This is it, [player_name]!"
            Eunice "Thank you so much, you're so good to me."
            Miku "Hurry up! Come in already!"
            play sound "audio/sfx/doorclose01.ogg"
            jump eunicemikuartworkintro

label eunicemikuartworkintro:
    scene eunicemikuartworkintro with fade
    play music MUSIC_MIKUS_THEME
    play sound "audio/sfx/hey02.ogg"
    Miku "Hey, [player_name]."
    Jimmy "Sup, Miku."
    Miku "You got here just in time."
    Miku "What do you think about our suits?"
    Jimmy "Very revealing..."
    play sound "audio/sfx/giggle01.ogg"
    Eunice "He, he, he..."
    Miku "It's a personal project of mine."
    Miku "And I'm also trying to make Eunice feel less ashamed of her body."
    Eunice "..."
    Miku "Here, take a picture with the camera you gave me!"
    __("{i}As [player_name] took the camera, he couldn't help but stare at their bodies through the lens.{/i}")
    Jimmy "Have you thought about something more artistic?"
    play sound "audio/sfx/hmm03.ogg"
    Miku "What do you have in mind?"
    Jimmy "Since we're in an Art classroom, how about I paint you both?"
    Eunice "Really? Can you do that?"
    Jimmy "Well, I got some skills from my dad, he's a painter."
    Miku "Miss Bakshi says you're really good."
    Jimmy "Well, I try."
    Miku "So, what should we do?"
    Jimmy "Stand right there, so I can get both of your figures in one painting."
    __("{i}The girls nodded in agreement and took up their positions.{/i}")
    play sound "audio/sfx/giggle01.ogg"
    Eunice "This is so cool." 
    Eunice "I've never been painted before."
    Miku "Me neither."
    Miku "I can't wait to see how it turns out."
    call eunice_painting_game from _call_eunice_painting_game

label eunicepaintingsuccess:
    stop music
    play music MUSIC_MIKUS_THEME
    Jimmy "Close enough..."
    play sound "audio/sfx/gasp01.ogg"
    Miku "[player_name], oh my god..."
    play sound "audio/sfx/wow01.ogg"
    Eunice "Wow, are we kissing?"
    Miku "Well, I guess we have to respect the artist's point of view..."
    Eunice "The painting is beautiful."
    Jimmy "Thank you."
    play sound "audio/sfx/femaleclearthroat.ogg"
    Miku "[player_name], could you turn your head for a bit?"
    Jimmy "Sure..."
    play sound "audio/sfx/whisperfemale.ogg"
    __("{i}As [player_name] turned his head, he started hearing both girls whispering to each other.{/i}")
    __("{i}He heard giggles while they seemed to be doing something he couldn't see.{/i}")
    Eunice "[player_name], you can turn back now."
    play sound "audio/sfx/sexyintro.ogg"
    scene eunicemikuartworkreward with fade
    Miku "I think this is how he painted us, right?"
    Eunice "Mhmhum..."
    Jimmy "This is so fucking hot right now."
    play sound "audio/sfx/laugh01.ogg"
    Miku "Ha, ha, ha, ha. Let's join our tongues."
    Eunice "Oh, no, that's gross ha, ha, ha, ha."
    scene eunicemikuartworkoutro with fade
    Miku "Thank you so much, [player_name]."
    Jimmy "Well, since I'm the one looking at your naked chests..."
    Jimmy "I'm the one who has to be grateful."
    play sound "audio/sfx/giggle02.ogg"
    Miku "You deserve it."
    Miku "Well, I'm done for today."
    Eunice "Me too... By the way, [player_name]. Thanks again for the book."
    $ Jimmy.inventory.remove(ItemArtBook05)
    $ quests.euniceTheaterpractice = SATISFIED
    Jimmy "See you later, then."
    $ MikuDaylimit = True
    $ gotoscene('mainbuildingrighthallway', transition=fade)

label eunicepaintingfail:
    stop music
    play music MUSIC_MIKUS_THEME
    play sound "audio/sfx/clearthroat01.ogg"
    Jimmy "Oh, crap. Sorry, girls. I'm still getting the hang of it."
    Miku "Oh, don't worry, [player_name]."
    play sound "audio/sfx/hmm01.ogg"
    Miku "It's so cool that you even try."
    Eunice "Yes, don't feel bad about it."
    Eunice "You can paint us whenever you want."
    Miku "Exactly, we can be your muse, whenever."
    Jimmy "Thank you."
    scene eunicemikuartworkintro with fade
    play sound "audio/sfx/hmm03.ogg"
    Miku "Well, I'm done for today."
    Eunice "Me too... By the way, [player_name]. Thanks again for the book."
    $ Jimmy.inventory.remove(ItemArtBook05)
    $ quests.euniceTheaterpractice = SATISFIED
    Jimmy "See you later, then."
    $ MikuDaylimit = True
    $ gotoscene('mainbuildingrighthallway', transition=fade)
