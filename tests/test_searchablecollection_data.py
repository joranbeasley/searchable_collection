class SimpleSearchExampleClass:
    def __str__(self):
        return str(self.__dict__)

    def __repr__(self):
        return "<s:" + str(self) + ">"

    def __init__(self, **kwargs):
        self.__dict__.update(**kwargs)
    @staticmethod
    def create(string_field1="",string_field2="",int_field1=0,int_field2=-2,int_field3=-10,list_field1=[1,2],list_field2=["a","b"],subclass=None):
        return SimpleSearchExampleClass(**locals())
    @staticmethod
    def generate(include_subclasses=True):
        import random
        data = {
            "string_field1": "a string [" + str(random.randint(100000, 100000000)) + "]",
            "string_field2": random.choice("Hello World Apples Spices Rabits Doggos".split()),
            "int_field1": random.randint(1000, 10000),
            "int_field2": random.randint(1, 5),
            "int_field3": random.randint(100, 500),
            "list_field1": [random.randint(1, 100) for _ in range(15)],
            "list_field2": random.sample(["apple", "pie", "raspberry", "shortcake", "evening"], 2),
            "subclass": SimpleSearchExampleClass.generate(False) if include_subclasses else None
        }
        return SimpleSearchExampleClass(**data)

def test_create_simpleclass():
    simple_class = SimpleSearchExampleClass.create("asd","dsa",1,15,100,[7,7,7],["a","b"],{"a":7})
    assert simple_class.string_field1 == "asd"
    assert simple_class.string_field2 == "dsa"
    assert simple_class.int_field1 == 1
    assert simple_class.int_field2 == 15
    assert simple_class.int_field3 == 100
    assert simple_class.list_field1 == [7,7,7]
    assert simple_class.list_field2 == ['a','b']
    assert simple_class.subclass == {"a":7}


    generated_class = SimpleSearchExampleClass.generate()
    assert generated_class.subclass is not None
    assert generated_class.subclass.subclass is None


