def get_invoice_items(items):
    # Items is a dictionary with a quantity and price key, and a name key
    # Return a list of all the invoice line items in the following format:
    # quantity name subtotal currency
    # For example, if we had the following:
    # [
    #   {'name': 'Apple', 'quantity': 1, price: 0.2 },
    #   {'name': 'Orange', 'quantity': 4, price: 0.3 },
    # ]
    # We should return the following:
    # ['1 Apple 0.200KD', '4 Orange 1.200KD']
    # ---
    # Write your code here
    invoice_items=[]
    for item in items:
     # print(item)
      #tesr=item['Quantity'] item['name'] item['Price']
      item_1=str(item['quantity'])+' '+ item['name']+ ' '+str(item['price'])
      invoice_items.append(item_1)  
    #print(invoice_items)
    return invoice_items
def get_total(items):
    # Items is a dictionary with a quantity and price key
    # Calculate the total of all items in the cart
    # Write your code here
    total=0
    for item in items:
        total_item=(int(item['quantity'])*float(item['price']))
        total=total+total_item
    return total

def print_receipt(invoice_items, total):
    # invoice_items will be the list of formatted items received from
    # `get_invoice_items`, and total will be a float. Print out a nice receipt
    # displaying a title, all the invoice items on separate lines, and the
    # total at the end.
    # ---
    # Write your code here
    print("\n---------")
    print("receipt")
    print("---------")
    for item in invoice_items:
        print(item)
    print("---------")    
    print(f"Total Price: {total}")

def main():
    # Write your main logic here
    # items=[]
    # items_D={}
    # items_Dw={}

    # count=0
    # item_name=input("Item (enter 'done' when finished): ")
    # while item_name  != "Done":
    #    print(items)

    #    items_D['name']=item_name
    #    Price=int(input("Price: "))
    #    Quantity=int(input("Quantity: "))
    #    items_D['Price']=Price
    #    items_D['Quantity']=Quantity
    #    items.append(items_D)
    #    count=count+1
    #    print(items)
    #    item_name=input("Item (enter 'done' when finished): ")
    #    items_D==items_D.join(str(count))
    # items_D['name']=item_name
    # Price=int(input("Price: "))
    # Quantity=int(input("Quantity: "))
    # items_D['Price']=Price
    # items_D['Quantity']=Quantity
    # items.append(items_D)
    # item_name=input("Item (enter 'done' when finished): ")
   
    # items_Dw['name']=item_name
    # Price=int(input("Price: "))
    # Quantity=int(input("Quantity: "))
    # items_Dw['Price']=Price
    # items_Dw['Quantity']=Quantity
    # items.append(items_Dw)
    # print(items)
    # print(items_D)  
    #print_receipt(get_invoice_items(items),get_total(items))   
 #def main():
    # Write your main logic here
    items = []
    item_name =  input("Item (enter 'done' when finished): ")
    while item_name != "Done":
        price = float(input("Price: "))
        quantity = int(input("Quantity: "))
        items.append({"name": item_name, "price": price, "quantity": quantity})

        item_name = input("Item (enter 'Done' when finished): ")
    
    invoice_items = get_invoice_items(items)
    total = get_total(items)

    print_receipt(invoice_items, total)


if __name__ == "__main__":
    main()
