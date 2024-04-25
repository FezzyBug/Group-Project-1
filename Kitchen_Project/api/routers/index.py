from . import orders, order_details, customers, promotions, menu_items, reviews, data_analysis


def load_routes(app):
    app.include_router(orders.router)
    app.include_router(customers.router)
    app.include_router(promotions.router)
    app.include_router(menu_items.router)
    app.include_router(reviews.router)
    app.include_router(data_analysis.router)
