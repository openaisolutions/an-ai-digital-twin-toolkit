# training_thread/training.py

class Training:
    def __init__(self):
        self.training_materials = []

    def create_training_material(self, title, content):
        """
        Create a training material with a title and content.

        Args:
            title (str): The title of the training material.
            content (str): The content of the training material.
        """
        training_material = {"title": title, "content": content}
        self.training_materials.append(training_material)

    def get_all_training_materials(self):
        """
        Retrieve all training materials created in the current Training instance.

        Returns:
            list: A list of dictionaries containing the training material's title and content.
        """
        return self.training_materials

    def find_training_material_by_title(self, title):
        """
        Search for a training material by its title.

        Args:
            title (str): The title of the training material to search for.

        Returns:
            dict: The training material with the specified title, or None if not found.
        """
        for material in self.training_materials:
            if material["title"] == title:
                return material
        return None

