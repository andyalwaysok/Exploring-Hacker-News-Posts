def data_distribution(dataset):
    ask_posts   =   []
    show_posts  =   []
    other_posts =   []

    for row in dataset:
        title           =   row[1].strip()

        if title.lower() == 'title':
            continue

        if 'ask hn' in title.lower():
            ask_posts.append(row)
        elif 'show hn' in title.lower():
            show_posts.append(row)
        else:
            other_posts.append(row)

    print('The number of ask posts is: ', len(ask_posts))
    print('The number of show posts is: ', len(show_posts))
    print('The number of other posts is: ', len(other_posts))
    return ask_posts, show_posts, other_posts


def explore_data(dataset):
    length_row = len(dataset)
    length_col = len(dataset[0])

    print('The total number of rows for is: ', length_row)
    print('The total number of columns for is: ', length_col)
    print('The first three rows look like this: ')
    print('\n')
    for row in dataset[:3]:
        print(row)
        print('\n')

    ask, show, other = data_distribution(dataset)
    return ask, show, other