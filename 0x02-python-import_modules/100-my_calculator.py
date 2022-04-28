#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    import calculator_1 as calculator

    argc = len(sys.argv) - 1
    if argc != 3:
        print(f"Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)
    else:
        operators = {"+", "-", "*", "/"}
        if not sys.argv[2] in operators:
            print(f"Unknown operator. Available operators: +, -, * and /")
            exit(1)
        else:
            a = int(sys.argv[1])
            b = int(sys.argv[3])
            if sys.argv[2] == "+":
                print(f"{a} + {b} = {calculator.add(a, b)}")
            elif sys.argv[2] == "-":
                print(f"{a} - {b} = {calculator.sub(a, b)}")
            elif sys.argv[2] == "*":
                print(f"{a} * {b} = {calculator.mul(a, b)}")
            else:
                print(f"{a} / {b} = {calculator.div(a, b)}")
