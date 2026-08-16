import pandas as pd
import matplotlib.pyplot as plt


# ==========================================
# 1. READ SALES DATA
# ==========================================

data = pd.read_csv("data/salces.cvs")


# ==========================================
# 2. CALCULATE SALES FOR EACH ORDER
# Sales = Quantity × Price
# ==========================================

data["Sales"] = data["Quantity"] * data["Price"]


# ==========================================
# 3. DISPLAY SALES DATA
# ==========================================

print("========== SALES DATA ==========")
print(data)


# ==========================================
# 4. TOTAL SALES
# ==========================================

total_sales = data["Sales"].sum()

print("\n========== TOTAL SALES ==========")
print("Total Sales:", total_sales)


# ==========================================
# 5. SALES BY PRODUCT
# ==========================================

product_sales = data.groupby("Product")["Sales"].sum()

print("\n========== SALES BY PRODUCT ==========")
print(product_sales)


# ==========================================
# 6. BEST-SELLING PRODUCT
# ==========================================

best_product = product_sales.idxmax()
best_product_sales = product_sales.max()

print("\n========== BEST-SELLING PRODUCT ==========")
print("Product:", best_product)
print("Sales:", best_product_sales)


# ==========================================
# 7. SALES BY CITY
# ==========================================

city_sales = data.groupby("City")["Sales"].sum()

print("\n========== SALES BY CITY ==========")
print(city_sales)


# ==========================================
# 8. BEST-PERFORMING CITY
# ==========================================

best_city = city_sales.idxmax()
best_city_sales = city_sales.max()

print("\n========== BEST-PERFORMING CITY ==========")
print("City:", best_city)
print("Sales:", best_city_sales)


# ==========================================
# 9. SALES BY CATEGORY
# ==========================================

category_sales = data.groupby("Category")["Sales"].sum()

print("\n========== CATEGORY-WISE SALES ==========")
print(category_sales)


# ==========================================
# 10. BEST CATEGORY
# ==========================================

best_category = category_sales.idxmax()
best_category_sales = category_sales.max()

print("\n========== BEST CATEGORY ==========")
print("Category:", best_category)
print("Sales:", best_category_sales)


# ==========================================
# 11. PRODUCT-WISE SALES CHART
# ==========================================

plt.figure(figsize=(10, 5))

product_sales.plot(kind="bar")

plt.title("Product-wise Sales")
plt.xlabel("Product")
plt.ylabel("Sales")

plt.tight_layout()

plt.show()
# ==========================================
# 11. SALES CHARTS
# ==========================================

# Product-wise Sales
plt.figure(figsize=(10, 5))
product_sales.plot(kind="bar")
plt.title("Product-wise Sales")
plt.xlabel("Product")
plt.ylabel("Sales")
plt.tight_layout()
plt.savefig("output/product_sales.png")
plt.show()


# City-wise Sales
plt.figure(figsize=(10, 5))
city_sales.plot(kind="bar")
plt.title("City-wise Sales")
plt.xlabel("City")
plt.ylabel("Sales")
plt.tight_layout()
plt.savefig("output/city_sales.png")
plt.show()


# Category-wise Sales
plt.figure(figsize=(8, 5))
category_sales.plot(kind="bar")
plt.title("Category-wise Sales")
plt.xlabel("Category")
plt.ylabel("Sales")
plt.tight_layout()
plt.savefig("output/category_sales.png")
plt.show()