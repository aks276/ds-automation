import cell_creation

import data


def get_models(config):
    if "type" not in config:
        raise ValueError("'type' not in config")
    cells = []
    cells.extend(data.get_data_cells(config=config))
    cells.append(cell_creation.md_cell("#### Model Building"))
    if config["type"] == "classification":
        cells.append(cell_creation.code_cell("import autosklearn.classification"))
        cells.append(cell_creation.code_cell("automl = autosklearn.classification.AutoSklearnClassifier()"))
    elif config["type"] == "regression":
        cells.append(cell_creation.code_cell("import autosklearn.regression"))
        cells.append(cell_creation.code_cell("automl = autosklearn.regression.AutoSklearnRegressor()"))
    else:
        raise NotImplementedError(f"{config['type']} not yet implemented.")
    cells.append(cell_creation.code_cell("automl.fit(X_train, y_train)"))

    cells.append(cell_creation.md_cell("Performance Measures"))
    cells.append(cell_creation.code_cell("from sklearn.metrics import accuracy_score"))
    cells.append(cell_creation.code_cell("y_hat = automl.predict(X_test)"))
    cells.append(cell_creation.code_cell("print('Accuracy score', accuracy_score(y_test, y_hat))"))
    
    cells.append(cell_creation.md_cell("##### Run Information of the models"))
    cells.append(cell_creation.code_cell("print(automl.sprint_statistics())"))

    cells.append(cell_creation.code_cell("import pprint"))
    cells.append(cell_creation.code_cell("pprint(automl.show_models(), indent=4)"))

    cells.append(cell_creation.md_cell("#### Saving the model"))
    cells.append(cell_creation.code_cell("import pickle"))
    cells.append(cell_creation.code_cell("pickle.dump(automl, open('saved_model.sav', 'wb'))"))

    return cells
