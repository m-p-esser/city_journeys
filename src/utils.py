import pathlib


def find_root(start_from=__file__, indicators=[".env", "pyproject.toml"]):
    found_root_dir = False
    search_dir = pathlib.Path(start_from).parent

    while found_root_dir == False:
        print(f"Checking directory: {search_dir}")
        file_paths = list(search_dir.glob("*.*"))
        for idx, fp in enumerate(file_paths):
            if fp.name in indicators:
                root_dir = search_dir
                print(f"Root directory found \n. The Root directory is: {root_dir}")
                found_root_dir == True
                return root_dir
            if idx + 1 == len(file_paths):
                search_dir = search_dir.parent


def recursively_find_file(root_dir: pathlib.Path, file_name):

    file_paths = root_dir.rglob(file_name)
    first_found_file_path = list(file_paths)[0]

    return first_found_file_path


if __name__ == "__main__":
    root_dir = find_root()
    recursively_find_file(root_dir, 'cities.csv')