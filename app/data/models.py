from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import (
    ForeignKey,
    and_,
    String,
    Enum,
    Numeric,
    Boolean,
    Column,
    DateTime,
    ARRAY,
)
from sqlalchemy.orm import (
    configure_mappers,
    DeclarativeBase,
    mapped_column,
    relationship,
)
from uuid import uuid4

from .enums import UserRole, ListingPurpose, PropertyType

configure_mappers()


def get_uuid():
    return uuid4().hex


class Base(DeclarativeBase):
    pass


db = SQLAlchemy(model_class=Base)


class User(db.Model):
    __tablename__ = "users"

    id = mapped_column(String, primary_key=True, unique=True, default=get_uuid)
    type = mapped_column(Enum(UserRole), nullable=False)
    name = mapped_column(String(255), nullable=False)
    password = mapped_column(String(255), nullable=False)
    email = mapped_column(String(100), unique=True)
    phone = mapped_column(String(20), nullable=False)

    terms = relationship("TermAcceptance")
    ads = relationship("PropertyAd", back_populates="announcer")

    __mapper_args__ = {"polymorphic_on": type}


class Broker(User):
    __tablename__ = "brokers"

    creci_number = mapped_column(Numeric, unique=True)

    __mapper_args__ = {
        "polymorphic_identity": UserRole.broker,
        "polymorphic_on": "type",
    }


class SysManager(User):
    __tablename__ = "sys_managers"

    __mapper_args__ = {
        "polymorphic_identity": UserRole.sysAdmin,
        "polymorphic_on": "type",
    }


class Announcer(User):
    __tablename__ = "announcers"

    document_number = mapped_column(String(14), unique=True)

    __mapper_args__ = {
        "polymorphic_identity": UserRole.announcer,
        "polymorphic_on": "type",
    }


class TermAcceptance(db.Model):
    __tablename__ = "term_acceptances"

    id = mapped_column(String, primary_key=True, unique=True, default=get_uuid)
    term_version = mapped_column(String(20), nullable=False)
    accepted_at = mapped_column(DateTime(timezone=True))
    device_id = mapped_column(String(20))

    user_id = mapped_column(ForeignKey("users.id"))
    user = relationship("User", back_populates="terms")


class PropertyAd(db.Model):
    __tablename__ = "property_ads"

    id = Column(String, primary_key=True, unique=True, default=get_uuid)
    neighboorhood = mapped_column(String(64))
    city = mapped_column(String(64))
    listing_purpose = mapped_column(Enum(ListingPurpose), nullable=False)
    property_type = mapped_column(Enum(PropertyType), nullable=False)
    uf = mapped_column(String(2))
    min_budget = mapped_column(Numeric(precision=20, scale=2))
    max_budget = mapped_column(Numeric(precision=20, scale=2))
    active = mapped_column(Boolean, default=False)
    mustHaveItems = mapped_column(ARRAY(String), nullable=True)
    desiredItems = mapped_column(ARRAY(String), nullable=True)

    # Foreign key to link to Announcer (or any other type)
    announcer_id = mapped_column(
        ForeignKey("users.id", onupdate="CASCADE", ondelete="CASCADE")
    )

    announcer = relationship(
        "User",
        primaryjoin=and_(User.id == announcer_id, User.type == UserRole.announcer),
        back_populates="ads",
    )

    def __repr__(self):
        return "<id {}>".format(self.id)
