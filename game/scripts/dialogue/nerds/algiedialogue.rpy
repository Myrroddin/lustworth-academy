#VARIABLES
default quests.algieScroll = LOCKED

#LABELS
label algiedialogue:
    hide screen freeroamhud with None
    stop music
    if Jimmy.hasItem(ItemCrownofGods):
        if quests.beatrixGetlaid == COMPLETE:
            menu:
                __("Replay RPG Campaign v0.5.4"):
                    jump rpgcampaignact1
                __("Nevermind"):
                    $ gotoscene('schoollibrarynerdcliquehq')
        if quests.beatrixGetlaid == SATISFIED:
            jump rpgcampaignact1
    elif quests.rescueBucky == COMPLETE:
        if quests.beatrixGetlaid == ACTIVE:
            if BeatrixDaylimit == True:
                show algie uniform neutral with dissolve
                Algie "[player_name]! We are currently on an important meeting."
                Algie "You should come back tomorrow!"
                Jimmy "Alright."
                $ gotoscene('schoollibrarynerdcliquehq')
            else:
                jump rpgcampaignintro
    elif quests.algieScroll == ACTIVE:
        jump .active
    elif quests.algieScroll == SATISFIED:
        jump .satisfied
    else:
        $ gotoscene('schoollibrarynerdcliquehq')

label .active:
    show algie uniform neutral with dissolve
    Algie "Oh, [player_name]! Did you find the scroll?"
    Jimmy "I'm on it."
    Algie "Please, hurry. The fate of our campaign it's in your hands."
    $ gotoscene('schoollibrarynerdcliquehq')

label .satisfied:
    play music MUSIC_NERDSCLIQUE_THEME
    show algie uniform neutral with dissolve
    Algie "[player_name]! Did you find the scroll?"
    Jimmy "Here it is."
    $ Jimmy.inventory.remove(ItemAlgieScroll)
    Algie "Oh, this is the first step towards our glorious goal."
    Algie "You have proven yourself to be very useful, friend"
    Algie "The king wants a word with you."
    hide algie
    show earnest uniform neutral with dissolve
    $ Earnest.met = True
    Earnest "You did good, apprentice."
    Earnest "If you keep succeding like this, you might be able to enter our order."
    Jimmy "I'm not interested in any 'order', pal."
    play sound "audio/sfx/earnestohha.ogg"
    Earnest explain "I understand your scepticism, but we can still benefit each other with a merely transactional relationship."
    Earnest "The electoral campaign for Class president is starting next week, and I need a campaign manager."
    Earnest "Historically, we, the nerds have always won the election year after year because of our unmatched intelligence."
    Earnest "But, this year the polls are in favor of the Preps and their new candidate. So, I'm a bit worried."
    Earnest "I need someone capable of helping me destroy those presumptuous dickheads and win the election."
    Jimmy "Well, honestly, I'm not much into elections, so."
    play sound "audio/sfx/earnestcanpayyou.ogg"
    Earnest "[player_name], I can pay you, generously."
    Jimmy "I'm listening."
    Earnest "I knew I was born a natural leader."
    Earnest "I will contact you very soon."
    Earnest "In the meantime, you can help us end our RPG campaign, so we can focus our efforts on the coming election."
    Jimmy "Right..."
    Earnest "Algie, do you know where Bucky is?"
    Algie "He went out a couple of minutes ago to the Auto Shop to get some parts for his science project."
    Earnest "Well, let's hope he doesn't get in trouble."
    Earnest "That is all for now, apprentice."
    Jimmy "..."
    hide earnest with dissolve
    show algie uniform neutral with dissolve
    Algie "Well! Thank you so much [player_name]."
    Algie "I hope we can be good friends from now on!"
    Jimmy "Not a chance."
    play sound "audio/sfx/algiepretendfriends.ogg"
    Algie smug "Well, you can just pretend we're friends, at least."
    Algie "Ha, ha... ha."
    play sound "audio/sfx/algienevermind.ogg"
    Algie neutral "Nevermind."
    Algie "Well, here's the payment we promised."
    $ Jimmy.money += 100
    call yougotmoney from _call_yougotmoney_9
    Algie "See ya!"
    hide algie with dissolve
    $ quests.algieScroll = COMPLETE
    call nexttime from _call_nexttime_25
    $ gotoscene('schoollibrarynerdcliquehq')

