import requests
import json

def summarize_article(api_key, article_text, word_limit=160):
    url = "https://generativelanguage.googleapis.com/v1/models/gemini-pro:generateContent"
    headers = {"Content-Type": "application/json"}
    
    prompt = f"Summarize the following text in a clear and concise manner, highlighting the key points and main takeaways. Maintain the original context and intent. Keep it within {word_limit} words.\n\n{article_text}"
    
    data = {
        "contents": [{"parts": [{"text": prompt}]}],
        "generationConfig": {"maxOutputTokens": 200}  # Adjust token limit as needed
    }
    
    response = requests.post(f"{url}?key={api_key}", headers=headers, json=data)
    
    if response.status_code == 200:
        result = response.json()
        return result.get("candidates", [{}])[0].get("content", "Summary not available.")
    else:
        return f"Error: {response.status_code}, {response.text}"


