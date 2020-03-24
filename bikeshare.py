import time
import pandas as pd
import numpy as np

CITY_DATA = {'Chicago': 'chicago.csv',
             'New York City': 'new_york_city.csv',
             'Washington': 'washington.csv'}


def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.
    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """

    print('\nHello! Let\'s explore some US bikeshare data!')
    
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    while True:
      city = input('\nWould you like to see data from Chicago, New York City, or Washington?\n')
      if city not in ('New York City', 'Chicago', 'Washington'):
        print('Sorry, there is either a mispelling or you entered the wrong city. Try again, please.\n Choose either Chicago, New York City or Washington.')
        continue
      else:
        break

    # TO DO: get user input for month (all, january, february, ... , june)
    while True:
      month = input('\nFor which month? Type: January, February, March, April, May, June, or all\n')
      if month not in ('January', 'February', 'March', 'April', 'May', 'June', 'all'):
        print('Sorry, there is either a mispelling or you entered the wrong month. Try again, please.')
        continue
      else:
        break

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
      day = input('\nFor which day? Type: Sunday, Monday, Tuesday, Wednesday, Thursday, Friday, or all\n')
      if day not in ('Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'all'):
        print('Sorry, there is either a mispelling or you entered the wrong day. Try again, please.')
        continue
      else:
        break

    print('-'*40)
    return city, month, day


def load_data(city, month, day):

    """
    Loads data for the specified city and filters by month and day if applicable.
    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    # load data file into a dataframe
    df = pd.read_csv(CITY_DATA[city])

    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month and day of week from Start Time to create new columns

    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name

    # filter by month if applicable
    if month != 'all':
   	 	# use the index of the months list to get the corresponding int
        months = ['January', 'February', 'March', 'April', 'May', 'June']
        month = months.index(month) + 1

    	# filter by month to create the new dataframe
        df = df[df['month'] == month]

        # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day.title()]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nMost Frequent Times of Travel:\n')
    start_time = time.time()

    # TO DO: display the most common month
    popular_month = df['month'].mode()[0]
    if popular_month == 1:
        print('Most Common Month: January')
    elif popular_month == 2:
        print('Most Common Month: February')
    elif popular_month == 3:
        print('Most Common Month: March')
    elif popular_month == 4:
        print('Most Common Month: April')
    elif popular_month == 5:
        print('Most Common Month: May')
    elif popular_month == 6:
        print('Most Common Month: June')
    else:
	    print('Most Common Month:', popular_month)

    

    # TO DO: display the most common day of week
    popular_day = df['day_of_week'].mode()[0]
    print('Most Common day:', popular_day)

    # TO DO: display the most common start hour
    df['hour'] = df['Start Time'].dt.hour
    popular_hour = df['hour'].mode()[0]
    print('Most Common Hour:', popular_hour,':00')

    print('\nThis took %s seconds.' % (time.time() - start_time))
    print('-'*40)

    
def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nMost Popular Stations and Trip:\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    Start_Station = df['Start Station'].value_counts().idxmax()
    print('Most Commonly used start station:', Start_Station)

    # TO DO: display most commonly used end station
    End_Station = df['End Station'].value_counts().idxmax()
    print('\nMost Commonly used end station:', End_Station)

    # TO DO: display most frequent combination of start station and end station trip
    Combination_Station = df.groupby(['Start Station', 'End Station']).count()
    print('\nMost Commonly used combination of start station and end station trip:', Start_Station, ' and ', End_Station)

    print('\nThis took %s seconds.' % (time.time() - start_time))
    print('-'*40)

    
def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nTrip Duration:\n')
    start_time = time.time()

    # TO DO: display total travel time
    Total_Travel_Time = sum(df['Trip Duration'])
    print('Total travel time:', round(Total_Travel_Time/86400, 2), ' days.')

    # TO DO: display mean travel time
    Mean_Travel_Time = df['Trip Duration'].mean()
    print('Mean travel time:', round(Mean_Travel_Time/60, 2), ' minutes.')

    print('\nThis took %s seconds.' % (time.time() - start_time))
    print('-'*40)

    
def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nUser Stats:\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_types = df['User Type'].value_counts()
    #print(user_types)
    print('User Types:\n', user_types)

    # TO DO: Display counts of gender
    try:
      gender_types = df['Gender'].value_counts()
      print('\nGender Types:\n', gender_types)
    except KeyError:
      print('\nGender Types:\nNo data available.')

    # TO DO: Display earliest, most recent, and most common year of birth
    try:
      Earliest_Year = df['Birth Year'].min()
      print('\nEarliest Year of Birth:', int(Earliest_Year))
    except KeyError:
      print('\nEarliest Year of Birth:\nNo data available.')

    try:
      Most_Recent_Year = df['Birth Year'].max()
      print('\nMost Recent Year of Birth:', int(Most_Recent_Year))
    except KeyError:
      print('\nMost Recent Year of Birth:\nNo data available.')

    try:
      Most_Common_Year = df['Birth Year'].value_counts().idxmax()
      print('\nMost Common Year of Birth:', int(Most_Common_Year))
    except KeyError:
      print('\nMost Common Year of Birth:\nNo data available.')

    print('\nThis took %s seconds.' % (time.time() - start_time))
    print('-'*40)

    
def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

        start_again = input('\nDo you want to start over again? Type \'yes\' or \'no\'.\n')
        if start_again.lower() != 'yes':
            break

            
if __name__ == "__main__":
	main()