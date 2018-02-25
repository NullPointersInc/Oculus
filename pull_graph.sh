#!/usr/bin/env bash

# Script to pull retrained and inference graphs

# This needs to be run from the root of the project directory

# This script pulls retrained graph, labels and frozen inference graphs for classifying notes from public dropbox link

if [ "$1" = "-n" ]; then
		# From Oculus/
		cd classify_note
		wget -O retrained_graph.pb https://www.dropbox.com/s/pso39wq6z01jtli/retrained_graph.pb?dl=1
		wget -O retrained_labels.txt https://www.dropbox.com/s/ad9pxe60nib0wiv/retrained_labels.txt?dl=1
		cd ..
		echo "retrained graph & labels for classifying note downloaded successfully"

elif [ "$1" = "-o" ]; then
		# From Oculus/
		cd object_detection/object_detection
		if [ -d "model_to_use" ]; then
  			rm -rf model_to_use
		fi
		mkdir model_to_use && cd model_to_use
		wget -O frozen_inference_graph.pb https://www.dropbox.com/s/glznbxe3c9inoqo/frozen_inference_graph.pb?dl=1
		cd ../../..
		echo "frozen inference graph for classifying object downloaded successfully"

elif [ "$1" = "-a" ]; then
		# From Oculus/
		cd classify_note
		wget -O retrained_graph.pb https://www.dropbox.com/s/pso39wq6z01jtli/retrained_graph.pb?dl=1
		wget -O retrained_labels.txt https://www.dropbox.com/s/ad9pxe60nib0wiv/retrained_labels.txt?dl=1
		cd ..
		echo "retrained graph & labels for classifying note downloaded successfully"

		cd object_detection/object_detection
		if [ -d "model_to_use" ]; then
  			rm -rf model_to_use
		fi
		mkdir model_to_use && cd model_to_use
		wget -O frozen_inference_graph.pb https://www.dropbox.com/s/glznbxe3c9inoqo/frozen_inference_graph.pb?dl=1
		cd ../../..
		echo "frozen inference graph for classifying object downloaded successfully"

elif [ "$1" = "-h" ]; then
		echo "Usage: sh pull_graph.sh option"
		echo "options:"
		echo "-o : pull inference graph for object recognition"
		echo "-n : pull retrained graph and labels for note recognition"
		echo "-a : pull both the graphs"
		echo "-h : help"
		echo ""
		echo "Example:"
		echo "To pull inference graph,"
		echo "sh pull_graph.sh -o"

else
		echo "Invalid option, please use -h for help menu"
fi
