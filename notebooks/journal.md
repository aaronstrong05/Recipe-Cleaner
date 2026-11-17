`how is data stored in these HTML pages for the recipe?`

    the ingredients seems to be stored in list like objects, 
    
    EX:| "recipeIngredient":["1 1\/4 cup (250 g) granulated sugar","16 tablespoons (226 g) unsalted butter ( room temperature)","2 tablespoons (28 g) light brown sugar (packed)", ... ]

    instructions seem to be stored in typical dictionary type objects, with ID names to reference what category of text a given seciton belongs to, IE: @howtostep, @howtosection.

    EX: {"@type":"HowToStep","text":"With the mixer on low, add in the eggs one at a time, 
    taking care to fully blend the first before adding the second. Scrape the sides and bottom of the bowl to make sure everything is incorporated.","name":"With the mixer on low, add in the eggs one at a time, taking care to fully blend the first before adding the second. Scrape the sides and bottom of the bowl to make sure everything is incorporated.","url":"https:\/\/www.displacedhousewife.com\/snickerdoodles\/#wprm-recipe-16896-step-0-2"}

`Why do you think a recipe site puts this hidden block in its page at all? Who is it for? (Think about what searches for recipes look like.)`

    indgredients, prep time, cook time, total time, and maybe other things of the keyword variety are stored here to do the same thing im trying to do, parse queries and match it with keywords that belong to the recipe.

`How many JSON-LD blocks expect on this page?`

    I really dont know tbh, I think maybe just one or two?

    It has 1

`Why choose .get_text() over .string?`

    .get_text() is able to ignore nested styling tags, and .string wont look into them, so if there were to be nested HTML in that ldblock then .get_text() wouldnt give me an issue, i only cared about raw text length

`When the block gets parsed, will it be a dict or a list?`

    I think it will return as a dict due to the design of the ld block in the html file, it already heavily resembles a dict

    It came out as a list

`What is in @context?`

    I dont know, my guess is something with the styling of the page?

    It contains www.Schema.org


`First item keys vs last items keys`

    The first item has keys that all pertain to the actual article itself, things like publishing date, edit date, comments, ratings, ect...
    The last item has all the pertinent information to the recipe, all labled with the word 'recipe' first, "recipeYield" "recipeInstructions" "recipeIngredient"

`NutritionBool`
    only looks into the LD blocks for structured nutrition information, however some sites have it stored in a seperate visible location.
    This leads to sites that have it stored seperately returning False. *FIX LATER*