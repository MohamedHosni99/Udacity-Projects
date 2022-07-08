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
    while True:
        city = input("Please choose a city from (chicago,new york city,washignton):").lower()
        if city not in CITY_DATA:
            print("invalid city name")
            print("Please choose a city from (chicago,new york city,washignton)")
        else:
            break    

    # TO DO: get user input for month (all, january, february, ... , june)
    while True:
        month= input("please choose a month from (janruary,february,march,april,may,june) or type'all' to display all months :").lower()
        months=['janruary','february','march','april','may','june','all']
        if month not in months:
            print("invalid month name")
        else:
            break    



    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
       day=input("please enter a day of the week or type 'all' to display all days :").lower()
       days= ['saturday','sunday','monday','tuesday','wednesday','thursday','friday','all']
       if day not in days:
           print("please enter a valid day name")
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
    # to load data file into a data frame 
    df=pd.read_csv(CITY_DATA[city]) 
    
   # convert the Start Time column to datetime   
    df['Start Time']=pd.to_datetime(df['Start Time']) 
   
    # extract month from Start Time to create a new column
   
    df['month']=df['Start Time'].dt.month 
   
   #extract day of week from Start Time  to creat a new column

    df['day_of_week']=df['Start Time'].dt.day_name()
     
    
    #filter by month if applicable
    if month !='all':
       
        # use the index of months list to corresponding int
        months=['janruary','february','march','april','may','june']
        month=months.index(month)+1  
       
       #filter by month to create the new data frame
        df =df[df['month'] == month] 

    #filter by the day of the week if applicable
    if day != 'all':
     # filter by day of week to create the new dataframe     
     df=df[df['day_of_week']== day.title()]    
          

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    print("the most common month is:{}".format(df['month'].mode()[0]))

    # TO DO: display the most common day of week
    print("the most common day is:{}".format(df['day_of_week'].mode()[0]))

    # TO DO: display the most common start hour
    df['hour']=df['Start Time'].dt.hour # extract hour from Start Time column to create an hour column
    print("the most common hour is: {}".format(df['hour'].mode()[0]))    

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    print("the most commonly used Start Station is:{} ".format(df['Start Station'].mode()[0]))


    # TO DO: display most commonly used end station
    print("the most commonly used End Station is:{} ".format(df['End Station'].mode()[0]))     

    # TO DO: display most frequent combination of start station and end station trip
    df['combination_start_end']= df['Start Station']+','+df['End Station']  #  a new data frame to concatenate between start station and end station
    print("the most frequent combination of start station and end staion is:{} ".format(df['combination_start_end'].mode()[0]))



    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    print("Total Travel Time = {}".format(df['Trip Duration'].sum().round()))  # approximation to nearset integer using round() 

    # TO DO: display mean travel time
    print("Average Travel Time = {}".format(int(df['Trip Duration'].mean())))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df,city):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    print("\nCounts of User Type\n",df['User Type'].value_counts())

    # TO DO: Display counts of gender
    if city !='washington':
        print("\nCounts of Gender\n",df['Gender'].value_counts())


    # TO DO: Display earliest, most recent, and most common year of birth
        print("The Earliest Year of Birth is :",int(df['Birth Year'].min()))
        print("The Most Recent Year of Birth is:",int(df['Birth Year'].max()))
        print("The Most Common Year of Birth is:",int(df['Birth Year'].mode()[0]))
    else:
        print("invalid Data for This City")    

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def display_data(df): 
    # display subsequent rows of data according to user answer 
    
    i=0
    user_input= input("would you like to display the first five rows of data? please Enter yes or no ").lower() #convert the user input to lower case using lower() function 
  


    if user_input == 'no':
        print("Thank You")
         
    else:
          while i+5 < df.shape[0]:
              
              print(df.iloc[i:i+5])
              i+=5 
              user_input= input("would you like to display the next five rows of data? please Enter yes or no ").lower() 
              if user_input == 'no':
               break  
     
def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

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
