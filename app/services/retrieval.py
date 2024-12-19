from app.utils.utils import get_embeddings
from app.database.data_processing import collection

#Desarrollo del Módulo de Retrieval-Augmented
def busqueda_en_db(question):
    """
    Busca en la base de datos y combina los 3 resultados más relevantes.
    """
    try:
        #Uso la funcion creada anteriormente para los embeddings de la pregunta
        prompt_embedding = get_embeddings([question])[0]

        # Realizar la búsqueda en ChromaDB
        resultados = collection.query(
            query_embeddings=[prompt_embedding],
            n_results=3
        )

        documentos = resultados['documents']
        if not documentos:
            return "No se encontraron resultados relevantes en la base de datos."
        return documentos

    except Exception as e:
        return f"Error al realizar la búsqueda: {str(e)}"
