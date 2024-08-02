print('''
Hi mate ! Welcome to Mad Libs !
Mad Libs is a game with a basic story template that has blank spaces which need to be filled by the player (you <3).
The fun part is that the player inputs words without knowing the story ahead of time.

Here are the steps:
1.Choose one of the templates by choosing a number: 1,2 or 3.
2.Enter words that will match the description provided by the game.
3.If you are run out of ideas, type 'idk' and the game will enter the word for you.
4.Enjoy your story !

If you are ready, let's start.
''')

choice = input('Choose a number: 1,2 or 3: ')
while choice != '1' and choice != '2' and choice != '3':
    choice = input('Invalid choice, try again: ')

print('The creation of your story begins now!')

def get_input(prompt, category):
    user_input = input(prompt)
    if user_input == 'idk':
        user_input = random.choice(category)
    return user_input

#to pluralize the noun if needed
def plural(noun, quantity):
    if int(quantity) > 1:
        return noun + 's'
    else:
        return noun

#to use the right preposition before the noun
prepositions = ['a', 'an']
vowel = ["a", "e", "i", "o"]
def preposition(noun):
    for i in vowel:
        if noun[0] == i:
            return prepositions[1] + ' ' + noun
        else:
            return prepositions[0] + ' ' + noun


import random
number = [5,9,15,36,48,65,25,45,30,80,44,71,86,99,10,50,33,6,8,22,11,66,79,500]
measure_of_time = ['second', 'minute', 'hour', 'day', 'week', 'month', 'year', 'decade', 'millenial']
mode_of_transportation = ['car', 'bicycle', 'airplane', 'helicopter', 'motorcycle', 'bus', 'helicopter', 'cruise', 'boat', 'track', 'hot air balloon', 'van', 'carriage', 'taxi', 'subway', 'train', 'submarine']
adjective = ['flabby', 'glamorous', 'gorgeous', 'handsome', 'long', 'magnificent', 'muscular', 'plain', 'helpful', 'important', 'inexpensive', 'mealy', 'mushy', 'odd', 'poor', 'powerful', 'rich', 'shy', 'calm', 'delightful', 'eager', 'faithful', 'gentle', 'happy', 'jolly', 'kind', 'lively', 'nice', 'obedient', 'polite', 'proud']
verb = ['accept', 'afford', 'arrange', 'behave', 'begin', 'borrow', 'cancel', 'choose', 'compare', 'continue', 'deliver', 'describe', 'enjoy', 'explain', 'finish', 'follow', 'guess', 'improve', 'involve', 'join', 'laugh', 'manage', 'offer', 'order', 'prefer', 'prepare', 'promise', 'provide', 'receive', 'recommend', 'refuse', 'repeat', 'respect', 'search', 'suggest', 'travel', 'use']
noun = ['child', 'teacher', 'student', 'book', 'pen', 'computer', 'phone', 'city', 'car', 'house', 'school', 'hospital', 'dog', 'cat', 'friend', 'family', 'table', 'chair', 'window', 'door', 'market', 'store', 'restaurant', 'park', 'road', 'river', 'mountain', 'beach', 'river', 'music', 'art', 'movie', 'song', 'game', 'sport', 'museum', 'library', 'garden', 'apartment']
color = ['red', 'blue', 'green', 'yellow', 'orange', 'purple', 'pink', 'brown', 'black', 'white', 'gray', 'cyan', 'magenta', 'violet', 'beige', 'maroon', 'teal', 'turquoise']
part_of_the_body= ['heads', 'hairs', 'eyes', 'ears', 'noses', 'mouths', 'teeth', 'tongues', 'necks', 'shoulders', 'arms', 'elbows', 'hands', 'fingers', 'thumbs', 'chests', 'stomachs', 'waists', 'backs', 'hips', 'legs', 'knees', 'ankles', 'feet', 'toes', 'skins', 'bones', 'muscles', 'veins', 'hearts']
silly_word = ['flibber', 'wobble', 'doodle', 'zany', 'gobble', 'fizzle', 'snicker', 'blubber', 'bamboozle', 'giggle', 'doozy', 'kerfuffle', 'higgledy-piggledy', 'flapdoodle', 'mumbo-jumbo', 'poppycock', 'dingleberry', 'hoot', 'lollygag', 'jiggly']
persons_name = ['James', 'Mary', 'John', 'Patricia', 'Robert', 'Jennifer', 'Michael', 'Linda', 'William', 'Elizabeth', 'David', 'Barbara', 'Richard', 'Susan', 'Joseph', 'Jessica', 'Charles', 'Sarah', 'Thomas', 'Karen', 'Daniel', 'Nancy', 'Matthew', 'Betty', 'Anthony', 'Helen', 'Mark', 'Sandra', 'Paul', 'Donna', 'Andrew', 'Carol', 'Joshua', 'Ruth', 'Kevin', 'Sharon', 'Brian', 'Michelle', 'George']
adjective_feeling = ['happy', 'sad', 'angry', 'excited', 'nervous', 'anxious', 'joyful', 'frustrated', 'content', 'disappointed', 'elated', 'scared', 'worried', 'bored', 'hopeful', 'confident', 'surprised', 'angry', 'guilty', 'relieved', 'ashamed', 'pleased', 'jealous', 'upset', 'grateful']
animal = ['cat', 'dog', 'bird', 'fish', 'horse', 'lion', 'tiger', 'bear', 'rabbit', 'deer', 'wolf', 'elephant', 'giraffe', 'zebra', 'kangaroo', 'panda', 'monkey', 'whale', 'dolphin', 'shark', 'snake', 'rat', 'mouse', 'frog', 'penguin', 'camel', 'cheetah', 'chipmunk', 'clownfish', 'coyote', 'crab', 'dingo', 'dolphin', 'eagle']
verb_ing = ['running', 'jumping', 'swimming', 'dancing', 'singing', 'writing', 'reading', 'eating', 'driving', 'cooking', 'playing', 'sleeping', 'talking', 'walking', 'painting', 'studying', 'laughing', 'working', 'shopping', 'traveling']
adverb_ly = ['happily', 'quickly', 'easily', 'slowly', 'loudly', 'gently', 'kindly', 'seriously', 'frequently', 'bravely', 'sadly', 'clearly', 'boldly', 'carefully', 'generously', 'quietly', 'honestly', 'smoothly', 'rarely', 'naturally']
place = ['house', 'city', 'town', 'country', 'school', 'office', 'library', 'park', 'hospital', 'restaurant', 'mall', 'museum', 'hotel', 'airport', 'market', 'garden', 'theater', 'building', 'room', 'café']
magical_creature = ['dragons', 'unicorns', 'phoenixes', 'griffins', 'goblins', 'elves', 'trolls', 'mermaids', 'centaurs', 'sphinxes', 'faeries', 'nymphs', 'ogres', 'chimeras', 'selkies', 'djinns', 'banshees', 'krakens', 'hydras', 'werewolves']
room_in_a_house = ['living room', 'kitchen', 'bedroom', 'bathroom', 'dining room', 'office', 'hallway', 'basement', 'attic', 'laundry room', 'garage', 'guest room', 'playroom', 'study room', 'pantry', 'mudroom', 'sunroom', 'media room', 'library']

