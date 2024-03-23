## Testing Prompts

We simulate an AI chef.
We create a prompt to constrain text generation to 
to inputs that are in the following categories only

1. List of ingredients
2. Dish name
3. Recipe for a dish.

The AI should respond with an error for inputs outside
the three categories.

We include chefs with different personalities to see 
a variety of responses.

Report.txt is a sample output run using the following
command:

```
script 'python main.py' Report.txt
```