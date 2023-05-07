import os
import yaml

def create_chapter_folders(repo_path, toc_file):
    with open(toc_file, 'r') as f:
        toc = yaml.safe_load(f)

    for entry in toc:
        chapter_folder = entry['file'].split('/')[0]
        chapter_path = os.path.join(repo_path, chapter_folder)

        # Create the main chapter folder if it doesn't exist
        if not os.path.exists(chapter_path):
            os.makedirs(chapter_path)

        # Create subfolders for src, test, examples, and interactive
        subfolders = ['src', 'test', 'examples', 'interactive']
        for subfolder in subfolders:
            subfolder_path = os.path.join(chapter_path, subfolder)
            if not os.path.exists(subfolder_path):
                os.makedirs(subfolder_path)

repo_directory = "."
toc_path = "_toc.yml"
create_chapter_folders(repo_directory, toc_path)
