#STYLES
style planner_profile_header is planner_header_bold:
    underline True
    xcenter planner_left_center
    ypos 0.18

style planner_profile_about is planner_text:
    xcenter planner_left_center
    xmaximum gui.planner_profile_about_width
    ypos gui.planner_profile_about_ypos
    justify True
    line_spacing gui.planner_profile_about_spacing
    first_indent 40

#SCREENS
screen planner_profile_contents(char, img, xpos, height, bio):
    $ ypos = 951

    if not girlMet(char):
        $ xsize, ysize = (1920, 1080)
        $ fillRect = Fixed(Solid('#666'), xsize=xsize, ysize=ysize)
        $ img = AlphaMask(fillRect, img)
    add img:
        pos xpos, ypos
        ysize height
        yanchor 1.0
        fit 'contain'

    if not char.met:
        text "???":
            style 'planner_profile_about'
            first_indent 0
    elif bio is None:
        text "{i}Bio coming soon{/i}":
            style 'planner_profile_about'
            first_indent 0
    else:
        text bio:
            style 'planner_profile_about'

#PROFILES
screen planner_alice_profile:
    $ bio = "Alice is a shy, innocent girl that spends most of her time reading and daydreaming about space. Her connection with you is instant. She likes spaceships, especially ones with a phallic shape for some reason."
    use planner_profile_contents(Alice, 'alice roommate intro', 1000, 820, bio)

screen planner_antonella_profile:
    $ bio = "Antonella is Kassandra's libertine older sister. Single and experienced, she lives by her own rules and always gets what she wants. She refuses to be tied down by a long-term relationship. Girls just want to have fun!"
    use planner_profile_contents(Antonella, 'antonella wine', 330, 750, bio)

screen planner_audrey_profile:
    $ bio = "Even though her cousin Neil is the real shop teacher at Trustworth, Audrey is far more talented than him when it comes to machinery. Everyone goes to her for car repairs, earning her the nickname \"the machine queen.\""
    use planner_profile_contents(Audrey, 'audrey neutral', 330, 750, bio)

screen planner_barbara_profile:
    $ bio = "Like her sister Sally, Barbara is not used to being around men, having lived on an isolated mountain ranch her entire life. She dreams of becoming a cheerleader, but since she's home-schooled, that seems unlikely."
    use planner_profile_contents(Barbara, 'barbara neutral', 1050, 775, bio)

screen planner_beatrix_profile:
    $ bio = "Intelligent, arrogant, and short-tempered, Beatrix can be difficult to deal with. However, those who persist at getting behind her nerdy facade will find that she is also a loyal friend to those she respects."
    if calendar.event == HALLOWEEN_EVENT:
        use planner_profile_contents(Beatrix, 'beatrix mavis neutral', 1010, 780, bio)
    else:
        use planner_profile_contents(Beatrix, 'beatrix uniform smile', 125, 780, bio)

screen planner_blair_profile:
    $ bio = "Blair is easy-going and a bit of a tomboy. She's always gotten along better with boys than girls. She loves cars, tattoos, rock and roll, and baggy clothes. She is always fighting with her sister, Cassidy."
    use planner_profile_contents(Blair, 'blair roommate intro', 600, 765, bio)

screen planner_cassidy_profile:
    $ bio = "Cassidy was born at almost the exact same time as you. She's a spoiled brat with an inflated ego who pretends to hate you, only to hide how much she likes you."
    if calendar.event == HALLOWEEN_EVENT:
        use planner_profile_contents(Cassidy, 'cassidy daphne neutral', 275, 775, bio)
    else:
        use planner_profile_contents(Cassidy, 'cassidy pajama neutral', 105, 850, bio)

screen planner_christy_profile:
    $ bio = "Considered the hottest cheerleader in school, Christy acts like everyone is expecting her to act. However, behind that slutty façade she hides a more interesting personality to discover, if you're lucky."
    if calendar.event == HALLOWEEN_EVENT:
        use planner_profile_contents(Christy, 'christy pokemon', 100, 830, bio)
    else:
        use planner_profile_contents(Cassidy, 'christy uniform neutral', 105, 830, bio)

screen planner_dakota_profile:
    $ bio = "Taking care of a ranch is no easy task, but for an independent, strong-willed woman like Dakota, it comes naturally. The only things she loves more than her ranch are her two daughters, Barbara and Sally."
    use planner_profile_contents(Dakota, 'dakota neutral', 260, 790, bio)

screen planner_eunice_profile:
    $ bio = "Often bullied by her looks, Eunice's overweight is a direct result of the stress she deals with everyday. Maybe you can help her become a more confident woman and get rewarded by those huge thights."
    use planner_profile_contents(Eunice, 'eunice uniform happy', 230, 790, None)

