import pymongo


class AuthDB:

    def __init__(self):
        # opens a connection with the local database
        self.client = pymongo.MongoClient()
        self.db = self.client.db
        # naming the collection
        self.collection = self.db.auths

    def insert(self, data):
        try:
            post_id = self.collection.insert_one(data).inserted_id
        except:
            return 'Error'
        return 'Successfully added ' + str(data)

    def find_user(self, user):
        try:
            res = self.collection.find_one(user)  # attempt to find data in db
            # ensure all aspects of login information match
            if res['Tag'] == user['Tag']:
                return True
            else:
                return False
        except:
            return False

    def user_status(self, user):
        try:
            res = self.collection.find_one(user)
            return res['Status']  # placeholder status field, may change later
        except:
            return 'Attempt to access user status failed.'  # placeholder error message

    # updates a user's status
    def change_status(self, user, new_status):
        try:
            res = self.collection.find_one(user)
        except:
            return 'User not found in database.'
        self.collection.update_one(user, {'$set': {'Status': str(new_status)}})
        return 'Updated ' + str(user) + ' status to ' + str(new_status)

    # clears the database, this can be used to remove duplicate objects in the database when testing
    def clear_db(self):
        self.db.drop_collection(self.collection)
