'''
1. Write an app for a cafe. Decide on the items in the cafe, stock of each item in the morning, 
stock in the evening, sales amount at the end of the day and profit for each item. You need to restock an item 
if the supply reaches 20% of the stock. Print the 3 items with highest sales, and top 3 highest profit.
'''

#PROGRAM :

#importing time
import time
startTime = time.time()
timeLimit = 30

#initialization
itemsInCafe = ['coffee','tea','cappucino','cookie']
itemPrice = [40,35,50,30]
itemProfit = [12,10,14,5]
itemStock = [30,30,20,40]
itemStockRefill = [30,30,20,40]
itemSales = [0,0,0,0]
topSale = [0,0,0,0]
topProfit = [0,0,0,0]

quantityInWords = ['one','two','three','four','five','six','seven','eight','nine']
quantityInDigits = ['1','2','3','4','5','6','7','8','9']

#getting customer input and calculating the sold item
def CustomerInput(customerInput) :
    
    list1 = list(customerInput.split())
    totalCost = 0
    quantities = []
    
    #taking the input and filtering valuse
    for i in range(len(itemsInCafe)) :
        
        if itemsInCafe[i] in list1:
            
            index = (list1.index(itemsInCafe[i])) - 1
            
            for x in range(len(quantityInWords)) :
                
                if quantityInWords[x] in list1[index] or quantityInDigits[x] in list1[index] :
                    
                    quantities.insert(i,int(quantityInDigits[x]))

        else:
            
            quantities.insert(i,0)

        #updating the stock
        itemStock[i] -= quantities[i]
        itemSales[i] += quantities[i]

        if quantities[i] != 0 :

            print(f'{itemsInCafe[i].capitalize()} Cost = {itemPrice[i] * quantities[i]}') 

        totalCost += (itemPrice[i] * quantities[i])

        #stock refill checking condition
        if itemStock[i] <= (itemStockRefill[i] * 0.2):
        
            itemStock[i] = itemStockRefill[i]
            print(f"{itemsInCafe[i]} Refilled....")
            
    print(f'Total bill = {totalCost}')
    
#displaying top 3 sales and profit item
def topItemsCategory():

    a = 0

    #finding the profit for all items
    for x in range(len(itemSales)) :
        topSale[x] = itemSales[x]
        topProfit[x] = itemSales[x] * itemProfit[x]

    print("\nTop 3 Sales items")
    
    #loop to print top items in order
    for i in range (6) :

        if i < 3 :

            #printing the top sales
            a = topSale.index(max(topSale))
            print(f"{i+1} - {max(topSale)} - {itemsInCafe[a]}")
            topSale[a] = 0
            continue

        elif i == 3 :

            print("\nTop 3 Profit items")

        #printing the top profit
        a = topProfit.index(max(topProfit))
        print(f"{i-2} - {max(topProfit)} - {itemsInCafe[a]}")
        topProfit[a] = 0

def main() :

    print("\t...Welcome to the cafe..")
    print("(Here are the items that we can served)")
    banner = ''

    #displaying items
    for item in range(len(itemsInCafe)) :

        banner += '\n' + str(item+1) + ' - ' + str(itemsInCafe[item].upper())

    #checking time duration
    while (time.time() - startTime) < timeLimit :    

        print(banner)
        customerInput = input("Enter ur order... : ")

        #calling function to take customer input
        CustomerInput(customerInput.lower())

    #calling function to print top results 
    topItemsCategory()

    #refilling the stock
    for z in range(len(itemsInCafe)) :
            
        itemStock[z] = itemStockRefill[z]
        
    print("All items Refilled....")

main()