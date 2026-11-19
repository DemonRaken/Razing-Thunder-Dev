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
    _("A massive seating area where spectators gather to watch the races.")
)

define mp_breakroom = MapData(
    _("Staff Break Room"),
    "placeholder_breakroom",  # Image file
    _("A resting area where the Derby's staff can take a break between their duties, eat lunch and do other things.")
)

define mp_corridor = MapData(
    _("Staff Service Corridor"),
    "test fence",  # Image file
    _("This is a suspicious corridor.")
)

define mp_paddock = MapData(
    _("Parade Ring"),
    "placeholder_paddock",  # Image file
    _("An area where horses are presented before the race, allowing spectators and jockeys to see them up close.")
)


define mp_stables = MapData(
    _("Stables"),
    "placeholder_stables",  # Image file
    _("The facilities where horses are housed, groomed, and prepared for competition.")
)


define mp_lockers = MapData(
    _("Jockeys Locker Room"),
    "placeholder_lockers",  # Image file
    _("A designated area where jockeys can change clothes, store their belongings, and prepare for their races.")
)


# ============================

define de_mate = Evidence(
    _("Mate"),
    "mate-transparent", # Image file
    _("Personal possessions."),
_("""Bitter and ready for the road.
""")
)

define de_mask = Evidence(
    _("Mask"),
    "evidence-mask-transparent", # Image file
    _("Personal possessions."),
_("""The mask I use to conceal my identity when fighting crime.""")
)

define de_medicalreport = Evidence(
    _("Veterinary Medical Report"),
    "evidence-med-report",  # Image file
    _("Obtained from Inspector Medina."),
    _("Examination confirmed acute Halosodrin (Sodrin-HX) poisoning in the affected horses. The substance causes progressive muscular weakness and impaired coordination. Symptoms may remain subtle while the animal is at rest, but strenuous physical activity can rapidly aggravate its effects, resulting in cardiac irregularities and sudden collapse during exertion. No injection marks or evidence of injected substances were found. Traces of Halosodrin were instead detected around the horses' mouths, indicating oral exposure. The compound is a veterinary additive intended for cattle and poultry, but highly toxic to horses.")
                        
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
    _("A trail of dried blood drops. It leads from a small pool of blood towards the stable's entrance, where it abruptly ends. The pool of blood has been covered with loose hay.")
)

define de_bodybag = Evidence(
    _("Body Bag"),
    "evidence-body-bag",
    _("Found in the staff break room"),
    _("A large black plastic body bag, capable of holding an adult-sized person. It was stuffed inside a trash bin and hastily covered with other discarded rubbish. Its interior is heavily stained with dried blood.")
)

define de_callrecords = Evidence(
    _("Renata's Phone"),
    "evidence-call-records",
    _("Obtained from Renata"),
    _("The phone's call log. Its only call from today was from Esteban, at 10:17 AM.")
)

define de_casualclothes = Evidence(
    _("Orange Clothes"),
    "evidence-casual-clothes",
    _("Found in Lucas' locker"),
    _("A colorful Hawaiian shirt, a pair of beige trousers, dark aviator sunglasses, and casual shoes.")
)

define de_notebook = Evidence(
    _("Notebook"),
    "evidence-notebook",
    _("Found in Lucas's locker"),
    _("""A small, notebook with worn corners and pages. It contains handwritten entries listing race dates, horse names, and monetary values. Most entries are checked off, except for the last one.
    \n {s}Relámpago — $3,000 {/s}
    \n {s}Merluza Pelusa — $4,000{/s}
    \n {s}Perla Negra — $7,000{/s}
    \n Lucero — $5,000""")
)

define de_autopsy = Evidence(
    _("Autopsy Report"),
    "evidence-autopsy",
    _("Obtained from the police"),
    _("""{u}Victim{/u}: Vicente Ruiz\n{u}Estimated Time of Death{/u}: 10:17 AM\n{u}Cause of Death{/u}: Severe blunt force trauma to the back of the head.\nSustained multiple bruises across the face and front of the body. Both legs fractured. No apparent injuries to the hands or forearms.""")
)

define de_screen = Evidence(
    _("Screen"),
    "screen",  # Image file
    _("Just an ordinary screen showing a test pattern."),
    _("No, Monika won't come out of it, no matter how much you stare at it.")
)

define de_alibi = Evidence(
    _("Alibi Notes"),
    "evidence-alibi",  # Image file
    _("Notes taken by Antonio."),
    _("Medina, Sebastian and Lorenzo were together at the luxury observatory from 10:00 AM to 10:42 AM.\nRenata was at the luxury box's cafe since 10 AM. She received a call from Esteban at 10:17 AM. They met there at 10:24 AM and went to the racetrack. They left at 10:34 AM.\nEsteban was smoking from 10:00 AM to 10:17 AM by the grandstands.\nLucas was with Vicente at the parade ring from 10 AM to 10:10 AM. He stayed at the observation area by the grandstands until 10:42 AM.")
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

define dp_chispa = CharacterProfile(
    _("La Chispa"),
    "side chispa smile",  # Image file
    _("Age: 4"),
    _("My trusty mare and partner in crime-fighting. I couldn't ask for a better friend to watch my back.")
)
define dp_catalina = CharacterProfile(
    _("Catalina Moreno"),
    "pcata",
    _("Age: 26"),
    _("A cold, direct, and perfectionist jockey who strives for undisputed superiority. Horse: Dama de Plata.")
)

define dp_medina = CharacterProfile(
    _("Sofía Medina"),
    "pmedi",
    _("Age: 34"),
    _("A methodical and capable local police inspector. Known for her dry demeanor and occasional sarcasm, she takes her investigations seriously.")
)

define dp_lorenzo = CharacterProfile(
    _("Lorenzo Villarreal"),
    "penzo",
    _("Age: 55"),
    _("The flamboyant host of the Razing Thunder Derby. A large, top-hat-wearing showman who puts the success and spectacle of the event above everything else.")
)

define dp_sebastian = CharacterProfile(
    _("Sebastian Castillo"),
    "pseb",
    _("Age: 28"),
    _("A wealthy heir and Renata's sponsor. Arrogant, impulsive, and an avid gambler. He has a taste for luxury watches.")
)

define dp_lucas = CharacterProfile(
    _("Lucas Mendoza"),
    "plu",
    _("Age: 25"),
    _("A reserved and hardworking jockey, often considered the underdog of the competition. Horse: Lucero.")
)

define dp_vicente = CharacterProfile(
    _("Vicente Ruiz"),
    "pvi",
    _("Age: 48"),
    _("Lucas's trainer. A patient and pragmatic person who believes success comes from discipline and consistent effort.")
)

define dp_renata = CharacterProfile(
    _("Renata Vargas"),
    "prena",
    _("Age: 23"),
    _("A loud, boastful, and hot-tempered jockey who wants to prove her worth through her own abilities. Horse: Pícaro.")
)

define dp_esteban = CharacterProfile(
    _("Esteban Rojas"),
    "pes",
    _("Age: 42"),
    _("Renata's trainer. A disciplined, cordial, and professional person who presents himself as dependable and courteous.")
)