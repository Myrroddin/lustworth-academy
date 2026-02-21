# # a simple function that puts a string into the clipboard
# a simple function that puts a string into the clipboard
init python: # Start an initialization Python block.
    import pygame.scrap # Import the pygame clipboard module.
    def clip_put(m): # Define a function 'clip_put' to copy a string 'm' to the clipboard.
        pygame.scrap.put(pygame.scrap.SCRAP_TEXT, m.encode("utf-8")) # Puts the text 'm' (encoded as UTF-8) into the clipboard.
    def find_my_mouse(): # Define the main utility function.
        m = renpy.get_mouse_pos() # Gets the current mouse cursor position as a tuple (x, y).
        pos = str(m[0]) + "," + str(m[1]) # Formats the coordinates into a string "x,y".
        clip_put(pos) # Calls 'clip_put' to copy the formatted position string to the clipboard.
    config.underlay.append( # Appends a displayable to Ren'Py's underlay (behind the main screen).
        renpy.Keymap( # Creates a keymap to bind a keypress to an action.
            K_BACKQUOTE=lambda: find_my_mouse() # Binds the backquote key (`) to call the 'find_my_mouse' function.
# )
        )
    )