import pandas as pd
import random
import joblib

from sklearn.ensemble import (
    RandomForestRegressor,
    GradientBoostingRegressor
)

from sklearn.multioutput import (
    MultiOutputRegressor
)

from sklearn.model_selection import (
    train_test_split
)

from sklearn.metrics import (
    mean_absolute_error
)

from optimizer import optimize_design

real_df = pd.read_csv(
    "naval_dataset.csv"
)

optimizer_rows = []

for _ in range(300):

    target_range = random.randint(
        20,
        150
    )

    stealth = random.choice(
        [0,1,2]
    )

    depth = random.choice(
        [0,1]
    )

    stealth_label = (
        "Low"
        if stealth == 0
        else "Medium"
        if stealth == 1
        else "High"
    )

    depth_label = (
        "Shallow"
        if depth == 0
        else "Deep"
    )

    result = optimize_design(
        target_range,
        stealth_label,
        depth_label
    )

    best = result["best"]

    optimizer_rows.append({

        "mission":"Synthetic",

        "range":target_range,

        "stealth":stealth,

        "depth":depth,

        "diameter":best["diameter"],

        "length":best["length"],

        "speed":best["speed"],

        "mass":best["mass"]
    })

optimizer_df = pd.DataFrame(
    optimizer_rows
)

df = pd.concat(
    [
        real_df,
        optimizer_df
    ],
    ignore_index=True
)

mission_map = {

    "Anti-Submarine":0,

    "Heavy Strike":1,

    "Mine Warfare":2,

    "Coastal Defense":3,

    "Synthetic":4
}

df["mission_encoded"] = (
    df["mission"]
    .map(mission_map)
)

X = df[
    [
        "mission_encoded",
        "range",
        "stealth",
        "depth"
    ]
]

y = df[
    [
        "diameter",
        "length",
        "speed",
        "mass"
    ]
]
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)
rf_model = RandomForestRegressor(
    n_estimators=500,
    random_state=42
)

rf_model.fit(
    X_train,
    y_train
)
gb_model = MultiOutputRegressor(

    GradientBoostingRegressor(
        n_estimators=200,
        random_state=42
    )

)

gb_model.fit(
    X_train,
    y_train
)
rf_pred = rf_model.predict(
    X_test
)

gb_pred = gb_model.predict(
    X_test
)

rf_error = mean_absolute_error(
    y_test,
    rf_pred
)

gb_error = mean_absolute_error(
    y_test,
    gb_pred
)

print(
    "Random Forest MAE:",
    rf_error
)

print(
    "Gradient Boosting MAE:",
    gb_error
)

joblib.dump(
    rf_model,
    "rf_model.pkl"
)

joblib.dump(
    gb_model,
    "gb_model.pkl"
)

print(
    "Physics Based Model Trained"
)

print(X.head())