from dotenv import load_dotenv
import os
import cohere

load_dotenv("/.env")  # Load .env file

api_key = os.getenv("COHERE_API_KEY")

co = cohere.ClientV2()



# Exportar 
__all__ = ["co"]