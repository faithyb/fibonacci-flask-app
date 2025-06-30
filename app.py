from flask import Flask, render_template, request, jsonify
import matplotlib.pyplot as plt
import csv
import os

app = Flask(__name__)

# Generate Fibonacci sequence
def generate_fibonacci(n):
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    elif n == 2:
        return [0, 1]
    sequence = [0, 1]
    for i in range(2, n):
        sequence.append(sequence[i - 1] + sequence[i - 2])
    return sequence

# Plot and save image
def plot_fibonacci(sequence, filename="static/fibonacci_plot.png"):
    plt.figure()
    plt.plot(sequence, marker='o')
    plt.title("Fibonacci Sequence")
    plt.xlabel("Index")
    plt.ylabel("Fibonacci Number")
    plt.grid(True)
    plt.tight_layout()
    plt.savefig(filename)
    plt.close()

# Save to CSV
def save_to_csv(sequence, filename="static/fibonacci_sequence.csv"):
    with open(filename, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["Index", "Fibonacci Number"])
        for i, num in enumerate(sequence):
            writer.writerow([i, num])

# Save to TXT
def save_to_txt(sequence, filename="static/fibonacci_sequence.txt"):
    with open(filename, mode='w') as file:
        file.write(", ".join(str(num) for num in sequence))

# Web interface
@app.route('/', methods=['GET', 'POST'])
def index():
    sequence = []
    error_message = None
    if request.method == 'POST':
        try:
            terms = int(request.form['terms'])
            if terms < 1:
                error_message = "Please enter a number greater than 0."
            elif terms > 10000:
                error_message = "Number too large. Please enter less than 10,000."
            else:
                sequence = generate_fibonacci(terms)
                plot_fibonacci(sequence)
                save_to_csv(sequence)
                save_to_txt(sequence)
        except ValueError:
            error_message = "Invalid input. Please enter a valid integer."
    return render_template('index.html', sequence=sequence, error=error_message)

# JSON API route
@app.route('/api/fibonacci')
def fibonacci_api():
    try:
        terms = int(request.args.get('terms', 10))
        if terms < 1 or terms > 10000:
            return jsonify({"error": "Number must be between 1 and 10000"}), 400
        sequence = generate_fibonacci(terms)
        return jsonify({"terms": terms, "sequence": sequence})
    except (ValueError, TypeError):
        return jsonify({"error": "Invalid input"}), 400

if __name__ == '__main__':
    # Ensure static directory exists
    os.makedirs('static', exist_ok=True)
    app.run(debug=True)
