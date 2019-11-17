import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    print("Which city you want to see data for Chicago, Washington or New York ?")

    city = input()
    entered_city = city.lower()
    while entered_city not in {"chicago", "new york", "washington"}:
        print("Your entered city %s is not available " % (entered_city))
        entered_city = input("\n You have entered wrong city! Enter correct city:   ").lower()
        continue

    # TO DO: get user input for month (all, january, february, ... , june)
    print("Would you like to filter data by month, day, both, or not at all? Type 'none' for no")

    month = input()
    entered_month = month.lower()
    while entered_month not in {"January", "February", "March", "April", "May", "June"}:
        print("Your entered month %s is not available " % (entered_month))
        entered_month = input("\n You have entered wrong month! Enter correct month:   ").lower()
        continue

    print("Selected month is %s " % (entered_month))

    if entered_month == 'month':
        print("Which month would you like to filter by? January, February, March, April, May, June")
        month = input()
        entered_month = month.lower()
        entered_day = 'all'

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    day = input()
    entered_day = day.lower()
    while entered_day not in {"Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"}:
        print("Your entered day %s is not available " % (entered_day))
        entered_day = input("\n You have entered wrong day! Enter correct day:   ").lower()
        continue

    print("Selected day is %s " % (entered_day))

    print('-'*40)
    return entered_city,entered_month,entered_day

def load_data(city,month,day):
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
    df['entered_day'] = df['Start Time'].dt.weekday_name

    if month != 'all':
        entered_month = ["January", "February", "March", "April", "May", "June"]
        month = entered_month.index(month)+1
        df = df[df['month'] == month]

    if day != 'all':
        df = df[df['entered_day'] == day.title()]

    print('-'*40)
    return df

def time_stats(df):

    """Displays statistics on the most frequent times of travel."""
    print("Calculating the Most Frequent Time's of travel")
    start_time = time.time()
     # TO DO: display the most common month
    common_month = df['Start Time'].dt.month.mode()[0]
    print("The Most common Month is %s " % (common_month))
    # TO DO: display the most common day of week
    common_day = df['Start Time'].dt.weekday_name.mode()[0]
    print("The Most common Day is %s " % (common_day))
    # TO DO: display the most common start hour
    common_hour = df['Start Time'].dt.hour.mode()[0]
    print("Most common Hour is %s " % (common_hour))

    print("This took %s seconds" % (time.time() - start_time))
    """ To calculate the total time took for processing above results """
    print('-'*40)

def station_stats(df):

    """Displays statistics on the most popular stations and trip."""
    print("Calculating the Most Frequent Station's of travel")
    start_time = time.time()

    # TO DO: display most commonly used start station

    start_station = df['Start Station'].mode()[0]
    print("The Most commonly Start Station is %s " % (start_station))

    # TO DO: display most commonly used end station

    end_station = df['End Station'].mode()[0]
    print("The Most commonly End Station is %s " % (end_station))

    # TO DO: display most frequent combination of start station and end station trip

    Comb_Station = df.groupby(['Start Station', 'End Station']).count()
    print('\nThe Most Commonly used combination of start and end stations:', start_station, " & ", end_station)

    print("This took %s seconds" % (time.time() - start_time))
    print('-'*40)

def trip_duration_stats(df):

    """Displays statistics on the total and average trip duration."""
    print("Calculating Trip Duration...!")
    start_time = time.time()

 # TO DO: display total travel time

    total_time = df['Trip Duration'].sum()
    print("The Total Travel Time is %s " % (total_time))

    # TO DO: display mean travel time

    mean_time = df['Trip Duration'].mean()
    print("Mean Travel Time is %s " % (mean_time))

    print("This took %s seconds" % (time.time() - start_time))
    print('-'*40)

def user_stats(df,city):

    """Displays statistics on bikeshare users."""
    print("Calculating User stats..!")
    start_time = time.time()
   # TO DO: Display counts of user types

    if 'User Type' in df.columns:
        print(df['User Type'].value_counts())
    else:
        print("Sorry..! for %s User Type data is not available " % (city))

    # TO DO: Display counts of gender

    if 'Gender' in df.columns:
        print(df['Gender'].value_counts())
    else:
        print("Sorry..! for %s Gender data is not available " % (city))

    # TO DO: Display earliest, most recent, and most common year of birth

    if 'Birth Year' in df.columns:
        min_year = df['Birth Year'].min()
        print("The Most Earliest Birth Year is %s " % (min_year))

        max_year = df['Birth Year'].max()
        print("The Most Recent Birth Year is %s " % (max_year))

        common_year = df['Birth Year'].mode()[0]
        print("The Most common Birth Year is %s " % (common_year))
    else:
        print("Sorry..! for %s Birth Year data is not available " % (city))
    print('-'*40)

def display_data(df):
        print("Would you like see five rows of data ?? Enter yes or no ")
        set_data = input()
        set_data = set_data.lower()

        i = 0
        while set_data == 'yes':
            print(df[:i])
            print("Would you like to see five more rows of data ?? Enter yes or no ")
            i += 5
            set_data = input()
            set_data = set_data.lower()

def main():
    while True:
        city,month,day = get_filters()
        df = load_data(city,month,day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df,city)
        display_data(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break

if __name__ == "__main__":
	main()
