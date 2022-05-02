#!/usr/bin/python3
def multiple_returns(sentence):
    create_tuple = tuple(sentence)
    if not sentence:
        create_tuple = (None, )
    
    lenght = len(sentence)
    first_letter = create_tuple[0]
    return (lenght, first_letter)
