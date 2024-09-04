import csv
import os
import locale

def load_data(filename):
    products = []

    try:
        with open(filename, 'r', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            for row in reader:
                id = int(row['id'])
                name = row['name']
                desc = row['desc']
                price = float(row['price'])
                quantity = int(row['quantity'])
                products.append({
                    "id": id,
                    "name": name,
                    "desc": desc,
                    "price": price,
                    "quantity": quantity
                })
    except FileNotFoundError:
        print(f"File {filename} not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

    return products

def get_product(id, products):
    return products[id]

def get_products(products):
    product_list = []
    for product in products:
        product_info = f"Product: {product['name']} \t {product['desc']} \t {locale.currency(product['price'], grouping=True)}"
        product_list.append(product_info)
    
    return "\n".join(product_list)

locale.setlocale(locale.LC_ALL, 'sv_SE.UTF-8')

os.system('cls' if os.name == 'nt' else 'clear')

products = load_data('db_products.csv')

print(get_products(products))
