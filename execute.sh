#! /bin/sh
echo "Initiating data_collection"
python3 src/data_collection.py
echo "Data collection finished"

echo "Initiating data processing"
python3 src/data_preprocessing.py
echo "Data processing finished"

echo "Visualizing data"
python3 src/visualization.pycd
