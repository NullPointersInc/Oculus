# From Oculus/
protoc object_detection/protos/*.proto --python_out=.

# From Oculus/
export PYTHONPATH=$PYTHONPATH:`pwd`:`pwd`/slim

# From Oculus/
python object_detection/builders/model_builder_test.py

# From Oculus/object_detection
cd object_detection
jupyter notebook object_detection_tutorial.ipynb
