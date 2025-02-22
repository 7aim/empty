import re

text = "Hocam merhaba kolay gelsin. Hocam ben size bir şey danişacaktim."
pattern = r"Hocam"

print(re.search(pattern, text)) #find pattern stats in text
print(re.search(pattern, text).span()) #position
print(re.search(pattern, text).group()) #pattern

re.finditer(text,pattern) #try every condition


#pattern

"\d" #digit
"\w" #digit+string+_
"\s" #space
"\D" #not digit
"\W" #not digit+string+_
"\S" #not space

"\w{5}" #5
"\w{5,6}" #5 or 6
"\w{5,}" #5 or more
"\w*" #0 or more
"\w+" #1 or more
"\w?" #0 or 1

"|" #or
"^" #start
"$" #end 
"." #any
"\(" #output: ( 





