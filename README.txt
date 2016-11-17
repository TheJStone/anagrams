Using python 2.7
I first parse the words into a dictionary of sets where each key is an ordered lower case string
and the set are all of the words that match this anagram encoding. Then, when given a string, I will just convert that
string into a ordered lower case string and check if it exists in the dictionary. If it does, I will take the set, sort it,
and push it into a string with them spaced to print. Otherwise, if it does not exist in the map, I will print '-'.

I decided to do most of the heavy loading with in offline step by preprocessing the data given the significant number of
strings to be queried anagrams for. I could just order the letters to find a particular anagram match as they all have
the same exact characters but just in a different order. So, a dictionary mapping this order to any matching words seemed
like the best fit for this problem.

1. offline step O(Number of entries in dictionary txt)
   online step O(1)
2. O(number of entries in dictionary*100)
3. assuming I could use cheap disk storage,
    I would use python's shelve class which are serialized on-disk dictionaries
    that one can open and read individual values without pulling the whole
    dictionary into memory. allowing one to process all data into dictionary
    without having to use more than the current list pulled from the dictionary.
