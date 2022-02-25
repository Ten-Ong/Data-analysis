candy_list = ["snickers", "M&M", "Kit Kat","Starburts","gummy","Juicy Fruit"]

allowance = 3
cart = []


for candy in candy_list:
   print(f'[{str(candy_list.index(candy))}] {candy}')
   
print ("Which candy would you like to eat?") 
 

for x in range(allowance):
    selected= int(input("input the number of candy you like?"))
    
    cart.append(candy_list[selected])
    
print("you choice: ")
for candy in cart:
    print(candy)