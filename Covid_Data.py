# -- Processing and Visualisation of Covid 19 data from a CSV file.
# Barclay Cousin 12/01/22

# Here I am importing the required python modules. I am assigning nicknames so they can be easily called. 
import pandas as pd
import matplotlib.pyplot as plt


# Here I am defining a function for the processing of data


df = pd.read_csv("covid_19_data.csv")



def covid_19_data_visualisation():
    """
    This function gets data from a user of which is processed and can later be visualised using Matplotlib.
    It loads in a CSV file and returns values within that time frame and age range specified. 
    Any errors raised will be an incorrect age range or incorrect month range.
    Best practice would be to run these functions from the main menu.
    """


    df = pd.read_csv("covid_19_data.csv")

    
    # Here is a program which showcases the availible categories to chose from. 
    for col_name in df.columns:
        if "Age" in col_name:
            print("-" * 20)
            print(col_name)
    

    user_age_range = input("-------------------------\nHello! welcome to the covid 19 data visulisation program\nplease select an above age range you wish to collect data on. For example Age[15-19]")
                           
    new_user_age_range = user_age_range.strip()
    

    #example - "2020-12-01"
    start_date = input("Please select a date you wish to start from, without quotation marks in the following format - yyyy-mm-dd: ")
    print("-"*20)

    # example 2021-01-31
    end_date = input("Please select a date you wish to end at, without quotation marks in the following format - yyyy-mm-dd: ")


    
    
    # Creating the variable equal to the reference of date and a specified age group
    x = df[["date",new_user_age_range]]

    months = x[(x["date"] >= start_date) & (x["date"] <= end_date)]

    
    
    # Wrapping the statement in the while loop will allow me to catch any unwated inputs. 
    while True:
        try:
            # Collecting a user input to determine if they would like to view the data in a line chart or a bar chart.
            graph_type = input("\nPlease Enter 1 if you wish to view the data in a line chart and Enter 2 if you wish to view the data in a bar chart")
            if graph_type == "1":
                            
                plt.plot(months["date"], months[new_user_age_range])
                plt.title('Line Chart Visulasiation For Covid 19 Case Data: ')
                plt.xlabel("date")
                plt.ylabel(new_user_age_range)
                ax = plt.gca()
                plt.xticks(rotation=90)
                for label in ax.get_xaxis().get_ticklabels()[::2]:
                    label.set_visible(False)
                plt.show()
                break
        
            elif graph_type == "2":
                
                plt.bar(months["date"],months[new_user_age_range])
                plt.title('Bar Chart Visulasiation For Covid 19 Case Data:')
                plt.xlabel("date")
                plt.ylabel(new_user_age_range)
                ax = plt.gca()
                plt.xticks(rotation=90)
                for label in ax.get_xaxis().get_ticklabels()[::2]:
                    label.set_visible(False)
                plt.show()
                break
            else:
                print("I am afraid you have entered an invalid input. Please try again.")
                
        finally:
            print('-'*20)

    

    
# Calling the function
covid_19_data_visualisation()

