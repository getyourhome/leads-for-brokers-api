from werkzeug.security import generate_password_hash

from ..data.models import db, PropertyAd, Announcer
from ..data.enums import ListingPurpose, PropertyType


class RegisterService:
    def __init__(self):
        pass

    def create(self, property):
        announcer = Announcer(
            name=property["name"],
            email=property["email"],
            phone=property["phone"],
            document_number=property["document_number"],
            password=generate_password_hash(property["password"]),
        )

        new_ad = PropertyAd(
            neighboorhood=property["neighboorhood"],
            city=property["city"],
            uf=property["uf"],
            mustHaveItems=property["must_have_items"],
            desiredItems=property["desired_items"],
            min_budget=property["min_budget"],
            max_budget=property["max_budget"],
            active=True,
            listing_purpose=ListingPurpose(property["listing_purpose"]),
            property_type=PropertyType(property["property_type"]),
            announcer=announcer,
        )
        db.session.add(announcer)
        db.session.add(new_ad)
        db.session.commit()
        return new_ad