if choice == '1':
    Number = get_input('Number: ', number)
    Measure_of_time = plural(get_input('Measure of time in singular form: ', measure_of_time), Number)
    Mode_of_transportation = preposition(get_input('Mode of transportation: ', mode_of_transportation))
    Adjective = preposition(get_input('Adjective: ', adjective))
    Adjective2 = get_input('Another adjective: ', adjective)
    Noun = get_input('Noun: ', noun) + 's'
    Color = get_input('Color: ', color)
    Part_of_the_body = get_input('Body part in a plural form: ', part_of_the_body)
    Verb = get_input('Verb: ', verb)
    Number2 = get_input('Another number: ', number)
    Noun2 = plural(get_input('Another noun in singular form: ', noun), Number2)
    Noun3 = preposition(get_input('Another noun: ', noun))
    Part_of_the_body2 = get_input('Another body part: ', part_of_the_body)
    Noun4 = get_input('Another noun: ', noun)
    Adjective3 = get_input('Another adjective: ', adjective)
    Silly_word = get_input('Silly word: ', silly_word)
        
    print(f'''
    Here is your story:
    It was about {Number} {Measure_of_time} ago when I arrived at the hospital in {Mode_of_transportation}. The hospital is
    {Adjective} place, there are a lot of {Adjective2} {Noun} here. There are nurses here who have {Color} {Part_of_the_body}.
    If someone wants to come into my room I told them that they have to {Verb} first. I’ve decorated my room with {Number2}
    {Noun2}. Today I talked to a doctor and they were wearing {Noun3} on their {Part_of_the_body2}. I heard that all doctors 
    {Verb} {Noun4} every day for breakfast. The most {Adjective3} thing about being in the hospital is the {Silly_word} {Noun}!
    ''')

