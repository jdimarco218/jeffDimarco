import random

DEBUG = True

class Groove(object):
    """
    " Holds the entire groove.
    "
    " Design:
    "  The next note is chosen with a random weighting system.  There are
    "  multiple weightings used. Most weightings are stochastic and can work
    "  without a history of the preceding melody notes (minimal exceptions).
    "  Scale - The 1,3,5 of the current harmony chord are weighted higher
    "  in the melody
    "  Proximity - Closer notes to the current note is weighted higher
    "  while the current note has a unique weighting (default low).
    "  Starting Range - Notes closer to the starting octave roote note are
    "  weighted slightly higher.
    "  1 Jump - 
    "  6 Jump - 
    "  Sequence offest - 
    "  
    " Attributes:
    "     TODO
    """
    
    # number of steps skipped for this note on the scale
    scaleSteps = [0, 1, 2, 2, 3, 4, 5, 5, 6, 7, 7, 8, 9, 10, 10]
    # whole, whole, half, whole, whole, whole, half

    allNotesList = ["C0","CsDf0","D0","DsEf0","E0","F0","FsGf0","G0","GsAf0","A0","AsBf0","B0",
                    "C1","CsDf1","D1","DsEf1","E1","F1","FsGf1","G1","GsAf1","A1","AsBf1","B1",
                    "C2","CsDf2","D2","DsEf2","E2","F2","FsGf2","G2","GsAf2","A2","AsBf2","B2",
                    "C3","CsDf3","D3","DsEf3","E3","F3","FsGf3","G3","GsAf3","A3","AsBf3","B3",
                    "C4","CsDf4","D4","DsEf4","E4","F4","FsGf4","G4","GsAf4","A4","AsBf4","B4",
                    "C5","CsDf5","D5","DsEf5","E5","F5","FsGf5","G5","GsAf5","A5","AsBf5","B5",
                    "C6","CsDf6","D6","DsEf6","E6","F6","FsGf6","G6","GsAf6","A6","AsBf6","B6",
                    "C7","CsDf7","D7","DsEf7","E7","F7","FsGf7","G7","GsAf7","A7","AsBf7","B7",
                    "C8"]
    allTMNotesList=["C0","Db0","D0","Eb0","E0","F0","Gb0","G0","Ab0","A0","Bb0","B0",
                    "C1","Db1","D1","Eb1","E1","F1","Gb1","G1","Ab1","A1","Bb1","B1",
                    "C2","Db2","D2","Eb2","E2","F2","Gb2","G2","Ab2","A2","Bb2","B2",
                    "C3","Db3","D3","Eb3","E3","F3","Gb3","G3","Ab3","A3","Bb3","B3",
                    "C4","Db4","D4","Eb4","E4","F4","Gb4","G4","Ab4","A4","Bb4","B4",
                    "C5","Db5","D5","Eb5","E5","F5","Gb5","G5","Ab5","A5","Bb5","B5",
                    "C6","Db6","D6","Eb6","E6","F6","Gb6","G6","Ab6","A6","Bb6","B6",
                    "C7","Db7","D7","Eb7","E7","F7","Gb7","G7","Ab7","A7","Bb7","B7",
                    "C8"]

    allFreqsList = ["%-48", "%-47", "%-46", "%-45", "%-44", "%-43", "%-42", "%-41", "%-40", "%-39", "%-38", "%-37", "%-36", "%-35", "%-34", "%-33", "%-32", "%-31", "%-30", "%-29", "%-28", "%-27", "%-26", "%-25", "%-24", "%-23", "%-22", "%-21", "%-20", "%-19", "%-18", "%-17", "%-16", "%-15", "%-14", "%-13", "%-12", "%-11", "%-10", "%-9", "%-8", "%-7", "%-6", "%-5", "%-4", "%-3", "%-2", "%-1","%+0", "%+1", "%+2", "%+3", "%+4", "%+5", "%+6", "%+7", "%+8", "%+9", "%+10", "%+11", "%+12", "%+13", "%+14", "%+15", "%+16", "%+17", "%+18", "%+19", "%+20", "%+21", "%+22", "%+23", "%+24", "%+25", "%+26", "%+27", "%+28", "%+29", "%+30", "%+31", "%+32", "%+33", "%+34", "%+35", "%+36", "%+37", "%+38", "%+39", "%+40", "%+41", "%+42", "%+43", "%+44", "%+45", "%+46", "%+47", "%+48"]

    durationMapToStr = {1.0:"w", 0.5:"h", 0.25:"q", 0.125:"e", 0.0625:"s"}

    allNotesFreqsDict = {}

    phraseDuration = 1.0

    def __init__(self, attributeList, key="C", chordProgression=[0,3,4,3]):#bwo=3, bdo=2, bdf=3.25, pwo=10, pwf=1.8, sjwo=2, lnjwo=2, rf=0, rc=17):
        """ TODO """
        for i in range(len(self.allNotesList)):
            self.allNotesFreqsDict[self.allNotesList[i]] = self.allFreqsList[i]
        self.key = key 
        self.bpm = 80
        self.range = 2
        self.phraseCount = 4
        # Input parameters
        self.chordProgression = chordProgression # 1-4-5-4 default
        # Determine which attributes are present otherwise use default values
        receivedAttributeList = []
        if len(attributeList) > 0 and attributeList[0] != "":
            receivedAttributeList.append(attributeList[0])
        else:
            receivedAttributeList.append(3) # Default value
        if len(attributeList) > 1 and attributeList[1] != "":
            receivedAttributeList.append(attributeList[1])
        else:
            receivedAttributeList.append(2) # Default value
        if len(attributeList) > 2 and attributeList[2] != "":
            receivedAttributeList.append(attributeList[2])
        else:
            receivedAttributeList.append(3.25) # Default value
        if len(attributeList) > 3 and attributeList[3] != "":
            receivedAttributeList.append(attributeList[3])
        else:
            receivedAttributeList.append(10) # Default value
        if len(attributeList) > 4 and attributeList[4] != "":
            receivedAttributeList.append(attributeList[4])
        else:
            receivedAttributeList.append(1.8) # Default value
        if len(attributeList) > 5 and attributeList[5] != "":
            receivedAttributeList.append(attributeList[5])
        else:
            receivedAttributeList.append(2) # Default value

        #self.baseWeightOffset = bwo # Used to normalize weights across types
        #self.baseDistanceOffset = bdo
        #self.baseDistanceFactor = bdf
        #self.proximityWeightOffset = pwo
        #self.proximityWeightFactor = pwf 
        #self.sixJumpWeightOffset = sjwo
        self.lastNoteJumpWeightOffset = 2
        self.rangeFloor = 0
        self.rangeCeil  = 17 # Two octaves plus current note
        # Generate!
        self.melody = Melody(self.phraseCount, receivedAttributeList[0], receivedAttributeList[1], receivedAttributeList[2], receivedAttributeList[3], receivedAttributeList[4], receivedAttributeList[5], self.lastNoteJumpWeightOffset, self.rangeFloor, self.rangeCeil)

    def genMelody(self):
        """ Create the underlying before the melodies over top of them """
        underlyingOffset = 2
        for currPhrase in range(self.phraseCount):
            # Get current chord for this phrase and offset it
            self.melody.phraseList[currPhrase].underlyingList.append(Note(self.chordProgression[currPhrase], underlyingOffset)) 
        for currPhrase in range(self.phraseCount):
            self.genPhraseMelody(currPhrase)

    def genPhraseMelody(self, phraseNum):
        """ Generate melodic notes """
        duration = 0
        choiceDuration = 0.25
        while duration < Groove.phraseDuration:
        #for i in range(8):
            #if i == 0 and phraseNum == 0:
            if duration == 0 and phraseNum == 0:
                """ Gen initial note """
                self.melody.phraseList[phraseNum].noteList.append(Note(0))
                duration += self.melody.phraseList[phraseNum].noteList[0].duration
            else:
                """ Gen next note """
                if self.melody.phraseList[phraseNum].noteList:
                    currNote = self.melody.phraseList[phraseNum].noteList[-1]
                    # TODO figure out more normal way to calc this lol
                    # TODO use previous duration as a factor???
                    # Set weights for duration
                    durationWeights = [  2,   4,   10,    10,      0]
                    #                 whol, haf, quar, eight, sixtee, thirty2
                    durationVals =    [1.0, 0.5, 0.25, 0.125, 0.0625]
                    # Remove weights that will not fit into remaining phrase
                    for i in range(len(durationVals)):
                        if durationVals[i] > (Groove.phraseDuration - duration):
                            durationWeights[i] = 0
                    # TODO
                    if DEBUG:
                        print "Currently assigned duration: " + str(duration)
                        for currDuration in durationWeights: 
                            print str(currDuration ) + ", "
                        print ""
                    # Pick a duration based on the weights
                    wSum = sum(x for x in durationWeights)
                    choiceVal = random.uniform(0, wSum)
                    checkVal = 0
                    for i in range(len(durationWeights)): 
                        checkVal += durationWeights[i] # weight index
                        if checkVal > choiceVal:
                            break; # we use the current weight
                    # HERE 
                    choiceDuration = durationVals[i]
                else:
                    # If this is the first note of the phrase, use last phrase's last note
                    currNote = self.melody.phraseList[phraseNum-1].noteList[-1]
                isLastNoteInPhrase = False
                if duration + choiceDuration >= Groove.phraseDuration:
                    isLastNoteInPhrase = True
                self.melody.phraseList[phraseNum].noteList.append(self.melody.genNextNote(currNote, phraseNum, isLastNoteInPhrase))
                self.melody.phraseList[phraseNum].noteList[-1].duration = choiceDuration
                duration += self.melody.phraseList[phraseNum].noteList[-1].duration


    def printGroove(self):
        print "### Groove ###\n"
        for i in range(len(self.melody.phraseList)):
            print "  --Phrase " + str(i) + "--"
            """ Print each note in the current phrase with duration, melody """
            for note in self.melody.phraseList[i].noteList:
                print str(note.noteVal) + "." + str(note.octave) + str(self.durationMapToStr[note.duration]) + " ",
            print ""
            """ Print each note in the current phrase, underlying """
            for note in self.melody.phraseList[i].underlyingList:
                print str(note.noteVal) + "." + str(note.octave) + " ",
            print ""


