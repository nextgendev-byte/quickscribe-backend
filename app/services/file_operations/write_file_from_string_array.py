def write_file_from_array(file_path, array):
    with open(file_path, "w") as file:
        for index, item in enumerate(array):
            file.write(f"{item}\n")
            print(f"ROUND {index + 1}")
        print(f"Result is ready at {file_path}")
