import requests
import pyfiglet
import termcolor
from random import choice

# Print the ASCII art
def displayAscii(input="BA DUM TSS"):
    ascii_art = pyfiglet.figlet_format(input)
    colored_ascii = termcolor.colored(ascii_art, color="magenta")
    return colored_ascii

# Get the jokes from the API
def getDadJoke(input=None):
    url = "https://icanhazdadjoke.com/search"
    response = requests.get(
        url,
        headers={"Accept": "application/json"},
        params={"term": input}
    )
    data = response.json()
    num_jokes = data["total_jokes"]
    results = data["results"]
    if num_jokes == 0:
        return (f"Sorry, I don't have any jokes about {input}! Please try again.")
    elif num_jokes == 1:
        print(f"I've got one joke about {input}. Here it is:")
        return results[0]["joke"]
    # If there are multiple jokes, print a random one
    else:
        print(f"I've got {num_jokes} jokes about {input}. Here's one:")
        return choice(results)["joke"]
