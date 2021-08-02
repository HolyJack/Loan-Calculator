import math
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--type")
parser.add_argument("--principal")
parser.add_argument("--payment")
parser.add_argument("--periods")
parser.add_argument("--interest")

args = parser.parse_args()
choice = None
i = 0
counter = 0
payment = 0
periods_number = 0
loan_principal = 0

if args.type is None:
    print("Incorrect parameters")
    exit(0)
else:
    counter += 1

if args.interest is None or float(args.interest) < 0:
    print("Incorrect parameters")
    exit(0)
else:
    counter += 1
    i = float(args.interest) / (12 * 100)

if args.principal is not None:
    loan_principal = int(args.principal)
    counter += 1
else:
    choice = "p"

if args.payment is not None:
    payment = int(args.payment)
    counter += 1
else:
    choice = "a"

if args.periods is not None:
    periods_number = int(args.periods)
    counter += 1
else:
    choice = "n"

if counter != 4:
    print("Incorrect parameters")
    exit(0)

if args.type == "diff" \
        and args.payment is None:
    overpayment = -loan_principal
    for iterator in range(periods_number):
        d = loan_principal / periods_number + i * (loan_principal - loan_principal * iterator / periods_number)
        overpayment += math.ceil(d)
        print("Month {}: payment is {}".format(iterator + 1, math.ceil(d)))
    print()
    print("Overpayment = {}".format(overpayment))
elif args.type == "annuity":
    if choice == "a":
        payment = loan_principal * (i * pow(1 + i, periods_number)) / (pow(1 + i, periods_number) - 1)
        print("Your annuity payment = {}".format((payment)))
    elif choice == "p":
        loan_principal = math.floor(payment / ((i * pow(1 + i, periods_number)) / (pow(1 + i, periods_number) - 1)))
        print("Your loan principal = {}".format(loan_principal))
    elif choice == "n":
        periods_number = math.ceil(math.log(payment / (payment - i * loan_principal), 1 + i))
        print("It will take {} years and {} months to repay this loan!".
              format(round(periods_number / 12) - 1, periods_number % 12) if periods_number >= 12 and periods_number % 12 != 0 else
              "It will take {} years to repay this loan!".
              format(int (periods_number / 12)) if periods_number >= 12 else
              "It will take {} months to repay this loan!".
              format(n))
    overpayment = math.ceil(payment) * periods_number - loan_principal
    print("Overpayment = {}".format(math.ceil(overpayment)))
else:
    print("Incorrect parameters")

