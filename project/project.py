import random
import requests

API_KEY = "66c75cfb0e7d4d1dbf248ed5af00f2ed"
BASE_URL = "https://api.spoonacular.com/recipes/complexSearch"
RECIPE_URL = "https://api.spoonacular.com/recipes/{id}/information"

def get_cuisine_for_country(country):
    cuisine_map = {
        "Afghanistan": "Middle Eastern", "Albania": "Eastern European", "Algeria": "African",
        "Andorra": "European", "Angola": "African", "Antigua and Barbuda": "Caribbean",
        "Argentina": "Latin American", "Armenia": "Middle Eastern", "Australia": "Australian",
        "Austria": "European", "Azerbaijan": "Middle Eastern", "Bahamas": "Caribbean",
        "Bahrain": "Middle Eastern", "Bangladesh": "Indian", "Barbados": "Caribbean",
        "Belarus": "Eastern European", "Belgium": "European", "Belize": "Latin American",
        "Benin": "African", "Bhutan": "Asian", "Bolivia": "Latin American",
        "Bosnia and Herzegovina": "Eastern European", "Botswana": "African", "Brazil": "Latin American",
        "Brunei": "Asian", "Bulgaria": "Eastern European", "Burkina Faso": "African",
        "Burundi": "African", "Cabo Verde": "African", "Cambodia": "Asian",
        "Cameroon": "African", "Canada": "American", "Central African Republic": "African",
        "Chad": "African", "Chile": "Latin American", "China": "Chinese",
        "Colombia": "Latin American", "Comoros": "African", "Congo, Democratic Republic of the": "African",
        "Congo, Republic of the": "African", "Costa Rica": "Latin American", "Croatia": "Eastern European",
        "Cuba": "Caribbean", "Cyprus": "Mediterranean", "Czech Republic": "Eastern European",
        "Denmark": "Nordic", "Djibouti": "African", "Dominica": "Caribbean",
        "Dominican Republic": "Caribbean", "Ecuador": "Latin American", "Egypt": "Middle Eastern",
        "El Salvador": "Latin American", "Equatorial Guinea": "African", "Eritrea": "African",
        "Estonia": "Nordic", "Eswatini": "African", "Ethiopia": "African",
        "Fiji": "Asian", "Finland": "Nordic", "France": "French",
        "Gabon": "African", "Gambia": "African", "Georgia": "Middle Eastern",
        "Germany": "German", "Ghana": "African", "Greece": "Greek",
        "Grenada": "Caribbean", "Guatemala": "Latin American", "Guinea": "African",
        "Guinea-Bissau": "African", "Guyana": "Caribbean", "Haiti": "Caribbean",
        "Honduras": "Latin American", "Hungary": "Eastern European", "Iceland": "Nordic",
        "India": "Indian", "Indonesia": "Asian", "Iran": "Middle Eastern",
        "Iraq": "Middle Eastern", "Ireland": "British", "Israel": "Middle Eastern",
        "Italy": "Italian", "Jamaica": "Caribbean", "Japan": "Japanese",
        "Jordan": "Middle Eastern", "Kazakhstan": "Asian", "Kenya": "African",
        "Kiribati": "Asian", "Korea, North": "Korean", "Korea, South": "Korean",
        "Kuwait": "Middle Eastern", "Kyrgyzstan": "Asian", "Laos": "Asian",
        "Latvia": "Nordic", "Lebanon": "Middle Eastern", "Lesotho": "African",
        "Liberia": "African", "Libya": "African", "Liechtenstein": "European",
        "Lithuania": "Nordic", "Luxembourg": "European", "Madagascar": "African",
        "Malawi": "African", "Malaysia": "Asian", "Maldives": "Asian",
        "Mali": "African", "Malta": "Mediterranean", "Marshall Islands": "Asian",
        "Mauritania": "African", "Mauritius": "African", "Mexico": "Mexican",
        "Micronesia": "Asian", "Moldova": "Eastern European", "Monaco": "European",
        "Mongolia": "Asian", "Montenegro": "Eastern European", "Morocco": "African",
        "Mozambique": "African", "Myanmar": "Asian", "Namibia": "African",
        "Nauru": "Asian", "Nepal": "Indian", "Netherlands": "European",
        "New Zealand": "Australian", "Nicaragua": "Latin American", "Niger": "African",
        "Nigeria": "African", "North Macedonia": "Eastern European", "Norway": "Nordic",
        "Oman": "Middle Eastern", "Pakistan": "Indian", "Palau": "Asian",
        "Panama": "Latin American", "Papua New Guinea": "Asian", "Paraguay": "Latin American",
        "Peru": "Latin American", "Philippines": "Asian", "Poland": "Eastern European",
        "Portugal": "Mediterranean", "Qatar": "Middle Eastern", "Romania": "Eastern European",
        "Russia": "Eastern European", "Rwanda": "African", "Saint Kitts and Nevis": "Caribbean",
        "Saint Lucia": "Caribbean", "Saint Vincent and the Grenadines": "Caribbean",
        "Samoa": "Asian", "San Marino": "Italian", "Sao Tome and Principe": "African",
        "Saudi Arabia": "Middle Eastern", "Senegal": "African", "Serbia": "Eastern European",
        "Seychelles": "African", "Sierra Leone": "African", "Singapore": "Asian",
        "Slovakia": "Eastern European", "Slovenia": "Eastern European", "Solomon Islands": "Asian",
        "Somalia": "African", "South Africa": "African", "South Sudan": "African",
        "Spain": "Spanish", "Sri Lanka": "Indian", "Sudan": "African",
        "Suriname": "Caribbean", "Sweden": "Nordic", "Switzerland": "European",
        "Syria": "Middle Eastern", "Taiwan": "Chinese", "Tajikistan": "Asian",
        "Tanzania": "African", "Thailand": "Thai", "Timor-Leste": "Asian",
        "Togo": "African", "Tonga": "Asian", "Trinidad and Tobago": "Caribbean",
        "Tunisia": "African", "Turkey": "Middle Eastern", "Turkmenistan": "Asian",
        "Tuvalu": "Asian", "Uganda": "African", "Ukraine": "Eastern European",
        "United Arab Emirates": "Middle Eastern", "United Kingdom": "British",
        "United States": "American", "Uruguay": "Latin American", "Uzbekistan": "Asian",
        "Vanuatu": "Asian", "Vatican City": "Italian", "Venezuela": "Latin American",
        "Vietnam": "Vietnamese", "Yemen": "Middle Eastern", "Zambia": "African",
        "Zimbabwe": "African"
    }
    return cuisine_map.get(country, country)

