import os


def move_file(command: str) -> None:
    command_elements = command.split()

    if len(command_elements) != 3:
        return

    if command_elements[0] != "mv":
        return

    _, source_file_name, destination_file_name = command_elements

    try:
        with open(source_file_name, "r") as source_file:
            content = source_file.read()

        os.remove(source_file_name)

        if "/" in destination_file_name:

            *path_folders, _ = destination_file_name.split("/")

            for i in range(len(path_folders)):
                path_to_folder = "/".join(path_folders[: i + 1])

                try:
                    os.mkdir(path_to_folder)

                except FileExistsError:
                    print(f"folder {path_to_folder} exists!")

        with open(destination_file_name, "w") as destination_file:
            destination_file.write(content)

    except FileNotFoundError:
        print(f'file "{source_file_name}" not found')
