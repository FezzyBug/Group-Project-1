from . import orders, order_details, recipes, sandwiches, resources, data_analysis, menu_items, reviews, customer, promotions

from ..dependencies.database import engine


def index():
    orders.Base.metadata.create_all(engine)
    order_details.Base.metadata.create_all(engine)
    recipes.Base.metadata.create_all(engine)
    sandwiches.Base.metadata.create_all(engine)
    resources.Base.metadata.create_all(engine)
    #New items for our tables
    menu_items.Base.metadata.create_all(engine)
    data_analysis.Base.metadata.create_all(engine)
    resources.Base.metadata.create_all(engine)
    reviews.Base.metadata.create_all(engine)
    customer.Base.metadata.create_all(engine)

