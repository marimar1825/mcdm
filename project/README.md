# Global Recipe Explorer
# Video Demo: <URL HERE>

Description:
Hello! This is team MCDM's Global Recipe Explorer, a Python app that lets you explore recipes from all 195 countries in the world, using the Spoonacular API. Our names are Daniela and Maelle, my GitHub username is `marimar1825`, we are respectively in BOS5 and in BOS1. We built this because we wanted a fun way to discover food from every corner of the globe!

# What It Does
This app uses the Spoonacular API to fetch recipes for all 195 sovereign countries! It maps each country to a cuisine (like "Italy" to "Italian" or "Gambia" to "African"). Features:
1. **Pick a country**: Type any country (e.g., "El Salvador", "France", "Brazil"), and it finds two recipes.
2. **Search for a recipe**: Search by country or ingredient (e.g., "rice"), get up to five matches.
3. **Get a random recipe**: Grabs a random dish from the API’s huge database.
4. **Exit**: Closes the app.

From Afghanistan to Zimbabwe, it’s got every country covered!

# Files
- **project.py**: The main code! Connects to Spoonacular API with:
  - main(): Runs the menu loop.
  - get_cuisine_for_country(): Maps all 195 countries to cuisines.
  - get_recipes_by_country(): Fetches two recipes.
  - display_recipe(): Shows recipe details.
  - search_recipes(): Searches by term.
- **test_project.py**: Tests with `pytest`
- **requirements.txt**: Lists `pytest` and `requests`.

# Design Choices
We used Spoonacular (free, 150 calls/day) and mapped all 195 countries to its cuisines—like "Italian" for Italy or "African" for The Gambia. Some countries share cuisines (e.g., "Latin American"), but every one is included! If a country’s cuisine isn’t specific, the API tries its best. 

# How to Set Up and Run It
1. **Get an API Key**:
   - Sign up at [Spoonacular](https://spoonacular.com/food-api).
   - Grab your free API key (150 calls/day).
2. **Install Dependencies**:
   - Put files in a folder.
   - In terminal: `pip install -r requirements.txt`.
3. **Add Your Key**:
   - Open `project.py`, replace `YOUR_API_KEY_HERE` with your key.
4. **Run It**:
   - `python project.py` in terminal.
   - Try "El Salvador" or any country!
5. **Test It**:
   - `pytest` to verify functions.

# What I Learned
- Mapping 195 countries to cuisines was a big task!
- Using APIs for live, global data.
- Handling cases where small countries share cuisines.
- Testing with a full world scope.

Typing out every country took effort, but now it’s truly global! The API’s limits (150 calls) mean some testing patience, though.

# What’s Next?
- Better API error handling.
- Maybe split the country list into a file.