elif choice == '2':
    Persons_name = get_input("Person's name: ", persons_name)
    Noun = get_input('Noun: ', noun)
    Adjective_feeling = get_input('Adjective that expresses a feeling: ', adjective_feeling)
    Verb = get_input('Verb: ', verb)
    Adjective_feeling2 = get_input('Another adjective that expresses a feeling: ', adjective_feeling)
    Animal = preposition(get_input('Animal: ', animal))
    Verb2 = get_input('Another verb: ', verb)
    Verb_ing = get_input('Verb ending with -ing: ', verb_ing)
    Adverb_ly = get_input('Adverb ending with -ly: ', adverb_ly)
    Number = get_input('Number: ', number)
    Measure_of_time = plural(get_input('Measure of time in singular form: ', measure_of_time), Number)
    Color = preposition(get_input('Color: ', color))
    Silly_word = plural(get_input('Silly word: ', silly_word), Number)
    Noun2 = get_input('Another noun in singular form: ', noun) + 's'

    print(f'''
    Here is your story:
    This weekend I am going camping with {Persons_name}. I packed my lantern, sleeping bag, and {Noun}. I am so {Adjective_feeling}
    to {Verb} in a tent. I am {Adjective_feeling2} we might see {Animal}, I hear they’re kind of dangerous. While we’re camping,
    we are going to hike, fish, and {Verb2 }. I have heard that the {Color} lake is great for {Verb_ing}. Then we will {Adverb_ly}
    hike through the forest for {Number} {Measure_of_time}. If I see {Color} {Animal} while hiking, I am going to bring it home
    as a pet! At night we will tell {Number} {Silly_word} stories and roast {Noun2} around the campfire!!
    ''')

else:
    Persons_name = get_input("Person's name: ", persons_name)
    Adjective = preposition(get_input('Adjective: ', adjective))
    Color = preposition(get_input('Color: ', color))
    Animal = get_input('Animal: ', animal)
    Place = preposition(get_input('Place: ', place))
    Adjective2 = get_input('Another adjective: ', adjective)
    Magical_creature = get_input('Magical creature in plural form: ', magical_creature)
    Adjective3 = get_input('Another adjective: ', adjective)
    Magical_creature2 = get_input('Another magical creature in plural form: ', magical_creature)
    Room_in_a_house = get_input('Room in a house: ', room_in_a_house)
    Noun = get_input('Noun in singular form: ', noun) + 's'
    Noun2 = preposition(get_input('Another noun in singular form: ', noun))
    Noun3 = get_input('Another noun in singular form: ', noun) + 's'
    Adjective4 = get_input('Another adjective: ', noun)
    Noun4 = get_input('Another noun in singular form: ', noun) + 's'
    Number = get_input('Number: ', number)
    Measure_of_time = plural(get_input('Measure of time in singular form: ', measure_of_time), Number)
    Verb_ing = get_input('Verb ending with -ing: ', verb_ing)
    Adjective5 = preposition(get_input('Another adjective: ', adjective))
    Noun5 = get_input('Another noun in singular form: ', noun)

    print(f'''
    Your story:
    Dear {Persons_name}, I am writing to you from {Adjective} castle in an enchanted forest. I found myself here one day after
    going for a ride on {Color} {Animal} in {Place}. There are {Adjective2} {Magical_creature} and {Adjective3} {Magical_creature2} here! In the
    {Room_in_a_house} there is a pool full of {Noun}. I fall asleep each night on {Noun2} of {Noun3} and dream of {Adjective4} {Noun4}.
    It feels as though I have lived here for {Number} {Measure_of_time}. I hope one day you can visit, although the only way to
    get here now is {Verb_ing} on {Adjective5} {Noun5}!!
    ''')
