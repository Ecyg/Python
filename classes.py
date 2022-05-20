class Student:
    class_attribute = "I am a class attribute"
    all = []
    def __init__(self, name:str , gpa:float , major:str , remote:bool = False) -> None:

        #print(f"Student object created : {name} {gpa}, {major}")

        #How can I check to see if the parameter passed to this function are within my expectations?
        # Example : How can I check to see if GPA is greater than 0.0 (there are two ways, hint : be assertive)

        #Assign to self object
        self.name = name
        self.gpa = gpa
        self.major = major
        self.remote = remote

        #Add that object to the list
        Student.all.append(self)

    def printStudent(self):
        print(f"Student Name : {self.name}\nGPA : {self.gpa}\nMajor : {self.major}\nAre they remote? {self.remote}")

# I am overwriting the assigned objects "major" value with a class attribute. Note that I had to call the class to access it.
    def overwrite_major(self) -> None:
        self.major = self.class_attribute



def main():
    #list of calls 

    Student1 = Student("Matthew", 3.6, "Computer Science") #Create an instance of the class
    Student2 = Student("Tristan", 4.0, "Biology")
    #print(Student1.name)   # Call a descriptor of the class (object)
    #print(Student2.name)
    #print(Student1.remote)  
    #Student2.printStudent()  # Call a function of the class


    #print(Student.class_attribute)  #Access the class attribute from the class
    #print(Student1.class_attribute)  #Access the class attribute from an instance

    #Here I am assigning a new value to a class attribute, then calling the function overwrite_major()
    #which changes the value of the object from the class, but only for this instance
    #Not all students would have their major change to physics. 
    #Student2.class_attribute = "Physics"
    #Student2.overwrite_major()
    #Student2.printStudent()


    #print(Student2.__dict__)   # Hidden attribute of all classes that returns all attribute of an object
    #print(Student.__dict__)   #You can do this for an instance of the class as well

    #We created a list of all of our objects. Let's call it
    #print(Student.all)

    #We can do some cool stuff with that, like call of the name values of all the objects created by the class
    '''
    for instance in Student.all:
        print(instance.name)
    '''


if __name__ == "__main__":
    main()