import random

friends = ["Alice", "Bob", "Charlie", "David", "Emanuel"]

random_friend = friends[random.randint(0, 4)]
print(random_friend)

random_chosen_friend = random.choice(friends)
print(random_chosen_friend)
