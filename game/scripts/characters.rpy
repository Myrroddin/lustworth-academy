init offset = -1

init python:
    class LustworthCharacter:
        def __init__(self, name, key, color=Color('#fff'), **kwargs):
            self.name = name
            self.color = color
            self.key = key
            self.char = Character(name, color=color, **kwargs)
            self.met = False
            self.eventMet = {
                HALLOWEEN_EVENT: False,
                CHRISTMAS_EVENT: False,
                SPRINGBREAK_EVENT: False
            }
            # Only used by romanceable characters
            self.relPoints = 0

        def _show(self, image):
            # Don't show if not already showing
            if not renpy.showing(self.key):
                return
            # Custom attribute handling
            attrs = renpy.game.context().say_attributes
            if attrs is not None:
                renpy.show(image + ' ' + ' '.join(attrs))
                # Apply transition
                transitions = renpy.game.interface.transition
                transition = transitions.pop(None, dissolve)
                renpy.with_statement(transition)
                # Clear attributes
                renpy.game.context().say_attributes = None

        def _say(self, *args, **kwargs):
            self.char(*args, **kwargs)

        def __call__(self, *args, **kwargs):
            # Show
            self._show(self.key)
            # Say
            self.char.name = self.name if galleryMode or self.met else '???'
            self._say(*args, **kwargs)

    class MainCharacter(LustworthCharacter):
        def __init__(self, name, **kwargs):
            LustworthCharacter.__init__(self, name, 'jimmy', **kwargs)
            self.outfit = JIMMY_DEFAULT
            self.money = 0
            self.stats = {
                'guts':     1,
                'wits':   1,
                'endurance':    1,
                'charisma':     1,
            }
            # TODO: implement a proper inventory system
            self.inventory = []

        def hasItem(self, item):
            for i in self.inventory:
                if i.name == item.name:
                    return True
            return False

        def __call__(self, *args, **kwargs):
            self._show(self.key + ' ' + self.outfit)
            self._say(*args, **kwargs)

# Jimmy
default Jimmy = MainCharacter("[player_name]", color='#3D88D8')
image jimmy neutral        = 'jimmy [Jimmy.outfit] neutral'
image jimmy talk           = 'jimmy [Jimmy.outfit] talk'
image jimmy smug           = 'jimmy [Jimmy.outfit] smug'
image jimmy suspicious     = 'jimmy [Jimmy.outfit] suspicious'
image jimmy suspicious arm = 'jimmy [Jimmy.outfit] suspicious arm'
image jimmy leave          = 'jimmy [Jimmy.outfit] leaving'
image jimmy unamused       = 'jimmy [Jimmy.outfit] unamused'
image jimmy unamused arm   = 'jimmy [Jimmy.outfit] unamused arm'

# Romanceable characters
## Clique girls - main
default Beatrix   = LustworthCharacter("Beatrix", key='beatrix', color='#6CC14B')
default Violet    = LustworthCharacter("Violet", key='violet', color='#D333B5')
default Lola      = LustworthCharacter("Lola", key='lola', color='#B01E34')
default Mandy     = LustworthCharacter("Mandy", key='mandy', color='#5598F4')
## Clique girls - secondary
default Miku      = LustworthCharacter("Miku", key='miku', color='#B6DF55')
default Eunice    = LustworthCharacter("Eunice", key='eunice', color='#EF4646')
default Tatiana   = LustworthCharacter("Tatiana", key='tatiana', color='#AA2844')
default Christy   = LustworthCharacter("Christy", key='christy', color='#EE5949')
default Ruby      = LustworthCharacter("Ruby", key='ruby', color='#EA61AE')
default Serenity  = LustworthCharacter("Serenity", key='serenity', color='#eba83b')
## Teachers & staff
default Dawson    = LustworthCharacter("Ms. Dawson", key='missdawson', color='#BB3D39')
default Punny     = LustworthCharacter("Ms. Punny", key='misspunny', color='#e33849')
default Jones     = LustworthCharacter("Ms. Jones", key='missjones', color='#79DF55')
default Aurora    = LustworthCharacter("Ms. Bakshi", key='aurora', color='#f17d2a')
default Audrey    = LustworthCharacter("Audrey", key='audrey', color='#4DBAF0')
default White     = LustworthCharacter("Mr. White", key='white', color='#27E79E')
default Marlon    = LustworthCharacter("Marlon", key='marlon', color='#63D839')
default Edna      = LustworthCharacter("Edna", key='edna', color='#e9b53d')
default Vanessa   = LustworthCharacter("Vanessa", key='vanessa', color='#ec66d6')
## Other
default Fiona     = LustworthCharacter("Fiona", key='fiona', color='#A565F2')
default Wendy     = LustworthCharacter("Wendy", key='wendy', color='#F0594D')
default Kassandra = LustworthCharacter("Kassandra", key='kassandra', color='#E165B2')
default Cassidy   = LustworthCharacter("Cassidy", key='cassidy', color='#E0CB1D')
default Blair     = LustworthCharacter("Blair", key='blair', color='#63D839')
default Alice    = LustworthCharacter("Alice", key='alice', color='#EA6363')
default Jill      = LustworthCharacter("Officer Jillian", key='jill', color='#3FC5E4')
default Dakota    = LustworthCharacter("Dakota", key='dakota', color='#1EDFE8')
default Barbara   = LustworthCharacter("Barbara", key='barbara', color='#EFC046')
default Sally     = LustworthCharacter("Sally", key='sally', color='#EF4646')
default Antonella = LustworthCharacter("Antonella", key='antonella', color='#E8D61E')
default Izumi     = LustworthCharacter("Izumi", key='izumi', color='#B01E34')
default Jake      = LustworthCharacter("Jake", key='jake', color='#569722')
## Voragor
default Sage     = LustworthCharacter("Old Sage", key='sage', color='#EA6363')
default Pascal    = LustworthCharacter("Pascal", key='pascal', color='#63D839')

