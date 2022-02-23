# Retreive UK arrest data and visualise
# Barclay Cousin # 12/01/22

# Importing the specific libraries
import requests
import matplotlib.pyplot as plt
from datetime import *


def stop_and_search_data():

    '''
    This function processes the forces in the country and them does a web request
    to access stop data for a specified area.
    The errors raised at current time which are not patched is the exception when
    you enter an incorrect police force. I was not able to address this due to time
    constraints.
    '''
    # Creating the data required
    POLICE_FORCE_URL = "https://data.police.uk/api/forces"
    FORCE_LOCATIONS = []

    # Requesting the website
    web_handler =requests.get(POLICE_FORCE_URL)
    if web_handler.status_code == requests.codes.ok: 
        locations = web_handler.json()
        for v in locations:
            FORCE_LOCATIONS.append(v['id'])
        print(FORCE_LOCATIONS[:])

        
    print("-"*20)

    # Chose a location to retrieve data from using the API - eg avon-and-somerset
    location = input("Please chose an above location to request stop data on: ")


    # Optional. (YYYY-MM) Limit results to a specific month. eg 2021/09
    date_from = input("Please chose a date you wish to retrieve data starting from: ")

    ###date_to NO IDEA
    while True:
        try:
            
            URL = 'https://data.police.uk/api/stops-force?force='+location+'&'+date_from
            print(URL)
            
            power_request = requests.get(URL)

            print("Status code", power_request.status_code)
            break
        except ValueError as ve:
            print("You entered incorrect details, please try again", ve)
            break
        
        finally:
            break

    # Creating some values to be used later
    counter_one = 0
    counter_two = 0
    counter_three = 0
    master_list = []
    male = 0
    female = 0
    gender = []

    if power_request.status_code == requests.codes.ok:
        power = power_request.json()
        for x in power:
            age_range = x.get('age_range')
            if age_range == "10-17":
                counter_one +=1  # Appending one to the counter which is later used to plot data
            elif age_range == "18-24":
                counter_two +=1

            elif age_range == "25-34":
                counter_three +=1

            
            # This data is attainable but was not used within the process 
            date_time = x.get('datetime')
            date_time = datetime.fromisoformat(date_time)
            date_time = str(date_time.date())
            
            sex = x['gender']
            if sex == "Male":
                male +=1
            elif sex == "Female":
                female += 1
            
            #print(age_range)

        #Appending the age data to a list
        master_list.append(counter_one)
        master_list.append(counter_two)
        master_list.append(counter_three)

        gender.append(male)
        gender.append(female)

    # Here I am setting up everything required to display a bar chart
    while True:
            try:
                graph_type = input("\nPlease Enter 1 if you wish to view the data in a bar chart and Enter 2 if you wish to view the data in a pie chart")
                if graph_type == "1":
                    
                    no = ["10-17", "18-24", "25-34"]
                    plt.bar(no,master_list)
                    plt.title('Bar Chart Visulasiation For Stop & Search By Age Data:')
                    plt.xlabel("Age Ranges")
                    plt.ylabel("Total Police Stops")
                    plt.show()
                    break
                # Here I am setting up the required features to create a pie chart
                elif graph_type == "2":
                    labels = "male", "female"
                    explode = (0, 0.1) # only "explode" the 2nd slice (i.e. 'Hogs')
                    fig1, ax1 = plt.subplots()
                    ax1.pie(gender, explode=explode, labels=labels, autopct='%1.1f%%',
                            shadow=True, startangle=90)
                    ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
                    plt.title("Pie Chart Showing Stops Based Off Gender")
                    plt.show()
                else:
                    print("I am afraid you have entered an invalid input. Please try again.")
                break
            except Exception as ve:
                print("You entered incorrect details, please try again - Error Type", ve)
                break
            else:
                print('Try again, you entered a wrong number')
            finally:
                break
              
            

# Calling the function 
stop_and_search_data()
