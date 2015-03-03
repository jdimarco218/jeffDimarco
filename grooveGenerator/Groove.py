import random

DEBUG = True

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
        self.phraseCount = 4
        self.chordProgression = [0, 3, 4, 3] # 1-4-5-4 default
        self.melody = Melody(self.phraseCount)

    def genMelody(self):
        for currPhrase in range(self.phraseCount):
            self.genPhrase(currPhrase)

    def genPhrase(self, phrase):
        """ Generate melodic notes """
        for i in range(8):
            if i == 0:
                """ Gen initial note """
                self.melody.phraseList[phrase].noteList.append(Note(0))
            else:
                """ Gen next note """
                currNote = self.melody.phraseList[phrase].noteList[i-1]
                self.melody.phraseList[phrase].noteList.append(self.melody.genNextNote(currNote))
        """ Generate underlying """
        startingOctave = self.melody.phraseList[0].noteList[0].octave # Use the very first note's octave as a reference
        if startingOctave >= 2: # Get lower if possible, TODO it might sound bad if not going lower
            startingOctave -= 2
        else:
            startingOctave = 0
        # Get current chord for this phrase
        self.melody.phraseList[phrase].underlyingList.append(Note(self.chordProgression[phrase], startingOctave)) 


    def printGroove(self):
        print "### Groove ###\n"
        for i in range(len(self.melody.phraseList)):
            print "  --Phrase " + str(i) + "--"
            """ Print each note in the current phrase, melody """
            for note in self.melody.phraseList[i].noteList:
                print str(note.noteVal) + "." + str(note.octave) + " ",
            print ""
            """ Print each note in the current phrase, underlying """
            for note in self.melody.phraseList[i].underlyingList:
                print str(note.noteVal) + "." + str(note.octave) + " ",
            print ""


class Note(object):
    """
    " TODO
    """

    def __init__(self, noteVal, octave=4):
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
            self.phraseList.append(Phrase(i))
        """ TODO """

    def genNextNote(self, currNote):
        weights = {}
        self.genNoteRange(weights, currNote)
        if DEBUG:
            for currList in weights.values():
                print "Note: " + str(currList[0].noteVal) + "." + str(currList[0].octave) + "  w: " + str(currList[1])
            print ""
        """ Pick a value based on the weights """
        wSum = sum(x[1] for x in weights.values())
        choiceVal = random.uniform(0, wSum)
        checkVal = 0
        for weight in weights.items():
            checkVal += weight[1][1] # weight index
            if checkVal > choiceVal:
                break; # we use the current weight
        return weight[1][0] # Note index

    def genNoteRange(self, weights, currNote):

        """ Generate a range one octave down and up """
        baseWeightOffset = 3 # Used to normalize weights across types
        baseDistanceOffset = 2
        baseDistanceFactor = 1.25
        rangeFloor = 0
        rangeCeil  = 17 # Two octaves plus current note
        if currNote.octave == 0:
            rangeFloor = 8 - currNote.noteVal # skip that many notes off the bottom

        for i in range(rangeFloor, rangeCeil):

            """ Determine notes octave """
            nextNoteVal = (currNote.noteVal - 8 + i) % 8
            nextOctave = currNote.octave
            if (currNote.noteVal - 8 + i) < 0:
                nextOctave = currNote.octave - 1
            elif (currNote.noteVal - 8 + i) > 8:
                nextOctave = currNote.octave + 1

            """ Weight equal to number of steps difference """
            absDistance = abs((currNote.noteVal + currNote.octave * 8) - (nextNoteVal + nextOctave * 8))
            invertedDistance = ((rangeCeil - 1) / 2) - absDistance # Close notes should have higher weights
            nextDistanceWeight = baseDistanceOffset + baseDistanceFactor * invertedDistance
            """ Special rule! Avoid same note again """
            if nextNoteVal == currNote.noteVal and nextOctave == currNote.octave:
                nextDistanceWeight = 0 # TODO: determine how to handle same note if wanted

            """ Weigh the 1 highest, 3 & 5 medium, and the rest low """
            nextScaleWeight = 2
            if nextNoteVal == 0:
                nextScaleWeight = baseWeightOffset * 3
            elif nextNoteVal == 2 or nextNoteVal == 4:
                nextScaleWeight = baseWeightOffset * 2
            else: 
                nextScaleWeight = baseWeightOffset

            weights[i] = [Note(nextNoteVal, nextOctave), nextDistanceWeight + nextScaleWeight] 

class Phrase(object):
    """
    " TODO
    """

    def __init__(self, phraseNum):
        self.noteList = []
        self.underlyingList = []
        self.phraseNum = phraseNum
        """ TODO """
