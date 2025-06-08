from faker import Faker
from datetime import datetime, timedelta, timezone
import uuid
import random
import json
import csv

fake = Faker()

# Load product catalog from CSV
with open("products.csv", newline="", encoding="utf-8") as f:
    reader = csv.DictReader(f)
    product_catalog = list(reader)

# Ensure we only sample valid product_ids
valid_products = [product for product in product_catalog]


def generate_order_events():
    order_id = f"ORD-{uuid.uuid4().hex[:8]}"
    user_id = random.randint(1000, 9999)
    product = random.choice(valid_products)
    product_id = product["product_id"]
    region = random.choice(["SP", "RJ", "MG", "RS", "BA"])
    base_time = datetime.now(timezone.utc)
    price = float(product["price"])  # Use price from catalog

    # Define event sequence and time offsets in minutes
    base_events = [
        ("ORDER_CREATED", 0),
        ("PAYMENT_CONFIRMED", 5),
        ("ORDER_PACKED", 60),
        ("ORDER_SHIPPED", 120),
    ]

    # Decide if delivery is delayed (10% chance)
    is_delayed = random.random() < 0.10
    delivery_delay = 1440 if is_delayed else 240  # 1 day or 4 hours
    base_events.append(("ORDER_DELIVERED", delivery_delay))

    # 2% chance of return
    include_return = random.random() < 0.02
    if include_return:
        base_events.append(("ORDER_RETURNED", delivery_delay + 360))

    events = []
    for event_type, delay_minutes in base_events:
        event_time = base_time + timedelta(minutes=delay_minutes)
        event = {
            "event_id": str(uuid.uuid4()),
            "event_type": event_type,
            "timestamp": event_time.isoformat(),
            "order_id": order_id,
            "user_id": user_id,
            "product_id": product_id,
            "region": region,
            "price": price,
        }
        if event_type == "ORDER_DELIVERED":
            event["is_delayed"] = is_delayed
        if event_type == "ORDER_RETURNED":
            event["is_returned"] = include_return

        events.append(event)

    return events


# Write 1000 synthetic orders to a JSONL file
with open("order_events.jsonl", "w", encoding="utf-8") as f:
    for _ in range(1000):
        for event in generate_order_events():
            f.write(json.dumps(event) + "\n")

print("✅ order_events.jsonl file generated with valid product references and prices from catalog.")
