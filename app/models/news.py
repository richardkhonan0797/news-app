from .. import db

class NewsModel(db.Model):
    __tablename__ = 'news'

    id = db.Column(db.Integer, primary_key = True)
    source_id = db.Column(db.String)
    source_name = db.Column(db.String)
    author = db.Column(db.String)
    title = db.Column(db.String)
    description = db.Column(db.String)
    url = db.Column(db.String)
    urlToImage = db.Column(db.String)
    publishedAt = db.Column(db.String)
    content = db.Column(db.String)
    country = db.Column(db.String)
    category = db.Column(db.String)

    def save_all_to_db(objects):
        db.session.add_all(objects)
        db.session.commit()

    @classmethod
    def count_by_country_and_category(cls, country, category):
        return cls.query.filter_by(country=country, category=category).count()

    @classmethod
    def find_by_country_and_category(cls, country, category):
        return cls.query.filter_by(country=country, category=category).all()

    @classmethod
    def delete_by_country_and_category(cls, country, category):
        cls.query.filter_by(country=country, category=category).delete()
