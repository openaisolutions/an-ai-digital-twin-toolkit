import os
import yaml

def update_toc(root_dir, existing_toc_file, output_toc_file):
    with open(existing_toc_file, 'r') as toc_file:
        existing_toc = yaml.safe_load(toc_file)

    toc_entries = []

    for root, dirs, files in os.walk(root_dir):
        for file in files:
            if file.endswith(".md") or file.endswith(".ipynb") or file.endswith(".py"):
                filepath = os.path.join(root, file)
                relative_filepath = os.path.relpath(filepath, root_dir)
                title = os.path.splitext(file)[0].replace('_', ' ').title()
                entry = {"file": relative_filepath, "title": title}
                toc_entries.append(entry)

    updated_toc = []

    for entry in existing_toc:
        for new_entry in toc_entries:
            if entry["file"] == new_entry["file"]:
                entry["title"] = new_entry["title"]
                toc_entries.remove(new_entry)
                break
        updated_toc.append(entry)

    updated_toc.extend(toc_entries)

    with open(output_toc_file, 'w') as toc_file:
        yaml.dump(updated_toc, toc_file)

root_directory = "."
existing_toc_path = "_toc.yaml"
output_toc_path = "path/to/your/updated/_toc.yml"
update_toc(root_directory, existing_toc_path, output_toc_path)

