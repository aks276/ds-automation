import cell_creation


def get_data_cells(config):
    test_size = config["test_split"] if "test_split" in config else 0.2
    cells = []
    path = config["path"]
    cells.append(cell_creation.md_cell("#### Splitting the data"))
    for data, path in path.items():
        cells.append(
            cell_creation.code_cell(f"{data}_y = {data}['{config['target_col']}']")
        )
        cells.append(
            cell_creation.code_cell(
                f"{data}_X = {data}.drop(['{config['target_col']}'], axis=1)"
            )
        )
    if len(config["path"]) < 2:
        cells.append(
            cell_creation.code_cell(
                "from sklearn.model_selection import train_test_split"
            )
        )
        cells.append(
            cell_creation.code_cell(
                f"X_train, X_test, y_train, y_test = train_test_split(train_data_X, train_data_y, test_size={test_size})"
            )
        )
    return cells
