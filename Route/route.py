from fastapi import APIRouter, HTTPException
from confiq.confiq import collection
from model.tenant_model import User 
from serializaion.serialized import convert_product, convert_products
from model.product_model import Product
import random 
import validator
from password_validator import PasswordValidator


route = APIRouter()
schema = PasswordValidator()


@route.get("/get-user")
def get_users():
    return {"message": "user fetched successfull"}

@route.post("/create_product")
def create_product(product: Product):
    product_dict = product.dict()
    result = collection.insert_one(product_dict)
    return convert_product(collection.find_one({"_id": result.inserted_id}))

@route.get("/all-products")
def get_products():
    results = collection.find()
    return convert_products(results)

@route.get("/get_product/{name}")
def get_product(name: str):
    result = collection.find_one({"name": name})
    return convert_product(result)
    
    
# @route.post("/users")
# def create_user(user:User):
#     try:
#         userId = random.choice(range(1,45))
#         user.userId = userId[0]
#         user_dict = user.dict()
#         if(user_dict["name"] == ""):
#             raise HTTPException(status_code = 400, details = "Name is required")
#         if(user_dict["email"] == ""):
#             raise HTTPException(status_code=400, details = "Email is needed")
#         if (not validators.email(user_dict["email"])):
#             raise HTTPException(status_code=400, details = "Email is not valid")
#         if(user_dict["password"] == ""):
#             raise HTTPException(status_code=400, details = "password is required")
#         if (schema.validate(user_dict["password"]) == False):
#             raise HTTPException(status_code = 400, details = "password not srong")
#         if (int(user_dict["age"])<= 18):
#             raise HTTPException(status_code=400, details = "Age must be at least 18")
#         # if(user_dict["gender"]lower().find("male") == -1 and user_dict["gender"].lower().find("female") == -1):
#         #     raise HTTPException(status_code=400, details = "Gender must be either male or female")
#         if(user_dict["bio"] == ""):
#             raise HTTPException(status_code =400, details = "Bio is required")
        
#         result = userCollection.insert_one(user_dict)
#         userResult = userCollection.find_one({"_id:result.inserted_id"})
#         return convertUser(userResult)
#     except HTTPException as e:
#         raise HTTPException(status_code=500, details = {"message": "Server error"})
    
  
    
        
        
# @route.get("/users")
# def  get_users(): 
#      Users = userCollection.find()
#      return convertUser(users) 
 
# @route.get("/user/{userId}")
# def get_user(userId:str):
#     user = userCollection.find_one({"userId": userId})
#     return convertUser(user)   