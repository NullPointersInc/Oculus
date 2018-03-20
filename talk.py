from google_speech import Speech

speak_file = open("output.txt", "r")
speak = speak_file.read()
speech = Speech(speak, lang="en")
sox_effects = ("speed", "1")
speech.play(sox_effects)
