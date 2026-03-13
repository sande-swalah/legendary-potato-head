from flask import Blueprint, request, jsonify

prodcut_routes_blueprint = Blueprint("products", __name__, url_prefix="/prodcuts")

def create_routes(controllers):
    
    @prodcut_routes_blueprint("/", methods=["GET"])
    def fetch():
        return jsonify(controllers.fetch_all_data())
    
    @prodcut_routes_blueprint("/products", methods=["POST"])
    def create_a_record():
        return controllers.create_product(request.json)
    
    return prodcut_routes_blueprint
