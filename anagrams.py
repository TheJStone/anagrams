import sys

def getOrderedStr(str):
    """
    :param str: a String
    :return: lexographical ordering of this string in lower case
    """
    return ''.join(sorted(str.lower()))

def parseDict(fileLoc):
    """

    :param fileLoc: location of txt file with one word per line
    :return: a dictionary of sets mapping an ordered lowercase string to all words with
        those exact characters. returns None if unable to open the file.
    """

    #tries to open the file. returns None if unsuccessful
    try:
        filep = open(fileLoc, 'r')
    except "FileNotFoundError":
        return None

    if filep == None: return None

    dict = {}
    #iterates the file, pulls out a word, gets its ordering
    # and puts the ordering in the dictionary to return
    for line in filep:
        line = line.strip('\n')
        if len(line) > 0:
            orderedStr = getOrderedStr(line)
            if orderedStr not in dict:
                dict[orderedStr] = set([])
            dict[orderedStr].add(line)
    return dict;

def getAnagrams(dict, str):
    """
    :param dict: a dictionary mapping a string ordering to a set of words.
        should be the return value from parseDict
    :param str: a String to get the anagram for
    :return: "-" if no anagram matches found in dictionary or
        a string containing all words spaced out
    """
    orderedStr = getOrderedStr(str)

    if orderedStr in dict:
        anagramSet = dict[orderedStr]
        return " ".join(sorted(list(anagramSet)))
    else: return "-"

def main():

    #obtains the dictionary
    if len(sys.argv) < 2:
        print "error: need dictionary location"
        return
    else:
        dict = parseDict(sys.argv[1])

    if dict is None:
        print "could not parse file"
        return

    #waits for input from user. will exit on empty string
    while(True):
        line = raw_input(">").strip('\n')
        if line == "":
            break;
        print getAnagrams(dict, line)



if __name__ == "__main__":
    main()