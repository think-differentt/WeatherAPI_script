#Create a Python Application which asks the user for their zip code or city.
#Use the zip code or city name in order to obtain weather forecast data from: http://openweathermap.org/
#Display the weather forecast in a readable format to the user.
#Use comments within the application where appropriate in order to document what the program is doing.
#Use functions including a main function.
#Allow the user to run the program multiple times.
#Validate whether the user entered valid data. If valid data isn’t presented notify the user.
#Use the Requests library in order to request data from the webservice.
#Use Python 3.
#Use try blocks when establishing connections to the webservice. You must print a message to the user indicating whether or not the connection was successful.

#b15c469fd15ac99f42fd131c12433903 ---API KEY
# URL - api.openweathermap.org/data/2.5/weather?zip={zip_code},us &appid=b15c469fd15ac99f42fd131c12433903


print ("------------------Welcome to my weather application---------------------")

# PROMPT USER FOR ZIP CODE
zip_code = input("Please enter your ZIP code:")

# PROMPT USER AGAIN FOR ZIP CODE
print("Your reponse is invalid.")
#INSERT VALIDATION CRITERIA
# retry_question()

#requests.get('api.openweathermap.org/data/2.5/weather?zip={zip_code},us &appid=b15c469fd15ac99f42fd131c12433903')
#DISPLAY THE WEATHER FORECAST-
current_weather = 'Null'
print(current_weather)



# ANOTHER TRY
def retry_question():
 retry_answer = print("Would you have to try again?"+" [Y]yes [N]no")
 if retry_anser == 'Yes' or'Y':
    pass
 else:
    print("Have a great day. :)")

