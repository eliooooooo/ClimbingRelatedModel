import pandas as pd
import numpy as np
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Embedding, LSTM, Dense, Dropout
import pickle

# Charger les données
df = pd.read_csv('./data.csv')

# Séparer les features (Texte) et les labels
X = df['Texte']
y = df['Label']

# Entraîner le tokenizer
tokenizer = Tokenizer(num_words=5000)
tokenizer.fit_on_texts(X)

# Sauvegarder le tokenizer
with open('tokenizer.pickle', 'wb') as handle:
    pickle.dump(tokenizer, handle, protocol=pickle.HIGHEST_PROTOCOL)

# Convertir les textes en séquences
X_sequences = tokenizer.texts_to_sequences(X)
X_padded = pad_sequences(X_sequences, maxlen=100)

# Créer le modèle
model = Sequential()
model.add(Embedding(input_dim=5000, output_dim=64))
model.add(LSTM(128, return_sequences=True))
model.add(Dropout(0.5))
model.add(LSTM(64))
model.add(Dense(1, activation='sigmoid'))

# Compiler le modèle
model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])

# Entraîner le modèle
model.fit(X_padded, y, epochs=100, batch_size=64, validation_split=0.2)

# Sauvegarder le modèle
model.save('climbing_related.h5')