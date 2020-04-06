from .resources.news import News

def initialize_routes(api):
    api.add_resource(News, '/<string:country>/<string:category>')