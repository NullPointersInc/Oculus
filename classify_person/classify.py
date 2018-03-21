import math
import os
import sys
import imutils
import cv2
from google_speech import Speech
import tensorflow as tf

os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'

image_path = sys.argv[1]

# image = cv2.imread(image_path)
# image = imutils.rotate(image, 270)
# cv2.imwrite('image.jpg', image)
# # change this as you see fit
#
# image_path = "image.jpg"


# Read in the image_data
image_data = tf.gfile.FastGFile(image_path, 'rb').read()

# Loads label file, strips off carriage return
label_lines = [line.rstrip() for line
               in tf.gfile.GFile("retrained_labels.txt")]

# Unpersists graph from file
with tf.gfile.FastGFile("retrained_graph.pb", 'rb') as f:
    graph_def = tf.GraphDef()
    graph_def.ParseFromString(f.read())
    tf.import_graph_def(graph_def, name='')

with tf.Session() as sess:
    # Feed the image_data as input to the graph and get first prediction
    softmax_tensor = sess.graph.get_tensor_by_name('final_result:0')

    predictions = sess.run(softmax_tensor,
                           {'DecodeJpeg/contents:0': image_data})

    # Sort to show labels of first prediction in order of confidence
    top_k = predictions[0].argsort()[-len(predictions[0]):][::-1]

    speak_string = "This looks like "
    # Display the predicted result
    for node_id in top_k[0:1]:
        human_string = label_lines[node_id]
        score = predictions[0][node_id]
        speak_string = speak_string + str(human_string) + " probability is "
        format_score = score * 100
        format_score = math.ceil(format_score * 100) / 100
        speak_string = speak_string + str(format_score)
        print('%s (score = %.5f)' % (human_string, format_score))
        # os.system("google_speech -l en " + speak_string)
        speech = Speech(speak_string, lang="en")
        sox_effects = ("speed", "1")
        speech.play(sox_effects)
