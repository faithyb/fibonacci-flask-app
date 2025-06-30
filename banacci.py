
def generate_fibonacci(n):
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    elif n == 2:
        return [0, 1]
    
    sequence = [0, 1]
    for i in range(2, n):
        next_number = sequence[i-1] + sequence[i-2]
        sequence.append(next_number)
    return sequence

# usage:
if __name__ == "__main__":
    try:
        terms = int(input("Enter the number of Fibonacci terms to generate: "))
        fib_sequence = generate_fibonacci(terms)
        print("Fibonacci Sequence:")
        print(fib_sequence)
    except ValueError:
        print("Please enter a valid integer.")
