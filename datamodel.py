import MySerializer

class MyRootModel(MySerializer):
    #make dictionary where keys are attributes and values convert to proper type)
    my_attrs = {'an_attr': int , 'another_attr': str}


    def __init__(self, **kwargs):
        for k,v for my_attrs.items():
            val_type  = kwargs.get(v)
            setattr(self, v, val_type(v))




