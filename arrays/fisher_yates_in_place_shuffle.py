import random


def get_random(floor, ceiling):
    return random.randrange(floor, ceiling + 1)

# Shuffle the input in place
def shuffle(the_list):
    n = len(the_list)
    
    if n <= 1:
        return the_list

    index = 0
    for index in range(0, n):
        random_index = get_random(index, n-1)
        if index != random_index:
            the_list[index], the_list[random_index] = the_list[random_index], the_list[index]


sample_list = [1, 2, 3, 4, 5, 8, 15, 45, 84]
print('Sample list:', sample_list)

print('Shuffling sample list...')
shuffle(sample_list)
print(sample_list)
