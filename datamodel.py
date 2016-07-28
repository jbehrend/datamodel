from SerializeConvert import MySerializer

class MyRootModel(MySerializer):
    #make dictionary where keys are attributes and values convert to proper type)
    my_attrs = {'an_attr': int , 'another_attr': str}


    def __init__(self, **kwargs):
        for k,v in self.my_attrs.items():
            val  = kwargs.get(k)
            setattr(self, k, v(val))




