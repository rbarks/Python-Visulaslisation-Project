# This is the user interface for selecting the processing and visulisation of Covid 19 data and police stop and search data.
# Barclay Cousin 12/01/22

print("**************")
request = input("Hello and welcome to the dashboard. If you wish to load covid data please enter 1 and if you wish to load Stop and search data please enter 2: ")
new_request = request.strip()

while True:
    try:
        if new_request == "1":
            from Covid_Data.py import covid_19_data_visualisation
            covid_19_data_visualisation()
            break
        elif new_request == '2':
            from Stop_And_Search import stop_and_search_data
            stop_and_search_data()
            break
        else:
            print("Incorrect entry, please make sure you entered the correct number and try again")
    finally:
        print('-'*20)
        break
        

# Additional Notes

# I am aware of the dangling while loop causing my program to be an infinite
# loop when I enter 2. Due to time constraints I was not able to address this.
