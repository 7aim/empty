import re

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