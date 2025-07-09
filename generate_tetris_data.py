import pandas as pd
import random
from datetime import datetime, timedelta

# Configuration
num_rows = 200
start_date = datetime(2025, 1, 1)
block_shapes = ['T', 'L', 'Z', 'O', 'I']
colors = {'T': 'Red', 'L': 'Blue', 'Z': 'Green', 'O': 'Yellow', 'I': 'Purple'}
regions = ['North', 'South', 'East', 'West']

# Generate data
data = []
for _ in range(num_rows):
    date = start_date + timedelta(days=random.randint(0, 90))
    shape = random.choice(block_shapes)
    color = colors[shape]
    region = random.choice(regions)
    quantity = random.randint(1, 20)
    revenue = quantity * random.randint(80, 150)  # assume $80–$150 per block

    data.append({
        'Date': date.strftime('%Y-%m-%d'),
        'BlockShape': shape,
        'Color': color,
        'Region': region,
        'QuantitySold': quantity,
        'Revenue': revenue
    })

# Convert to DataFrame
df = pd.DataFrame(data)

# Save to CSV
df.to_csv("tetris_blocks.csv", index=False)
print("✅ Synthetic Tetris data saved as tetris_blocks.csv")
