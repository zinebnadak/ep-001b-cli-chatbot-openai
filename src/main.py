import os
from openai import OpenAI
from openai import RateLimitError, APIError
from dotenv import load_dotenv 

load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_AI_KEY"))

conversation_history = []
      

print('Assistant ready. Type "quit" or "exit" to terminate!')

while True:     #runs forever
    user_input = input("Type something: ")
    if user_input.lower() in ["quit", "exit"]:
        print("Goodbye! :)")
        break
    conversation_history.append({"role":"user", "content" : user_input})    #append the input to history


    try:                                                                    #error handle 
        response = client.responses.create(
            model = "gpt-4o-mini",                                          #parameters names must stay the same messages for Anthropic and input for OpenAI
            input = conversation_history,
            max_output_tokens= 250,
            instructions="You are a helpful assistant."
        )
        print(response.output_text)
        reply = response.output[0].content[0].text                               #drill into "text"
        conversation_history.append({"role" : "assistant", "content" : reply}) 

    except RateLimitError:
        print("Rate limit hit! Wait a moment and try again later.")

    except APIError as e:
        print(f"API error: {e}")
    
                  
# print(conversation_history)


