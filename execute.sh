#! /bin/sh
echo "Initiating data_collection"
python src/data_collection.py
echo "Data collection finished"

echo "Initiating data processing"
python src/data_preprocessing.py
echo "Data processing finished"

echo "Visualizing data"
python src/visualization.pycd