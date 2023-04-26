import os
import yaml

def create_file_structure(file_structure, root_dir):
    """
    Creates the file and folder structure based on the YAML file.
    """
    for item in file_structure:
        for folder, contents in item.items():
            folder_path = os.path.join(root_dir, folder)
            os.makedirs(folder_path, exist_ok=True)

            if isinstance(contents, dict):
                create_file_structure([contents], folder_path)
            else:
                for file in contents:
                    if isinstance(file, str):
                        file_path = os.path.join(folder_path, file)
                        open(file_path, 'w').close()
                    else:
                        create_file_structure([file], folder_path)

if __name__ == '__main__':
    with open('digital_twin_guide.yaml') as f:
        file_structure = yaml.load(f, Loader=yaml.FullLoader)

    create_file_structure(file_structure, os.getcwd())