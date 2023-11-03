# number_of_seconds = int(input("Number of Seconds: "))
# message = ""

# if number_of_seconds < 0:
#     message = "Enter a number above 0.\nRerun program and try again."
# else:
#     if number_of_seconds >= 0 and number_of_seconds < 60:
#         seconds = format(number_of_seconds % 60)
#         message = "Seconds = " + seconds
        
#     elif number_of_seconds >= 60 and number_of_seconds <36000:
#         minutes = format(number_of_seconds // 60)
#         seconds = format(number_of_seconds % 60)
#         message = "Minutes = ", minutes, "Seconds= ", seconds
#     elif number_of_seconds >= 3600 and number_of_seconds < 86400:
#         hours = format(number_of_seconds // 3600)
#         minutes = format((number_of_seconds % 3600) // 60)
#         seconds = format((number_of_seconds % 3600) % 60)
#         message = f"{hours}: {minutes}: {seconds}"
#     elif number_of_seconds >=86400:
#         days = format(number_of_seconds // 86400)
#         hours = format((number_of_seconds % 86400) % 3600)
#         minutes = format((number_of_seconds % 86400) % 3600//60)
#         seconds = format((number_of_seconds%86400) // 3600%60)
#         message = f"{days}::{hours}:{minutes}:{seconds}"

# print(message)

import datetime

# Get the current time
# current_time = datetime.datetime.now()

# # Format and print the current time
# formatted_time = current_time.strftime("%H:%M:%S")
print(datetime.datetime.now().strftime("%H:%M:%S"))

