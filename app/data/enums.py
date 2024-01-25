import enum


class ListingPurpose(enum.Enum):
    rental = 1
    purchase = 2
    both = 3


class UserRole(enum.Enum):
    announcer = 1
    broker = 2
    sysAdmin = 3


class PropertyType(enum.Enum):
    house = "house"
    apartment = "apartment"
    commercial = "commercial"
