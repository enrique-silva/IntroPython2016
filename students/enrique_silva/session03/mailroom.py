#!/usr/bin/env python

# User prompt at the beggining of program, asking what the user would like to do.

donor_list=[['Enrique Silva',[100, 200, 300]],['Jon Smith',[200, 300, 400]],['Ally Smith',[200, 300, 500]],['Anny Gill', [300, 600, 1500]],['Terry Bill', [500, 750, 1000]]]

msg = """
What would you like to do?

To send a thank you: type "s"
To print a report: type "p"
To exit: type "x"
"""

def main(donor_list):
    """run the main interactive loop"""

    response = ''
    # keep asking until the users responds with an 'x'
    while True:  # make sure there is a break if you have infinite loop!
        print(msg)
        response = input("==> ").strip()  # strip() in case there are any spaces

        if response == 'p':
            print_report(donor_list)
        elif response == 's':
            send_thanks(donor_list)
        elif response == 'x':
            break
        else:
            print('please type "s", "p", or "x"')

def send_thanks(donor_list):
    """Send a thank you note to donor, add the donor to the list, or  accept
    a new donation"""
    see_list=input('Press Enter to see donor list or enter first name and last name: ')
    if see_list=='':
        print_donor_list(donor_list)


def print_donor_list(donor_list):
    for donor in donor_list:
        print(donor[0])


def print_report(donor_list):
    print("This will print a report")


main(donor_list)
