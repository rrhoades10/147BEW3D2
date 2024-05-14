# Encapsulation
# Encapsulating a class's attributes
# Managing who, when, and where our class attributes are being access
# Data Bundling - controlling access to attributes

# Public - Accessible from anywhere - outside or inside the class
# object_name.attribute
# object_name.get_attribute() <-- this will return that specific attribute
# Most accessible type of attribute
# self.model

# Protected - Accessible only from within the class or sublcasses
# self._phone_number - underscore precedes the attribute name
# Kind of accessible - middle ground between public and private

# Private - Accessible only from within the class they're defined in
# self.__password
# python mangles attribute names that have the leading double underscore
# mangles to this --> _User__password

class Smartphone:
    def __init__(self, model, serial_number, operating_system):
        self.model = model #Public Attribute
        self._operating_system = operating_system # Protected Attribute
        self.__serial_number = serial_number # Private Attribute

    def show_info(self):
        # access info within the class here
        # except for __serial_number which is private
        # so should only be accessibly through a getter -- more on that later
        print(f"Model: {self.model}")
        print(f"Operating System: {self._operating_system}")
        print(f"Serial Number: Hidden for security purposes")

# create instance of Smartphone 
my_phone = Smartphone("Iphone 13", "v257ho3", "IOS")

# accessing the public attribute
print(my_phone.model)

# You can but SHOULD NOT access a protected variable outside the class
# outside - accessing the variable without a class method
# accessing the attribute directly through the object
print(my_phone._operating_system) #python's access modifiers are just naming conventions
# DONT DO THIS ^^^^
# accessing a private attribute outside of the class throws an attribute error
# print(my_phone.__serial_number)
# python mangles the attribute name that has the double underscore
# _ClassName__private_attribute
print(my_phone._Smartphone__serial_number) # we can still access private attributes BUT WE SHOULD NOT

# GETTERS and SETTERS
# GETTER - method for reading and accessing private attributes
# SETTER - method for controlling the way we modify private attributes
class Smartphone:
    def __init__(self, model, serial_number, operating_system):
        self.model = model #Public Attribute
        self._operating_system = operating_system # Protected Attribute
        self.__serial_number = serial_number # Private Attribute

    def show_info(self):
        # access info within the class here
        # except for __serial_number which is private
        # so should only be accessibly through a getter -- more on that later
        print(f"Model: {self.model}")
        print(f"Operating System: {self._operating_system}")
        print(f"Serial Number: Hidden for security purposes")

    # getter - secure way of accessing a private attribute
    def get_serial_number(self):
        return self.__serial_number
    
    # setter - secure way of modifying private attributes
    def set_serial_number(self, new_number): 
        self.__serial_number = new_number

    def show_info(self):
        print(f"Here is my operating system: {self._operating_system}")

    # using a setter in a method that is going alter a private attribute
    # rather than directly accessing the private attribute
    # we call the setter to set the private attribute to something new
    # additional functionality making sure the new serial number is a valid length
    # def update_serial_number(self):
    #     new_num = input("What is your new serial number ")
    #     if len(new_num) >= 10:
    #         self.set_serial_number(new_num)
    #     else:
    #         print("That serial number is invalid")

    # altering a public attribute with no setter
    # directly access the public attribute within the method and change it
    # to whatever the new value is going to be
    # def change_model(self):
    #     model = input("What is the new model? ")
    #     self.model = model

my_phone = Smartphone("Nokia Camera Phone", "354v6q6b7nc4", "Nokia dsigfb")
# accessing public attribute
print(my_phone.model)

print(my_phone.get_serial_number())

my_phone.set_serial_number("95v6bc25c39")
print(my_phone.get_serial_number())

# ========== INHERITANCE ==============
# a subclass (or child) inheriting from a super class (or parent)
# When a class inherits from another, it gets access to the parent class's 
# attributes and methods
# we can even instantiate attributes in the child class through the parent class's init

# PARENT CLASS
class Smartphone:
    def __init__(self, model):
        self.model = model #Public Attribute 
        

    def make_call(self, number):
        print(f"Making a call to {number}")

    def send_message(self, number, message):
        print(f"Sending message to {number}: {message}")

my_phone = Smartphone("Iphone 13")
my_phone.make_call("773202LUNA")

  #     child class       parent class - the inherited class hoes in the parentheses
class SmartCameraPhone(Smartphone):
    def __init__(self, model, camera_resolution):
        # calls the init from the parent class
        # to instantiate any inherited attributes
        super().__init__(model) #model is an attribute inherited from the SmartPhone class
        self.camera_resolution = camera_resolution # unique attribute to the child class

    # method unique to the child class
    def take_photo(self):
        print(f"Taking a photo with {self.camera_resolution} resolution")

    # Method Overriding
    # using a method from the parent class to better fit the needs of the child class
    # Polymorphism - inherit the method but the behavior of that method changes
    def make_call(self, number):
        # Overriding the make_call method
        print(f"Making a video call with {self.camera_resolution} resolution to {number}" )

        

camera_phone = SmartCameraPhone("Nokia", "4k")

# calling parent methods through the instantiated child class
camera_phone.make_call("773202LUNA")
camera_phone.send_message("773202LUNA", "Please come give me new floors")
# calling method unique to the child class
camera_phone.take_photo()
# accessing model attribute that was set in the parent class
print(camera_phone.model)
# creating an instance of the parent class
my_phone = Smartphone("Iphone 13")
# trying to access methods from the child class
# my_phone.take_photo() Attribute error take_photo does not exist in the parent class

# Method overloading 
# overriding a method from the parent class - multiple methods have the same name
# they have different parameters
class CellPhone():
    def send_message(self, text):
        print(f"Sending text: {text}")

class SmartPhone(CellPhone):
    # overloading the parent method, by using the same method name with additional parameters
    # to meet the needs of the child class
    #                             optional parameters, this method can send a text and optionally an image or video
    def send_message(self, text, image="", video=""):
        #                           if no argument is provided, image and video are empty strings
        if image:
            print(f"Sending text: {text} and image: {image}")
        if video:
            print(f"Sending text: {text} and image: {video}")
        print(f"Sending text: {text}")

    def send_parent_message(self, text): #calling parent method
        super().send_message(text)

my_phone = SmartPhone()
my_phone.send_parent_message("Hello have a nice day")
# send_message("Hello have a nice day!")
# send_message("Hello here is a picture of my dogs", "<picture of some toes>")








