# init python:
init python: # Start an initialization Python block for the game logic.
    import random # Import the standard 'random' module for randomization.
    
    def seed_random():
        import time # <-- LOCAL IMPORT!
        random.seed(time.perf_counter_ns()) # Seeds the random number generator using high-resolution time, ensuring better randomness.

    seed_random()
    
    def victory_sound():
        renpy.play("audio/sfx/fightvictory.ogg")

    def defeat_sound():
        renpy.play("audio/sfx/fightlose.ogg")

    class shooter_clock(renpy.Displayable): # Define a custom displayable class to act as a game clock/redraw mechanism.
        def __init__(self): # Constructor for the clock.
            super(renpy.Displayable,self).__init__() # Calls the parent (renpy.Displayable) constructor.
            self.start = 0 # Initialization variable (not directly used here, but good practice).
            self.current = 0 # A counter to track frames or updates.
        def render(self,width,height,st,at): # The custom render method, called every frame.
            self.current += 1 # Increments the counter on every frame/render.

#     renpy.redraw(self, 0)
            renpy.redraw(self, 0) # Forces Ren'Py to redraw this displayable (and thus the screen) on the next frame.
            return renpy.Render(0, 0) # Returns an empty render object (0x0 size) as the clock is invisible.

    class shooter_enemy(renpy.Displayable): # Define a custom displayable class for an enemy object.
        def __init__(self, images, x, y, z, idle_limit=200): # Constructor. 'images' is a list of image names, x/y/z are coordinates/zoom.
            super(renpy.Displayable,self).__init__() # Calls the parent (renpy.Displayable) constructor.
            self.image = random.choice(images) # Picks a random image from the provided list for the enemy's base look.
            self.x = x # Horizontal screen position.
            self.y = y # Vertical screen position.
#    self.z = z
            self.z = z # Zoom/scale factor.
            self.yzoom = .01 # Vertical zoom factor, starts small for a "pop-up" effect.
            self.stat = "_idle" # Current status/state of the enemy (e.g., "_idle", "_shooting", "_dead").
            self.time = 0 # A simple time counter for state duration.
            self.parent = None # Placeholder for the parent handler object.
            self.idle_limit = idle_limit
        def change(self, stat): # Method to change the enemy's state.
            self.stat = stat # Sets the new state.
            self.time = 0 # Resets the state time counter.
#        def shoot(self):
        def shoot(self): # Method to handle the enemy shooting.
            renpy.play("audio/sfx/shooter/gun_1.ogg", "sound") # Plays a sound effect for the enemy shooting on the "sound" channel.
            self.change("_shooting") # Changes the enemy state to "_shooting".
            self.parent.got_shot() # Notifies the handler that the player has been hit/got shot.
        def render(self,width,height,st,at): # The custom render method, called every frame.
            if self.yzoom < 1: # Check if the "pop-up" animation is complete.
                self.yzoom += .2 # Gradually increases vertical zoom for the animation.
            else:
#                self.yzoom = 1
                self.yzoom = 1 # Locks the vertical zoom to 1 (normal) once it reaches full size.
            self.time += 1 # Increments the state time counter.
            if self.time > self.idle_limit and self.stat == "_idle": 
                self.shoot()
            elif self.time > 100 and self.stat == "_shooting": # If in the shooting state for over 100 frames...
#  self.change("_idle")
                self.change("_idle") # ...it returns to the idle state.
            elif self.time > 100 and self.stat == "_dead": # If in the dead state for over 100 frames...
                self.change("hidden") # ...it is set to the "hidden" state (removed from screen).
            img = self.image + self.stat # Constructs the image tag by combining the base image name and the state (e.g., "cowboy_1" + "_idle").
            if self.stat == "hidden": # If the state is "hidden"...
                return renpy.Render(0, 0) # ...return an empty render, effectively making it invisible.
            t = Transform(img, # Creates a Transform object for the image with specified properties.
# xanchor=0.5, yanchor=0.5, zoom = self.z, yzoom = self.yzoom, nearest = True)
                xanchor=0.5, yanchor=0.5, zoom = self.z, yzoom = self.yzoom, nearest = True) # Sets anchors, overall zoom, vertical zoom (for pop-up), and `nearest=True` for pixel art scaling.
            child_render = renpy.render(t, width, height, st, at) # Renders the transformed image.
            cw, ch = child_render.get_size() # Gets the width and height of the rendered image.

            rv = renpy.Render(cw, ch) # Creates the final render object with the child's size.
            rv.blit(child_render, (0, 0)) # Copies the image render onto the final render object.

            renpy.redraw(self, 0) # Forces a redraw on the next frame.
            return rv # Returns the final render object.

#   class shooter_handler:
    class shooter_handler: # Define the main class to manage the game state and logic.
        def __init__(self, enemies, kill_limit): # Constructor. 'enemies' is a list of possible enemy configurations.
            self.enemies = enemies # Stores the list of enemy configurations.
            self.active_enemies = [] # A list to hold the currently spawned shooter_enemy objects.
            self.stat = "start" # The overall game state ("start", "playing", "dead").
            self.clock = shooter_clock() # Creates an instance of the custom clock displayable.
            self.health = 5 # Player's starting health.
            self.bullets = 6 # Player's starting bullets.
