import google.generativeai as genai
from langchain_google_genai import ChatGoogleGenerativeAI
from config import GOOGLE_API_KEY
from utils import setup_logger

logger = setup_logger(name=__name__)

llm = ChatGoogleGenerativeAI(model="gemini-1.5-flash-latest", google_api_key=GOOGLE_API_KEY)
response = llm.invoke("Where is South Africa located?")

logger.info(response.content)