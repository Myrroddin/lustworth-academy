#VARIABLES
define wallofprankmasters.maxPage = 5

default wallofprankmasters.checked = False
default wallofprankmasters.secretPassage = False

#SCREENS
screen wallofprankmasters:
    imagemap:
        ground "wallofprankmasters[page]"
        hover "wallofprankmasters[page]hover"

        if page > 1:
            hotspot (411, 198, 67, 876) clicked Jump("wallofprankmasters_prevpage")
        if page < wallofprankmasters.maxPage:
            hotspot (1355, 235, 87, 843) clicked Jump("wallofprankmasters_nextpage")
        hotspot (822, 945, 186, 132) clicked Jump("wallofprankmasters_secretpassagelock")
        hotspot (1646, 0, 267, 1064) clicked Jump("wallofprankmasters_exit")
        hotspot (0, 0, 289, 1070) clicked Jump("wallofprankmasters_exit2")

#LABELS
label wallofprankmasters:
    $ quick_menu = False
    hide screen freeroamhud
    scene wallofprankmasters1
    if not wallofprankmasters.checked:
        Developer "{i}Special thanks to our most loyal Patrons.{/i}"
        Developer "{i}You're awesome, and you will be immortalized in this monument.{/i}"
        $ wallofprankmasters.checked = True
    $ page = 1

label wallofprankmasters_loop:
    scene expression ('wallofprankmasters{}'.format(page))
    call screen wallofprankmasters
    jump wallofprankmasters_loop

label wallofprankmasters_prevpage:
    $ page -= 1
    jump wallofprankmasters_loop

label wallofprankmasters_nextpage:
    $ page += 1
    jump wallofprankmasters_loop

label wallofprankmasters_exit:
label wallofprankmasters_exit2:
    $ quick_menu = True
    $ gotoscene('boysdormtvroom')

label wallofprankmasters_secretpassagelock:
    if not wallofprankmasters.secretPassage:
        if not sexscenes.angiesNote:
            "\"If you don't have an invitation, you can't join the fornication.\""
            jump wallofprankmasters_loop
        else:
            "\"Welcome, fellow traveller.\""
            jump wallofprankmasters_secretpassage
    "\"Welcome, fellow traveller.\""
    jump wallofprankmasters_secretpassage

label wallofprankmasters_secretpassage:
    scene secretpassagedark01 with fade
    $ quick_menu = True
    if not wallofprankmasters.secretPassage:
        "{i}[player_name] didn't know what secrets were hiding below the depths of the school grounds.{/i}"
        "{i}It was too dark to distinguish anything but a dim light that led to an exit up ahead.{/i}"
        "Those are some weird mushrooms..."
        "And believe me, I've seen a bunch."
        "I wonder what I can find in these caverns."
        "But it's too dark to explore now."
        "I better get out of here."
        $ wallofprankmasters.secretPassage = True
    else:
        pause 0.8
    $ gotoscene('girlsdormsecretfloor', transition=fade)
