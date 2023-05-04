from design_thread import nx

# Define the design parameters
dimensions = (10, 20, 30)
material = "steel"

# Create the 3D model
model = nx.create_model(dimensions, material)

# Save the model to a file
nx.save_model(model, "part.prt")
