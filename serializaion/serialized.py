def convert_product(product) -> dict:
    return {
        "id": str(product["_id"]),
        "name": product["name"],
        "price": product["price"],
        "color": product["color"]     
    } 
   
def convert_products(products) -> list:
    return [convert_product(product) for product in products]




def convert_user(user) -> dict:
    return{
        "id": str(user["_id"]),
        "name": user["name"],
        "email": user["email"],
        "password": user["password"]
    }
    
def convert_users(users) -> list:
    return[convert_user(user) for user in users]
        