from flask_restful import Resource
from flask_jwt_extended import (
    jwt_required
)
from ...models.news import NewsModel
from ...schemas.news import NewsSchema
from ...helpers.fetchnewnews import updating

news_list_schema = NewsSchema(many=True)


class News(Resource):
    @jwt_required
    def get(self, country, category):
        if updating:
            return {'message': 'Please come back in 10 minutes. Updating the news.'}, 400
        return news_list_schema.dump(NewsModel.find_by_country_and_category(country, category)), 200