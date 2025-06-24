import pandas as pd
import random
from datetime import datetime, timedelta

colors = ['Red', 'Blue', 'Green', 'Yellow', 'Purple']
shapes = ['L', 'I', 'O', 'T', 'Z', 'S', 'J']

def random_date():
    return datetime.now() - timedelta(days=random.randint(0, 30))

def generate_data(rows=50):
    data = []
    for _ in range(rows):
        color = random.choice(colors)
        shape = random.choice(shapes)
        qty = random.randint(1, 10)
        price = round(random.uniform(5.0, 20.0), 2)
        total = round(qty * price, 2)
        date = random_date().strftime("%Y-%m-%d")
        data.append([color, shape, qty, price, total, date])

    df = pd.DataFrame(data, columns=["Color", "Shape", "Qty", "Price", "Total", "Date"])
    df.to_csv("tetris_sales.csv", index=False)
    print("Generated tetris_sales.csv!")

if __name__ == "__main__":
    generate_data()
