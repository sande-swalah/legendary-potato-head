from flask import Blueprint, request, jsonify

prodcut_routes_blueprint = Blueprint(
    "products", 
    __name__, 
    url_prefix="/prodcuts"
)

def create_routes(controllers):
    
    @prodcut_routes_blueprint.route("/", methods=["GET"])
    def fetch():
        res = controllers.fetch_all_data()
        return jsonify([r.to_dict() for r in res])
    
    @prodcut_routes_blueprint.route("/", methods=["POST"])
    def create_a_record():
        payload = request.json
        print(f"this is the user data {payload}")

        user_input = controllers.create_product(payload)

        return jsonify(user_input.to_dict()), 201
    
    return prodcut_routes_blueprint
