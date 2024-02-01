#capitalize() , the first character of the string is converted to upper case.
str = "this is string example wow!!!";
print (str.capitalize())

#count(), counts the number of times a specific ‘substring’, occurrence in the main string
str = "this is string example ... wow!!!";
print(str.count('s'))

#find() , will locate the position of searching ‘substring’, (index)
print(str.find('example'))

#lower(),returns a copy of the string in which all case−based characters have been lowercased.
str = "THIS IS STRING EXAMPLE ... WOW!!!";
print (str.lower())

#replace(), this method returns a copy of the string with all occurrences of substring old replaced by new.
str = "this is string example ... wow!!! this is really string";
print (str.replace("is", "was"))

#swapcase(), this method returns a copy of the string in which al l the case−based characters have had their case swapped.
str = "this is string example ... wow!!!";
print (str.swapcase())

#title(),returns a copy of the string in which first characters of all the words are capitalized.
str = "this is string example ... wow!!!";
print (str.title())
