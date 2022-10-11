import cell_creation


def read_csv_to_dataframe(config: dict):
    if "path" not in config:
        raise ValueError("'path' key not found in config")
    cells = []
    paths = config["path"]
    for data, path in paths.items():
        cells.append(cell_creation.code_cell(f"{data} = pd.read_csv({path})\n"))
    return cells
