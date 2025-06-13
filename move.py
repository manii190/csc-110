'''
venna mani abhiram reddy
CSC110
Project -1
The code writes down the names within a
paragraph rather than the functions.

'''
def create_story(person_one,street_name,person_two,
object_name,vehicle,adjective):
    
    '''
    this code tells story of two friends
    who stuggled to shift
    Christmas tree to new house.
    Args:
    person_one: friend who is moving to new home
    street_name: location of new home
    person_two: the friend who came to help
    object_name: object which could not get into the truck
    vehicle: the truck that can weight Christmas tree
    adjective: to describe the rented vehicle
    Returns :
    story of two friends who stuggled to shift
    Christmas tree to new house.
    '''

    #the  functions are kept where the words should be pasted
    story=(f"""{person_one} decided to move from their apartment on 5th
to a condo on {street_name}. They called their friend {person_two}
for help. However, they could not fit {object_name} into
the moving truck, so they had to rent a {adjective} {vehicle}
in order to move it!""")
    return story

person_one = "Janet"
street_name = "Loopdydoo Avenue"
person_two = "Richard"
object_name = "Christmas tree"
vehicle = "Horse-drawn carriage"
adjective = "Off-road"
story = create_story(person_one,street_name,person_two
,object_name,vehicle,adjective)
print(story)