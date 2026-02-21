label clarissadialogue:
    hide screen freeroamhud with None
    play music MUSIC_CLARISSA_THEME
    show clarissa office neutral with dissolve
    Clarissa "Hello, how can I help you?"
    jump .dialogmenu

label .dialogmenu:
    menu:
        "Ask for the Art Book" if quests.artclassBook == ACTIVE:
            Jimmy "Hey, Miss, I'm looking for a book for the art teacher."
            Jimmy "She told me you would know something about it."
            Clarissa "Right, yes, Miss Bakshi sends students here regularly."
            Clarissa "I'm sorry I cannot help you right now, I'm busy."
            Clarissa "However, my assistant will be happy to help you find the book you're looking for."
            Clarissa "You remember where to look for her, right?"
            Jimmy "Yes, thank you, Miss."
            Clarissa "You're welcome, mister."
        "Ask for Eunice's Book" if quests.euniceTheaterpractice == ACTIVE:
            if libraryeunicebookintro == False:
                Jimmy "Good day, Miss."
                Clarissa "Oh, hello, Mister [player_surname]."
                Clarissa "How can I help you, today?"
                Jimmy "I was looking for the assistant, Miku. Do you know where she might be?"
                Clarissa "Oh, well, I'm not sure where she might be."
                Clarissa "But, if you're looking for a book, that I can help you with."
                Jimmy "Yes, I actually need a book."
                Clarissa "Can you tell me the name?"
                jump eunicebookselection
            else:
                Jimmy "Good day, Miss."
                Clarissa "Oh, hello, Mister [player_surname]."
                Clarissa "How can I help you?"
                Jimmy "Well, it turns out I got the wrong book the last time."
                Clarissa "Oh, well, you're not the first to make that mistake."
                Clarissa "Give me the one you have and I'll get the right one for you."
                if Jimmy.hasItem(ItemArtBook02):
                    $ Jimmy.inventory.remove(ItemArtBook02)
                if Jimmy.hasItem(ItemArtBook03):
                    $ Jimmy.inventory.remove(ItemArtBook03)
                if Jimmy.hasItem(ItemArtBook04):
                    $ Jimmy.inventory.remove(ItemArtBook04)
                if Jimmy.hasItem(ItemArtBook05):
                    $ Jimmy.inventory.remove(ItemArtBook05)
                $ eunicewrongbook = False
                $ eunicecorrectbook = False
                Clarissa "Can you tell me the name?"
                jump eunicebookselection2
        "Nevermind":
            pass
    $ gotoscene('schoollibrarymainhall')

label eunicebookselection:
    Jimmy "Uhh..."
    menu:
        "The Contemplative Palette":
            Clarissa "Okay, here you go."
            call item_pickup(ItemArtBook02) from _call_item_pickup
            Jimmy "That was fast, thank you."
            $ eunicewrongbook = True
            $ libraryeunicebookintro = True
            Clarissa "You're welcome, mister."
            $ gotoscene('schoollibrarymainhall')
        "The Companionable Plate":
            Clarissa "Okay, here you go."
            call item_pickup(ItemArtBook03) from _call_item_pickup_4
            Jimmy "That was fast, thank you."
            $ eunicewrongbook = True
            $ libraryeunicebookintro = True
            Clarissa "You're welcome, mister."
            $ gotoscene('schoollibrarymainhall')
        "The Compassionate Palate":
            Clarissa "Okay, here you go."
            call item_pickup(ItemArtBook05) from _call_item_pickup_5
            Jimmy "That was fast, thank you."
            $ eunicecorrectbook = True
            $ libraryeunicebookintro = True
            Clarissa "You're welcome, mister."
            $ gotoscene('schoollibrarymainhall')
        "The Consoling Paladin":
            Clarissa "Okay, here you go."
            call item_pickup(ItemArtBook04) from _call_item_pickup_6
            Jimmy "That was fast, thank you."
            $ eunicewrongbook = True
            $ libraryeunicebookintro = True
            Clarissa "You're welcome, mister."
            $ gotoscene('schoollibrarymainhall')
        "The Commendable Palate" if consolingpalading == False:
            Clarissa "Mhmm, that book doesn't exist."
            Clarissa "At least, not in my library."
            Jimmy "Oh, right..."
            $ consolingpalading = True
            jump eunicebookselection

label eunicebookselection2:
    Jimmy "Uhh..."
    menu:
        "The Contemplative Palette":
            Clarissa "Here you go."
            call item_pickup(ItemArtBook02) from _call_item_pickup_36
            Jimmy "Thank you."
            $ eunicewrongbook = True
            Clarissa "You're welcome, mister."
            $ gotoscene('schoollibrarymainhall')
        "The Companionable Plate":
            Clarissa "Here you go."
            call item_pickup(ItemArtBook03) from _call_item_pickup_37
            Jimmy "Thank you."
            $ eunicewrongbook = True
            Clarissa "You're welcome, mister."
            $ gotoscene('schoollibrarymainhall')
        "The Compassionate Palate":
            Clarissa "Here you go."
            call item_pickup(ItemArtBook05) from _call_item_pickup_38
            Jimmy "Thank you."
            $ eunicecorrectbook = True
            Clarissa "You're welcome, mister."
            $ gotoscene('schoollibrarymainhall')
        "The Consoling Paladin":
            Clarissa "Here you go."
            call item_pickup(ItemArtBook04) from _call_item_pickup_39
            Jimmy "Thank you."
            $ eunicewrongbook = True
            Clarissa "You're welcome, mister."
            $ gotoscene('schoollibrarymainhall')
        "The Commendable Palate" if consolingpalading == False:
            Clarissa "Mhmm, that book doesn't exist."
            Clarissa "At least, not in my library."
            Jimmy "Oh, right..."
            $ consolingpalading = True
            jump eunicebookselection