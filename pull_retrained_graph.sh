cd classify_note
wget -O retrained_graph.pb https://www.dropbox.com/s/pso39wq6z01jtli/retrained_graph.pb?dl=1
wget -O retrained_labels.txt https://www.dropbox.com/s/ad9pxe60nib0wiv/retrained_labels.txt?dl=1
cd ..

echo "retrained graph & labels for classifying note downloaded successfully"

cd classify_person
wget -O retrained_graph.pb https://www.dropbox.com/s/xcfgw7qb42npwld/retrained_graph.pb?dl=1
wget -O retrained_labels.txt https://www.dropbox.com/s/6hks023tcws5hzd/retrained_labels.txt?dl=1
cd ..

echo "retrained graph & labels for classifying person downloaded successfully"

cd object_detection/object_detection
mkdir model_to_use && cd model_to_use
wget -O frozen_inference_graph.pb https://www.dropbox.com/s/glznbxe3c9inoqo/frozen_inference_graph.pb?dl=1
cd ../../..

echo "frozen inference graph for classifying object downloaded successfully"
