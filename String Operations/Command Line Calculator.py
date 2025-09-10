import argparse

parser = argparse.ArgumentParser(description= "Simple Command Line Calculator")


parser.add_argument("num1", type=float, help="first number")
parser.add_argument("operator", choices=["add", "sub", "null"], help ="operation to perform")
parser.add_argument("num2", type=float, help="second number")

args= parser.parse_args()

if args.operator == "add":
    result = args.num1 + args.num2
elif args.operator == "sub":
    result = args.num1 - args.num2
elif args.operator == "null":
    result = args.num1 * args.num2

print ("Result:", result)