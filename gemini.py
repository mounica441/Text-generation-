import google.generativeai as genai
genai.configure(api_key="AIzaSyDhq7wzLQEs9nxwA2ssvbZpGkxbq5oTj3Q")
model = genai.GenerativeModel("gemini-1.5-flash")
response = model.generate_content("Explain how AI works")
print(response.text)