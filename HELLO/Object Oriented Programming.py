"""class car:
    #serve as constructor, automatically invoke
    #giving an class variable inside the function itself
    #used decorater @property and setter as @color.setter
    def __init__(self, model = "bmw", color = "red"):
        print("calling__init")
        self.model ="maruthi"
        self.color ="red"
        self.seat_count =  5
        self.country = "India"
        self.speed = 100

def increse_speed(self):


#model
# color
# no of seats
# country
# number of wheels

#create object code

my_car = car()
your_car = car()
my_car.model = "maruthi"
your_car.model = "honda"
your_car.color = "red"
print(my_car.model)
print(your_car.model)
print(your_car.__dict__)"""

"""class postit():
    def __init__(self):
        print("callin__init__")
        self.backgroundcolor = "red"
        self.text = "Object Oriented Programming"
        self.textcolor = "blue"
        self.name = "postit"
my_self = postit()
print(my_self.textcolor)
print(my_self.name)
idea1 = postit()
awesome = "a pink with black text"
superb = "a yellow with green text"
print(idea1)
print(awesome)
print(superb)"""

class Blogspot:
    def __init__(self, Authorname, a_title, publicationdate):
        print("calling__init__")
        self.Authorname = "an author name"
        self.a_title = "what is the title"
        self.publication_date= 5/11/2021
new_blogspot = Blogspot()
new_blogspot.Authorname = "Lorem Ipsum"
new_blogspot.a_title = "titled by John Doe"
new_blogspot.publication_date = "2000.05.04"
new_blogspot.note = "Lorem ipsum dolor sit amet."
new1_blogspot = Blogspot()
new1_blogspot.Authorname= "Wait but why"
new1_blogspot.a_title = "Tim Urban"
new1_blogspot.publication_date ="2010.10.10."
new1_blogspot.note = "A popular long-form, stick-figure-illustrated blog about almost everything."
new2_blogspot = Blogspot()
new2_blogspot.Authorname = "One Engineer Is Trying to Get IBM to Reckon With Trump"
new2_blogspot.a_title = "William Turton"
new2_blogspot.publication_date = "2017.03.28."
new2_blogspot.note = "Daniel Hanley, a cybersecurity engineer at IBM, doesn’t want to be the center of attention. When I asked to take his picture outside one of IBM’s New York City offices, he told me that he wasn’t really into the whole organizer profile thing."
print(new_blogspot)
print(new1_blogspot)
print(new2_blogspot)




