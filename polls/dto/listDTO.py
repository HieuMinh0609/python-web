import json
from json import JSONEncoder
class AddressDTO:
    def __init__(self, recipientName, addressDetail, recipientPhone,id):
        self.recipientName = recipientName
        self.addressDetail = addressDetail
        self.recipientPhone = recipientPhone
        self.id=id

class AddressDTOEncoder(JSONEncoder):
        def default(self, o):
            return o.__dict__