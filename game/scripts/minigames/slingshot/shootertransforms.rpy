# transform alpha(a):
transform alpha(a): # Defines a transform named 'alpha' that takes an argument 'a' (alpha value, 0.0 to 1.0).
    alpha a # Sets the displayable's opacity.
transform rotate(r): # Defines a transform named 'rotate' that takes an argument 'r' (angle in degrees).
    rotate_pad False # Disables extra padding Ren'Py adds for rotation.
    rotate r # Rotates the displayable by 'r' degrees.
transform zoom(z, n=False): # Defines a transform named 'zoom' that takes an overall scale factor 'z' and an optional boolean 'n' for nearest-neighbor scaling.
    nearest n # Sets nearest-neighbor scaling if 'n' is True (good for pixel art).
    zoom z # Sets the overall scale factor.
transform flip(x=1, y=1, n=False): # Defines a transform named 'flip' that takes x/y zoom factors (to flip) and an optional nearest-neighbor flag.
    nearest n # Sets nearest-neighbor scaling.
    xzoom x yzoom y # Sets the horizontal ('x') and vertical ('y') scale factors. Use -1 to flip an axis.
transform additive(a): # Defines a transform named 'additive' that takes an argument 'a' (additive value).
    additive a # Sets the additive blend factor (makes it glow or brighter).

# spin

#





