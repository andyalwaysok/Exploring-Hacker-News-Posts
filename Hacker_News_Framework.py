from csv import reader
import explore_data_module as edm
import clean_analyzing_data_module as cdm

directory   = 'C:\\Personal Projects\\Dataquest\\Python Project\\Hackers News\\'

hn  = list(reader(open(directory + 'HN_posts_year_to_Sep_26_2016.csv')))

print('Data Exploration Process')
ask, show, other = edm.explore_data(hn)
print('\n')

print('Data Cleaning and Analyzing Process')
cdm.data_cleaning_analyzing(ask, show)
