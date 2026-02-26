#VARIABLES
default quests.bathtubclimax = LOCKED

#LABELS
label kassandrabackyardincident:
    hide screen freeroamhud
    stop music
    scene kassandrahangingclothes01 with fade
    __("That day, [player_name] walked out to the backyard with a special sense of admiring everything around him.")
    __("As he approached the clothesline, he saw his [landlady_name], Kassandra, hanging clothes.")
    __("She was humming a tune, and he could see the joy on her face as she went about her work.")
    scene kassandrahangingclothes02 with vpunch
    __("He approached her quietly, not wanting to startle her, but as he got closer, Kassandra turned around and let out a scream.")
    __("She stumbled backward, tripping over her own feet, and [player_name] quickly caught her as his back hit the ground.")
    scene kassandrahangingclothes03 with vpunch
    Kassandra "Oh, my god, [player_name]!"
    Jimmy "..."
    scene jimmytownbackyard with fade
    show kassandra housedress with dissolve
    Jimmy "Are you okay?"
    __("Kassandra's face was flushed with embarrassment as she brushed herself off.")
    Kassandra "I'm sorry, I didn't hear you coming."
    Jimmy "Don't worry."
    __("To divert attention he quickly looked up at the old tree house that stood in the corner of the yard.")
    Jimmy "Hey, [landlady_name], what's up with that tree house?"
    __("Kassandra's face lit up with a smile as she recalled the memories of her three daughters trying to build it together.")
    Kassandra "Oh, yes, the three sisters who couldn't agree on anything"
    Kassandra "I remember it like it was yesterday."
    Kassandra "They all wanted to spend more time in it than the others, and it became a competition."
    __("They both laughed out loud. Then [player_name] took a deep breath and said...")
    Jimmy "Maybe one day, I'll try to finish it."
    __("Kassandra's smile turned into a proud grin as she looked at him.")
    Kassandra "That would be wonderful, [player_name]. I'm sure the girls would love that."
    Jimmy "Alright, I'll leave you to your stuff."
    Kassandra "Sorry for what happened again!"
    Jimmy "No problem."
    $ quests.bathtubclimax = SATISFIED
    $ gotoscene('townhousediningroom')

label kassandrabathtubclimax:
    hide screen freeroamhud
    stop music
    scene jimmyhouselivingroomnight with fade
    __("[player_name] walked down the hallway, his eyes half-closed as he tried to shake off the grogginess that comes with being woken up late at night.")
    scene jimmyhousediningroomnight with fade
    __("He reached the kitchen and opened the drawer to grab a glass.")
    __("As he filled it with water, he heard a faint sound coming from the living room.")
    scene jimmyhouselivingroomnight with fade
    __("He walked towards the sound and noticed a strange noise coming from the door next to the stairs.")
    __("His curiosity got the best of him and he decided to take a peek inside.")
    call kassandra_bathgasm_scene from _call_kassandra_bathgasm_scene
    scene jimmytownbedroomnight with fade
    Jimmy "Fuck, that was close."
    Jimmy "That was so fucking weird."
    Jimmy "Watching my [landlady_name] having an orgasm like that."
    Jimmy "It made me hard..."
    Jimmy "I mean she's a beautiful woman but, this is too much, dude."
    Jimmy "I need to go to sleep."
    $ quests.bathtubclimax = COMPLETE
    $ gotoscene('townhousejimmysroom')
