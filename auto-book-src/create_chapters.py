import os
import yaml
import shutil

def create_chapter_folders(repo_path, toc_file, source_directory, examples_directory, tests_directory):
    with open(toc_file, 'r') as f:
        toc = yaml.safe_load(f)

    for entry in toc:
        if 'part' in entry:
            section_folder = entry['part'].replace(' ', '_')
            for chapter in entry['chapters']:
                chapter_file = chapter['file']
                chapter_folder = chapter_file.split('/')[1] if '/' in chapter_file else chapter_file
                chapter_path = os.path.join(repo_path, section_folder, chapter_folder)

                # Create the main chapter folder if it doesn't exist
                if not os.path.exists(chapter_path):
                    os.makedirs(chapter_path)

                # If the chapter is in Section 3, create src, test, and examples subfolders
                if section_folder == "Section_3":
                    subfolders = ['src', 'test', 'examples']
                    for subfolder in subfolders:
                        subfolder_path = os.path.join(chapter_path, subfolder)
                        if not os.path.exists(subfolder_path):
                            os.makedirs(subfolder_path)

                        # Move existing files to the new structure
                        try:
                            src_path = os.path.join(source_directory, chapter_folder)
                            if subfolder == "src" and not os.path.exists(os.path.join(subfolder_path, chapter_folder)) and os.path.exists(src_path):
                                shutil.move(src_path, subfolder_path)
                            elif subfolder == "examples":
                                src_path = os.path.join(examples_directory, chapter_folder)
                                if not os.path.exists(os.path.join(subfolder_path, chapter_folder)) and os.path.exists(src_path):
                                    shutil.move(src_path, subfolder_path)
                            elif subfolder == "test":
                                src_path = os.path.join(tests_directory, chapter_folder)
                                if not os.path.exists(os.path.join(subfolder_path, chapter_folder)) and os.path.exists(src_path):
                                    shutil.move(src_path, subfolder_path)
                        except FileNotFoundError:
                            print(f"Skipping {subfolder} for {chapter_folder}, folder not found.")

toc_path = "_toc.yaml"
repo_directory = "."
source_directory = "./section_3/src"
examples_directory = "./section_3/examples"
tests_directory = "./section_3/tests"
create_chapter_folders(repo_directory, toc_path, source_directory, examples_directory, tests_directory)
