import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():

    print('Hello!! Let\'s explore some US bikeshare data!')

    cities = ['chicago','new york city','washington']
    city = input("What city are you interested in hearing about: ").lower()

    while city not in cities:
        print("Oops! Please enter either Chicago, New York City, or Washington!")
        city = input("What city are you interested in: ").lower()

    print("Nice! Let's explore {}.".format(city.title()))

    months = ['all','january','february','march','april','may','june']
    month = input("What month are you interested in: ").lower()

    while month not in months:
        print("Oops! Please enter either January, February, March, April, May, June, or All")
        month = input("What month are you interested in: ").lower()

    print("Awesome! Let's explore {} in {}!".format(city.title(),month.title()))

    days = ['all','monday','tuesday','wednesday','thursday','friday','saturday','sunday']
    day = input("Finally, what day are you interested in: ").lower()

    while day not in days:
        print('Oops! Please enter Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, Sunday, or All.')
        day = input("Finally, what day are you interested in: ").lower()

    print("Great! We are going to explore {} in {} on {}. Let's get started!".format(city.title(),month.title(),day.title()))

    print('-'*40)
    return city, month, day

def load_data(city, month, day):
    df = pd.read_csv(CITY_DATA[city])
    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name
    # filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
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

    print('\nCalculating The Most Frequent Time of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common start hour
    df['hour'] = df['Start Time'].dt.hour
    popular_hour = df['hour'].mode()[0]
    print('Most Popular Start Hour:', popular_hour)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    popular_st_station = df['Start Station'].mode()[0]
    print('Most Popular Start Station:', popular_st_station)

    # TO DO: display most commonly used end station
    popular_end_station = df['End Station'].mode()[0]
    print('Most Popular End Station:', popular_end_station)

    # TO DO: display most frequent combination of start station and end station trip
    df['Trip'] = ('Start Station: ' + df['Start Station'] + ' End Station: ' + df['End Station'])
    popular_trip = df['Trip'].mode()[0]
    print('Most Popular Trip:', popular_trip)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_time = df['Trip Duration'].sum()
    print("The total trip duration is:", total_time)

    # TO DO: display mean travel time
    average_time = df['Trip Duration'].mean()
    print("The average trip duration is:", average_time)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_types = df['User Type'].value_counts()
    print(user_types)
    try:
        # TO DO: Display counts of gender
        genders = df['Gender'].value_counts()
        print(genders)
        # TO DO: Display earliest, most recent, and most common year of birth
        earliest_yr = int(df['Birth Year'].min())
        print("The earliest year of birth is:", earliest_yr)

        recent_yr = int(df['Birth Year'].max())
        print("The most recent year of birth is:", recent_yr)

        common_yr = int(df['Birth Year'].mode()[0])
        print("The most common year of birth is:", common_yr)
    except:
        print("Unfortunately, no gender or birth year available for Washington.")
    finally:
        print("\nThis took %s seconds." % (time.time() - start_time))
        print('-'*40)

def display_raw(df):
    response = input('Would you like to see more data? Please answer yes or no: ').lower()
    if response == 'yes':
        i = 0
        while True:
            print(df.iloc[i:i+5])
            i += 5
            more = input('Would you like to see more data? Please enter yes or no: ').lower()
            if more != 'yes':
                break

def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        display_raw(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break

if __name__ == "__main__":
	main()
