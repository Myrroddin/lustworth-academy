#VARIABLES
default yearbook.checked = False

#SCREENS
screen yearbook:
    imagemap:
        ground "yearbookpage[page]"
        hover "yearbookpage[page]hover"

        if page > 1:
            hotspot (71, 548, 410, 399) clicked SetVariable('page', page - 1)
        if page < 14:
            hotspot (1436, 626, 382, 356) clicked SetVariable('page', page + 1)
        hotspot (0, 0, 197, 187) clicked Jump("mainbuildingentrance")

#LABELS
label yearbook:
    hide screen freeroamhud
    scene yearbookpage1
    if not yearbook.checked:
        Developer "{i}This is a special place for our Tier 5 patrons.{/i}"
        Developer "{i}You'll be immortalized in this sacred book forever in Lustworth Academy.{/i}"
        Developer "{i}If you want to be part of this selected group, become a Tier 5 'Badass' patron and fill the appliance form to get your avatar.{/i}"
        Developer "{i}Thank you very much for your support. You're the best.{/i}"
        $ yearbook.checked = True
    $ page = 1
    jump yearbook_loop

label yearbook_loop:
    scene expression ('yearbookpage{}'.format(page))
    call screen yearbook
    jump yearbook_loop
