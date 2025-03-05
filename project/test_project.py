from project import get_recipes_by_country, display_recipe, search_recipes

def test_get_recipes_by_country():
    italy_recipes = get_recipes_by_country("Italy")
    assert italy_recipes is not None
    assert len(italy_recipes) <= 2
    gambia_recipes = get_recipes_by_country("Gambia")
    assert gambia_recipes is None or len(gambia_recipes) <= 2  

def test_display_recipe():
    try:
        display_recipe(716429)  
        assert True
    except:
        assert False
    try:
        display_recipe(999999999) 
        assert True  
    except:
        assert False

def test_search_recipes():
    japan_search = search_recipes("Japanese")
    assert japan_search is not None
    assert len(japan_search) <= 5
    rice_search = search_recipes("rice")
    assert rice_search is not None
    assert len(rice_search) > 1
    fake_search = search_recipes("xyzxyz")
    assert fake_search is None or len(fake_search) == 0