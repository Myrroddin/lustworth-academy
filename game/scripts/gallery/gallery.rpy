#VARIABLES
default alicegallery = False
default antonellagallery = False
default audreygallery = False
default barbaragallery = False
default beatrixgallery = False
default blairgallery = False
default cassidygallery = False
default christygallery = False
default dakotagallery = False
default eunicegallery = False
default fionagallery = False
default kassandragallery = False
default lolagallery = False
default mandygallery = False
default mikugallery = False
default auroragallery = False
default dawsongallery = False
default jonesgallery = False
default punnygallery = False
default jilliangallery = False
default rubygallery = False
default sallygallery = False
default tatianagallery = False
default violetgallery = False
default wendygallery = False


screen gallery():
    tag menu
    ## Esto asegura que cualquier otra pantalla de menu es remplazada.
    window:
        style "mm_root"

    imagemap:
        idle "images/misc/gallery/gallerybackground.webp"
        hover "images/misc/gallery/gallerybackgroundhover.webp"

        # This is so that everything transparent is invisible to the cursor.
        alpha False

        hotspot (1611, 144, 63, 63)  action Return()

        #Alice
        imagebutton:
            if Alice.met == True:
                xalign 0.122
                yalign 0.26
                idle ('images/misc/gallery/girlbuttons/alicebutton.webp')
                hover ('images/misc/gallery/girlbuttons/alicebuttonhover.webp')
                action [SetVariable("alicegallery", True), ShowMenu('alicegallery')]
            else:
                xalign 0.122
                yalign 0.26
                idle ('images/misc/gallery/girlbuttons/lockedbutton.webp')

        #Antonella
        imagebutton:
            if Antonella.met == True:
                xalign 0.215
                yalign 0.26
                idle ('images/misc/gallery/girlbuttons/antonellabutton.webp')
                hover ('images/misc/gallery/girlbuttons/antonellabuttonhover.webp')
                action [SetVariable("antonellagallery", True), ShowMenu('antonellagallery')]
            else:
                xalign 0.215
                yalign 0.26
                idle ('images/misc/gallery/girlbuttons/lockedbutton.webp')

        #Audrey
        imagebutton:
            if Audrey.met == True:
                xalign 0.31
                yalign 0.26
                idle ('images/misc/gallery/girlbuttons/audreybutton.webp')
                hover ('images/misc/gallery/girlbuttons/audreybuttonhover.webp')
                action [SetVariable("audreygallery", True), ShowMenu('audreygallery')]
            else:
                xalign 0.31
                yalign 0.26
                idle ('images/misc/gallery/girlbuttons/lockedbutton.webp')

        #Barbara
        imagebutton:
            if Barbara.met == True:
                xalign 0.40
                yalign 0.26
                idle ('images/misc/gallery/girlbuttons/barbarabutton.webp')
                hover ('images/misc/gallery/girlbuttons/barbarabuttonhover.webp')
                action [SetVariable("barbaragallery", True), ShowMenu('barbaragallery')]
            else:
                xalign 0.40
                yalign 0.26
                idle ('images/misc/gallery/girlbuttons/lockedbutton.webp')

        #Beatrix
        imagebutton:
            if Beatrix.met == True:
                xalign 0.49
                yalign 0.26
                idle ('images/misc/gallery/girlbuttons/beatrixbutton.webp')
                hover ('images/misc/gallery/girlbuttons/beatrixbuttonhover.webp')
                action [SetVariable("beatrixgallery", True), ShowMenu('beatrixgallery')]
            else:
                xalign 0.49
                yalign 0.26
                idle ('images/misc/gallery/girlbuttons/lockedbutton.webp')

        #Blair
        imagebutton:
            if Blair.met == True:
                xalign 0.582
                yalign 0.26
                idle ('images/misc/gallery/girlbuttons/blairbutton.webp')
                hover ('images/misc/gallery/girlbuttons/blairbuttonhover.webp')
                action [SetVariable("blairgallery", True), ShowMenu('blairgallery')]
            else:
                xalign 0.582
                yalign 0.26
                idle ('images/misc/gallery/girlbuttons/lockedbutton.webp')

        #Cassidy
        imagebutton:
            if Cassidy.met == True:
                xalign 0.678
                yalign 0.26
                idle ('images/misc/gallery/girlbuttons/cassidybutton.webp')
                hover ('images/misc/gallery/girlbuttons/cassidybuttonhover.webp')
                action [SetVariable("cassidygallery", True), ShowMenu('cassidygallery')]
            else:
                xalign 0.678
                yalign 0.26
                idle ('images/misc/gallery/girlbuttons/lockedbutton.webp')

        #Christy
        imagebutton:
            if Christy.met == True:
                xalign 0.769
                yalign 0.26
                idle ('images/misc/gallery/girlbuttons/christybutton.webp')
                hover ('images/misc/gallery/girlbuttons/christybuttonhover.webp')
                action [SetVariable("christygallery", True), ShowMenu('christygallery')]
            else:
                xalign 0.769
                yalign 0.26
                idle ('images/misc/gallery/girlbuttons/lockedbutton.webp')

        #Dakota
        imagebutton:
            if Dakota.met == True:
                xalign 0.122
                yalign 0.438
                idle ('images/misc/gallery/girlbuttons/dakotabutton.webp')
                hover ('images/misc/gallery/girlbuttons/dakotabuttonhover.webp')
                action [SetVariable("dakotagallery", True), ShowMenu('dakotagallery')]
            else:
                xalign 0.122
                yalign 0.438
                idle ('images/misc/gallery/girlbuttons/lockedbutton.webp')

        #Eunice
        imagebutton:
            if Eunice.met == True:
                xalign 0.215
                yalign 0.438
                idle ('images/misc/gallery/girlbuttons/eunicebutton.webp')
                hover ('images/misc/gallery/girlbuttons/eunicebuttonhover.webp')
                action [SetVariable("eunicegallery", True), ShowMenu('eunicegallery')]
            else:
                xalign 0.215
                yalign 0.438
                idle ('images/misc/gallery/girlbuttons/lockedbutton.webp')

        #Fiona
        imagebutton:
            if Fiona.met == True:
                xalign 0.31
                yalign 0.438
                idle ('images/misc/gallery/girlbuttons/fionabutton.webp')
                hover ('images/misc/gallery/girlbuttons/fionabuttonhover.webp')
                action [SetVariable("fionagallery", True), ShowMenu('fionagallery')]
            else:
                xalign 0.31
                yalign 0.438
                idle ('images/misc/gallery/girlbuttons/lockedbutton.webp')

        #Kassandra
        imagebutton:
            if Kassandra.met == True:
                xalign 0.40
                yalign 0.438
                idle ('images/misc/gallery/girlbuttons/kassandrabutton.webp')
                hover ('images/misc/gallery/girlbuttons/kassandrabuttonhover.webp')
                action [SetVariable("kassandragallery", True), ShowMenu('kassandragallery')]
            else:
                xalign 0.40
                yalign 0.438
                idle ('images/misc/gallery/girlbuttons/lockedbutton.webp')

        #Lola
        imagebutton:
            if Lola.met == True:
                xalign 0.49
                yalign 0.438
                idle ('images/misc/gallery/girlbuttons/lolabutton.webp')
                hover ('images/misc/gallery/girlbuttons/lolabuttonhover.webp')
                action [SetVariable("lolagallery", True), ShowMenu('lolagallery')]
            else:
                xalign 0.49
                yalign 0.438
                idle ('images/misc/gallery/girlbuttons/lockedbutton.webp')

        #Mandy
        imagebutton:
            if Mandy.met == True:
                xalign 0.582
                yalign 0.438
                idle ('images/misc/gallery/girlbuttons/mandybutton.webp')
                hover ('images/misc/gallery/girlbuttons/mandybuttonhover.webp')
                action [SetVariable("mandygallery", True), ShowMenu('mandygallery')]
            else:
                xalign 0.582
                yalign 0.438
                idle ('images/misc/gallery/girlbuttons/lockedbutton.webp')

        #Miku
        imagebutton:
            if Miku.met == True:
                xalign 0.678
                yalign 0.438
                idle ('images/misc/gallery/girlbuttons/mikubutton.webp')
                hover ('images/misc/gallery/girlbuttons/mikubuttonhover.webp')
                action [SetVariable("mikugallery", True), ShowMenu('mikugallery')]
            else:
                xalign 0.678
                yalign 0.438
                idle ('images/misc/gallery/girlbuttons/lockedbutton.webp')

        #Aurora
        imagebutton:
            if Aurora.met == True:
                xalign 0.769
                yalign 0.438
                idle ('images/misc/gallery/girlbuttons/aurorabutton.webp')
                hover ('images/misc/gallery/girlbuttons/aurorabuttonhover.webp')
                action [SetVariable("auroragallery", True), ShowMenu('auroragallery')]
            else:
                xalign 0.769
                yalign 0.438
                idle ('images/misc/gallery/girlbuttons/lockedbutton.webp')

        #Dawson
        imagebutton:
            if Dawson.met == True:
                xalign 0.122
                yalign 0.605
                idle ('images/misc/gallery/girlbuttons/dawsonbutton.webp')
                hover ('images/misc/gallery/girlbuttons/dawsonbuttonhover.webp')
                action [SetVariable("dawsongallery", True), ShowMenu('dawsongallery')]
            else:
                xalign 0.122
                yalign 0.605
                idle ('images/misc/gallery/girlbuttons/lockedbutton.webp')

        #Jones
        imagebutton:
            if Jones.met == True:
                xalign 0.215
                yalign 0.605
                idle ('images/misc/gallery/girlbuttons/jonesbutton.webp')
                hover ('images/misc/gallery/girlbuttons/jonesbuttonhover.webp')
                action [SetVariable("jonesgallery", True), ShowMenu('jonesgallery')]
            else:
                xalign 0.215
                yalign 0.605
                idle ('images/misc/gallery/girlbuttons/lockedbutton.webp')

        #Punny
        imagebutton:
            if Punny.met == True:
                xalign 0.31
                yalign 0.605
                idle ('images/misc/gallery/girlbuttons/punnybutton.webp')
                hover ('images/misc/gallery/girlbuttons/punnybuttonhover.webp')
                action [SetVariable("punnygallery", True), ShowMenu('punnygallery')]
            else:
                xalign 0.31
                yalign 0.605
                idle ('images/misc/gallery/girlbuttons/lockedbutton.webp')

        #Jillian
        imagebutton:
            if Jill.met == True:
                xalign 0.40
                yalign 0.605
                idle ('images/misc/gallery/girlbuttons/jillbutton.webp')
                hover ('images/misc/gallery/girlbuttons/jillbuttonhover.webp')
                action [SetVariable("jilliangallery", True), ShowMenu('jilliangallery')]
            else:
                xalign 0.40
                yalign 0.605
                idle ('images/misc/gallery/girlbuttons/lockedbutton.webp')

        #Ruby
        imagebutton:
            if Ruby.met == True:
                xalign 0.49
                yalign 0.605
                idle ('images/misc/gallery/girlbuttons/rubybutton.webp')
                hover ('images/misc/gallery/girlbuttons/rubybuttonhover.webp')
                action [SetVariable("rubygallery", True), ShowMenu('rubygallery')]
            else:
                xalign 0.49
                yalign 0.605
                idle ('images/misc/gallery/girlbuttons/lockedbutton.webp')

        #Sally
        imagebutton:
            if Sally.met == True:
                xalign 0.582
                yalign 0.605
                idle ('images/misc/gallery/girlbuttons/sallybutton.webp')
                hover ('images/misc/gallery/girlbuttons/sallybuttonhover.webp')
                action [SetVariable("sallygallery", True), ShowMenu('sallygallery')]
            else:
                xalign 0.582
                yalign 0.605
                idle ('images/misc/gallery/girlbuttons/lockedbutton.webp')

        #Tatiana
        imagebutton:
            if Tatiana.met == True:
                xalign 0.678
                yalign 0.605
                idle ('images/misc/gallery/girlbuttons/tatianabutton.webp')
                hover ('images/misc/gallery/girlbuttons/tatianabuttonhover.webp')
                action [SetVariable("tatianagallery", True), ShowMenu('tatianagallery')]
            else:
                xalign 0.678
                yalign 0.605
                idle ('images/misc/gallery/girlbuttons/lockedbutton.webp')

        #Violet
        imagebutton:
            if Violet.met == True:
                xalign 0.769
                yalign 0.605
                idle ('images/misc/gallery/girlbuttons/violetbutton.webp')
                hover ('images/misc/gallery/girlbuttons/violetbuttonhover.webp')
                action [SetVariable("violetgallery", True), ShowMenu('violetgallery')]
            else:
                xalign 0.769
                yalign 0.605
                idle ('images/misc/gallery/girlbuttons/lockedbutton.webp')

        #Wendy
        imagebutton:
            if prologue.firstNight == True:
                xalign 0.122
                yalign 0.775
                idle ('images/misc/gallery/girlbuttons/wendybutton.webp')
                hover ('images/misc/gallery/girlbuttons/wendybuttonhover.webp')
                action [SetVariable("wendygallery", True), ShowMenu('wendygallery')]
            else:
                xalign 0.122
                yalign 0.775
                idle ('images/misc/gallery/girlbuttons/lockedbutton.webp')
