import openai

def bot(user_input):
    openai.api_key = "YOUR_API_KEY"
    
    prompt = f"Bhai, ek college student rant kar raha hai: '{user_input}'. Usko ek masti bhara aur relatable jawab de Hindi slang mein."
    
    response = openai.ChatCompletion.create(
        model="gpt-4o-mini",
        messages=[{"role": "system", "content": "Tu ek chill senior hai jo college ki life aur struggles ko relate karta hai.Tu har ek response de 5 baar emojis ke sath."},
                  {"role": "user", "content": prompt}]
    )
    
    return response["choices"][0]["message"]["content"]


user_input = input("Chal bol kya bolta  : \n")
response = bot(user_input)
print(response)
print("Bot Powered by @sankya")
