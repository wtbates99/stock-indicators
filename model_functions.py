import pandas as pd
import numpy as np
from sklearn.model_selection import (
    train_test_split,
    cross_val_score,
    GridSearchCV,
    RandomizedSearchCV,
)
from sklearn.metrics import mean_squared_error
from sklearn.impute import SimpleImputer
from xgboost import XGBRegressor


def prepare_data(data, target_column, columns_to_drop):
    X = data.drop(columns=columns_to_drop)
    y = data[target_column]
    X.replace([np.inf, -np.inf], np.nan, inplace=True)
    imputer = SimpleImputer(strategy="median")
    X_imputed = imputer.fit_transform(X)
    X = pd.DataFrame(X_imputed, columns=X.columns)
    return X, y


def split_data(X, y, test_size=0.2, random_state=42):
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=test_size, random_state=random_state
    )
    return X_train, X_test, y_train, y_test


def train_and_evaluate_model(X_train, X_test, y_train, y_test, model):
    model.fit(X_train, y_train)
    y_pred = model.predict(X_test)
    rmse_test = np.sqrt(mean_squared_error(y_test, y_pred))
    print(f"Baseline RMSE: {rmse_test}")
    return model


def perform_cross_validation(X, y, model, cv=5):
    cv_scores = cross_val_score(model, X, y, cv=cv, scoring="neg_mean_squared_error")
    cv_rmse_scores = np.sqrt(-cv_scores)
    print(f"CV RMSE: {cv_rmse_scores.mean()} ± {cv_rmse_scores.std()}")


def tune_hyperparameters(X_train, y_train, model, param_grid):
    grid_search = GridSearchCV(
        model, param_grid, cv=5, scoring="neg_mean_squared_error"
    )
    grid_search.fit(X_train, y_train)
    print(f"Best parameters: {grid_search.best_params_}")
    best_model = grid_search.best_estimator_
    return best_model


def evaluate_model_performance(model, X_test, y_test):
    y_pred = model.predict(X_test)
    rmse = np.sqrt(mean_squared_error(y_test, y_pred))
    return rmse


def grid_s_cv(X_train, y_train, model, param_grid, cv=5):
    grid_search = GridSearchCV(
        model, param_grid, cv=cv, scoring="neg_mean_squared_error", n_jobs=-1
    )
    grid_search.fit(X_train, y_train)
    best_model = grid_search.best_estimator_
    best_score = np.sqrt(-grid_search.best_score_)
    return best_model, best_score


def random_s_cv(X_train, y_train, model, param_distributions, cv=5, n_iter=10):
    random_search = RandomizedSearchCV(
        model,
        param_distributions,
        n_iter=n_iter,
        cv=cv,
        scoring="neg_mean_squared_error",
        n_jobs=-1,
        random_state=42,
    )
    random_search.fit(X_train, y_train)
    best_model = random_search.best_estimator_
    best_score = np.sqrt(-random_search.best_score_)
    return best_model, best_score


def select_best_model(
    baseline_model, grid_model, grid_score, random_model, random_score, X_test, y_test
):
    baseline_score = evaluate_model_performance(baseline_model, X_test, y_test)
    # Comparing baseline with grid and random search models
    print(
        f"SCORE COMPARISONS: \nBASELINE: {baseline_score}\nGRID: {grid_score}\nRANDOM: {random_score}\n"
    )
    if grid_score < baseline_score and grid_score <= random_score:
        print("Grid Search Model selected.")
        return grid_model
    elif random_score < baseline_score and random_score < grid_score:
        print("Random Search Model selected.")
        return random_model
    else:
        print("Baseline Model selected.")
        return baseline_model
