from bson.json_util import dumps
from bson.objectid import ObjectId
from app import collection

class Service : 
    def add_patient (self, payload) :
        if isinstance(payload ,dict) :
            collection.insert_one(payload)
        elif isinstance(payload, list) :
            collection.insert_many(payload)
        else :
            raise ValueError("Unsupported data type")

    def get_all_patient (self) :
        result = collection.find()
        patients = dumps(result)
        return patients
        
    def get_patient(self, id) :
        result = collection.find_one({'_id' : ObjectId(id)}, {'_id': 0})
        patient = dumps(result)
        return patient

    def remove_patient(self,id) : 
        result = collection.delete_one({'_id' : ObjectId(id)})
        if result.deleted_count > 0 :
            return "Removed successfully"
        else : 
            return "No data found with the given ID"
    
    def update_patient(self, id, payload):
        for item in payload:
            res = collection.update_one({'_id': ObjectId(id)}, {'$set': item})
        if res.modified_count > 0:
            return "Updated successfully"
        else:
            return "No data found with the given ID"
