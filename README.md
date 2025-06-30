# fibonacci-flask-app
# Fibonacci Flask App 🔢

This web application generates a Fibonacci sequence using Flask. Users can enter a number, see the sequence, download it as `.txt` or `.csv`, and view a plot.

## Features
- Input number of Fibonacci terms
- Display sequence on screen
- Download as CSV or TXT
- View matplotlib plot
- JSON API endpoint: `/api/fibonacci?terms=10`

## To Run Locally
```bash
pip install flask matplotlib
python app.py
