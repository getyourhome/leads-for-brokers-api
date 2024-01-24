from ..extensions.models import db, PropertyAd, ListingPurpose


class PropertyService:
    def __init__(self):
        pass

    def create(self, property):
        print(property)
        new_ad = PropertyAd(
            neighboorhood=property["neighboorhood"],
            city=property["city"],
            uf=property["uf"],
            mustHaveItems=property["must_have_items"],
            desiredItems=property["desired_items"],
            min_budget=property["min_budget"],
            max_budget=property["max_budget"],
            term_acceptance=property["term_acceptance"],
            active=True,
            listing_purpose=ListingPurpose(property["listing_purpose"]),
        )
        db.session.add(new_ad)
        db.session.commit()
        return new_ad
