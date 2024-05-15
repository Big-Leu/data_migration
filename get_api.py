from flask import Flask, request, jsonify
from flask_cors import CORS
from insert_data import insert_data,get_contact,validate_input,sanitize_input,create_model

app = Flask(__name__)
CORS(app)

@app.route("/api/v1/form/contact", methods=["POST"])
def post_details():
    data = request.json
    print(data)
    fields = {field: type(value).__name__ for field, value in data.items()}
    Contact = create_model("Contact", "contacts", fields)
    if not data:
        return jsonify({"message": "INVALID"}), 400
    
    sanitized_data = sanitize_input(data)
    
    if not validate_input(sanitized_data):
        print("returned from validate_input")
        return jsonify({"message": "INVALID"}), 400
    
    insert_data(sanitized_data,Contact)
    
    return jsonify({"message": "OK"}), 200


@app.route("/api/v1/form/detail", methods=["GET"])
def get_deatails():
    return get_contact()


if __name__ == "__main__":
    app.run(debug=True)
