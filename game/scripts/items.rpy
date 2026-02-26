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

define ItemCassidyDildo     = Item(__("Cassidy's dildo"),       'cassidysdildo_sprite',     descr=__("Cassidy's dildo. If I give it to her, she should leave me alone and I can sneak out."))
define ItemGrantsBag        = Item(__("Grant's bag"),           'grantsbag_sprite',         descr=__("Grant's bag. It's slimy, and it smells. I should give this back to him as soon as possible."))
define ItemBlairUsb         = Item(__("USB drive"),             'blairsusb_sprite',         descr=__("My USB stick. I can use it to finish setting up my PC."))
define ItemFionaPadlock     = Item(__("Fiona's padlock"),       'fionaspadlock_sprite',     descr=__("Fiona's padlock. I should return it to her."))
define ItemBeatrixDiary     = Item(__("Beatrix's diary"),       'beatrixsdiary_sprite',     descr=__("Beatrix's diary. Full of fantasies about her and her furry friend, Trevor."))
define ItemEuniceChocolates = Item(__("Eunice's chocolates"),   'euniceschocolates_sprite', descr=__("Eunice's chocolates. Derek already ate a few, I hope she doesn't mind."))
define ItemPolaroidCamera   = Item(__("Polaroid camera"),       'polaroidcameraitem',       price=150, descr=__("A Polaroid camera. Cool instant photos for everyone."))
define ItemShaggyCostume    = Item(__("Shaggy costume"),        'shaggycostumeitem',        price=50,  descr=__("A Shaggy costume. I can wear it to the Halloween party."))
define ItemPirateCostume    = Item(__("Pirate costume"),        'piratecostumeitem',        price=200,  descr=__("A Pirate costume. I can wear it to the Halloween party."))
define ItemHeroCostume      = Item(__("Superhero costume"),     'homelandercostumeitem',    price=500,  descr=__("A Superhero costume. I can wear it to the Halloween party."))
define ItemAppleCider       = Item(__("Apple juice"),           'applecider_sprite',        descr=__("I think it's apple juice. This should do for Beatrix."))
define ItemVoltium          = Item(__("Voltium"),               'voltium_sprite',           descr=__("Voltium, I guess. I should bring it to Mandy and Christy at the pool."))
define ItemFakeFlag         = Item(__("Fake Flag"),             'fakeflag_sprite',          descr=__("I have to replace the preps' flag on the roof with this one."))
define ItemSprayCan         = Item(__("Spray Can"),             'spraycan_sprite',          descr=__("Gotta leave a message of some kind. I'm not sure where's the best spot to do that."))
define ItemDermatitisCream  = Item(__("Dermititis Cream"),      'herpescream_sprite',       descr=__("A treatment for facial dermatitis. Beatrix needs this."))
define ItemDogManure        = Item(__("Dog Manure"),            'dogmanure_sprite',         descr=__("Pete says I can make Derby leave his room with this."))
define ItemAlgieScroll      = Item(__("Algie Scroll"),          'algiescroll_sprite',       descr=__("This is the scroll Algie asked me to fetch for him."))
define ItemHeadmasterKey    = Item(__("Headmaster Key"),        'headmasterkey_sprite',     descr=__("The key to the Headmaster's office. I wonder what Fiona is planning to do with this?"))
define ItemShapedBranch     = Item(__("Shaped Branch"),         'shapedbranch_sprite',      descr=__("It's a small branch, perfectly shaped for a slingshot."))
define ItemRubberBand       = Item(__("Rubber Band"),           'rubberband_sprite',        descr=__("It's a rubber band, and seems to be perfect for a slingshot."))
define ItemStonesAmmo       = Item(__("Stones Ammo"),           'stonesammo_sprite',        descr=__("These little stones are ideal to be fired with a slingshot."))
define ItemSlingshot        = Item(__("Slingshot"),             'slingshot_sprite',         descr=__("The only one I trust."))
define ItemArtBook01        = Item(__("Art book"),              'artbook1_sprite',          descr=__("It's the art book I need to deliver to the Art Class teacher."))
define ItemMemos01          = Item(__("Miss Dawson Memos"),     'memos01_sprite',           descr=__("This is one of the memos I need to deliver to the Cafeteria manager or the Concierge"))
define ItemMemos02          = Item(__("Miss Dawson Memo"),      'memos02_sprite',           descr=__("This is one of the memos I need to deliver to the Cafeteria manager or the Concierge"))
define ItemPartyInvitation  = Item(__("Halloween Party Invitation"), 'partyinvitation_sprite', descr=__("This is an invitation for the Halloween party at the Harrison House"))
define ItemDonutBox         = Item(__("Donut Box"),             'donutbox_sprite',          descr=__("These are Fiona's lost donuts."))
define ItemGrapeWine        = Item(__("Grape Wine"),            'grapewine_sprite',         descr=__("This is the wine I recovered for Fiona."))
define ItemIceBag           = Item(__("Ice Bag"),               'icebag_sprite',            descr=__("A small bag of ice."))
define ItemMoneyFound01     = Item(__("Money!"),                'money01_sprite',           descr=__("Some money I found somewhere in the street."))
define ItemArtBook02        = Item(__("Eunice Book"),            'artbook2_sprite',          descr=__("I believe this is the book Eunice ask me to fetch for her."))
define ItemArtBook03        = Item(__("Eunice Book 2"),            'artbook3_sprite',          descr=__("Maybe this is the book Eunice ask me to fetch for her."))
define ItemArtBook04        = Item(__("Eunice Book 3"),            'artbook4_sprite',          descr=__("Is this the book Eunice ask me to fetch for her?"))
define ItemArtBook05        = Item(__("Eunice Book 4"),            'artbook5_sprite',          descr=__("This has to be the book Eunice ask me to fetch for her."))
define ItemCrownofGods      = Item(__("Crown of The Gods"),         'crowngods_sprite',        descr=__("You can feel the power emanating from this artifact... Nah, it's just a fancy piece of can."))
