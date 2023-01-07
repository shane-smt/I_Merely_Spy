from csv import reader


def import_csv_layout(filepath: str) -> list:
    terrain = []
    with open(filepath) as level:
        layout = reader(level, delimiter=",")
        for row in layout:
            terrain.append(list(row))
        return terrain
