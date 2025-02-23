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

#test

#azercell 050 or 051
#nar 070
#bakcell 055

tel_no = input("Lutfen tel no giriniz: ")

def operator_bul(tel_no):

    pattern = r"\d{3}-?\d{3}-?\d{2}-?\d{2}"
    no_stat = re.search(pattern,tel_no)
    if no_stat:
        no = no_stat.group()
        if no.startswith("050") or no.startswith("051"):
            return "Azercell"
        elif no.startswith("070"):
            return "Nar"
        elif no.startswith("055"):
            return "Bakcell"
        else:
            return "Sebeke bulunamadi..."
    else:
        print("Basarisiz")
        tel_no = input("Lutfen tel no giriniz: ")
        operator_bul(tel_no)

    
print(operator_bul(tel_no))

