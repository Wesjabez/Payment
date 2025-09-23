# lets play a little with the so called classes in python i guess

# so first eith creating a simple class

class User:
    def __init__(self, name , age , gender ,  national_ID,photo):
        self. __name =name
        self. __age = age
        self. __gender = gender
        self. __national_ID = national_ID
        self.__photo = photo


    #now for some validations
    #string
    @property
    def name(self):
        return[self.__name,self.__age, self.__gender,self.__national_ID,self.__photo]
    
    @name.getter
    def name(self):
        print (f'This account belongs to a {self.__gender} user, {self.__name} of age {self.__age} of national ID {self.__national_ID}.')

    @name.setter
    def name(self,name_value): #  , age_value, gender_value, nationaId_value
        #name validation( check for the length, type of characters used)
        if isinstance(name_value, str) and name_value.isalpha() and 5 <= len(name_value) <= 20:
            self.__name = name_value
        else:
            raise ValueError (" invalid characters used")
    @property
    def age(self):
        return (self.__age)
    
    @age.setter
    def age(self, age_value):
        if isinstance(age_value,int) and not isinstance(age_value, bool) and 0 <= age_value <= 101:
            self.__age = age_value
        else:
            raise ValueError (" invalid age")

    #now for some age validation
p1 = User("Bill", 21, "male", 112211, "jpg")

p1.name = 'constantine'
p1.name
p1.age =40
p1.name