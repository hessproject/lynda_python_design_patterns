def count_to(count):

    numbers_in_german = ['eins', 'zwei', 'drei', 'vier', 'funf']

    #built in iterator, creates tuple like (1, 'eins')
    iterator = zip(range(count), numbers_in_german)

    #Iterate through list, extract numbers and put them in generator
    for position, number in iterator:
        yield number

for num in count_to(6):
    print('{}'.format(num))