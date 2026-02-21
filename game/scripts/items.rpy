init python:
    class Item:
        def __init__(self, name, image, descr=None, price=0):
            self.name = name
            self.image = image
            self.descr = descr
            self.price = price

        def __eq__(self, other):
            if isinstance(other, Item):
                return self.name == other.name
            return NotImplemented

define ItemCassidyDildo     = Item("Cassidy's dildo",       'cassidysdildo_sprite',     descr="Cassidy's dildo. If I give it to her, she should leave me alone and I can sneak out.")
define ItemGrantsBag        = Item("Grant's bag",           'grantsbag_sprite',         descr="Grant's bag. It's slimy, and it smells. I should give this back to him as soon as possible.")
define ItemBlairUsb         = Item("USB drive",             'blairsusb_sprite',         descr="My USB stick. I can use it to finish setting up my PC.")
define ItemFionaPadlock     = Item("Fiona's padlock",       'fionaspadlock_sprite',     descr="Fiona's padlock. I should return it to her.")
define ItemBeatrixDiary     = Item("Beatrix's diary",       'beatrixsdiary_sprite',     descr="Beatrix's diary. Full of fantasies about her and her furry friend, Trevor.")
define ItemEuniceChocolates = Item("Eunice's chocolates",   'euniceschocolates_sprite', descr="Eunice's chocolates. Derek already ate a few, I hope she doesn't mind.")
define ItemPolaroidCamera   = Item("Polaroid camera",       'polaroidcameraitem',       price=150, descr="A Polaroid camera. Cool instant photos for everyone.")
define ItemShaggyCostume    = Item("Shaggy costume",        'shaggycostumeitem',        price=50,  descr="A Shaggy costume. I can wear it to the Halloween party.")
define ItemPirateCostume    = Item("Pirate costume",        'piratecostumeitem',        price=200,  descr="A Pirate costume. I can wear it to the Halloween party.")
define ItemHeroCostume      = Item("Superhero costume",     'homelandercostumeitem',    price=500,  descr="A Superhero costume. I can wear it to the Halloween party.")
define ItemAppleCider       = Item("Apple juice",           'applecider_sprite',        descr="I think it's apple juice. This should do for Beatrix.")
define ItemVoltium          = Item("Voltium",               'voltium_sprite',           descr="Voltium, I guess. I should bring it to Mandy and Christy at the pool.")
define ItemFakeFlag         = Item("Fake Flag",             'fakeflag_sprite',          descr="I have to replace the preps' flag on the roof with this one.")
define ItemSprayCan         = Item("Spray Can",             'spraycan_sprite',          descr="Gotta leave a message of some kind. I'm not sure where's the best spot to do that.")
define ItemDermatitisCream  = Item("Dermititis Cream",      'herpescream_sprite',       descr="A treatment for facial dermatitis. Beatrix needs this.")
define ItemDogManure        = Item("Dog Manure",            'dogmanure_sprite',         descr="Pete says I can make Derby leave his room with this.")
define ItemAlgieScroll      = Item("Algie Scroll",          'algiescroll_sprite',       descr="This is the scroll Algie asked me to fetch for him.")
define ItemHeadmasterKey    = Item("Headmaster Key",        'headmasterkey_sprite',     descr="The key to the Headmaster's office. I wonder what Fiona is planning to do with this?")
define ItemShapedBranch     = Item("Shaped Branch",         'shapedbranch_sprite',      descr="It's a small branch, perfectly shaped for a slingshot.")
define ItemRubberBand       = Item("Rubber Band",           'rubberband_sprite',        descr="It's a rubber band, and seems to be perfect for a slingshot.")
define ItemStonesAmmo       = Item("Stones Ammo",           'stonesammo_sprite',        descr="These little stones are ideal to be fired with a slingshot.")
define ItemSlingshot        = Item("Slingshot",             'slingshot_sprite',         descr="The only one I trust.")
define ItemArtBook01        = Item("Art book",              'artbook1_sprite',          descr="It's the art book I need to deliver to the Art Class teacher.")
define ItemMemos01          = Item("Miss Dawson Memos",     'memos01_sprite',           descr="This is one of the memos I need to deliver to the Cafeteria manager or the Concierge")
define ItemMemos02          = Item("Miss Dawson Memo",      'memos02_sprite',           descr="This is one of the memos I need to deliver to the Cafeteria manager or the Concierge")
define ItemPartyInvitation  = Item("Halloween Party Invitation", 'partyinvitation_sprite', descr="This is an invitation for the Halloween party at the Harrison House")
define ItemDonutBox         = Item("Donut Box",             'donutbox_sprite',          descr="These are Fiona's lost donuts.")
define ItemGrapeWine        = Item("Grape Wine",            'grapewine_sprite',         descr="This is the wine I recovered for Fiona.")
define ItemIceBag           = Item("Ice Bag",               'icebag_sprite',            descr="A small bag of ice.")
define ItemMoneyFound01     = Item("Money!",                'money01_sprite',           descr="Some money I found somewhere in the street.")
define ItemArtBook02        = Item("Eunice Book",            'artbook2_sprite',          descr="I believe this is the book Eunice ask me to fetch for her.")
define ItemArtBook03        = Item("Eunice Book 2",            'artbook3_sprite',          descr="Maybe this is the book Eunice ask me to fetch for her.")
define ItemArtBook04        = Item("Eunice Book 3",            'artbook4_sprite',          descr="Is this the book Eunice ask me to fetch for her?")
define ItemArtBook05        = Item("Eunice Book 4",            'artbook5_sprite',          descr="This has to be the book Eunice ask me to fetch for her.")
define ItemCrownofGods      = Item("Crown of The Gods",         'crowngods_sprite',        descr="You can feel the power emanating from this artifact... Nah, it's just a fancy piece of can.")