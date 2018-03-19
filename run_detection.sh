#!/usr/bin/env bash

# Oculus unified script

# This needs to be run from the root of the project directory

# This script executes python scripts from "classify_notes", "classify_person", "object_detection"

if [ "$1" = "-o" ]; then
		# From Oculus/
		cd object_detection
		python3 oculus.py
		cd ..

elif [ "$1" = "-p" ]; then
		# From Oculus/
		cd classify_person
		python3 classify.py image.jpg
		cd ..

elif [ "$1" = "-n" ]; then
		# From Oculus/
		cd classify_note
		python3 classify.py image.jpg
		cd ..

elif [ "$1" = "-l" ]; then
		# From Oculus/
		sh run.sh

elif [ "$1" = "-h" ]; then
		echo "Usage: sh run_detection.sh option"
		echo "options:"
		echo "-o : run object recognition"
		echo "-p : run face recognition"
		echo "-n : run note recognition"
		echo "-l : run image labelling"
		echo "-h : help"
		echo ""
		echo "Example:"
		echo "To run face recognition,"
		echo "sh run_detection.sh -p"
else
		echo "Invalid option, please use -h for help menu"
fi
