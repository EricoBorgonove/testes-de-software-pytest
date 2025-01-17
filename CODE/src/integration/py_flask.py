from flask import Flask, jsonify

app = Flask(__name__)

users = {"1": {"name": "Taiana"}, "2": {"name": "Bob"}}

@app.route("/users/<user_id>")
def get_user(user_id):
    user = users.get(user_id)
    if user:
        return jsonify(user), 200
    return jsonify({"error": "User not found"}), 404

if __name__ == "__main__":
    app.run()
