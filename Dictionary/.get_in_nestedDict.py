dealership = {
    "car_001": {"brand": "Toyota", "price": 20000}
}

price = dealership.get("car_999", {}).get("price")   # Return None
price = dealership.get("car_999", {}).get("price",0)  # Return zero(0)

print(f"Price: {price}")

