from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.dialects.postgresql import JSONB
from sqlalchemy import String, Enum, Numeric, Boolean, Column
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from uuid import uuid4
import enum


def get_uuid():
    return uuid4().hex


class ListingPurpose(enum.Enum):
    rental = 1
    purchase = 2
    both = 3


class Base(DeclarativeBase):
    pass


db = SQLAlchemy(model_class=Base)


class PropertyAd(db.Model):
    __tablename__ = "property_ads"

    id = Column(String, primary_key=True, unique=True, default=get_uuid)
    neighboorhood = mapped_column(String(64))
    city = mapped_column(String(64))
    listing_purpose = mapped_column(Enum(ListingPurpose), nullable=False)
    uf = mapped_column(String(2))
    mustHaveItems = mapped_column(JSONB)
    desiredItems = mapped_column(JSONB)
    min_budget = mapped_column(Numeric(precision=20, scale=2))
    max_budget = mapped_column(Numeric(precision=20, scale=2))
    term_acceptance = mapped_column(Boolean, default=False)
    active = mapped_column(Boolean, default=False)

    def __repr__(self):
        return "<id {}>".format(self.id)
