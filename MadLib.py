name = input("Enter a name: ")
noun = input("Enter a noun: ")
adjective1 = input("Enter an adjective: ")
adjective2 = input("Enter another adjective: ")
adjective3 = input("Enter another adjective: ")
adjective4 = input("Enter another adjective: ")
place = input("Enter a place: ")
any_object = input("Enter an object: ")
animal = input("Enter an animal: ")
clothing_item = input("Enter a clothing item: ")
silly_word = input("Enter a silly word: ")
number = input("Enter a number: ")
type_of_music = input("Enter a type_of_music: ")
verb_ending_in_ing = input("Enter a verb_ending_in_ing: ")
creature = input("Enter a creature: ")
plural_noun = input("Enter a plural noun: ")
preference = input("Choose between 1 and 2: ")


story1 = f"""One day, a {adjective1} boy named {name} decided to go to the {place}. He was carrying a {adjective2} {noun} in his backpack.

Suddenly, he heard a {adjective3} noise coming from behind a {any_object}. Out jumped a {adjective4} {animal} wearing a {clothing_item}!

'Hello!' said the animal. 'I need your help to find my {noun}.'

Without thinking, {name} shouted a {silly_word} and followed the animal into a {adjective1} cave.

Inside the cave, they saw {number} glowing {plural_noun} and a {adjective2} {creature} dancing to {type_of_music}.

'This is so {adjective3}!' said {name}.

In the end, they found the missing {noun} and celebrated by {verb_ending_in_ing} together.

It was the most {adjective4} day in the life of {name}.
"""
story2 = f"""
One evening, a {adjective1} girl named {name} was sent to the {place} on a secret mission. In her bag, she carried a {adjective2} {noun} for protection.

As she walked, a {adjective3} sound echoed from behind a {any_object}. Suddenly, a {adjective4} {animal} appeared, dressed in a {clothing_item}!

“I’ve been waiting for you,” said the {animal}. “You must help me recover my lost {noun}.”

Without hesitation, {name} yelled {silly_word} and followed the {animal} into a {adjective4} tunnel.

Deep inside, they discovered {number} glowing {plural_noun} and a {adjective3} {creature} moving to the rhythm of {type_of_music}.

“I can’t believe this is so {adjective1}!” said {name}.

At last, they retrieved the missing {noun} and celebrated by {verb_ending_in_ing} side by side.

It turned out to be the most {adjective2} adventure of {name}’s life.
"""
if preference == '1':
    print("Here is your story: ")
    print(story1)
elif preference == '2':
    print("Here is your story: ")
    print(story2)


