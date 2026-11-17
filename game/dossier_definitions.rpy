init -1 python:
    from dataclasses import dataclass

    @dataclass
    class Evidence:
        name: str
        image: str
        desc_short: str
        desc_long: str

    @dataclass
    class CharacterProfile:
        name: str
        image: str
        desc_short: str
        desc_long: str
    
    @dataclass
    class MapData:
        name: str
        image: str
        desc: str

    class Dossier:
        def __init__(self):
            self.items = []

        def add(self, item):
            if item not in self.items:
                renpy.notify(_("Dossier has been updated.") + " " + item.name + " " + _("was discovered.") )
                self.items.append(item)
            else:
                renpy.notify(_("It's already in the dossier."))

        def remove(self, index):
            self.items.pop(index)

        def remove_by_name(self, name):
            for i, it in enumerate(self.items):
                if it.name == name:
                    self.items.pop(i)
                    return
            # optional: raise or return False if not found

        def get(self, index):
            return self.items[index]

        def find(self, name):
            for it in self.items:
                if it.name == name:
                    return it
            return None

        def has(self, name):
            return any(it.name == name for it in self.items)

        def __len__(self):
            return len(self.items)

        def __iter__(self):
            return iter(self.items)   


    class Dossier_dict:
        def __init__(self):
            self.items = {}

        def add(self, key, item):
            self.items[key] = item

        def remove(self, key):
            del self.items[key]

        def get(self, key):
            return self.items.get(key)


default dossier = Dossier()   

# ============================

define mp_grandstands = MapData(
    _("Main Racetrack"),
    "placeholder_granstands",  # Image file
    _("Grandstands are also known as Main Race Tracks.")
)

define mp_breakroom = MapData(
    _("Staff Break Room"),
    "placeholder_breakroom",  # Image file
    _("Here the staff eats lunch and does other things.")
)

define mp_corridor = MapData(
    _("Staff Service Corridor"),
    "test fence",  # Image file
    _("This is a suspicious corridor.")
)

define mp_paddock = MapData(
    _("Parade Ring"),
    "placeholder_paddock",  # Image file
    _("The Parade Ring is also known as Paddock.")
)


define mp_stables = MapData(
    _("Stables"),
    "placeholder_stables",  # Image file
    _("Horses can be found in here.")
)


define mp_lockers = MapData(
    _("Jockeys Locker Room"),
    "placeholder_lockers",  # Image file
    _("All sorts of items belonging to the Jockeys can be found in here.")
)


# ============================

define de_mate = Evidence(
    _("Mate"),
    "mate-transparent", # Image file
    _("This mate is passed down the generations."),
_("""Etiam lobortis nulla odio, non bibendum felis suscipit non. Duis erat nibh, feugiat viverra porta vel, luctus vel orci. Donec maximus porttitor tempus. Etiam metus nunc, blandit vel nisl sed.
""")
)

define de_mask = Evidence(
    _("Mask"),
    "evidence-mask-transparent", # Image file
    _("Personal possessions."),
_("""The mask I use to conceal my identity when fighting crime.""")
)

define de_medicalreport = Evidence(
    _("Medical Report"),
    "evidence-med-report",  # Image file
    _("Obtained from Inspector Medina."),
    _("Horse feels ill from bad drugs.")
                        
)

define de_victimnotes = Evidence(
    _("Victim's Notes"),
    "evidence-victim-notes",  # Image file
    _("Notes taken by Antonio."),
    _("Body discovery: 10:42 AM\nA large wound is visible on the back of the head, while multiple bruises cover the face and front of the body.\nThe arms rest limply at the victim's sides, with no apparent injuries to the hands or forearms. Both legs appear to be broken.")
                        
)

define de_shovel = Evidence(
    _("Bloodstained Shovel"),
    "evidence-shovel",
    _("Found at the stables"),
    _("A heavy iron shovel normally used for stable work, such as mucking out stalls and moving feed. Its flat blade is smeared with dried blood and traces of hair, with a noticeable dent along its edge.")
)

define de_blooddrops = Evidence(
    _("Dried Bloodstains"),
    "evidence-blood-drops",
    _("Found inside the stables"),
    _("A trail of dried blood drops. It leads from a small pool of blood towards the entrance, where it abruptly ends. The pool of blood has been covered with loose hay.")
)

define de_bodybag = Evidence(
    _("Black Body Bag"),
    "evidence-body-bag",
    _("Found in the staff break room"),
    _("A large black plastic body bag, capable of holding an adult-sized person. It was stuffed inside a trash bin and hastily covered with other discarded rubbish. Its interior is heavily stained with dried blood.")
)

define de_callrecords = Evidence(
    _("Call Records"),
    "evidence-call-records",
    _("Obtained from the phone provider"),
    _("Records of a phone call between Esteban and Renata.")
)

define de_casualclothes = Evidence(
    _("Casual Clothing"),
    "evidence-casual-clothes",
    _("Found in Lucas's locker"),
    _("A colorful Hawaiian shirt, a pair of beige trousers, dark aviator sunglasses, and casual shoes.")
)

define de_notebook = Evidence(
    _("Notebook"),
    "evidence-notebook",
    _("Found in Lucas's locker"),
    _("""A small, black, leather-bound notebook with worn corners and yellowed pages. It contains handwritten entries listing race dates, horse names, and monetary values. Most entries are checked off, except for the last one.
    \n Relámpago - $3,000
    \n Merluza Pelusa - $4,000
    \n Perla Negra $7,000
    \n Lucero $5,000""")
)

define de_autopsy = Evidence(
    _("Autopsy Report"),
    "evidence-autopsy",
    _("Obtained from the police"),
    _("Victim: Vicente [SURNAME]\n\
    Estimated Time of Death: [TIME]\n\
    Cause of Death: Severe blunt force trauma to the back of the head.\n\
    \n\
    Findings:\n\
    - Severe blunt force trauma to the back of the head.\n\
    - Multiple bruises across the face and front of the body.\n\
    - Both legs fractured.\n\
    - No apparent injuries to the hands or forearms.\n")
)

define de_screen = Evidence(
    _("Screen"),
    "screen",  # Image file
    _("Just an ordinary screen showing a test pattern."),
    _("No, Monika won't come out of it, no matter how much you stare at it.")
)

define dp_tony = CharacterProfile(
    _("Antonio Ortiz"),
    "side tony smile",  # Image file
    _("Age: 22"),
    _("Me. Part-time private investigator and handyman; full-time ally of justice.")
)
define dp_leo = CharacterProfile(
    _("El Leopardo"),
    "side leo grin shine",  # Image file
    _("The Leopard man always carries a mate!"),
    _("Here comes the Leopard man to the rescue! After that he will treat you to his mate!")
)