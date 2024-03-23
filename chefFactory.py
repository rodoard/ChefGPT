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
    
    def genChatCompletion(self, user_input):
        self.messages.append({
            "role": "user",
            "content": user_input
        })
        stream = self.client.chat.completions.create(
          model=self.model,
          messages=self.messages,
          stream=True,
        )
        self.collected_messages = []
        for chunk in stream:
          chunk_message = chunk.choices[0].delta.content or ""
          print(chunk_message, end="")
          self.collected_messages.append(chunk_message)
        
        self.messages.append({
            "role": "system",
            "content": "".join(self.collected_messages)
          })
    
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
