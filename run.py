import google.generativeai as genai
from langchain_google_genai import ChatGoogleGenerativeAI
from config import GOOGLE_API_KEY

llm = ChatGoogleGenerativeAI(model="gemini-1.5-flash-latest", google_api_key=GOOGLE_API_KEY)
response = llm.invoke("Where is South Africa located?")

print(response.content)