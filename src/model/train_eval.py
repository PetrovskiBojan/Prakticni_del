import os
import pandas as pd
import numpy as np
import joblib
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.impute import SimpleImputer
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report

def train_and_save_model():
    df = pd.read_csv("../../data/processed/reference_dataset.csv")

    target = "Dropout"
    X = df.drop(columns=[target])
    y = df[target]

    test_idx = np.random.choice(df.index, size=1)[0]

    X_train = X.drop(index=test_idx)
    y_train = y.drop(index=test_idx)
    X_test = X.loc[[test_idx]]
    y_test = y.loc[[test_idx]]

    numeric_features = X_train.select_dtypes(include=["int64", "float64"]).columns.tolist()
    categorical_features = X_train.select_dtypes(include=["object", "category"]).columns.tolist()

    numeric_transformer = Pipeline([
        ("imputer", SimpleImputer(strategy="mean")),
        ("scaler", StandardScaler())
    ])

    categorical_transformer = Pipeline([
        ("imputer", SimpleImputer(strategy="constant", fill_value="missing")),
        ("onehot", OneHotEncoder(handle_unknown="ignore"))
    ])

    preprocessor = ColumnTransformer([
        ("num", numeric_transformer, numeric_features),
        ("cat", categorical_transformer, categorical_features)
    ])

    clf = Pipeline([
        ("preprocessor", preprocessor),
        ("classifier", RandomForestClassifier(random_state=42))
    ])

    clf.fit(X_train, y_train)

    y_pred = clf.predict(X_test)
    print(f"Test index: {test_idx}")
    print(f"True label: {y_test.values[0]}, Predicted: {y_pred[0]}")

    y_train_pred = clf.predict(X_train)
    print(classification_report(y_train, y_train_pred))

    os.makedirs("models", exist_ok=True)
    joblib.dump(clf, "../models/dropout_model.joblib")

if __name__ == "__main__":
    train_and_save_model()
