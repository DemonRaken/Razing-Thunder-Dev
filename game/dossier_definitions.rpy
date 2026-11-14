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

    class Dossier:
        def __init__(self):
            self.items = []

        def add(self, item):
            renpy.notify(_("Dossier has been updated.") + " " + item.name + " " + _("was discovered.") )
            self.items.append(item)

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

define de_mate = Evidence(
    "Mate",
    "mate-transparent",
    "This mate is passed down the generations.",
"""Etiam lobortis nulla odio, non bibendum felis suscipit non. Duis erat nibh, feugiat viverra porta vel, luctus vel orci. Donec maximus porttitor tempus. Etiam metus nunc, blandit vel nisl sed.
"""                        
)

define de_mask = Evidence(
    "Mask",
    "evidence-mask-transparent",
    "This epic mask can make you 1000 times more handsome.",
"""Duis erat nibh, feugiat viverra porta vel, luctus vel orci.
Nulla non arcu ut justo suscipit iaculis vehicula quis tortor. 
Nunc non fermentum tortor. Donec bibendum vel eros eu blandit. 
In vulputate est sit amet libero commodo aliquam. Cras nec sapien sodales,
semper felis vel, tincidunt augue. Nam non turpis sed felis lobortis congue. 
Aenean blandit tincidunt magna sed pretium.
Vestibulum varius lacus a ultrices molestie. 
Nulla fermentum condimentum faucibus. 
Quisque nec mi ut libero semper tempor ac in est. Nunc ac elit pharetra est mollis pellentesque.
Mauris vitae ullamcorper elit. Mauris ultrices tincidunt consectetur. 
Etiam malesuada magna sed augue aliquam vestibulum id id dolor. 
Etiam suscipit neque eu suscipit auctor. 
Fusce auctor magna ut dui semper, eu dignissim nisl egestas. 
In pharetra tincidunt purus ut vulputate. 
Quisque sit amet magna eget enim dapibus iaculis eu et massa.
"""                        
)

define de_medicalreport = Evidence(
    "Medical Report",
    "evidence-med-report",
    "Obtained from Inspector Medina.",
    "Horse feels ill from bad drugs."
                        
)


define de_screen = Evidence(
    "Screen",
    "screen",
    "Just an ordinary screen showing a test pattern.",
    "No, Monika won't come out of it, no matter how much you stare at it."
)

define dp_leo = CharacterProfile(
    "El Leopardo",
    "side leo grin shine",
    "The Leopard man always carries a mate!",
    "Here comes the Leopard man to the rescue! After that he will treat you to his mate!"
)