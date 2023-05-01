from design_thread import nx
from design_thread import cam

# Define the design parameters
dimensions = (10, 20, 30)
material = "steel"

# Create the 3D model
model = nx.create_model(dimensions, material)

# Generate machine instructions
instructions = cam.generate_instructions(model, "toolpath.txt")

# Save the instructions to a file
cam.save_instructions(instructions, "instructions.txt")
