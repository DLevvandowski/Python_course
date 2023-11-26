# Ex. 6.4 Glossary 2
# Now that you know how to iterate through a dictionary, modify the code of Exercise 6.3 from earlier in the chapter.
# Replace the print() series of calls with a loop that performs iteration through the dictionary's keys and values.
# After making sure the loop works properly, add another five Python-related terms to the glossary. When you run the
# program again, the newly added terms and their definitions should be automatically included in the displayed output.

glossary = {
    'variable': 'a named place in the computer where some value can be stored.',
    'list': 'an editable variable containing an ordered set of elements.',
    'tuple': 'A non-editable variable containing an ordered set of elements.',
    'zen_of_python': 'a collection of 19 "guiding principles" for writing computer programs that affect the design of '
                     'the Python programming language.',
    'comment': 'allows you to put notes in your programs to help other programmers reading your code.',
    'dictionary': 'is a data structure similar to an array, but you work on it based on keys (also called hashes) '
                  'rather than indexes.',
    'append() function': 'adds an element to the end of the list.',
    'pop() function': 'removes and returns the last element of the list.',
    'title() function': 'enlarges the first letters of all the words in the string, and decreases the remaining '
                        'letters.',
    'sorted() function': 'returns a new sorted list leaving the source list unchanged.',
}

print('Glossary of Python:')
for term, definition in glossary.items():
    print(f"{term.title()} - {definition}")
