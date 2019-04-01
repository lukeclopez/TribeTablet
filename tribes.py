class Tribe:
    def __init__(self, name, troops, levites):
        # *** Tribe Info ***
        self.name = name
        self.troops = troops
        self.levites = levites
        self.pro = ""
        self.con = ""

        # *** Tribe Status ***
        self.faithfulness = 0
        self.spiritual_prayer = 10
        self.conquest_prayer = 10
        self.is_faithful = True


judah = Tribe("Judah", 5, 4)
judah.pro = "Large tribe"
judah.con = "Tribe is spiritually weak"

gad = Tribe("Gad", 3, 6)
gad.pro = "Tribe is spiritually strong"
gad.con = "Small tribe"

naphtali = Tribe("Naphtali", 3, 5)
naphtali.pro = "Move an extra tile every turn"
naphtali.con = "Small tribe"

zebulun = Tribe("Zebulun", 4, 5)
zebulun.pro = "Teaching the law x2 when tribe unfaithful"
zebulun.con = "None"

tribes_list = [judah, gad, naphtali, zebulun]
