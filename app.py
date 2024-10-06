from flask import Flask, request, jsonify
from flask_cors import CORS
import tensorflow as tf
from tensorflow.keras.preprocessing.sequence import pad_sequences
import pickle

# Charger le modèle sauvegardé
model = tf.keras.models.load_model('./Model/climbing_related.h5')

# Charger le tokenizer sauvegardé
with open('./Model/tokenizer.pickle', 'rb') as handle:
    tokenizer = pickle.load(handle)

app = Flask(__name__)
CORS(app)  # Activer CORS pour toutes les routes

@app.route('/predict', methods=['POST'])
def predict():
    data = request.json
    user_query = data['query']

    # Affiche la requête pour le débogage
    print(f"Requête utilisateur: {user_query}")

    # Prétraitement de la requête
    sequence = tokenizer.texts_to_sequences([user_query])
    padded_sequence = pad_sequences(sequence, maxlen=100)

    # Affiche la séquence traitée pour vérification
    print(f"Séquence prétraitée: {padded_sequence}")

    # Faire la prédiction
    prediction = model.predict(padded_sequence)

    # Affiche la prédiction pour vérification
    print(f"Résultat de la prédiction: {prediction}")

    # Renvoyer la prédiction sous forme JSON
    return jsonify({'prediction': float(prediction[0][0])})

if __name__ == '__main__':
    app.run(debug=True)