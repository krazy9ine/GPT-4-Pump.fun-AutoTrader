import openai

openai.api_key = "YOUR_API_KEY"

def analyze_sentiment(prompt):
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": "You are an AI that analyzes cryptocurrency sentiment."},
            {"role": "user", "content": prompt}
        ]
    )
    return response['choices'][0]['message']['content']

# Example usage
prompt = "Analyze the social sentiment for token $PUMP in recent Reddit and Twitter discussions."
print(analyze_sentiment(prompt))