#          self.kills = 0
            self.kills = 0 # Player's kill count.
            self.kill_limit = kill_limit
        def start(self): # Method to start the game.
            self.stat = "playing" # Changes the game state to "playing".
        def restart(self): # Method to reset and restart the game.
            self.kills = 0 # Resets kills.
            self.health = 5 # Resets health.
            self.bullets = 6 # Resets bullets.
            self.active_enemies = [] # Clears all active enemies.
#            self.stat = "playing"
            self.stat = "playing" # Sets the game state to "playing".
        def spawn(self): # Method to handle enemy spawning.
            for i in self.active_enemies: # Loop through active enemies.
                if i.stat == "hidden": # If an enemy is in the "hidden" state...
                    self.active_enemies.remove(i) # ...remove it from the active list.
            if len(self.active_enemies) < 3: # Check if there are less than 3 enemies currently active.
#        e = random.choice(self.enemies)
                e = random.choice(self.enemies) # Select a random enemy configuration from the list.
                enemy = shooter_enemy(*e) # Create a new shooter_enemy instance using the configuration parameters.
                for i in self.active_enemies: # Check if the chosen spawn point is already occupied.
                    if i.x == enemy.x:
                        if i.y == enemy.y:
#                         return
                            return # If the position is the same, abort spawning to prevent overlap.
                enemy.parent = self # Sets the enemy's parent handler to this instance.
                self.active_enemies.append(enemy) # Adds the new enemy to the active list.
        def shoot(self, enemy): # Method to handle the player shooting. 'enemy' is the target (or None if a miss).
            if self.bullets > 0: # Check if the player has bullets.
                tag = f"shooter_bullets_{random.randint(0,10000)}" # Creates a unique tag for the bullet-hole displayable.
# = f"shooter_bullets_{random.randint(0,10000)}"
                x, y = [*renpy.get_mouse_pos()] # Gets the current mouse position where the bullet hole should appear.
                Show("shooter_bullets", x = x, y = y, z = 8, tag = tag, _tag = tag)() # Shows the 'shooter_bullets' screen (the bullet hole) at the mouse position.
                self.bullets -= 1 # Decrements the bullet count.
                renpy.play("audio/sfx/shooter/gun_2.ogg", "sound") # Plays the player's shooting sound effect.
#   if not enemy:
                if not enemy: # If the player shot but missed an enemy (enemy is None).
                    return # Exit the function.
                if not enemy.stat == "_dead": # Check if the target is not already dead.
                    renpy.play("audio/sfx/shooter/kill.ogg", "sfx1") # Play the kill/hit sound on the "sfx1" channel.
                    enemy.change("_dead")
                    self.kills += 1 # Kill count is incremented [cite: 17]
                    
                    # 💡 CHANGE 3: Check for the winning condition immediately after a kill
                    if self.kills >= self.kill_limit:
                        self.stat = "won"
                    # Change the enemy state to "_dead".
            else: # If the player has no bullets.
                renpy.play("audio/sfx/shooter/empty.ogg", "sound") # Play the "out of bullets" sound.
        def got_shot(self): # Method called when an enemy successfully shoots the player.
            if self.stat == "playing": # Check if the game is currently running.
                self.health -= 1 # Decrements the player's health.
                if self.health < 1: # Check if health has dropped to zero or below.
#                  self.stat = "dead"
                    self.stat = "dead" # Changes the game state to "dead".
                renpy.play("audio/sfx/shooter/hurt.ogg", "sfx1") # Plays the player 'hurt' sound.
        def reload(self): # Method to handle reloading.
            renpy.play("audio/sfx/shooter/reload.ogg", "sound") # Play the reload sound.
            self.bullets = 6

screen shooter(initial_enemies, kill_limit, timer_delay=1.0): # Define the main Ren'Py screen for the minigame.
    modal True # Makes the screen modal, capturing all input until it's hidden or returns.
    style_prefix "shooter" # Sets the style prefix for elements on this screen.
    default g = shooter_handler(initial_enemies, kill_limit=kill_limit)
    add g.clock # Adds the invisible custom clock object; its render method forces screen redraws.
    button: # This is the full-screen background button for missing a shot.
        background None # Makes the button transparent.
        action Function(g.shoot, None) # Calls g.shoot with None as the enemy argument (a miss).
    fixed: # A fixed layout box covering the full screen.
# xysize 1920,1080
        xysize 1920,1080 # Explicitly sets the size to standard 1080p resolution.
        for i in g.active_enemies: # Loop through all currently active enemy objects.
            button: # Creates a button for each active enemy.
                padding .0,.0 pos i.x,i.y background None anchor .5,1.0 # Positions the button using the enemy's x/y, anchors to the bottom center, and makes it transparent.
                add i # Adds the shooter_enemy displayable 'i' as the button's visual content.
                action Function(g.shoot, i) # Calls g.shoot, passing the enemy object 'i' as the argument (a hit).

    if g.stat == "start": # Content displayed when the game state is "start".
        imagebutton:
