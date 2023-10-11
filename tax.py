#!/usr/bin/env python3

# Created by: Lily Carroll
# Created on: Oct/10/2023
# This program calculates the total using the HST tax in Saskatchewan.

import constants


def main():
    # Get user input for the subtotal.
    subtotal = float(input("Enter your subtotal = $ "))

    # Calculate the tax.
    tax = subtotal * constants.HST

    # Calculate the total.
    total = subtotal + tax

    # Display the tax back to the user.
    print("")
    print("The tax would ben = ${:,.2f}".format(tax))

    # Display the total back to the user.
    print("")
    print("The total cost is = ${:,.2f}".format(total))


if __name__ == "__main__":
    main()
