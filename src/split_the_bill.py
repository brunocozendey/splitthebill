#!/usr/bin/python
import sys, getopt,json

def calculate_each_item_price(item):
    """Calculate the amount * price of each item

    Args:
        item (item): item from gorucery list.

    Returns:
        int: price of each item
    """
    return item['amount']*item['price']

def calculate_total_price(grocery_list):
    """Calculate the total price from groucery list.

    Args:
        grocery_list (list): groucery_list

    Returns:
        int: total price.
    """
    total = 0
    for item in grocery_list:
        total += calculate_each_item_price(item)
    return total

def divide_honestly(total_price,amount_people):
    """Divide the total price between the total amount people inside email_list.

    Args:
        total_price (int): Total price will be splitted
        amount_people (int): Amount emails in email_list

    Returns:
        float: price per person
        float: price per person to complete the total price, if need
    """
    price_per_cents = total_price*100
    price_per_person = price_per_cents//amount_people
    total_price_splitted = price_per_person*amount_people
    price_greater_values = int(price_per_cents%amount_people)
    
    if total_price_splitted != total_price:
        return price_per_person/100, (price_per_person+1)/100, price_greater_values
    else:
        return price_per_person/100, price_per_person/100, 0

def map_price_and_email(email_list,grocery_list):
    """Map the amount each person will pay.

    Args:
        email_list (list): email list
        grocery_list (list): grocery list

    Returns:
        dict: Dictionary mapping the price and the e-mail.
    """

    email_and_price = {}
    valor_normal, rounded_value, price_greater_values = divide_honestly(calculate_total_price(grocery_list),len(set(email_list)))
    for email in email_list:
        email_and_price[email]=valor_normal
    for value in range(price_greater_values):
        email_and_price[email_list[value]] = rounded_value
    return email_and_price

def main(argv):
    """
    Main function that calculate the total price from a grocery list and split it between the people in list emails.

    Args:
        argv (string): get the arg with file name.

    Raises:
        FileNotFoundError: If not found the list file. 
        FileNotFoundError: If not found the list file.
    """
    groceryfile = ''
    emailfile = ''
    try:
       opts, _ = getopt.getopt(argv,"hgl:el:",["glfile=","elfile="])
    except getopt.GetoptError:
        print ('split_the_bill.py --gl <grocerylist.txt> --el <emaillist.txt>')
        print ('Please provide input files or -h for help')
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            print ('split_the_bill.py --gl <grocerylist.txt> --el <emaillist.txt>')
            sys.exit()
        elif opt in ("-gl", "--glfile"):
            groceryfile = arg
        elif opt in ("-el", "--elfile"):
            emailfile = arg
   
    try:
        mf = open(groceryfile, "r", encoding='utf-8')
        mf.seek(0)
        grocery_list = mf.read()
        if grocery_list == '':
            grocery_list = "{}"
        grocery_list_json = json.loads(grocery_list)
    except:
        raise FileNotFoundError('Grocery list not found!')
    finally:
        mf.close()

    try:
        ef = open(emailfile, "r", encoding='utf-8')
        ef.seek(0)
        email_list = ef.read().splitlines()
        if email_list == []:
            email_list = ["Total"]
    except:
        raise FileNotFoundError('Email list not found!')
    finally:
        ef.close()
    print(json.dumps(map_price_and_email(email_list,grocery_list_json)))        

if __name__ == "__main__":
   main(sys.argv[1:])   