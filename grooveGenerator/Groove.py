import random

class Groove(object):
    """
    " Holds the entire groove.
    "
    " Attributes:
    "     TODO
    """

    def __init__(self):
        """ TODO """
        self.key = "C"
        self.bpm = 80
        self.range = 2
        self.phraseCount = 1
        self.melody = Melody(self.phraseCount)

    def genMelody(self):

        for currPhrase in range(self.phraseCount):
            self.genPhrase(currPhrase)

    def genPhrase(self, phrase):
        for i in range(8):
            if i == 0:
                """ Gen initial note """
                self.melody.phraseList[phrase].noteList.append(Note(0))
            else:
                """ Gen next note """
                currNote = self.melody.phraseList[phrase].noteList[i-1]
                self.melody.phraseList[phrase].noteList.append(self.melody.genNextNote(currNote))

    def printGroove(self):
        print "Groove:"
        for i in range(self.phraseCount):
            print "  --Phrase " + str(i) + "--"
            for j in range(len(self.melody.phraseList)):
                """ Print each note in the current phrase """
                for note in self.melody.phraseList[j].noteList:
                    print str(note.octave) + "." + str(note.noteVal) + " ",
                print ""


class Note(object):
    """
    " TODO
    """

    def __init__(self, noteVal, octave=2):
        """ TODO """
        self.noteVal = noteVal
        self.octave = octave

    def __str__(self):
        print str(self.noteVal)

class Melody(object):
    """
    " TODO
    """

    def __init__(self, phraseCount):
        self.phraseList = []
        for i in range(phraseCount):
            self.phraseList.append(Phrase())
        """ TODO """

    def genNextNote(self, currNote):
        weights = {}
        self.genNoteRange(weights, currNote)
        """ Pick a value based on the weights """
        wSum = sum(x[1] for x in weights.values())
        choiceVal = random.randint(0, wSum)
        checkVal = 0
        for weight in weights.items():
            checkVal += weight[1][1] # weight index
            if checkVal > choiceVal:
                break; # we use the current weight
        return weight[1][0] # Note index

    def genNoteRange(self, weights, currNote):
        """ Generate a range one octave down and up """
        if currNote.octave < 1:
            print "Generating from a low octave of: " + str(currNote.octave)
        for i in range(15):
            """ Determine notes octave """
            nextNoteVal = (currNote.noteVal - 8 + i) % 8
            nextOctave = currNote.octave
            if (currNote.noteVal - 8 + i) < 0:
                nextOctave = currNote.octave - 1
            elif (currNote.noteVal - 8 + i) > 8:
                nextOctave = currNote.octave + 1
            """ Weight equal to number of steps difference """
            nextDistanceWeight = abs((currNote.noteVal + currNote.octave * 8) - (nextNoteVal + nextOctave * 8))
            """ Weigh the 1 highest, 3 & 5 medium, and the rest low while the same note is lowest """
            nextScaleWeight = 2
            if nextNoteVal == 1:
                nextScaleWeight = 8
            elif nextNoteVal == 3 or nextNoteVal == 5:
                nextScaleWeight = 5
            elif nextNoteVal == currNote.noteVal:
                nextScaleWeight = 1
            else: 
                nextScaleWeight = 3
            weights[i] = [Note(nextNoteVal, nextOctave), nextDistanceWeight + nextScaleWeight] 

class Phrase(object):
    """
    " TODO
    """

    def __init__(self):
        self.noteList = []
        """ TODO """
