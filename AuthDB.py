import pymongo


class AuthDB:

    def __init__(self):
        # opens a connection with the local database
        self.client = pymongo.MongoClient()
        self.db = self.client.db
        # naming the collection
        self.collection = self.db.auth

    def insert(self, data):
        try:
            post_id = self.collection.insert_one(data).inserted_id
        except:
            return 'Error'
        return 'Successfully added ' + str(data)

    def find_user(self, data):
        try:
            res = self.collection.find_one(data)  # attempt to find data in db
            # ensure all aspects of login information match
            if res['username'] == data['username'] and res['password'] == data['password']:
                return True
            else:
                return False
        except:
            return False

    def user_status(self, data):
        try:
            res = self.collection.find_one(data)
            return res['status']  # placeholder status field, may change later
        except:
            return 'Attempt to access user status failed.'  # placeholder error message

    # clears the database, this can be used to remove duplicate objects in the database when testing
    def clear_db(self):
        self.db.drop_collection(self.collection)
