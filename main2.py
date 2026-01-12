# from fastapi import FastAPI, HTTPException
# from pydantic import BaseModel
# app = FastAPI()

# class Item(BaseModel):
#     email: str
#     password: str
#     pin: int | str
    
    
#     allData = []


# @app.get("/")
# def new_one():
#     return{"data": "onyem"}

# @app.get("/get-all-data")
# def getAllData():
#     return {"data": allData}

# @app.get("/fetch-age")
# def fetchage():
#     return{"data": "age" }

# @app.get("/fetch-name")
# def fetchName():
#     return({"data": allData[0]["name"]})

# @app.get("/fetch-course")
# def fetchCourse():
#     return{"data": "course"}

# @app.get("/fetch-city")
# def fetchCity():
#     return{"data": "city"}

# @app.post("/create-user")
# def createUser(data: Item):
#         if data.pin < 10:
#             raise HTTPException(status_code=400, detail="Pin is required")
#         allData.append(data)
#         return {"data": "Account created successfully"}
    
    
    
    
    
    
    
    
# from fastapi import FastAPI
# from pydantic import BaseModel
# app = FastAPI()

# class Item(BaseModel):
#     email: str
#     name: str
#     state: str
#     courses: list[str] = []
#     password:str 
#     plans : dict = {}

# class Auth(BaseModel):
#     email: str  
#     password: str  

# database = []

# @app.post("/create-account")
# def createAccount(data: Item):
#         if data.name == "":
#             return {"messeage":"failed to create account", "error":"name is required"}
#         elif data.email == "":
#             return{"messeage":"failed to create account", "error":"email is required"}
#         elif data.state == "":
#             return{"messeage":"failed to create account", "error":"state is required"}
#         elif data.courses == 0:
#             return{"messeage":"failed to create account", "error":"at least one course is required"}
#         elif data.password == "":
#             return{"messeage":"failed to create account", "error":"password is required"}
#         else:
#               return {"data": "account succesfull created"}
        
#         # data = {
#         #     "email": database["email"],
#         #     "name": database["name"],
#         #     "state" : database["state"],
#         #     "courses" :database["courses"],
#         #     "password" :database["password"],
#         #     "plans" : {}
#         # }
        
       

    
# @app.patch("/update-account")
# def updateAccount(data: Item):
#         database.append(data)
#         return {"data": "account succesfull updated"}
    
        
# @app.post("/login-account")
# def login(data: Auth):
#         # database.append(data)
#         return {"data": "login successful"}
    
# @app.get("/fetch-users")
# def fetchAccount():
#     return{"account": database}
    

# @app.get("/fetch-user/{userId}/account")
# def fetchAccounts(userId: str):
#     return{"account": userId}
  
  
# from fastapi import FastAPI, HTTPException
# from pydantic import BaseModel
# app = FastAPI()  

# class ProductModel(BaseModel):
#      name: str
#      price: str
#      color: str
 
# products = []

# @app.post("/add-product")
# def addProduct(product: ProductModel):
#     data = {
#         "Id": len(products) + 1,
#         "name": product.name,
#         "price": product.price,
#         "color": product.color
#     }
#     products.append(data)
#     return{"messeage":"product added succesfully", "data": product}

# @app.get("/get-all-product")
# def get_all_Product():
#       return{"total": len(products), "data": products}

# @app.get("/product/{productId}")
# def get_Product(productId: int):
#     for x in products:
#         if x["Id"] == productId:
#             return{"account": x}
#     else:
#         raise HTTPException(status_code=404, detail = "product not found")
    

# @app.delete("/delete-product/{productid}")
# def deleteProduct(productid: int):
#     for product in products:
#         if product["Id"] == productid:
#             products.remove(product)
#             return{"messeage":"product successfuly deleted"}
#         else:
#             return{ "product not found"}
    
    
# from pymongo import MongoClient
# from fastapi import FastAPI, HTTPException
# from pydantic import BaseModel
# app = FastAPI()

# class UserModel(BaseModel):
#     username: str
#     pin: int
#     country: str
    
# Users = []
    
    
# @app.post("/create-user")
# def createUser(user: UserModel):
#     data = {
#         "id": len(Users) + 1,
#         "username": user.username,
#         "pin": user.pin,
#         "country": user.country, 
#     }
#     Users.append(data)
#     return{"messeage": "user added successfully", "data": user}


# @app.patch("/update-pin/{username}")
# def updatePin(username: str, new_pin: int):
#     for user in Users:
#         if user["username"] == username:
#             user["pin"] = new_pin
#             return{"message": f"pin successfull updated, {new_pin}", "data": user}
#     else:
#         raise HTTPException(status_code=404, detail = "user not found")
   
   
    
# @app.patch("/update-username/{old_username}")
# def updateUsername(old_username: str, new_username: str):
#     for user in Users:
#         if user["username"] == old_username:
#             user["username"] = new_username
#             return{"messeage": "username updated successfully","data": user}
#     else:
#         raise HTTPException(status_code=404, detail = "user not found")
 
 
    
# @app.delete("/delete-user/{username}")
# def deleteUser(username: str):
#     for i, user in enumerate(Users):
#         if user["username"] == username:
#             deleted = Users.pop(i)
            
#             return{"messeage": "user deleted successfully", "info deleted": deleted}

   
   
# @app.get("/get-users/{pin}")
# def fetchUser(pin: int):
#     for user in Users:
#         if user["pin"] == pin:
#             return{"account": user}
      #  else:
#     raise HTTPException(status_code=404, detail = "user not found")
   
   
    
# @app.get("/get-all-users")
# def getUsers():
#       return{"total": len(Users), "data": Users}
  
  
  
  
  
  
# from fastapi import FastAPI, HTTPException
# from pydantic import BaseModel
# app = FastAPI()


# class UserModel(BaseModel):
#      id: int
#      username: str
#      country: str
#      pin: int
     
#      Users=[]
     
# @app.post("/createusers")
# def Create_user(user, UserModel):
#   data = {
    
#     "id": len(Users) + 1,
#     "username": user.username,
#     "pin": user.pin,
#     "country": user.country,
#   }
#   user.append(data)
#   return{"message": "user created succesfully", "data": user}

# @app.patch("/update-username,{old_username}")
# def update_username(old_username: str, new_name: str):
#   for user in Users:
#     if user["username"] == old_username:
#        user["username"] = new_name
#        return{"message": "username updated successfully", "data": user}
#     else:
#       raise HTTPException(status_code=404, detail = "user not found")
    
# @app.patch("/update-pin,{username}")
# def update_pin(old_pin: int, new_pin: int):
#   for user in Users:
#     if user["username"] == old_pin:
#        user["username"] = new_pin
#        return{"message": "pin updated successfully", "data": user}
#     else:
#       raise HTTPException(status_code=404, detail = "user not found")
     
# @app.delete("/delete-user, {uesrname}")
# def delete_user(usernam: str):
#   for i, in user enumerate(Users):
#     if user["username"] == username:
#       deleted = User.pop(i)
#       return{"message": "user deleted successfully", "data": user}
#     else:
#       raise HTTPException(status_code=404, detail = "user not found")
             
       
    
# uri = "mongodb://localhost:27017/product"
# client = MongoClient(uri)
# try:
#     database = client.get_database("sample_mflix")
#     movies = database.get_collection("movies")
#     # Query for a movie that has the title 'Back to the Future'
#     query = { "title": "Back to the Future" }
#     movie = movies.find_one(query)
#     print(movie)
#     print("database is connected")
#     client.close()
# except Exception as e:
#     raise Exception("Unable to find the document due to the following error: ", 




     
     
     