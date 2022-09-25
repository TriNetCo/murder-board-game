

class PresentationMixin():

    def present_all_game_information(self):
        print("Suspects: ")
        for suspect in self.suspects:
            name = suspect.display_name
            murder_note = " (Murderer)" if suspect.murderer else ""
            weapon = suspect.weapon["display_name"]

            info_line = "  "
            info_line += name
            info_line += murder_note
            info_line += " - " + weapon
            print(info_line)
        print()

        print("Board:")

        print(" A  B  C  D  ")
        print(" 3  4  6  2")
        print(" 9  6  5  7")
        print(" 4  2  3  9")
        print(" 7  5  8  4")

    def present_suspects(self):
        print("Suspects: ")
        for suspect in self.suspects:
            print("  " + suspect.display_name)
        print()
        
    def present_weapons(self):
        yaml_name = 'weapons'
        items = self.get_attributes(yaml_name, 'display_name')
        print("Weapons: ")
        for item in items:
            print("  " + item)
        print()

    def get_attributes(self, domain_name, property_name):
        domain = getattr(self, domain_name)
        if hasattr(domain[0], property_name):
            properties = [str(getattr(x, property_name)) for x in domain]
        else:
            properties = [str(x[property_name]) for x in domain]
        properties_str = ", ".join(properties)
        print(f"{domain_name} {property_name}: {properties_str}")
        
    """
    def __getattr__(self, name):
        def _missing(*args, **kwargs):
            # name = weapon_name
            return self.get_the_names(name)
        return _missing
    """
