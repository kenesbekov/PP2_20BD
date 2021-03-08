import re, csv
f = open("raw.txt", "r")
text = f.read()
f.close()
ls =[] #["Company, BIN, Product, Date, Address"]
ls.append(('Company Name: '+re.search(r"\bФилиал.*", text).group()+',Product Name,How Much,Unit Price,Total Price').split(','))  # Name of the company
ls.append(["BIN Number: "+re.search(r"\d+", text).group()]) #BIN number

x = re.split("\d+[.]\D", text)
for i in range(1, len(x)):
    currItem = x[i]
    item = [i]
    item.append(re.search(r".+", currItem).group()) #title
    item.append(re.search(r"\d+[,][0]{3}", currItem).group()[:1]) #cout
    item.append(re.search(r"[x].+\d+[,]\d{2}", currItem).group()[2:]) #unit price
    item.append(re.search(r"Стоимость\n.+", currItem).group()[10:]) #total price
    ls.append([item[0], item[1], item[2], item[3], item[4]])
ls.append(['Date: '+re.search(r"Время.+", x[len(x)-1]).group()[7:]]) #date
ls.append(['Address: '+re.search(r"г[.].+", x[len(x)-1]).group()]) #address
with open("ticket.csv", "w") as ticket_file:
    writer = csv.writer(ticket_file)
    writer.writerows(ls)