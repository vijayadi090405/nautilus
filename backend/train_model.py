import pandas as pd
import random
import joblib

from sklearn.ensemble import RandomForestRegressor

rows = []

for _ in range(10000):

    mission = random.randint(0, 2)

    stealth = random.randint(0, 2)

    depth = random.randint(0, 1)

    range_km = random.randint(10, 100)

    diameter = (
        0.45
        + (range_km / 500)
        + (stealth * 0.03)
    )

    length = (
        3
        + (range_km / 15)
    )

    speed = (
        70
        - (stealth * 10)
    )

    rows.append([
        mission,
        stealth,
        depth,
        range_km,
        diameter,
        length,
        speed
    ])

df = pd.DataFrame(
    rows,
    columns=[
        "mission",
        "stealth",
        "depth",
        "range",
        "diameter",
        "length",
        "speed"
    ]
)

X = df[
    [
        "mission",
        "stealth",
        "depth",
        "range"
    ]
]

y = df[
    [
        "diameter",
        "length",
        "speed"
    ]
]

model = RandomForestRegressor(
    n_estimators=200
)

model.fit(X, y)

joblib.dump(
    model,
    "model.pkl"
)

print(
    "Model Trained Successfully"
)