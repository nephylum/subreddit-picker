import pickle
from tensorflow.keras.models import Sequential, Model

# def pred_test(inputs):
#     model = pickle.load(open('Model.pkl', 'rb'))
#     return model.predict([inputs])[0]

input_t = "this is a test post I wonder where itll end up?"
model = pickle.load(open('model2.pkl', 'rb'))

pred = model.predict(input_t)
print(pred)
