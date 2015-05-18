import numpy as np

# k-nearest neighbors for hand written number determination.
def main(trainFeatures, trainLabels, valFeatures, valLabels, testFeatures, k):
    # main('digitsDataset/trainFeatures.csv','digitsDataset/trainLabels.csv','digitsDataset/valFeatures.csv','digitsDataset/valLabels.csv','digitsDataset/testFeatures.csv', k)
    # Import the files
    trainFeat = open(trainFeatures,"r").readlines()
    trainFeat = [line.rstrip() for line in trainFeat]
    trainFeat = [np.fromstring(line, sep=',') for line in trainFeat]

    trainLab = open(trainLabels,"r").readlines()
    trainLab = [line.rstrip() for line in trainLab]
    trainLab = [np.fromstring(line, sep=',') for line in trainLab]

    valFeat = open(valFeatures,"r").readlines()
    valFeat = [line.rstrip() for line in valFeat]
    valFeat = [np.fromstring(line, sep=',') for line in valFeat]

    valLab = open(valLabels,"r").readlines()
    valLab = [line.rstrip() for line in valLab]
    valLab = [np.fromstring(line, sep=',') for line in valLab]

    testFeat = open(testFeatures,"r").readlines()
    testFeat = [line.rstrip() for line in testFeat]
    testFeat = [np.fromstring(line, sep=',') for line in testFeat]

    # Naive attempt seems to be fast enough. Runs in a minute or two.
    valGuess = []
    for valLine in valFeat:
        distance = np.array([np.linalg.norm(valLine-trainLine) for trainLine in trainFeat])
        ind = np.argpartition(distance, k)[:k]
        kNeighbors = np.array([int(trainLab[i]) for i in ind])
        #print(kNeighbors)
        counts = np.bincount(kNeighbors)
        valGuess.append(np.argmax(counts))
    count = 0
    fileMade = open("digitsOutput"+ str(k) + ".csv", 'w')
    for guess in valGuess:
        fileMade.write(str(guess) + ",")
    fileMade.close()
    
    
##    for i in range(len(valLab)):
##        if valGuess[i] == int(valLab[i]):
##            count += 1
##        else: #There is an error in prediction. This will help trace back the images.
##            #print(i, valGuess[i], int(valLab[i]))


##    #testGuess = []           
##    testTrainFeat = trainFeat + valFeat
##    testTrainLab = trainLab + valLab
##    for testLine in testFeat:
##        distance = np.array([np.linalg.norm(testLine-trainLine) for trainLine in testTrainFeat])
##        ind = np.argpartition(distance, k)[:k]
##        kNeighbors = np.array([int(testTrainLab[i]) for i in ind])
##        #print(kNeighbors)
##        counts = np.bincount(kNeighbors)
##        print(str(np.argmax(counts)) + ',')

    return 
