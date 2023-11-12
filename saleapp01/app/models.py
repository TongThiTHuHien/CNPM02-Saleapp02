from sqlalchemy import Column, Integer, String, Float, ForeignKey
from sqlalchemy.orm import relationship
from app import db
from flask_login import UserMixin



class User(db.Model, UserMixin):
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50), nullable=False)
    username = Column(String(50), nullable=False, unique=True)
    password = Column(String(100), nullable=False)
    avatar = Column(String(100), default='https://cdn1.viettelstore.vn/images/Product/ProductImage/medium/iPad-Pro-12.9-gray1.jpg')


class Category(db.Model):
    __tablename__ = 'category'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50), nullable=False, unique=True)
    products= relationship('Product', backref='category', lazy=True)

    def __str__(self):
        return self.name


class Product(db.Model):
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50), nullable=False, unique=True)
    price = Column(Float, default=0)
    category_id = Column(Integer, ForeignKey(Category.id), nullable=False)
    image = Column(String(100))



if __name__ == "__main__":
    from app import app
    with app.app_context():
        # c1 = Category(name='Mobile')
        # c2 = Category(name='Tablet')
        #
        # db.session.add(c1)
        # db.session.add(c2)
        # db.session.commit()
        p1 = Product(name='Ipad 2022 ', price=23000000,
                     category_id=1, image="https://cdn1.viettelstore.vn/images/Product/ProductImage/medium/iPad-Pro-12.9-gray1.jpg")
        p2 = Product(name='Iphone 14 promax', price=21000000,
                     category_id=2, image="https://cdn1.viettelstore.vn/Images/Product/ProductImage/325815861.jpeg")
        p3 = Product(name='Iphone 15 pro', price=29000000,
                     category_id=2, image="https://cdn.viettelstore.vn/Images/Product/ProductImage/1616860216.jpeg")
        p4 = Product(name='Galaxy Note 20', price=23000000,
                     category_id=1, image="https://cdn.viettelstore.vn/Images/Product/ProductImage/2012289348.jpeg")
        p5 = Product(name='Galaxy Flip3', price=19000000,
                     category_id=1, image="https://cdn1.viettelstore.vn/images/Product/ProductImage/medium/Flip3-256.jpg")


        db.session.add_all([p1, p2, p3, p4, p5])
        db.session.commit()
        db.create_all()