def get_recipes_by_country(country):
    cuisine = get_cuisine_for_country(country)
    params = {
        "apiKey": API_KEY,
        "cuisine": cuisine,
        "number": 2  
    }
    response = requests.get(BASE_URL, params=params)
    if response.status_code == 200:
        data = response.json()
        return data["results"] if data["results"] else None
    return None

def display_recipe(recipe_id):
    url = RECIPE_URL.format(id=recipe_id)
    params = {"apiKey": API_KEY}
    response = requests.get(url, params=params)
    if response.status_code == 200:
        recipe = response.json()
        print(f"\nRecipe: {recipe['title']}")
        print("Ingredients:")
        for ingredient in recipe["extendedIngredients"]:
            print(f"- {ingredient['original']}")
        print("Instructions:")
        instructions = recipe["instructions"] or "No instructions provided."
        instructions = instructions.replace("<ol>", "").replace("</ol>", "")  
        instructions = instructions.replace("<li>", "").replace("</li>", "\n")  
        instructions = instructions.replace("<p>", "").replace("</p>", "")  
        instructions = "\n".join(line.strip() for line in instructions.splitlines() if line.strip()) 
        print(instructions)
        
    else:
        print("Sorry, no recipe found!")

def search_recipes(search_term):
    params = {
        "apiKey": API_KEY,
        "query": search_term,
        "number": 5  
    }
    response = requests.get(BASE_URL, params=params)
    if response.status_code == 200:
        data = response.json()
        return data["results"] if data["results"] else None
    return None

def main():
    print("Welcome to Global Recipe Explorer!")
    print("Explore recipes from all 195 countries in the world!")
    
    while True:
        print("\nWhat would you like to do?")
        print("1. Pick a country")
        print("2. Search for a recipe")
        print("3. Get a random recipe")
        print("4. Exit")
        
        choice = input("Enter your choice (1-4): ")
        
        if choice == "1":
            country = input("Enter any country (e.g., Italy, Gambia, Brazil): ")
            country_recipes = get_recipes_by_country(country)
            if country_recipes:
                print(f"\nPopular dishes for {country}:")
                for i, recipe in enumerate(country_recipes, 1):
                    print(f"{i}. {recipe['title']}")
                try:
                    recipe_num = int(input("Pick a recipe number: "))
                    if 1 <= recipe_num <= len(country_recipes):
                        display_recipe(country_recipes[recipe_num - 1]["id"])
                    else:
                        print("Invalid number!")
                except ValueError:
                    print("Please enter a number!")
            else:
                print(f"No recipes found for {country} - try another country!")
        
        elif choice == "2":
            search_term = input("Enter a country or ingredient to search: ")
            results = search_recipes(search_term)
            if results:
                print("\nFound these recipes:")
                for recipe in results:
                    print(f"- {recipe['title']}")
                pick = input("Type a recipe title to see details: ")
                for recipe in results:
                    if recipe["title"].lower() == pick.lower():
                        display_recipe(recipe["id"])
                        break
                else:
                    print("Recipe not found in results!")
            else:
                print("No matches found!")
        
        elif choice == "3":
            params = {"apiKey": API_KEY, "number": 1, "random": True}
            response = requests.get(BASE_URL, params=params)
            if response.status_code == 200 and response.json()["results"]:
                random_recipe = response.json()["results"][0]
                print("\nHere’s your random recipe:")
                display_recipe(random_recipe["id"])
            else:
                print("Couldn’t fetch a random recipe!")
        
        elif choice == "4":
            print("Goodbye!")
            break
        
        else:
            print("Please pick a valid option!")

if __name__ == "__main__":
    main()