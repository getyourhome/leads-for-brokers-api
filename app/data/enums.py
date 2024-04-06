import enum


class ListingPurpose(enum.Enum):
    rental = 1
    purchase = 2
    both = 3

    @classmethod
    def from_string(cls, purpose):
        purpose_map = {"rental": cls.rental, "purchase": cls.purchase, "both": cls.both}
        return purpose_map.get(purpose, cls.both)


class UserRole(enum.Enum):
    announcer = 1
    broker = 2
    sysAdmin = 3


class PropertyType(enum.Enum):
    house = "house"
    apartment = "apartment"
    commercial = "commercial"
