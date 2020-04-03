from .resources.news import News

def initialize_routes(api):
    api.add_resource(News, '/news/<string:country>/<string:category>')