import csv
import random
import uuid

# Product categories and example names
categories = {
    "Peripherals": ["Mouse Logitech", "Keyboard Redragon", "Headset HyperX"],
    "Informatics": ["Notebook Dell", "Monitor LG", "Desktop HP"],
    "Accessories": ["USB Cable", "HDMI Adapter", "Phone Holder"],
    "Gaming": ["Gaming Chair", "Gaming Mousepad", "Joystick Xbox"],
    "Storage": ["SSD Kingston", "HDD Seagate", "Flash Drive SanDisk"]
}

# Generate 100 unique products
products = []
for i in range(1, 101):
    category = random.choice(list(categories.keys()))
    name = random.choice(categories[category]) + f" {random.randint(1, 100)}"
    price = round(random.uniform(20, 5000), 2)
    product_id = f"PRD-{i:03d}"
    products.append([product_id, name, category, price])

# Save to CSV
with open("products.csv", mode="w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)
    writer.writerow(["product_id", "product_name", "category", "price"])
    writer.writerows(products)

print("✅ Product catalog saved to 'products.csv' with 100 items.")
