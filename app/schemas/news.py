from .. import ma
from ..models.news import NewsModel

class NewsSchema(ma.ModelSchema):
    class Meta:
        model = NewsModel