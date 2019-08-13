import sqlalchemy as db
from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy.ext.declarative import declarative_base
import sqlite3

Base = declarative_base()

engine = db.create_engine('sqlite:///RealEstateScraper.sqlite')
connection = engine.connect()
metadata = db.MetaData()
Session = sessionmaker(bind=engine)


class Property(Base):
    __tablename__ = 'Property'
    id = db.Column(db.Integer, primary_key=True)
    address = db.Column(db.String(500))
    bed_room = db.Column(db.Integer)
    bath_room = db.Column(db.Integer)
    car_space = db.Column(db.Integer)
    property_type = db.Column(db.String(50))
    ad_for_sale = relationship('AdForSale')


class AdForSale(Base):
    __tablename__ = 'AdForSale'
    id = db.Column(db.Integer, primary_key=True)
    ad_id = db.Column(db.String(50))
    list_date = db.Column(db.Date)
    scrape_date = db.Column(db.Date)
    website_domain = db.Column(db.String(50))

    url = db.Column(db.String(200))
    ad_type = db.Column(db.String(50))
    price = db.Column(db.Numeric)
    agent_company = db.Column(db.String(200))
    agent_address = db.Column(db.String(500))
    property_id = db.Column(db.Integer, db.ForeignKey('Property.id'))

Base.metadata.create_all(engine)

house = Property(address='12 Prestige Ave, Bella Vista',
                 bed_room=4,
                 bath_room=2,
                 car_space=2,
                 property_type='house')

house2 = Property(bed_room=3)
session = Session()
session.add(house)
session.add(house2)
session.commit()

houses = session.query(Property).all()
for house in houses:
    print(house.__dict__)
    print('*' * 100)



