import numpy as np
from sklearn.linear_model import LinearRegression


def train_model():

    # Historical sample data
    people = np.array([
        [0],
        [1],
        [2],
        [3],
        [4],
        [5],
        [6],
        [7]
    ])

    waiting_time = np.array([
        0,
        30,
        60,
        90,
        120,
        150,
        180,
        210
    ])

    model = LinearRegression()

    model.fit(people, waiting_time)

    return model


def predict_waiting_time(people_ahead):

    model = train_model()

    prediction = model.predict([[people_ahead]])

    return max(0, round(float(prediction[0])))