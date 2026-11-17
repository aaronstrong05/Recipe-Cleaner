import pandas as pd 
from pathlib import Path
from bs4 import BeautifulSoup
import json
import html

def load_ld_blocks(path):
    test_file_text = Path(path).read_text(encoding="utf-8")
    soup = BeautifulSoup(test_file_text, 'html.parser')

    ld_blocks = soup.find_all('script', type = "application/ld+json" )
    ld_parsed = []
    ld_flattened = []

    for block in ld_blocks:
        ld_flattened.append(block.get_text())
    for block in ld_flattened:
        parsed_block = json.loads(block)
        ld_parsed.append(parsed_block)
    return ld_parsed

def find_recipe(graph):
    recipe = None
    for item in graph:
        if not isinstance(item, dict):
            continue
        item_type = item.get("@type", "none")
        if isinstance(item_type, str):
            match  = item_type == "Recipe"
        
        else:
            match = "Recipe" in item_type
        
        if match:
            recipe = item
    return recipe

def get_steps(recipe):

    all_steps = []
    for sections in recipe["recipeInstructions"]:
        if sections.get("@type") == "HowToStep":
            all_steps.append(sections['text'])    
        else:
            for step in sections['itemListElement']:
                all_steps.append(step['text'])
    return all_steps

def steps_from_page(path):
    blocks = load_ld_blocks(path)
    steps = get_steps(find_recipe(blocks[0]["@graph"]))
    return steps

def summarize_page(path):
    blocks = load_ld_blocks(path)
    recipe = find_recipe(blocks[0]["@graph"])
    nutritionBool = "nutrition" in recipe
    page_data ={"Name": html.unescape(recipe["name"]), "Step count": len(steps_from_page(path)), "Ingredients": len(recipe["recipeIngredient"]), "Has Nutrition": nutritionBool}
    return page_data
