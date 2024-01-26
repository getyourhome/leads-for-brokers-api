from werkzeug.security import generate_password_hash

from ..data.models import db, Broker


class RegisterService:
    def __init__(self):
        pass

    def create(self, property):
        broker = Broker(
            name=property["name"],
            email=property["email"],
            phone=property["phone"],
            creci_number=property["creci_number"],
            password=generate_password_hash(property["password"]),
        )

        db.session.add(broker)
        db.session.commit()
        return broker
