import google.generativeai as genai
from config import GEMINI_API_KEY

# Configure Gemini
genai.configure(api_key=GEMINI_API_KEY)
model = genai.GenerativeModel(model_name="gemini-2.0-flash")

def ask_gemini(prompt):
    try:
        response = model.generate_content(prompt)

        # Handle multiple possible response formats
        if hasattr(response, 'text') and response.text:
            return response.text.strip()
        elif response.candidates:
            return response.candidates[0].content.parts[0].text.strip()
        else:
            return "⚠️ Gemini response was empty or unstructured."

    except Exception as e:
        return f"🚨 Something went wrong with Gemini: {str(e)}"