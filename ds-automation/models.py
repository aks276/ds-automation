import cell_creation

import data


def get_models(config):
    if "type" not in config:
        raise ValueError("'type' not in config")
    cells = []
    cells.append(
        cell_creation.code_cell(
            "import sklearn.model_selection\nimport sklearn.metrics"
        )
    )
    if config["type"] == "classification":
        cells.append(cell_creation.code_cell("import autosklearn.classification"))
        cells.append(cell_creation.code_cell("automl = autosklearn.classification.AutoSklearnClassifier()"))
    elif config["type"] == "regression":
        cells.append(cell_creation.code_cell("import autosklearn.regression"))
        cells.append(cell_creation.code_cell("automl = autosklearn.regression.AutoSklearnRegressor()"))
    else:
        NotImplementedError(f"{config['type']} not yet implemented.")
    cells.extend(data.get_data_cells(config=config))
    cells.append(cell_creation.md_cell("#### Model Building"))
    cells.append(cell_creation.code_cell("automl.fit(X_train, y_train)"))

    cells.append(cell_creation.md_cell("Performance Measures"))
    cells.append(cell_creation.code_cell("from sklearn.metrics import accuracy_score"))
    cells.append(cell_creation.code_cell("y_hat = automl.predict(X_test)"))
    cells.append(cell_creation.code_cell("print('Accuracy score', accuracy_score(y_test, y_hat))"))

    return cells