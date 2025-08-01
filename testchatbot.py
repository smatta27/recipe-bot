from chatbot import is_recipe_question

def test_is_recipe_question():
    assert is_recipe_question("How do I bake a cake?")

def test_is_recipe_question2():
    assert is_recipe_question("What's the weather today?")

def test_is_recipe_question3():
    assert is_recipe_question("Can you show me how to make scrambled eggs")

def test_is_recipe_question4():
    assert is_recipe_question("Hello")

def test_is_recipe_question5():
    assert is_recipe_question("How do I cook mashed potatoes")

def test_is_recipe_question6():
    assert is_recipe_question("What happens if I burn myself on the stove?")

def test_is_recipe_question7():
    assert is_recipe_question("Goodbye")

def test_is_recipe_question8():
    assert is_recipe_question("tutorial on how to make pasta")

def test_is_recipe_question9():
    assert is_recipe_question("what's a good restaurant near me?")
