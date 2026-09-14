# Run Birdnet

import birdnet

# Select model
model_onnx = birdnet.load("acoustic", "3.0", "onnx")

# Can also specify the floating point 16 model, which is supposed to be small and faster with the same results.  
birdnet.load("acoustic", "3.0", "onnx", precision="fp16")

# Run prediction model
predictions_onnx = model_onnx.predict("audio_files/soundscape.wav")

# The V3.0 model is for about 11,000 species. The output can be restricted to a defined species list. 
# This might be a good idea. 
predictions = model.predict(
  "audio_files/soundscape.wav",
  # predict only the species from the file
  custom_species_list="example/species_list.txt",
)

# Alternatively, a species list can be generated using birdnet geomodel given a set of coordinates. 
model = birdnet.load("geo", "3.0", "onnx")
predictions = model.predict(50, -123, week=24)
predictions.to_csv("outputs/location.csv")

# Could work with the data in Pandas to stay with Python. 
# Or export to csv and then work in R. 
predictions_onnx.to_csv("outputs/results.csv")

# Multi-file example
predictions_onnx = model_onnx.predict("audio_files/h63/")
predictions_onnx.to_csv("outputs/results.csv")
