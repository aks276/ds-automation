import cell_creation

def get_inference(config):
    cells = []
    cells.append(cell_creation.md_cell("#### Inference"))
    cells.append(cell_creation.code_cell("model = pickle.load(open('saved_model.sav', 'rb'))"))
    cells.append(cell_creation.code_cell("#### TODO: Code for determing input"))
    cells.append(cell_creation.code_cell("model.predict()"))

    return cells
