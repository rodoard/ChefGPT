from openai import OpenAI
from instructions import systemInstructions

class Chef:
    def __init__(self, info):
        self.client = info.get('client')
        self.name = info.get('name')
        self.model = info.get('model')
        self.messages = info.get('messages')
        self.collected_messages = []
        
    def getName(self): 
       return self.name
    
    def getCategory(self, input):
        messages = self.messages + [
         {
  "role": "system",
  "content": "Category: ingredients"
}, 
{
  "role": "system",
  "content": "Category: dish"
},

{
  "role": "system",
  "content": "Category: recipe"
},
{
  "role": "system",
  "content": "Category: other"
}

        ] + [{
            "role": "user",
            "content": input
        }]
         
        result = self.client.chat.completions.create(
          model=self.model,
          messages=messages,
        )
        if len(result.choices) == 0:
           return "other"

        return result.choices[0].message.content.split(":")[1].strip()

    def __genChatCompletion(self, user_input):
        messages =  self.messages + [user_input]
        stream = self.client.chat.completions.create(
          model=self.model,
          messages=messages,
          stream=True,
        )
        self.collected_messages = []
        for chunk in stream:
          chunk_message = chunk.choices[0].delta.content or ""
          print(chunk_message, end="")
          self.collected_messages.append(chunk_message)
        
    def genDishName(self, ingredients):
        # Method to generate a dish name
        self.__genChatCompletion({
        "role": "user",
        "content": f"""
        Suggest one dish I can make with the following ingredients: {ingredients}.  
        Do not suggest more than one dish.  Do not suggest a recipe or instructions.
        If you do not know, do not try to generate a dish name,
        you must say you do not know and end the conversation briefly.
        """
        })

    def genRecipe(self, dish):
        # Method to generate a recipe
        self.__genChatCompletion({
        "role": "user",
        "content": f"""
        Suggest a detailed recipe for this dish {dish}.
        If you do not know, do not try to generate a recipe,
        end the conversation briefly. if you know a recipe
        do not ask the user for permission to provide it, you 
        must provide a detailed recipe.
        """
        })

    def genCriticism(self, recipe):
        # Method to generate criticism
       self.__genChatCompletion({
        "role": "user",
        "content": f"Criticize the following recipe {recipe} and suggest ways to improve it."
        })

    def genInvalidInput(self):
        # Method to handle invalid input
        print("I'm sorry, I don't understand your request.")

    def handleInputCategory(self, category, input):
      if category == "ingredients":
        self.genDishName(input)
      elif category == "dish":
        self.genRecipe(input)
      elif category == "recipe":
        self.genCriticism(input)
      else:
        self.genInvalidInput()
    
def newChef(chef): 
  client = OpenAI()
  model = "gpt-3.5-turbo"
  messages = systemInstructions(chef["personality"])
  name = chef["name"]
  info = {
      'client':client,
      'model':model,
      'messages': messages,
      'name':name
  }
  return Chef(info)
