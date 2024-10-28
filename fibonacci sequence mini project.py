def fibonacci_sequence(count):
    sequence = []
    a, b = 0, 1
    for _ in range(count):
        sequence.append(a)
        a, b = b, a+b
    return sequence
try:
    num = int(input("Enter your number here: "))
    if num <= 0:
        print ("Please enter a positive number.")
    else:
        print(f"Fibonacci sequence is:")
        print(fibonacci_sequence (num))
except ValueError:
    print("Invalid! Please try again!")
