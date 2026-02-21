default inventory.page = 0

style inventory_text:
    font 'fonts/CyborgSister.ttf'
    outlines [(1, '#000', 0, 0)]
    size 64

screen inventory:
    zorder 150
    
    $ maxPage = getInventoryMaxPage()

    imagemap:
        ground 'inventoryhubidle'
        hover 'inventoryhubhover'

        hotspot (1352, 96, 128, 128) action Jump('inventory_exit')
        if inventory.page > 0:
            hotspot (360, 688, 88, 96) action SetVariable('inventory.page', inventory.page - 1)
        if inventory.page < maxPage:
            hotspot (360, 784, 88, 96) action SetVariable('inventory.page', inventory.page + 1)
    
    $ x, y = (554, 126)
    text str(inventory.page + 1):
        style 'inventory_text'
        xanchor 1.0
        pos x, y
    text "/":
        style 'inventory_text'
        pos x + 12, y
    text str(maxPage + 1):
        style 'inventory_text'
        pos x + 40, y

    for i in range(12):
        $ idx = inventory.page * 12 + i
        if idx < len(Jimmy.inventory):
            $ item = Jimmy.inventory[idx]
            $ x, y = getInventorySlotPos(i)
            use sprite(
                item.image, 
                (x, y, 180, 180), 
                action=Return(item), 
                focusMask=False)

init python:
    def getInventorySlotPos(i):
        row = i // 4
        col = i % 4
        x = 514 + 232 * col
        y = 274 + 224 * row
        return (x, y)
    
    def getInventoryMaxPage():
        return max(0, (len(Jimmy.inventory) - 1) // 12)
    
    def showInventoryItems():
        for i in range(12):
            idx = inventory.page * 12 + i
            if idx < len(Jimmy.inventory):
                item = Jimmy.inventory[idx]
                x, y = getInventorySlotPos(i)
                renpy.show(item.image, at_list=[Transform(pos=(x, y))])
    
    def showInventoryPageNum():
        x, y = (554, 126)
        maxPage = getInventoryMaxPage()
        renpy.show('page',
            what=Text(str(inventory.page + 1), style='inventory_text'), 
            at_list=[Transform(xpos=x, ypos=y, xanchor=1.0)])
        renpy.show('slash',
            what=Text("/", style='inventory_text'), 
            at_list=[Transform(xpos=x + 12, ypos=y)])
        renpy.show('maxpage',
            what=Text(str(maxPage + 1), style='inventory_text'), 
            at_list=[Transform(xpos=x + 40, ypos=y)])

label inventory_showscene:
    show inventoryhubidle
    $ showInventoryPageNum()
    $ showInventoryItems()
    return

#LABELS
label inventory:
    # Make free-roam HUD non-interactable
    show screen freeroamhud(False)
    jump inventory_loop

label inventory_loop:
    call inventory_showscene from _call_inventory_showscene
    call screen inventory
    call inventory_onclick(_return) from _call_inventory_onclick
    jump inventory_loop

label inventory_onclick(item):
    if item.descr is not None:
        # $ renpy.say(None, item.descr)
        $ renpy.show(
            'descr', 
            what=Text(item.descr, xmaximum=800, text_align=0.5),
            at_list=[Transform(xalign=0.5, yanchor=0.5, ypos=960)])
        $ renpy.pause()
        $ renpy.hide('descr')
    return

label inventory_exit:
    # return to current scene on inventory close
    $ gotoscene(scenemanager.scene)
