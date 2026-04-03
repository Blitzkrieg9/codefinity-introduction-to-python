vegetables = ["tomatoes", "potatoes", "onions"]
vegetables.remove("onions")


if not "carrots" in vegetables:
    vegetables.append("carrots")
else:
    print("Carrots are already in the list.")

if not "cucumbers" in vegetables:
    vegetables.append("cucumbers")
else:
    print("Cucumbers are already in the list.")

vegetables.sort()

print(f"Updated Vegetable Inventory: {vegetables}")