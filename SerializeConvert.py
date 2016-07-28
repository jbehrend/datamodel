import json

class MySerializer(object):

    @classmethod
    def deserialize(cls, jsonstr):
        #load from json to dict
        d = json.loads(jsonstr)
        #initialize object, return
        return cls(**d)

    def serialize(self):
        #iterate over self.my_attrs
        #get attrs, set into dicitonary
        my_dict = {}
        for i in self.my_attrs:
            a = getattr(self, i, None)
            my_dict[i] = a
        #return dumps(dictionary)
        jsonstr = json.dumps(my_dict)
        return jsonstr

