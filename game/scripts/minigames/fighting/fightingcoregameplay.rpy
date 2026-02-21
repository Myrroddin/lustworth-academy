default player_battleturn = False
default player_defending = False
default enemy_defending = False
default player_stunned = False
default enemy_stunned = False

init -1 python:
    import collections

    class Fighter:
        # This is the correct constructor that matches the call in battle_tutorial.rpy
        def __init__(self, name, clique, guts, wits, charisma, endurance_max, endurance_current, special_current, special_max):
            self.name = name
            self.clique = clique

            self.guts = guts
            self.wits = wits
            self.charisma = charisma
            self.endurance_max = endurance_max
            self.endurance_current = endurance_current

            self.special_current = special_current
            self.special_max = 10

screen battle_screen(player, enemy):

    # This makes the screen modal, meaning the player can't click on things outside of it
    
    bar value enemy.endurance_current range enemy.endurance_max:
        left_bar "images/sprites/minigames/wrestling/hud/health_bar_full.webp"
        right_bar "images/sprites/minigames/wrestling/hud/health_bar_empty.webp"
        xpos 1500 ypos 78 xmaximum 390
        ymaximum 85
    text enemy.name xpos 1600 ypos 57 style "battle_text"
    text "[enemy.endurance_current]/[enemy.endurance_max]" xpos 1670 ypos 110 style "battle_text"
    bar value enemy.special_current range enemy.special_max:
        left_bar "images/sprites/minigames/wrestling/hud/special_bar_full.webp"
        right_bar "images/sprites/minigames/wrestling/hud/special_bar_empty.webp"
        xpos 1500 ypos 155 xmaximum 390
        ymaximum 85
    text "Special: [enemy.special_current]/[enemy.special_max]" xpos 1590 ypos 210 style "battle_text"


    bar value player.endurance_current range player.endurance_max:
        left_bar "images/sprites/minigames/wrestling/hud/health_bar_full.webp"
        right_bar "images/sprites/minigames/wrestling/hud/health_bar_empty.webp"
        xpos 79 ypos 78 xmaximum 390
        ymaximum 85
    text player.name xpos 190 ypos 57 style "battle_text"
    text "[player.endurance_current]/[player.endurance_max]" xpos 250 ypos 110 style "battle_text"
    bar value player.special_current range player.special_max:
        left_bar "images/sprites/minigames/wrestling/hud/special_bar_full.webp"
        right_bar "images/sprites/minigames/wrestling/hud/special_bar_empty.webp"
        xpos 74 ypos 155 xmaximum 270
        ymaximum 60
    text "Special: [player.special_current]/[player.special_max]" xpos 160 ypos 210 style "battle_text"

screen battle_actions_screen():
    
    modal True

    vbox:
        xalign 0.1
        yalign 0.80
        spacing 10

        imagebutton:
            auto "images/sprites/minigames/wrestling/hud/attack_button_%s.webp"
            action Return("Attack")

        imagebutton:
            auto "images/sprites/minigames/wrestling/hud/defend_button_%s.webp"
            action Return("Defend")

        imagebutton:
            auto "images/sprites/minigames/wrestling/hud/special_button_%s.webp"
            action Return("Special")