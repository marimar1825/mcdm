# Global Recipe Explorer
# Video Demo: <https://youtu.be/SELSfIirY2M?feature=shared>

Description:
Hello! This is team MCDM's Global Recipe Explorer, a Python app that lets you explore recipes from all 195 countries in the world, using the Spoonacular API. We built this because we wanted a fun way to discover food from every corner of the globe!

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

# What We Learned
- Mapping 195 countries to cuisines was a big task!
- Using APIs for live, global data.
- Handling cases where small countries share cuisines.
- Testing with a full world scope.

Typing out every country took effort, but now it’s truly global! The API’s limits (150 calls) mean some testing patience, though.

# What’s Next?
- Better cuisine mapping: Some countries share cuisines, so we want to refine our categorization for even more accurate results.
- More recipes per search: Right now, we limit results, but with an upgraded API plan, we can offer more options.
- User favorites & reviews: Imagine saving your favorite dishes or rating recipes to help others!
- Dietary preferences: Future updates could allow searches by dietary needs : vegetarian, gluten-free, or vegan etc
- Pictures : We could also add pictures or videos of the dishes or the recipes 
- App : We would create an app or a website and not just run it in the terminal ! 
- Better API error handling: If the Spoonacular API runs into issues, we want our app to handle errors gracefully instead of crashing.
- Split the country list into a file: To improve organization and efficiency, we might store the country-to-cuisine mappings in a separate file rather than hardcoding them

# What Each File Does
- Project.py serves as the core of the Global Recipe Explorer application. It’s the file executed with python project.py to launch the program, bringing the entire recipe exploration experience to life. Think of it as the engine that powers the app, handling everything from user interactions to fetching and displaying recipes.
- Test_project.py is a file that tests the functions in project.py to make sure they work correctly. It’s like a quality check for the app, run using a tool called pytest. Just type pytest in the terminal, and it checks if everything behaves as expected.
- Requirements.txt is a text file that lists the extra tools (libraries) the app needs to work.
   Contents
   pytest: The tool to run the tests in test_project.py.
   requests: The library that lets project.py talk to the Spoonacular API.
- README.md is a Markdown file (.md means Markdown) that explains the project to anyone who sees it—like a user manual or a project introduction. It’s not code that runs; it’s documentation you read.

# References
- xAI. (2023). Grok [Artificial intelligence language model].
- OpenAI. (2022). ChatGPT [Artificial intelligence language model].
- Spoonacular. (n.d.). Spoonacular Food API [Web API].