from flask import Flask, request

from firebase_admin import credentials, firestore, initialize_app
app = Flask(__name__)

cred = credentials.Certificate(
    'key.json')
initialize_app(cred)
db = firestore.client()


@app.route("/", methods=["POST", "GET"])
def fire_route():
    doc = db.collection(u'events').document(
        u'09hQ1TqJgZg9Ary01xmKR89Z5W1y').get()
    return doc.to_dict()
