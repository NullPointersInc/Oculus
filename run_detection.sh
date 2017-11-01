# From Oculus/
protoc object_detection/protos/*.proto --python_out=.

# From Oculus/
export PYTHONPATH=$PYTHONPATH:`pwd`:`pwd`/slim

# From Oculus/object_detection
cd object_detection
python3 oculus.py

# Come back to parent dir
cd ..
