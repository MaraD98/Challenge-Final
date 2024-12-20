from langchain.text_splitter import RecursiveCharacterTextSplitter
import cohere
from dotenv import load_dotenv
import os
import hashlib

# Inicialización del cliente los clientes
load_dotenv(dotenv_path="app/.env")  # Load .env file
api_key = os.getenv("COHERE_API_KEY")
co = cohere.ClientV2()

#Funcion que divide un contenido en chunks
def split_text(content):
    """
    Divide el texto en chunks según el tamaño y solapamiento especificados.
    
    Args:
        content (str): El texto completo a dividir.
        chunk_size (int): Tamaño máximo de cada chunk.
        chunk_overlap (int): Cantidad de caracteres que se solapan entre chunks.

    Returns:
        List[str]: Lista de chunks.
    """
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=1300,
        chunk_overlap=100,
        length_function=len
    )
    return text_splitter.split_text(content)


#Funcion que genera embeddings un contenido 
def get_embeddings(document):
    """
    Genera embeddings utilizando Cohere.
    
    Args:
        textos (List[str]): Lista de textos a procesar.

    Returns:
        List[List[float]]: Lista de embeddings generados para cada texto.
    """
    embbeding_response = co.embed(
        texts=document,
        model="embed-multilingual-v3.0",
        input_type="search_document", 
        embedding_types=["float"]
    )
    return embbeding_response.embeddings.float


# Diccionario global para almacenar respuestas
response_cache = {}

def get_cached_response(question, response):
    """
    Verifica si la pregunta ya tiene una respuesta cacheada.
    Si no, almacena la respuesta generada.
    
    Args:
        question (str): La pregunta del usuario.
        response (str): La respuesta generada para la pregunta.
    
    Returns:
        str: La respuesta cacheada o generada.
    """
    # Crear un hash de la pregunta
    question_hash = hashlib.sha256(question.encode()).hexdigest()
    
    # Verificar si ya está en el cache
    if question_hash in response_cache:
        return response_cache[question_hash]
    
    # Si no está, guardar la respuesta en el cache
    response_cache[question_hash] = response
    return response

__all__ = ["co"]