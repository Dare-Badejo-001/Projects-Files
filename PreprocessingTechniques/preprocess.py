

def impute_missing_values(data, strategy="mean", fill_value=None):
    from sklearn.impute import SimpleImputer
    import pandas as pd
    if strategy == "constant" and fill_value is None: 
        raise ValueError("fill_value must be specifiec for strategy = 'constant")
    imputer = SimpleImputer(strategy=strategy, fill_value=fill_value) 
    return pd.DataFrame(imputer.fit_transform(data), columns=data.columns) 


def handle_outliers_iqr(data, threshold=1.5): 
    Q1 = data.quantile(0.25)
    Q3 = data.quantile(0.75)
    IQR = Q3 - Q1

    lower_bound = Q1 - (threshold * IQR)
    upper_bound = Q3 + (threshold * IQR)

    return data[~((data < lower_bound) | (data > upper_bound)).any(axis=1)]




def select_feature_rfe(data, target, n_features_to_select=5): 
    from sklearn.feature_selection import RFE
    from sklearn.linear_model import LogisticRegression
    model = LogisticRegression(solver='liblinear') 
    rfe = RFE(model, n_features_to_select=n_features_to_select)
    fit = rfe.fit(data, target) 

    selected_features = [f for f, s in zip(data.columns, fit.support_) if s]
    return selected_features



def apply_pca(data, n_components=2):
    import pandas as pd
    from sklearn.decomposition import PCA
    pca = PCA(n_components=n_components)
    principalComponents = pca.fit_transform(data)
    return pd.DataFrame(data=principalComponents, columns=[f'PC{i+1}' for i in range(n_components)])



def standardize_features(data):
    import pandas as pd
    from sklearn.preprocessing import StandardScaler
    scaler = StandardScaler()
    scaled_data = scaler.fit_transform(data)
    return pd.DataFrame(scaled_data, columns=data.columns)




def tune_hyperparameters(model, param_grid, X_train, y_train, cv=5):
    from sklearn.model_selection import GridSearchCV
    grid_search = GridSearchCV(estimator=model, param_grid=param_grid, cv=cv)
    grid_search.fit(X_train, y_train)
    return grid_search.best_params_




def apply_smote(X, y):
    from imblearn.over_sampling import SMOTE
    smote = SMOTE()
    X_res, y_res = smote.fit_resample(X, y)
    return X_res, y_res