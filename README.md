# Bill sharing description

## Goal
Share the bill among friends in a simple, fast and honest way

## How to use
Download the split_the_bill.py file
Just make sure that you have python3 installed, and two text files. 
One file is your friends mail list (email_list.txt) and other with grocery list you want to sahre (grocery_list.txt)

Now type on cmd:
> python .\split_the_bill.py --gl grocery_list.txt --el email_list.txt

The result will be printed on screen. 

Have fun =)


# Code 

* calculate_each_item_price(item):
Calculate the amount * price of each item
    Args:
        item (item): item from gorucery list.
    Returns:
        int: price of each item


* calculate_total_price(grocery_list):
Calculate the total price from groucery list.
    Args:
        grocery_list (list): groucery_list
    Returns:
        int: total price.


* divide_honestly(total_price,amount_people):
Divide the total price between the total amount people inside email_list.
    Args:
        total_price (int): Total price will be splitted
        amount_people (int): Amount emails in email_list
    Returns:
        float: price per person
        float: price per person to complete the total price, if need

* map_price_and_email(email_list,grocery_list):
Map the amount each person will pay.
    Args:
        email_list (list): email list
        grocery_list (list): grocery list
    Returns:
        dict: Dictionary mapping the price and the e-mail.


* main(argv):
Main function that calculate the total price from a grocery list and split it between the people in list emails.
    Args:
        argv (string): get the arg with file name.
    Raises:
        FileNotFoundError: If not found the list file. 
        FileNotFoundError: If not found the list file.

# Input file
* email_list.txt
A list of strings each line there is an email.


* grocery_list.txt
A list of Dictionary contaning:
* "item":"maçã",
* "amount": 5,
* "price": 9.89