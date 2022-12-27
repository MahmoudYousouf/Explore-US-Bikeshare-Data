
import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }
MONTHS = ['all', 'january', 'february', 'march', 'april', 'may', 'june']

DAYS = ['all', 'sunday', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday' ]              

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!\n')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    
    city = input("would you like to see data for Chicago, New York City or Washington?\n")

    while city.title() not in ['Chicago','New York City' ,'Washington'] :
        print ("Wrong Entry")
        city = input("would you like to see data for Chicago, New York City or Washington?\n")
        

    day = 'all'
    month = 'all'

    monthOrDay = input("would you like to filter the data by month, day or both.\n")
    while monthOrDay.title() not in ['Month', 'Day', 'Both'] :
        print ("Wrong Entry")
        monthOrDay = input("Choose between ( month, day or both ).\n")
    if  monthOrDay.title() in ['Both','Month'] :    
    
    # TO DO: get user input for month (all, january, february, ... , june)
        month = input("Which month ? January, February,  March,  April, May,  June or All\n")
        while month.lower()  not in MONTHS:
            print ("Wrong Entry")
            month = input("choose a month from( January, February,  March,  April, May,  June or All) \n")
    if  monthOrDay.title() in ['Both','Day'] : 
    
    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
        day = input("which day? please type your day as ('All', 'Saturday','Sunday','Monday','Tuesday','Wednesday','Thursday','Friday')\n")
        while day.lower() not in DAYS :
            print ("Wrong Entry")
            day = input("Select aday from ('All', 'Saturday','Sunday','Monday','Tuesday','Wednesday','Thursday','Friday')\n")
  
    print('-'*40)
    return city.lower(), month.lower(), day.lower()
#----------------------------------------------------------


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
    df = pd.read_csv(CITY_DATA[city])
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    
    df['month'] = df['Start Time'].dt.month
    df['day'] = df['Start Time'].dt.day_name()
    df['hour'] = df['Start Time'].dt.hour
    if month != 'all' :
        month = MONTHS.index(month)
        df = df[df['month'] == month]
    if day !='all' :
        df = df[df['day'] == day.title()]

    return df 

def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # display the most common month
    most_common_month = df['month'].mode()[0]
    print("The most common month is :", most_common_month)

    # display the most common day of week
    most_common_day_of_week = df['day'].mode()[0]
    print("The most common day of week is :", most_common_day_of_week)

    # display the most common start hour

    most_common_start_hour = df['hour'].mode()[0]
    print("The most common start hour is :", most_common_start_hour)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    most_common_start_station = df['Start Station'].mode()[0]
    print("The most commonly used start station :", most_common_start_station)

    # display most commonly used end station
    most_common_end_station = df['End Station'].mode()[0]
    print("The most commonly used end station :", most_common_end_station)

    # display most frequent combination of start station and end station trip
    most_common_start_end_station = df[['Start Station', 'End Station']].mode().loc[0]
    print("The most commonly used start station and end station : {}, {}"\
            .format(most_common_start_end_station[0], most_common_start_end_station[1]))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time
    total_travel = df['Trip Duration'].sum()
    print("Total travel time :", total_travel)

    # display mean travel time
    mean_travel = df['Trip Duration'].mean()
    print("Mean travel time :", mean_travel)

   
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def user_stats(df,city):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    print("Counts of user types:\n")
    print(df['User Type'].value_counts())

    # Display counts of gender
    if city != 'washington':
        print("\n\nCounts of gender:\n")
        print(df['Gender'].value_counts())

    # Display earliest, most recent, and most common year of birth  
        print("\n\nmost earliest year of birth: ")
        print(df['Birth Year'].min())
        print("most recent year of birth: ")
        print(df['Birth Year'].max())
        print("most common year of birth: " )
        print(df['Birth Year'].mode()[0])
    

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def viewing_data(df):
    view_data = input("Would you like to view 5 rows of individual trip data? Enter yes or no?\n").lower()
    start_loc = 0
    view_display ='no'

    while (view_data == 'yes' or view_display == 'yes' ):
        print(df.iloc[start_loc:start_loc+5].head())
        start_loc += 5
        view_data ='no'
        view_display = input("Do you wish to continue?: ").lower()
    else :
        print("Thanks for attempting")

        


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df,city)
        viewing_data(df)
        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()




