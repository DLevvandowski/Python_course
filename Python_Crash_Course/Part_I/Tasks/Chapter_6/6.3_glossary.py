# Ex. 6.3 Glossary
# The Python dictionary can be used to prepare an actual dictionary. However, to avoid confusion, we will call it a
# glossary.
# » Write down five programming words that you learned in earlier chapters. These words will be the keys in the glossary
#   while the values will be the meanings of each word.
# » Display each word and its meaning in elegantly formatted output. You can display a word, a colon and then an
#   explanation of the word in one line. Alternatively, put the word in one line and its explanation in the next
#   indented line. Use a new line character (\n) to insert a blank line between word-definition pairs.

glossary = {
    'variable': 'a named place in the computer where some value can be stored.',
    'list': 'an editable variable containing an ordered set of elements.',
    'tuple': 'A non-editable variable containing an ordered set of elements.',
    'zen_of_python': 'a collection of 19 "guiding principles" for writing computer programs that affect the design of '
                     'the Python programming language.',
    'comment': 'allows you to put notes in your programs to help other programmers reading your code.',
}

print("Glossary of Python:\n"
      f"Variable - {glossary['variable']}\n"
      f"List - {glossary['list']}\n"
      f"Tuple - {glossary['tuple']}\n"
      f"Zen of Python - {glossary['zen_of_python']}\n"
      f"Comment - {glossary['comment']}")