label algiescrollfound:
    hide screen freeroamhud with None
    scene boysbathroomplaceholder with fade
    play music MUSIC_FUNNY_MOMENT
    show derek confront left with dissolve
    Derek "Ha! I saw that ugly bitch with the same pimples on her face."
    Derek "You two have been making out, don't you?"
    show melvin herpes neutral with dissolve
    Unk "Understand my predicament, my good man."
    Unk "The very prospect of such an unsolicited labial congress precipitates a most distressing anaphylactic response within my person."
    Derek "Oh, you're not going to fool me... You might be a virgin, but I know herpes when I see it."
    Unk "Well, I got to admit that I'm afflicted with a peculiar constitutional frailty, but I haven't infected anyone else."
    play sound "audio/sfx/melvininfact.ogg"
    Unk "In fact, I'm very careful with this curse."
    Derek arms left "Yeah, right, Melvin... You're not getting out of here until you tell me how to get into Beatrix's trousers."
    $ Melvin.met = True
    Derek "I like ugly bitches cause they are easy to get, I don't give a fuck about the herpes."
    Melvin  "I'll say it once more. Her allergic problem has nothing to do with me."
    Melvin "Now, be gone. I have to deliver something important."
    Derek neutral left "Come on, weirdo... You're gonna deliver my fist into your face if you don't start speaking!"
    play sound "audio/sfx/clearthroat01.ogg"
    Jimmy "Everything okay over here, fellas?"
    Derek "..."
    Derek "There is something worst than herpes in this world... It's you, new kid."
    Derek "Can't you just leave me alone for a moment?"
    Jimmy "Well, seems like we keep bumping into each other."
    Jimmy "Maybe it's fate."
    Melvin jovial "Oh, fate is a beautiful, capricious lady. I'm sure she sent you here to help this humble servant."
    Jimmy "Well, Algie is kind of capricious, but he's surely not a lady, and not beautiful at all."
    Melvin laugh "Ho, ho, ho, ho, your statement is more than correct, my friend."
    Derek "Ha, so you're one of this dorks now."
    Derek "I knew you had it in you."
    Jimmy "Whatever, I need the scroll, Melvin."
    play sound "audio/sfx/melvinlisten.ogg"
    Melvin neutral "Well, sir. Listen, I've been trying to grab the Scroll of the Elders from the hidden vault..."
    Melvin "But, this brute is in my way, so I can't complete my task."
    Derek "I'm tired of this shit..."
    Derek "The next time we meet, new guy, will be the last time you'll get in my way."
    play sound "audio/sfx/run01.ogg"
    hide derek with vpunch
    __("{i}Scrambling to his feet, Derek shot one last glare before tucking his tail between his legs and running to the door.{/i}")
    Melvin "Unbelievable! I've never seen a man capable of transmiting such a powerful intimidation."
    Melvin laugh "You didn't even had to touch him, ho, ho, ho! Oh my lord!"
    Jimmy "Well, I have some story with that guy."
    Jimmy "You alright?"
    Melvin jovial "My deepest gratitude, Sir. Your intervention has been timely and... efficient."
    __("{i}Melvin showed [player_name] a roll of aged-looking paper, tied with a pristine red ribbon.{/i}")
    Melvin "Here, The Scroll of the Elders."
    call item_pickup(ItemAlgieScroll) from _call_item_pickup_40
    Jimmy "Thank you, I'll get it back to the library."
    Melvin neutral "Please, do, my friend. It's safer in your capable hands."
    Melvin "Deliver this to Guild Master Algernon with the utmost haste."
    Melvin "The fate of Cumalot hangs in the balance!"
    Jimmy "Right..."
    $ quests.algieScroll = SATISFIED
    $ gotoscene('mainbuildinglefthallway')