#          align .5,.5
            align 0.48,0.48 # Centers the button on the screen.
            idle "images/sprites/minigames/slingshot/start_button_idle.webp"
            # Specifies the image when the mouse hovers over it
            hover "images/sprites/minigames/slingshot/start_button_hover.webp"
            action Function(g.start) # Calls the handler's start method to begin the game.
    elif g.stat == "playing": # Content displayed when the game state is "playing".
        timer timer_delay repeat True action Function(g.spawn)
        
        bar value g.kills range g.kill_limit:
            left_bar "images/sprites/minigames/slingshot/panic_bar_full.webp"
            right_bar "images/sprites/minigames/slingshot/panic_bar_empty.webp"
            xpos 1500 ypos 78 xmaximum 390
            ymaximum 85

        # 💡 Health Indicator:
        hbox:
            align .0,1.0 spacing 10 offset 20,-20
            # The 'for' loop rebuilds the contents every time the screen updates
            for i in range(g.health):
                add "images/sprites/minigames/slingshot/shooter_health.webp" at zoom(2, True)

        # 💡 Bullet Indicator:
        if g.bullets > 0:
            hbox:
                align 1.0,1.0 spacing 10 offset -20,-20
                for i in range(g.bullets):
                    add "images/sprites/minigames/slingshot/shooter_bullets.webp" at zoom(2, True)

        else:
            # Reload button appears when g.bullets is 0
            imagebutton:
                align 1.0,1.0  offset -20,-20
                idle "images/sprites/minigames/slingshot/reload_button_idle.webp"
                # Specifies the image when the mouse hovers over it
                hover "images/sprites/minigames/slingshot/reload_button_hover.webp"
                action Function(g.reload)
        key "K_SPACE" action Function(g.reload) # Binds the Space key to the reload action.
    elif g.stat == "dead": # Content displayed when the game state is "dead".
        vbox:
            on "show" action Play(channel="sfx1", file="audio/sfx/fightlose.ogg")
            align 0, 0
            add "images/sprites/minigames/slingshot/defeat_screen.webp"
        
        hbox: # Horizontal box for the dead screen buttons.
            
            align .5,.5 spacing 10 # Centers the buttons.
            imagebutton:
                # Specifies the image for the normal state
                idle "images/sprites/minigames/slingshot/restart_button_idle.webp"
                # Specifies the image when the mouse hovers over it
                hover "images/sprites/minigames/slingshot/restart_button_hover.webp"
                # Defines the action that occurs when the button is clicked
                action Function(g.restart) # Calls the handler's restart method.
            imagebutton:
                # Specifies the image for the normal state
                idle "images/sprites/minigames/slingshot/skip_button_idle.webp"
                # Specifies the image when the mouse hovers over it
                hover "images/sprites/minigames/slingshot/skip_button_hover.webp"
                # Defines the action that occurs when the button is clicked
                action Return(g.kills) # Hides the screen and returns the player's kill count to the calling label.
    elif g.stat == "won":
        vbox:
            on "show" action Play(channel="sfx1", file="audio/sfx/fightvictory.ogg")
            align 0, 0.3
            add "images/sprites/minigames/slingshot/victory_screen.webp"
            imagebutton:
                align 0.5, 0.7
                # Specifies the image for the normal state
                idle "images/sprites/minigames/slingshot/continue_button_idle.webp"
                # Specifies the image when the mouse hovers over it
                hover "images/sprites/minigames/slingshot/continue_button_hover.webp"
                # Defines the action that occurs when the button is clicked
                action Return(g.kills)
    

style shooter_button:
    background Frame("shooter_frame", 6,6) padding (20,20)

screen shooter_bullets(x,y,z,tag): # A screen for displaying a temporary bullet hole.
    add "bullet hole" pos x,y anchor .5,.5 at zoom(4, True) # Adds the "bullet hole" image at the shot coordinates, scaled up.
    timer 1 repeat True action Hide(tag) # Sets a timer to hide the screen (the bullet hole) after 1 second using its unique tag.


##################### LOCATION VARIABLES ###########################

init python:
    # A function to get configuration based on location tag
    def get_battle_config(location):
        if location == "buckyrescue":
            return {
                "enemies": [ # Saloon enemies: Close, mid-zoom, fast-shooting
                    [["bully_1"], 1500, 950, 4, 150], 
                    [["bully_2"], 300, 1150, 5, 100],
                    [["bully_3", "bully_2"], 400, 600, 2, 200],
                    [["bully_4"], 1200, 650, 2, 150],
                    
                ],
                "timer_delay": 0.5,
                "kill_limit": 15, # Fast spawn
            }
        #elif location == "canyon":
            #return {
                #"enemies": [ # Canyon enemies: Far away, high-zoom, slower-shooting
                #    [["cowboy_4"], 200, 1000, 6],
                #    [["cowboy_5"], 1700, 1000, 6],
                #    [["cowboy_1"], 960, 500, 3], # Enemy on a high cliff
                #],
                #"timer_delay": 1.5 # Slower spawn
            #}
        # Use a default configuration if needed
        return get_battle_config("buckyrescue")
