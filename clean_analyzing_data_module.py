import datetime as dt

def data_cleaning_analyzing(ask, show):
    total_ask_comments = 0
    total_show_comments = 0

    for post in ask:
        num_comments = int(post[4])
        total_ask_comments += num_comments

    avg_ask_comments = round(total_ask_comments / len(ask), 2)
    print('Average number of comments in ask posts is: ', avg_ask_comments)

    for post in show:
        num_comments = int(post[4])
        total_show_comments += num_comments

    avg_show_comments = round(total_show_comments / len(show), 2)
    print('Average number of comments in show posts is: ', avg_show_comments)
    print('\n')

    result_list         = []
    counts_by_hour      = {}
    comments_by_hour    = {}

    for row in ask:
        num_comments = int(row[4].strip())
        created_at   = row[6].strip()

        result_list.append([created_at, num_comments])

    avg_by_hour = []

    for value in result_list:
        date = value[0]
        comm = value[1]

        time_strping    = dt.datetime.strptime(date, '%m/%d/%Y %H:%M')
        hour            = time_strping.strftime('%H')

        if hour not in counts_by_hour:
            counts_by_hour[hour]    = 1
            comments_by_hour[hour]  = comm
        else:
            counts_by_hour[hour]    += 1
            comments_by_hour[hour]  += comm

    for hour1, count in counts_by_hour.items():
        for hour2, comment in comments_by_hour.items():
            if hour1 == hour2:
                avg_by_hour.append([round(comment/count,2), hour1])

    sorted_list = sorted(avg_by_hour, reverse=True)

    print("Top 5 Hours for 'Ask HN' Comments")
    for each_list in sorted_list[:5]:
        print(each_list[1], ":00:", each_list[0], "average comments per post")