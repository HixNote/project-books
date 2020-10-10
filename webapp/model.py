from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Edition(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String, nullable=False)
    author = db.Column(db.String, db.ForeignKey('author.id'))
    other_creators = db.Column(db.String,)
    country = db.Column(db.String)
    original_language = db.Column(db.String)
    edition_language = db.Column(db.String)
    year_of_creating = db.Column(db.DateTime)
    year_of_edition = db.Column(db.DateTime)
    publishing = db.Column(db.String, db.ForeignKey('publishing.id'))
    edition_number = db.Column(db.Integer)
    ISBN = db.Column(db.String, db.ForeignKey('edition.id'), unique=True, nullable=False)
    #Нужно добавить приведение к единому формату, чтобы была проверка на уникальность.
    other_editions = db.relationship('Edition', backref='edition')
    pages_count = db.Column(db.Integer)    
    cover = db.Column(db.String)
    scans = db.Column(db.String)
    annotation = db.Column(db.Text)
    key_words = db.Column(db.String)
    catalog_items = db.relationship('Catalog', backref='edition')
    last_update = db.Column(db.DateTime)

    def __repr__(self):
        return f'<Edition: {title}, {publishing}, {edition_number}>'

class Author(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    pseudonim = db.Column(db.String, unique=True, nullable=False)
    real_name = db.Column(db.String, nullable=False)
    year_of_birth = db.Column(db.DateTime)
    photo = db.Column(db.String)
    country = db.Column(db.String)
    language = db.Column(db.String)
    books = db.relationship('Edition', backref='author')

    def __repr__(self):
        return f'<Author: {pseudonim}>'

class Publishing(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, unique=True, nullable=False)
    logo = db.Column(db.String)
    big_publishing = db.Column(db.String, db.ForeignKey('publishing.id'))
    books = db.relationship('Edition', backref='publishing')
    country = db.Column(db.String)
    town = db.Column(db.String)
    url = db.Column(db.String, unique=True)
    adress = db.Column(db.String)
    branches = db.relationship('Publishing', backref='publishing')


    def __repr__(self):
        return f'<Publishing: {name}, {town}>'

class Catalog(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    book = db.Column(db.String, db.ForeignKey('edition.id'), nullable=False)
    point_of_sell = db.Column(db.String, db.ForeignKey('shop.id'), nullable=False)
    price = db.Column(db.Float, nullable=False)
    url = db.Column(db.String, nullable=False)

    def __repr__(self):
        return f'<Catalog: {book}, {point_of_sell}>'

class Shop(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    url = db.Column(db.String, unique=True, nullable=False)
    adress = db.Column(db.String)
    catalog_items = db.relationship('Catalog', backref='shop')

    def __repr__(self):
        return f'<Shop: {name}, {url}>'

class Parsing(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.DateTime, nullable=False)
    source = db.Column(db.String, nullable=False)