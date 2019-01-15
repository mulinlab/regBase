import pandas as pd
from sklearn.externals import joblib
from xgboost import XGBClassifier

## loading best parameters
PARAM_SETS = {}
best_parmas = pd.read_json("./best_parmas")
for parm in best_parmas:
    PARAM_SETS[parm] = best_parmas[parm].to_dict()
    for parm_key in PARAM_SETS[parm].keys():
        if parm_key in {'max_depth', 'n_estimators', 'min_child_weight', 'reg_alpha' }:
            PARAM_SETS[parm][parm_key] = int(PARAM_SETS[parm][parm_key])

## training and save model into ./trained_model
for model_name in PARAM_SETS.keys():
    # ------------------------
    TRAIN_FILE = f'../train_dataset/{model_name}_dataset_XY.tsv'
    train_ds = pd.read_csv(TRAIN_FILE, sep='\t', na_values=['.'], header=0)
    train_ds = train_ds.drop(train_ds.columns[range(4)], axis=1)

    if model_name == 'REG_Common':
        train_ds = train_ds.drop(columns='PRVCS')

    train_ds = train_ds.values

    # ------------------------
    best_params = PARAM_SETS[model_name]
    model = XGBClassifier(n_jobs=-1, **best_params)
    y = train_ds[:, -1]
    X = train_ds[:, :-1]

    model.fit(X, y)

    joblib.dump(model, f'../trained_model/regBase_{model_name}.model')