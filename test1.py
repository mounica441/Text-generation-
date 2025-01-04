import google.generativeai as genai
genai.configure(api_key="AIzaSyDhq7wzLQEs9nxwA2ssvbZpGkxbq5oTj3Q")
model = genai.GenerativeModel("gemini-1.5-flash")
response = model.generate_content("Explain how AI works")
print(response.text)
generation_config = {
  "temperature": 0,
  "top_p": 0.95,
  "top_k": 64,
  "max_output_tokens": 8192,
  "response_mime_type": "text/plain",
}