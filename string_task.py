#1.
name = "  JOHn  ."
name = name.strip().replace(".", "").lower()
print(name)  


#2.
sentence_one = "The Dog Breed is German Shepherd"
result_one = sentence_one[9:24]  
print(result_one)

sentence_two = "Defeats for the Clinton forces, this was her moment of triumph” only display "
result_two=sentence_two[15:29]
print(result_two)


#4.
first_name= "  Joh.n"
last_name="  Do,e"
first_name=first_name.strip()
first_name=first_name.replace(".",'')
last_name=last_name.replace(',','')
last_name=last_name.strip()

full_name=first_name+''+last_name
print(full_name)


#4.Having the string r = '["E","W","C"]' #Manipulate it to display EWC
r='["E","W","C"]'
r=r.replace('[','').replace(']','').replace('"','').replace(',','')
r2=''.join(r)
print(r2)
