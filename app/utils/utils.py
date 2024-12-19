from langchain.text_splitter import RecursiveCharacterTextSplitter
import cohere
import os
from dotenv import load_dotenv


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

