Using python 2.7
1. offline step O(Number of entries in dictionary txt)
   online step O(1)
2. O(number of entries in dictionary*100)
3. assuming I could use cheap disk storage,
    I would use python's shelve class which are serialized on-disk dictionaries
    that one can open and read individual values without pulling the whole
    dictionary into memory. allowing one to process all data into dictionary
    without having to use more than the current list pulled from the dictionary.
