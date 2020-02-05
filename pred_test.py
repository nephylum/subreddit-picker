import numpy as np
from tensorflow.keras.preprocessing import sequence
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Embedding
from tensorflow.keras.layers import LSTM
from sklearn.feature_extraction.text import TfidfVectorizer

vect = TfidfVectorizer()
x = ['this is a test',
     'because i am dumb',
     'because I cant figure this out']
# y = ['what',
#      'why',
#      'why']
y = [0,
     1,
     1]
X = vect.fit_transform(x)
print(X)


print('Build model...')
model = Sequential()
model.add(Embedding(10000, 128))
model.add(LSTM(128, dropout=0.2, recurrent_dropout=0.2))
model.add(Dense(1, activation='sigmoid'))

# try using different optimizers and different optimizer configs
model.compile(loss='binary_crossentropy',
              optimizer='adam',
              metrics=['accuracy'])

print('Train...')
model.fit(X, y, batch_size=32, epochs=15,)
score, acc = model.evaluate(X, y,
                            batch_size=32)
print('Test score:', score)
print('Test accuracy:', acc)
