directions = ['north', 'south', 'east', 'west', 'down', 'up', 'down', 'right']
verbs = ['go', 'stop', 'kill', 'eat']
stops = ['the', 'in', 'at', 'of', 'from', 'at', 'it']
nouns = ['door', 'bear', 'princess', 'cabinet']


def scan(thewords):

    thewords = thewords.split()
    sentence = []

    for i in thewords:
        if i in directions:
            sentence.append(('direction', i))

        elif i in verbs:
            sentence.append(('verb', i))

        elif i in stops:
            sentence.append(('stop', i))

        elif i in nouns:
            sentence.append(('noun', i))

        elif i.isdigit():
            sentence.append(('number', convert_number(i)))

        else:            
            sentence.append(('error', i))

    return sentence

def convert_number(s):
    try:
        return int(s)

    except ValueError:
        return None

