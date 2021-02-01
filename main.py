import requests

# Instructions:

# Send a ‘GET’ command to a webserver with a user-specified variable and display the result on screen.
# (eg. my_script index.html www.byu.edu)

print("Hello get request!")

website = input("Please enter website name: ")
response = requests.get("https://" + website)

print("Response: " + str(response))
