import uuid

def workbench():
    user_id = uuid.uuid4()                 #    user_id = uuid.uuid4()                 # keep module name uuid, store value in user_id
    user1 = "NewUser" + str(user_id)       # convert UUID to string
    print(user1)

if __name__ == "__main__":
    workbench()