class Tribe:
    def __init__(self, name, troops, levites):
        self.name = name
        self.troops = troops
        self.levites = levites

        self.pro = ""
        self.con = ""


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
