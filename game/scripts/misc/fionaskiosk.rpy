default fionasKioskItems = []

#SCREENS
screen fionaskiosk(halloweenSkip=False):
    imagemap:
        ground "fionastoreshelf"
        hover "fionastoreshelfhover"

        if not halloweenSkip:
            hotspot (1572, 0, 346, 1080) clicked Jump('fionaskiosk_end')

    add "fiona clerk neutral":
        xpos -0.07

    for i in range(len(fionasKioskItems)):
        # Sprite
        $ item = fionasKioskItems[i]
        $ x, y = getKioskSlotPos(i)
        use sprite(
            item.image,
            (x, y, 180, 180),
            action=Return(item),
            focusMask=False)
        # Price
        $ x, y = getKioskPricePos(i)
        text "${}".format(item.price):
            xcenter x
            ypos y

init python:
    def getKioskSlotPos(i):
        row = i // 2
        col = i % 2
        x = 500 + 350 * col
        y = 205 + 280 * row
        return (x, y)
    
    def getKioskPricePos(i):
        x, y = getKioskSlotPos(i)
        return (x + 90, y + 185)
    
    def showKioskItems():
        for i in range(len(fionasKioskItems)):
            # Sprite
            item = fionasKioskItems[i]
            x, y = getKioskSlotPos(i)
            renpy.show(item.image, at_list=[Transform(pos=(x, y))])
            # Price
            x, y = getKioskPricePos(i)
            renpy.show(
                'slot{}'.format(i), 
                what=Text("${}".format(item.price)), 
                at_list=[Transform(xcenter=x, ypos=y)])

label fionaskiosk_showscene:
    scene fionastoreshelf
    show fiona clerk neutral:
        xpos -0.07
    $ showKioskItems()
    return

#LABELS
label fionaskiosk:
    show screen freeroamhud(showTray=False)
    play music MUSIC_FIONAS_THEME
    $ fionasKioskItems.sort(key=lambda x: x.price)
    call fionaskiosk_showscene from _call_fionaskiosk_showscene_2
    if len(fionasKioskItems) > 0:
        Fiona "Hey [player_name], see anything you like?"
    else:
        Fiona "Hey [player_name]. I'm all out of stock right now, check back later maybe?"
        Jimmy "Okay, sure."
        pause 0.3
        jump fionaskiosk_end
    jump fionaskiosk_loop

label fionaskiosk_loop:
    call fionaskiosk_showscene from _call_fionaskiosk_showscene_3
    call screen fionaskiosk
    call fionaskiosk_onclick(_return) from _call_fionaskiosk_onclick_1
    jump fionaskiosk_loop

label fionaskiosk_end:
    $ gotoscene('girlsdormfrontgate')

label fionaskiosk_onclick(item):
    show screen freeroamhud(showTray=False)
    Jimmy "Can I have the [item.name]?"
    Fiona "Sure, that'll be $[item.price]."
    if item.price <= Jimmy.money:
        play sound SOUND_PURCHASE
        $ Jimmy.money -= item.price
        # $ Jimmy.inventory.append(item)
        $ fionasKioskItems.remove(item)
        Fiona "Here ya go!"
        call item_pickup(item) from _call_item_pickup_21
        call fionaskiosk_quests from _call_fionaskiosk_quests
    else:
        Jimmy "Oh shit, I just realized I don't have enough."
        Jimmy "Uh, nevermind then."
    return

label fionaskiosk_quests:
    if item in [ItemShaggyCostume, ItemPirateCostume, ItemHeroCostume]:
        $ quests.halloweenCostume = SATISFIED
        $ quests.garyHalloweenHeist = COMPLETE
        show halloweenheistplans06 with dissolve
        Jimmy "So..."
        show halloweenheistplans07 with dissolve
        Jimmy "I got the costume."
        Jimmy "Seems like we are ready for Halloween."
    elif item == ItemPolaroidCamera:
        $ quests.mikuPhotoShoot = SATISFIED
    return

# label fionaskiosk_camera:
#     Jimmy "I'll take the camera."
#     Fiona "Great! That'll be $100."
#     play sound "audio/sfx/purchasesound.ogg"
#     $ Jimmy.money -= 100
#     $ quests.mikuPhotoShoot = SATISFIED
#     jump fionaskiosk_loop

# label fionaskiosk_shaggy:
#     Jimmy "I'll take the Shaggy costume."
#     Fiona "Great!"
#     play sound "audio/sfx/purchasesound.ogg"
#     $ Jimmy.money -= 100
#     $ quests.halloweenCostume = SATISFIED
#     $ Jimmy.inventory.append(JIMMY_SHAGGY)
#     jump fionaskiosk_loop

# label fionaskiosk_pirate:
#     Jimmy "I'll take the Pirate costume."
#     Fiona "Great!"
#     play sound "audio/sfx/purchasesound.ogg"
#     $ Jimmy.money -= 300
#     $ quests.halloweenCostume = SATISFIED
#     $ Jimmy.inventory.append(JIMMY_PIRATE)
#     jump fionaskiosk_loop

# label fionaskiosk_homelander:
#     Jimmy "I'll take the Superhero costume."
#     Fiona "Great!"
#     play sound "audio/sfx/purchasesound.ogg"
#     $ Jimmy.money -= 1000
#     $ quests.halloweenCostume = SATISFIED
#     $ Jimmy.inventory.append(JIMMY_HOMELANDER)
#     jump fionaskiosk_loop
