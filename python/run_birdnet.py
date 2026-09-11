# Runn Birdnet

import birdnet

# Select model
model_onnx = birdnet.load("acoustic", "3.0", "onnx")

# Run prediction model
predictions_onnx = model_onnx.predict("audio_files/soundscape.wav")

# Could work with the data in Pandas. But export to csv
# and then work in R. 
predictions_onnx.to_csv("outputs/results.csv")

# Multi-file example
predictions_onnx = model_onnx.predict("audio_files/h63/")
predictions_onnx.to_csv("outputs/results.csv")
