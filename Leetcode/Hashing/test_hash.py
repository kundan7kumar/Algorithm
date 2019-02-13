def main():
    '''
    Creating empty Dictionary
    '''
    # Creating an empty dict using empty brackets
    wordFrequency = {}

    # Creating an empty dict using dict()
    wordFrequency = dict()

    print(wordFrequency)

    '''
    Creating Dictionaries with literals
    '''
    wordFrequency = {
        "Hello": 7,
        "hi": 10,
        "there": 45,
        "at": 23,
        "this": 77
    }

    print(wordFrequency)

    '''
    Creating Dictionaries by passing parametrs in dict constructor
    '''
    wordFrequency = dict(Hello=7,
                         hi=10,
                         there=45,
                         at=23,
                         this=77
                         )

    print(wordFrequency)

    '''
    Creating Dictionaries by a list of tuples
    '''

    # List of tuples    
    listofTuples = [("Hello", 7), ("hi", 10), ("there", 45), ("at", 23), ("this", 77)]

    # Creating and initializing a dict by tuple
    wordFrequency = dict(listofTuples)

    print(wordFrequency)

    '''
    Creating Dictionary by a list of keys and initialzing all with same value
    '''

    listofStrings = ["Hello", "hi", "there", "at", "this"]

    # create and Initialize a dictionary by this list elements as keys and with same value 0

    wordFrequency = dict.fromkeys(listofStrings, 0)

    print(wordFrequency)

    '''
    Creating a Dictionary by a two lists
    '''
    # List of strings
    listofStrings = ["Hello", "hi", "there", "at", "this"]

    # List of ints
    listofInts = [7, 10, 45, 23, 77]

    # Merge the two lists to create a dictionary
    wordFrequency = dict(zip(listofStrings, listofInts))

    print(wordFrequency)


if __name__ == "__main__":
    main()