class Note(object):
    """
    " TODO
    """

    def __init__(self, noteVal, octave=4, duration=0.25):
        """ TODO """
        self.noteVal = noteVal
        self.octave = octave
        self.duration = duration 

    def __str__(self):
        print str(self.noteVal)

class Melody(object):
    """
    " TODO
    """

    def __init__(self, phraseCount, bwo, bdo, bdf, pwo, pwf, sjwo, lnjwo, rf, rc):
        self.phraseList = []
        for i in range(phraseCount):
            self.phraseList.append(Phrase(i))
        """ TODO """
        self.baseWeightOffset = bwo # Used to normalize weights across types
        self.baseDistanceOffset = bdo
        self.baseDistanceFactor = bdf
        self.proximityWeightOffset = pwo
        self.proximityWeightFactor = pwf 
        self.sixJumpWeightOffset = sjwo
        self.lastNoteJumpWeightOffset = lnjwo
        self.rangeFloor = rf
        self.rangeCeil  = rc

    def genNextNote(self, currNote, phraseNum, isLastNoteInPhrase = False):
        weights = {}
        self.genNoteWeights(weights, currNote, phraseNum, isLastNoteInPhrase)
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

    def genNoteWeights(self, weights, currNote, phraseNum, isLastNoteInPhrase):

        """ Generate a range one octave down and up """
        baseWeightOffset = self.baseWeightOffset # Used to normalize weights across types
        baseDistanceOffset = self.baseDistanceOffset
        baseDistanceFactor = self.baseDistanceFactor
        proximityWeightOffset = self.proximityWeightOffset 
        proximityWeightFactor = self.proximityWeightFactor
        sixJumpWeightOffset = self.sixJumpWeightOffset
        lastNoteJumpWeightOffset = self.lastNoteJumpWeightOffset
        rangeFloor = self.rangeFloor
        rangeCeil  = self.rangeCeil
        #if currNote.octave == 0:
        if currNote.octave <= 3:
            rangeFloor = 8 - currNote.noteVal # skip that many notes off the bottom
        maxOctave = 5
        if currNote.octave >= maxOctave:
            rangeCeil = 17 - currNote.noteVal - 12*(abs(maxOctave-currNote.octave)) # skip that many notes off the top

        for i in range(rangeFloor, rangeCeil):

            """ Determine notes octave """
            nextNoteVal = (currNote.noteVal - 8 + i) % 8
            nextOctave = currNote.octave
            if (currNote.noteVal - 8 + i) < 0:
                nextOctave = currNote.octave - 1
            elif (currNote.noteVal - 8 + i) >= 8:
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

            """ Weigh closer to the root slightly higher """
            nextProximityWeight = proximityWeightOffset - proximityWeightFactor * (abs(nextOctave - 4)) # 4 is root octave

            """ Weigh the six note jump slightly higher """
            sixJumpWeight = 0
            if abs( (nextOctave*8+nextNoteVal) - (currNote.octave*8+currNote.noteVal)) == 6:
                sixJumpWeight = sixJumpWeightOffset

            """ Weigh the last note jumping the next root slightly higher """
            lastNoteJumpWeight = 0
            if isLastNoteInPhrase:
                nextPhraseRoot = 0
                if phraseNum >= 0 and phraseNum < len(self.phraseList):
                    nextPhraseRoot = phraseNum
                if abs(self.phraseList[nextPhraseRoot].noteList[0].noteVal - nextNoteVal) == 1:
                    lastNoteJumpWeight = lastNoteJumpWeightOffset

            weights[i] = [Note(nextNoteVal, nextOctave), nextDistanceWeight + nextScaleWeight + nextProximityWeight + sixJumpWeight + lastNoteJumpWeight] 

class Phrase(object):
    """
    " TODO
    """

    def __init__(self, phraseNum):
        self.noteList = []
        self.underlyingList = []
        self.phraseNum = phraseNum
        """ TODO """
