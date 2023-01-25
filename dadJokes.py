import requests
import pyfiglet
import termcolor
from random import choice

# Get the user input
user_input = input("What would you like to search for? ")

# Get the jokes from the API
url = "https://icanhazdadjoke.com/search"
response = requests.get(
    url,
    headers={"Accept": "application/json"},
    params={"term": user_input}
)

# Get the data from the response
data = response.json()

# Get the number of jokes
num_jokes = data["total_jokes"]
results = data["results"]

# If there are no jokes, print a message
if num_jokes == 0:
    print(f"Sorry, I don't have any jokes about {user_input}! Please try again.")

# If there is only one joke, print it
elif num_jokes == 1:
    print(f"I've got one joke about {user_input}. Here it is:")
    print(results[0]["joke"])

# If there are multiple jokes, print a random one
else:
    print(f"I've got {num_jokes} jokes about {user_input}. Here's one:")
    print(choice(results)["joke"])

# Print the ASCII art
ascii_art = pyfiglet.figlet_format("Dad Joke 3000")
colored_ascii = termcolor.colored(ascii_art, color="magenta")
print(colored_ascii)