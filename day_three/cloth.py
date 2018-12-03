import re, time

MAX_SIZE = 1000

def regexParse(inputString):
    outputArray = re.findall(r'\d+', inputString)
    outputDict = {
        'id': int(outputArray[0]),
        'x': int(outputArray[1]),
        'y': int(outputArray[2]),
        'width': int(outputArray[3]),
        'height': int(outputArray[4])
    }
    return outputDict

def buildCloth():
    baseArray = ['.'] * MAX_SIZE
    for i in range(len(baseArray)):
        baseArray[i] = ['.'] * MAX_SIZE
    return baseArray

def mapToCloth(cloth, pattern):
    for i in range(pattern['x'], (pattern['x']) + pattern['width']):
        for j in range(pattern['y'], (pattern['y']) + pattern['height']):
            if cloth[i][j] == '.':
                cloth[i][j] = pattern['id']
            else:
                cloth[i][j] = 'X'
    return cloth

def countX(cloth):
    total = 0
    for i in cloth:
        for j in i:
            if j == 'X': total += 1
    return total

def findNoOverlap(cloth, pattern):
    for i in range(pattern['x'], (pattern['x']) + pattern['width']):
        for j in range(pattern['y'], (pattern['y']) + pattern['height']):
            if cloth[i][j] == 'X':
                return False
    return pattern['id']

def main(fileInput):
    start = time.time()
    
    patternArray = []
    cloth = buildCloth()
    for line in fileInput.readlines():
        patternArray.append(regexParse(line))
        
    for pattern in patternArray:
        cloth = mapToCloth(cloth, pattern)

    print('overlaps: %d' % countX(cloth))

    for pattern in patternArray:
        correctPattern = findNoOverlap(cloth, pattern)
        if not correctPattern == False:
            print('correct pattern: %s' % correctPattern)
            break

    end = time.time()
    print('runtime: %dms' % int((end-start)*1000))


inputFile = open('input.txt', 'r')

main(inputFile)