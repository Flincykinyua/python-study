#1 concatenation practice create 2 variables first name and last name and assign them to your first name and lastname 
#concernate them into a string

fname="Flincy"
lname="Murugi"
full_name="Flincy"+" "+"lname"
print(full_name)


#2 indexing practice given the string word python print the first and last characters using indexing
word="PYTHON"
print(word[0])
print(word[5])


# #3. Slicing practice 
#given the string phrase learning python is fun using slicing to extract and print the sustracting python
phrase ='learning python is fun!'
print(phrase[8:15])

# #.4 Reversing a string  reverse text 'reverse this'print the reversed version of the strings.
text= 'reverse this'
print(text[::-1])

#5 
greetings='hello world'
print(greetings.replace('world','python'))

#6
msg = 'python programming'
print(msg.lower())
print(msg.upper())

#7
sentence= 'This is a simple sentence'
print(sentence.count('s'))

#8check if the substring feature is present
quote= 'The best way to predict the is to create it'
print('future'in quote)

#9
description= 'data science'
print(len(description))

#10 remove whitespace: given that the strin name is john doe "remove the leading and trailing spaces and print the result."
name='    John Doe'
print(name.strip())
