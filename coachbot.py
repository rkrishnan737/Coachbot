from openai import OpenAI
client = OpenAI()

def chat(prompt):
    response = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[{
                "role": "user",
                "content": prompt
              },
              {
                "role": "developer",
                "content": "Answer as if you're a coach at the end of a sports movie giving a motivational speech."
              }
        ])
    
    return response.choices[0].message.content.strip()


while True:
    user_input = input("You: ")
    
    if user_input.lower() in ["quit", "exit", "bye", "^c"]:
        break
        
    response = chat(user_input)
    print("Coachbot: ", response)