init python:
    def get_girls():
        return [
            Alice, Antonella, Audrey, Barbara, Beatrix, Blair,
            Cassidy, Christy, Dakota, Eunice, Fiona, Kassandra,
            Lola, Mandy, Miku, Aurora, Dawson, Jones, Punny,
            Jill, Ruby, Sally, Tatiana, Violet, Wendy
        ]

# Supporting characters
## Students
default Pete       = LustworthCharacter("Pete", key='pete', color='#F45597')
default Gary       = LustworthCharacter("Gary", key='gary', color='#45C05B')
default Derby      = LustworthCharacter("Derby", key='derby', color='#569591')
## Teachers & staff
default Stapleneck = LustworthCharacter("Dr. Stapleneck", key='stapleneck', color='#83673A')
default Camembert  = LustworthCharacter("Mr. Camembert", key='camembert', color='#6158D9')
default Toord      = LustworthCharacter("Mr. Toord", key='toord', color='#E54B4B')
default Dewey      = LustworthCharacter("Mr. S", key='dewey', color='#EC4040')
default DrLed      = LustworthCharacter("Dr. Led", key='drled', color='#55DFAF')
default Clarissa   = LustworthCharacter("Clarissa", key='clarissa', color='#55cadf')
#default Neil       = Character("Neil",           color='#6158D9')
default Argon      = LustworthCharacter("Dr. Argon", key='argon', color='#FFFFFF')
default Dyson      = LustworthCharacter("Mr. Dyson", key='dyson', color='#FFFFFF')
## Nerd Clique
default Algie     = LustworthCharacter("Algie", key='algie', color='#D8BE51')
default Earnest   = LustworthCharacter("Earnest", key='earnest', color='#5CCB5B')
default Melvin    = LustworthCharacter("Melvin", key='melvin', color='#DD94DF')
default Bucky     = LustworthCharacter("Bucky", key='bucky', color='#5CCB5B')
##Bully Clique
default Derek      = LustworthCharacter("Derek", key='derek', color='#aee6df')
default Russell      = LustworthCharacter("Russell", key='russell', color='#d1ebe8')
## Other
default Donaguy    = LustworthCharacter("Mayor Donaguy", key='donaguy', color='#539A47')
default Grant      = LustworthCharacter("Grant the Hobo", key='grant', color='#63D839')
default Matunga   = LustworthCharacter("Matunga", key='matunga', color='#50c7cb')
## Secret girls
default Angie     = Character("Angie", color='#38CF71')
default Ivana     = Character("Ivana", color='#63EA9A')
default Claire    = Character("Claire", color='#E43F50')
default Tatsumaki = Character("Tatsumaki", color='#1EE870')
default Jinx      = Character("Jinx", color= '#D63CF1')
## Misc.
default Dad        = Character("Dad", color='#68A657')
default dSanta      = Character("Dear Santa", color='#e33636')
default Thad       = Character("Thad", color='#54D654')
default Unk        = Character("Unknown", color='#FFFFFF')
default Developer  = Character("Developer", color='#AE4DEE')

#DAYLIMITVARIABLES
default AliceDaylimit = False
default AntonellaDaylimit = False
default AudreyDaylimit = False
default FionaDaylimit = False
default WorkDaylimit = False
default PunnyDaylimit = False
default MikuDaylimit = False
default EuniceDaylimit = False
default BeatrixDaylimit = False
default ChristyDaylimit = False
default BlairDaylimit = False
default CassidyDaylimit = False
default SallyDaylimit = False
default RubyDaylimit = False
default TatianaDaylimit = False
default VioletDaylimit = False
default WendyDaylimit = False
default JillianDaylimit = False
default LolaDaylimit = False
default MandyDaylimit = False
default DawsonDaylimit = False
default JonesDaylimit = False
default BarbaraDaylimit = False
default ClarissaDaylimit = False
default DakotaDaylimit = False
default SerenityDaylimit = False
default KassandraDaylimit = False
