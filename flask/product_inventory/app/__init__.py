from flask import Flask

# we import modules from the app to configure
from app.model.product_repository import InMemoRepo
from app.view.product_services import ProductServiceLayer
from app.controllers.product_controllers import ProductController
from app.controllers.product_routes import create_routes

def create_app():
    # instantiate the product flask app as MKG(Make Kenya Great)
    MKG = Flask(__name__)

    # We instantiate the classes we have for out MVC architecture
    repo = InMemoRepo() # domain and crud operation
    service = ProductServiceLayer(repo) # bussiness logic

    controllers = ProductController(service) # match the url to a service to be executed
    product_routes = create_routes(controllers)

    # register some routes
    MKG.register_blueprint(product_routes)
    return MKG

