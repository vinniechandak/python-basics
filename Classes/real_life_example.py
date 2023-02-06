'''
A class is a family of objects
Classes can be used to simulate real life things
An object is an instance of a class, that means that an object is something that respects the clases atributes
For example we can define a Dog class and then use this class to define various diferents dogs objects
'''

class Dog():

    '''
    The __init__ method is the class constructor and it defines the "skeleton" of our class
    For example, here we must think how a dog is made
    A dog has: 
        his name
        -his race
        -his color
        -his number of legs (generaly four)
        -etc. lets start with this
    '''
    def __init__(self, name, race, color, legs=4): #The legs atribute is set to four by default (this means that if we dont asign anythig to this atribute it will be four) but we can change it 
        self.name = name
        self.race = race
        self.color = color
        self.legs = legs
        '''
        The self argument refers to the actual object that we will create (don't worry for now just know it goes there) 
        '''
    
    '''
    Now it is time to think what things can a dog do
    For example a dog can bark, so we define a function that will allow our dog to bark
    '''
    def bark(self):
        print('Woof')

    '''
    We can also define a function that tells us all the caracteristics of our dog
    Think this as the owner of the dog telling us his name, race, etc.
    '''
    def see_caracteristics(self):
        print(f'Name: {self.name} \nRace: {self.race} \nColor: {self.color} \nNumber of legs: {self.legs}') #This is an fstring, it is just a usefull tool to concatenate string and variables

'''
Now it is time to create some dogs!!!!
'''
dog1 = Dog('John', 'Golden Retriever', 'Beige')
dog2 = Dog('Tim', 'Husky', 'White', legs=3) #This dog lost a leg in an accident :( so we specify legs=3

'''
Now we can see our dogs caracteristics using on them the see_caracteristics method
'''
dog1.see_caracteristics()
dog2.see_caracteristics()

'''
Now it is time...
We can make our dos bark!!!!!
'''
dog1.bark()
dog2.bark()

