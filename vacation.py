'''
Tezza Reddy
CSC110
Project - 1
This function creates a story about two friends who are
planned to go on a vacation but they had a problem with their pet 
about finding a place to sit
'''

def create_story(person_one, person_two, pet_name, animal,
    place, adjective, verb, adverb):
    '''
    This function creates a story about two friends planning
    to go on a vacation but their have a problem with their
    pet polar bear they end up finding a sitter for
    their pet and then enjoy the vacation. 
    Args:
        person_one: first person
        person_two: friend of first person
        pet_name: name of the pet
        animal: polar bear
        place: the place where they are going for vacation
        adjective: which describes the behaviour of pet 
        verb: action being performed
        adverb: a word which modifies an adjective
    Returns:
        The story of two people planning move on a vacation
    '''

    # code written where words are inserted from the below code into story 
    story=(f"""{person_one} and {person_two} were best friends.
One day {person_one} and {person_two} decided to go on a
vacation to {place}. However, they didn't know
what to do with their {adjective} pet {animal} named {pet_name}.
{pet_name} had been causing problems, due to constant {verb}ing.
{person_one} found a sitter for their pet, and {adverb} went on the trip.""")
    return story
    
def main():
    '''
    This function contains all the values
    to be inserted into the variable "story" 
    '''
    person_one = "Joe" 
    person_two = "Lily" 
    pet_name = "Poncho"
    animal = "polar bear"
    place = "Madagascar"
    adjective = "Ridiculous"
    verb = "plank"
    adverb = "spastically"
    story = create_story(person_one, person_two, pet_name,
    animal, place, adjective, verb, adverb)
    print(story)
main()