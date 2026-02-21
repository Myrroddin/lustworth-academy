screen schoolminimap:
    zorder 100
    imagemap:
        ground "schoolminimapfall"
        hover "schoolminimapfallhover"

        hotspot (70, 40, 236, 236)    clicked Hide(), Return()
        hotspot (84, 806, 272, 214)   clicked Jump('schoolminimap_jimmysroom')
        hotspot (438, 294, 220, 220)  clicked Jump('schoolminimap_boysdorm')
        hotspot (736, 473, 220, 219)  clicked Jump('schoolminimap_mainbuilding')
        hotspot (1442, 350, 220, 221) clicked Jump('schoolminimap_gym')
        hotspot (1268, 729, 220, 219) clicked Jump('schoolminimap_garage')
        hotspot (810, 219, 221, 222)  clicked Jump('schoolminimap_library')

label schoolminimap_jimmysroom:
    $ gotoscene('boysdormjimmysroom')

label schoolminimap_boysdorm:
    $ gotoscene('boysdormtvroom')

label schoolminimap_mainbuilding:
    $ gotoscene('mainbuildingentrance')

label schoolminimap_gym:
    $ gotoscene('schoolgym')

label schoolminimap_garage:
    $ gotoscene('schoolgarage')

label schoolminimap_library:
    $ gotoscene('schoollibrarymainhall')
