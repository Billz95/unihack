from sqlalchemy import Column, ForeignKey, Integer, String, REAL
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy import create_engine

# import Owner

Base = declarative_base()


class Product(Base):
    __tablename__ = 'Product'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    owner = Column(String)
    price = Column(REAL)
    description = Column(String)
    img = Column(String)

    def dictify(self):
        return {
            'id': self.id,
            'name': self.name,
            'owner': self.owner,
            'price':self.price,
            'description':self.description,
            'img' : self.img
        }


class Owner(Base):
    __tablename__ = 'User'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    lon = Column(REAL)
    lat = Column(REAL)
    info = Column(String)

    def get_loc(self):
        return (self.lon, self.lat)


class Data(object):

    def createTable(self):

        engine = create_engine('sqlite:///data.db')
        Base.metadata.create_all(engine)

    def insertItem(self, name, owner, price, description, img):
        engine = create_engine('sqlite:///data.db')
        Base.metadata.bind = engine
        DBSession = sessionmaker(bind=engine)
        session = DBSession()

        product = Product(name=name, owner=owner, price=price, description=description, img=img)
        session.add(product)

        session.commit()
        session.close()

    def searchItemByName(self, name):
        print("\nSearch for item: " + name + "...")
        if name == '':
            return []

        engine = create_engine('sqlite:///data.db')
        Base.metadata.bind = engine
        DBSession = sessionmaker()
        DBSession.bind = engine
        session = DBSession()

        data = session.query(Product).filter(Product.name.contains(name))
        session.close()
        return data

    def searchItemById(self, id):
        print("\nSearch for item with id: " + str(id) + "...")
        engine = create_engine('sqlite:///data.db')
        Base.metadata.bind = engine
        DBSession = sessionmaker()
        DBSession.bind = engine
        session = DBSession()

        data = session.query(Product).filter(Product.id == id)

        session.close()
        return data

    def searchItemByOwnerName(self, ownername):
        engine = create_engine('sqlite:///data.db')
        Base.metadata.bind = engine
        DBSession = sessionmaker()
        DBSession.bind = engine
        session = DBSession()

        data = session.query(Product).filter(Product.owner == ownername)
        session.close()
        return data

    def searchItemByOwnerId(self, id):
        engine = create_engine('sqlite:///data.db')
        Base.metadata.bind = engine
        DBSession = sessionmaker()
        DBSession.bind = engine
        session = DBSession()

        data = session.query(Product).filter( Product.owner == session.query(Owner).get(id).name)
        session.close()
        return data

    def deleteItem(self, id):
        engine = create_engine('sqlite:///data.db')
        Base.metadata.bind = engine
        DBSession = sessionmaker()
        DBSession.bind = engine
        session = DBSession()

        data = session.query(Product).filter_by(id=id).first()
        session.delete(data)

        session.commit()
        session.close()

    def createOwner(self, name, lon, lat, info):
        engine = create_engine('sqlite:///data.db')
        Base.metadata.bind = engine
        DBSession = sessionmaker(bind=engine)
        session = DBSession()

        product = Owner(name=name, lon=lon, lat=lat, info=info)
        session.add(product)

        session.commit()
        session.close()

    def findOwner(self, name):
        engine = create_engine('sqlite:///data.db')
        Base.metadata.bind = engine
        DBSession = sessionmaker(bind=engine)
        session = DBSession()

        owners = session.query(Owner).filter_by(name=name)

        session.commit()
        session.close()
        return owners

    def updateItem(self, id, name, owner_name, price, description, img):
        engine = create_engine('sqlite:///data.db')
        Base.metadata.bind = engine
        DBSession = sessionmaker(bind=engine)
        session = DBSession()

        session.query(Product).filter_by(id=id).update(
            {'name': name, 'price': price, 'owner':owner_name, 'description': description, 'img':img})

        session.commit()
        session.close()

# data = Data()
# try:
#     data.createTable()
# except:
#     print("Table already there!")
#
# def tryInsert(name, owner, price, description):
#     try:
#         data.insertItem(name, owner, price, description)
#         print("Item insert succeed!")
#     except:
#         print("item already there!")
#
# def tryDelete(id):
#     try:
#         data.deleteItem(id)
#         print("Item:" , "id:" + str(id), "delete success")
#     except:
#         print("Item does not exist:" , "id:" + str(id))
#
# tryInsert('mobile phone', "JB-hifi", '100', 'cool')
# tryInsert('mobile phone', "JB-hifi", '99', 'cool')
# tryInsert('mobile phone', "JB-hifi", '98', 'cool')
# tryInsert('mobile phone', "JB-hifi", '97', 'cool')
# # tryDelete('005')
# tryInsert('mobile phone', "JB-hifi", '96', 'cool')
#
#
# data.searchItem('mobile phone')
# data1 = data.searchItem('005')
# data.search_author('Tom')
