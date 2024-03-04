from pymongo import MongoClient
from bson.objectid import ObjectId

class AnimalShelter(object):
  """ CRUD operations for Animal collection in MongoDB """

  def __init__(self, username, password):
    #
    # Connection Variables
    #
    USER = username
    PASS = password
    HOST = 'nv-desktop-services.apporto.com'
    PORT = 31372
    DB = 'AAC'
    COL = 'animals'
    
    #
    # Initialize Connection
    #
    self.client = MongoClient('mongodb://%s:%s@%s:%d' % (USER,PASS,HOST,PORT))
    self.database = self.client['%s' % (DB)]
    self.collection = self.database['%s' % (COL)]
    print ("Hello", USER)
   
# Complete this create method to implement the C in CRUD.
  def create(self, data):
    if data is not None:
        try:
          self.database.animals.insert_one(data)  # data should be dictionary 
          print("Your data has been inserted")
          return True
        except Exception as e:
            print(f"Error during insertion: {e}")
            return False
          
    else:
      raise Exception("Nothing to save, because data parameter is empty")

# Create method to implement the R in CRUD.
  def read(self, query):
    try:
       result = self.collection.find(query)
       return result
    except Exception as e:
      return str(e)	

# Update method to implement the U in CRUD
  def update(self, query, updateNumber, updateData):
        if query is not None:
            if updateNumber == "one":
                result = self.database.animals.update_one(query, updateData)
                if result.modified_count == 1:
                    print(result.modified_count, "object(s) updated")
                    return True
                else: 
                    print("Sorry, your entry has failed to update.")
                    return False
            
            if updateNumber == "many":
                result = self.database.animals.update_many(query, updateData)
                if result.modified_count > 0:
                    print(result.modified_count, "object(s) updated")
                    return True
                else: 
                    print("Sorry, your entry has failed to update.")
                    return False
        else:
            raise Exception("Nothing to update, because data parmater is empty")
            
# Delete method to implement the D in CRUD
  def delete(self, data):
        if data is not None:
            result = self.database.animals.delete_one(data)
            if result.deleted_count > 0:
                print(result.deleted_count, "object(s) deleted!")
                return True
            else:
                print("Something went wrong, and the deletion failed")
                return False
        else:
            raise Exception("No data was entered for deletion")
            
            