import cell_creation


def statistical_desciptions(config: dict):
    if "visualizations" not in config:
        raise ValueError("'visualization' key not found in config")
    cells = []

    cells.append(cell_creation.md_cell("## Statistical Visualizations"))

    ## Shape of the data
    cells.append(cell_creation.md_cell("##### Shapes of the data"))
    for data in config["path"]:
        cells.append(cell_creation.code_cell(f"{data}.shape"))

    vis = config["visualizations"]

    ## Head & tail of the data
    cells.append(cell_creation.md_cell("##### Head & Tail of the data"))
    cells.append(cell_creation.code_cell(f"{vis}.head()"))
    cells.append(cell_creation.code_cell(f"{vis}.tail()"))

    ## No. of null values
    cells.append(cell_creation.md_cell("##### No. of null values per column"))
    cells.append(cell_creation.code_cell(f"{vis}.isnull().sum()"))

    return cells