screen planner_fiona_profile:
    $ bio = "Fiona runs a small stand on campus selling various knickknacks. Although she has trouble managing the store, she is determined to prove she can do it without her father's help. She's also very open to new experiences."
    if calendar.event == HALLOWEEN_EVENT:
        use planner_profile_contents(Fiona, 'fiona waldo neutral', 1050, 760, bio)
    else:
        use planner_profile_contents(Fiona, 'fiona clerk neutral', 1050, 780, bio)

screen planner_kassandra_profile:
    use planner_profile_contents(Kassandra, 'kassandra neutral', 250, 800, None)

screen planner_lola_profile:
    $ bio = "Lola is promiscuous, very promiscuous. Even her boyfriend, Vincent, knows it, although everyone seems to play dumb because they fear him. You might as well get a piece of that cake too."
    use planner_profile_contents(Lola, 'lola neutral', 1025, 810, bio)

screen planner_mandy_profile:
    $ bio = "The most popular girl in school. The leader of the cheerleader team and the quaterback's girlfriend. What else is there to say? It will very hard to reach her, but not impossible."
    if calendar.event == HALLOWEEN_EVENT:
        $ img = Crop((450, 0, 750, 1080), 'mandy supergirl')
        use planner_profile_contents(Mandy, img, 1025, 810, bio)

screen planner_miku_profile:
    $ bio = "Miku loves cosplaying and taking sexy photos with her costumes. She's very flexible and seems to be inclined to do things her mom does. You can't help but wonder what's her mom's job."
    if calendar.event == HALLOWEEN_EVENT:
        use planner_profile_contents(Miku, 'miku wizard neutral', 210, 790, bio)
    else:
        use planner_profile_contents(Miku, 'miku uniform neutral', 200, 820, bio)

screen planner_aurora_profile:
    use planner_profile_contents(Aurora, 'aurora jumpsuit crossed', 200, 820, None)

screen planner_missdawson_profile:
    $ bio = "Miss Dawson is in love with Dr. Stapleneck, or at least has a kink for authority figures. However, she's open to experience the taste of youth, if you know how to treat her with respect."
    use planner_profile_contents(Dawson, 'missdawson neutral', 220, 780, bio)

screen planner_missjones_profile:
    use planner_profile_contents(Jones, 'missjones sit', 445, 700, None)

screen planner_misspunny_profile:
    $ bio = "The hot Spanish teacher. Every time she talks to you in another language, you feel your skin shivering and your bulge twitching. Maybe you can show her your ability to use your tongue as well."
    $ img = Crop((1000, 0, 780, 980), 'misspunny desk')
    use planner_profile_contents(Punny, img, 1035, 720, bio)

screen planner_jill_profile:
    $ bio = "Detective of the P.V.P.D, this beautiful agent is a hard to crack nut. You already gave her a pretty good first impression so it's a matter of time before you crack a case of sexual misconduct."
    use planner_profile_contents(Jill, 'jill police neutral', 280, 730, bio)

screen planner_ruby_profile:
    $ bio = "As a member of the royal family, she expects to be treated as the queen of England. However, Ruby secretly loves to experience mundane acts with the common people, some more sexual than others."
    if calendar.event == HALLOWEEN_EVENT:
        use planner_profile_contents(Ruby, 'ruby maeve', 180, 830, bio)

screen planner_sally_profile:
    $ bio = "Sally has lived on a secluded ranch her entire life and is not used to being around men, although she is very close with her sister Barbara. She is a cowgirl at heart and tries to emulate her mother, Dakota."
    use planner_profile_contents(Sally, 'sally neutral', 230, 760, bio)

screen planner_tatiana_profile:
    $ bio = "The spiciest latina in school, Tatiana loves fast cars and salsa music. Play your cards right, and you'll have a great time dancing and sweating before going to bed with this señorita."
    if calendar.event == HALLOWEEN_EVENT:
        use planner_profile_contents(Tatiana, 'tatiana pirate', 300, 770, None)

screen planner_wendy_profile:
    $ bio = "Mayor Jack Donaguy's daughter. She hates being overprotected by her dad and doesn't waste the opportunity to get intimate with the new guy in town. This relationship is extremely dangerous, but you love it."
    use planner_profile_contents(Wendy, 'wendy neutral', 60, 850, bio)

screen planner_violet_profile:
    if calendar.event == HALLOWEEN_EVENT:
        use planner_profile_contents(Violet, 'violet tinkerbell', 320, 770, None)
