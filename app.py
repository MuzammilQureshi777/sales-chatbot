from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# Simple logic-based response
def get_bot_response(message):
    message = message.lower()
    if "t-shirt" in message:
        return "We have amazing T-Shirts here: /products/tshirts"
    elif "discount" in message:
        return "We’re offering 10% off today! Use code: SAVE10"
    elif "contact" in message:
        return "You can contact us at contact@yourstore.com"
    else:
        return "I'm here to help with product questions, discounts, or contact info!"

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/chat", methods=["POST"])
def chat():
    user_msg = request.json.get("message")
    bot_reply = get_bot_response(user_msg)
    return jsonify({"response": bot_reply})

if __name__ == "__main__":
    app.run(debug=True)
