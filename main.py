""" Plural sight 3.8 Classes and Object Orientation"""
import iso6346

class ShippingContainer:
    # Class Attributes
    next_serial = 1337

    # # Method
    # # leading underscore bc implementation detail of this class, not intended for outside
    # @staticmethod
    # # Static bc only arg is self, then can get rid of self as a parameter
    # def _generate_serial():
    #     result = ShippingContainer.next_serial
    #     ShippingContainer.next_serial += 1
    #     return result

    """ Choosing class or static method
    if referring to the class object within the method (e.g. class attr or constructor) use CLASS METHOD
    if you don't need to refer to class or instance attr use STATIC METHOD
        - Static Method usually for implementation detail, in principle, it would also work fine if you removed it
        from the class and put in the global-scope function
    """

    # now do it as a class method, then replace ShippingContainer with cls bc clear were referring to this class
    @classmethod
    def _generate_serial(cls):
        result = cls.next_serial
        cls.next_serial += 1
        return result

    @staticmethod
    def _make_bic_code(owner_code, serial):
        return iso6346.create(
            owner_code=owner_code,
            serial=str(serial).zfill(6)
        )

    # having two diff class methods allows diff inputs, one for empty containers and one for those already filled
    # with items
    @classmethod
    def create_empty(cls, owner_code):
        return cls(owner_code, contents=[])

    @classmethod
    def create_with_items(cls, owner_code, items):
        return cls(owner_code, contents= list(items))


    # Constructor
    def __init__(self, owner_code, contents):
        # Instance Attributes
        self.owner_code = owner_code
        self.contents = contents
        self.bic = ShippingContainer._make_bic_code(
            owner_code=owner_code,
            serial=ShippingContainer._generate_serial()
        )

        """  Note instance attributes take precedence over class attributes when accessed through self
        so if used self.next_serial, instance attributed created, class attribute hidden.
        
        Python scoping rules: LEGB
        L: Local (inside current function)
        E: Enclosing (inside enclosing function)
        G: Global (at top level of module) - this is where 'next_serial' is, so refer to class by name within class def
        B: Built-in 
        """

# Testing create empty and create with items
c7 = ShippingContainer.create_empty("YML")
c8 = ShippingContainer.create_with_items("MAE", {"cola", "sprite", "fanta"})
print(f"c7 contains {c7.contents}")
print(f"c8 contains {c8.contents}")

print("c7 contains {}".format(c7.contents))

# Testing bic code creation
print(c7.bic)