from google_speech import Speech
#


def sp(speak):
    speech = Speech(speak, lang="en")
    sox_effects = ("speed", "1")
    speech.play(sox_effects)


def process(source):
    pos = source.rindex('(')
    sp(str(source[: pos]))


# Ignore first line
n = input()

# First line
sp("Looks like the situation is one of the following:")

# Line 1
n = input()
a = "Either " + str(n[n.index(')') + 2:])
process(a)

# Line 2
n = input()
a = "Or " + str(n[n.index(')') + 2:])
process(a)

# Line 3
n = input()
a = "Or maybe " + str(n[n.index(')') + 2:])
process(a)
