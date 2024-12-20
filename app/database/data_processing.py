import chromadb 
from app.utils.utils import split_text, get_embeddings
from app.models.schemas import LinkMetadata
import requests
from bs4 import BeautifulSoup


# Configuración de Chroma, directorio de persistencia
client = chromadb.PersistentClient(path="/path/to/save/to")

# Crea la colección
collection = client.get_or_create_collection(name="new_collection")

# Función principal para procesar los enlaces
def process_embeddings_link(link: LinkMetadata):
    
    try:
        #Verifico si el link fue procesado, esto es para pruebas
        existing_documents = collection.get(where={"documents": link})
        
        if existing_documents:
            print(f"El enlace {link} ya está en la base de datos. No se procesará de nuevo.")
            return
        
        # 1. Obtiene contenido del enlace
        response = requests.get(link.url)
        if response.status_code != 200: 
            raise Exception(f"No se pudo acceder al enlace. Código: {response.status_code}")
        
        soup = BeautifulSoup(response.content, "html.parser")
        document_content = soup.get_text(separator="\n", strip=True)
        
        if not document_content.strip():
            raise Exception("El contenido del documento está vacío.")

        # 2. Divide en fragmentos
        chunks = split_text(document_content)
        print(f"Texto dividido en {len(chunks)} fragmentos.")
            
        # 3. Genera embeddings con Cohere
        embeddings = get_embeddings(chunks)  

        # 4. Guarda en ChromaDB
        ids = [f"{link}_chunk_{i}" for i in range(len(chunks))]

        collection.add(
                ids=ids,
                documents=chunks,
                embeddings=embeddings
            )
        print("Embeddings guardados con éxito en ChromaDB.")

    except Exception as e:
        print(f"Error al procesar el enlace: {str(e)}")






#Exportar la colección
__all__ = ["collection", "client", "process_embeddings_link"]