import time
import pandas as pd
import numpy as np

# use lower() method to return the name to lower case (Case Insensitive)
# Use strip() method to remove whitespace from the beginning and the end of city name

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
    # input message
    city_input_message  = "Kindly Choose a city only from \"Chicago, New York City, Washington\": "
    month_input_message = "Kindly Choose a month \"[\"All\", \"January\", \"February\", \"March\", \"April\", \"May\", \"June\"]\": "
    day_input_message   = "Kindly Choose a day \"[\"All\", \"Monday\", \"Tuesday\", \"Wednesday\", \"Thursday\", \"Friday\", \"Saturday\", \"Sunday\"]\": "

    # Add list of months from January to June and "all months"
    months = ["all", "january", "february", "march", "april", "may", "june"]
    # Add list of days from monday to sunday and "all days"
    days = ["all", "monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "sunday"]
    
    print('Hello! Let\'s explore some US bikeshare data!')

    ####################################################################################################################################
    # get user input for city (Chicago, New York City, Washington). HINT: Use a while loop to handle invalid inputs
    city = input(city_input_message).lower().strip()
    # Use While loop to ask the user about the city name until he enters a valid data
    while city not in CITY_DATA.keys():
        print("Your Choise is invalid or not from the city list available")
        city = input(city_input_message).lower().strip()
    #####################################################################################################################################
    
    # get user input for month (all, january, february, ... , june)
    # Ask the User to input month name
    month = input(month_input_message).lower().strip()
    # Use While loop to ask the user to input a valid month from the list
    while month not in months:
        print("Your Choise is invalid or not from the months list available")
        month = input(month_input_message).lower().strip()
    #####################################################################################################################################

    # get user input for day of week (all, monday, tuesday, ... sunday)
    day = input(day_input_message).lower().strip()
    while day not in days:
        print("Your Choise is invalid or not from the days list available")
        day = input(day_input_message).lower().strip()

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
    # read the input city data by user by Pandas library 
    df = pd.read_csv(CITY_DATA[city])
    # convert "Start Time" from str to datetime
    df["Start Time"] = pd.to_datetime(df["Start Time"])
    # get the month, day, and hour
    df["month"] = df["Start Time"].dt.month
    df["day"]   = df["Start Time"].dt.day_name()
    df["hour"]  = df["Start Time"].dt.hour
    
    # get the month number
    if month != "all":
        months =  ["january", "february", "march", "april", "may", "june"]
        month = months.index(month) + 1
        df = df[df["month"] == month]
    # get the day name
    if day != "all":
        df = df[df["day"] == day.title()]    

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    #use mode() method to get the most common happened
    # display the most common month
    print("The most common month : {}".format(df["month"].mode()[0]))
    # display the most common day of week
    print("The most common day of the week : {}".format(df["day"].mode()[0]))
    # display the most common start hour
    print("The most common start hour : {}".format(df["hour"].mode()[0]))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    print("The most commonly used start station is {} station.".format(df["Start Station"].mode()[0]))

    # display most commonly used end station
    print("The most commonly used end station is {} station.".format(df["End Station"].mode()[0]))

    # display most frequent combination of start station and end station trip
    print("The most commonly trip is from {}.".format((df["Start Station"]+" station to "+df["End Station"]+" station").mode()[0]))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time
    # convert float number to int due to use sum() and round() methods
    print("Total Travel Time is {} seconds.".format(int(df["Trip Duration"].sum().round())))

    # display mean travel time
    # convert float number to int due to use mean() and round() methods
    print("Average Travel Time is around {} seconds.".format(int(df["Trip Duration"].mean().round())))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df, city):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    print(df["User Type"].value_counts().to_frame())

    # Display counts of gender and Year of birth
    if city == "chicago" or city == "new york city":
        # Display Gender Type and its value
        print("\nDisplay Gender Analysis")
        print("-" * 24)
        print(df["Gender"].value_counts().to_frame())
        print("\nDisplay Year of Birth Analysis")
        print("-" * 31)
        # Display earliest, most recent, and most common year of birth
        print("The most recent year of birth : {}".format(int(df["Birth Year"].min())))
        print("The most earliest year of birth : {}".format(int(df["Birth Year"].max())))
        print("The most common year of birth : {}".format(int(df["Birth Year"].mode()[0])))
    else:
        print("No Gender Data or Year of Birth available for this City.")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def display_raw_data(df):
    row = 0
    display_raw_data_massage = "Would you like to display the raw data (5 lines each time) ? Yes / No: "
    end_message = "Thank You, Good Bye"

    # Validate Input function to insure that user input is Yes or No only
    def validate_user_input():
        user_input = input(display_raw_data_massage).lower().strip()
        while user_input != "yes" and user_input != "no":
            print("\nIt is an invalid choice")
            user_input = input(display_raw_data_massage).lower().strip()
        return user_input

    user_input = validate_user_input()
    if user_input == "yes":
        # This loop will continue until the end of Dataframe or the user input is "No"
        while df.shape[0] > row+5:
            # print 5 rows each time
            print(df.iloc[row:row+5])
            row +=5
            user_input = validate_user_input()
            if user_input == "no":
                print(end_message)
                break
    else:
        print(end_message)



def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)
        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df, city)
        display_raw_data(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
