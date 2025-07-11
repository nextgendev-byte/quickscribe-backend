from data.translated import translation


def write_file_from_array(file_path, array):
    with open(file_path, "w") as file:
        for item in array:
            file.write(f"{item}")
            print("ROUND 1")
        print("FILE Written")


write_file_from_array("uploads/output.txt", translation)
