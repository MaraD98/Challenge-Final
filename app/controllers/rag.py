from services.retrieval import busqueda_en_db
from services.generation import prompt_final

#Integracion de los modulos
def RAG_answer(question):
    """
    Responde la consulta teniendo en cuenta lo siguiente:

    Parámetros:
        {document}: Usa solamente esa informacion para responder
        {question} (str): Pregunta del usuario.

    Retorna:
        str: La respuesta generada o un mensaje de error si ocurre algo inesperado.
    """
    try:
        # Busca el documento más relevante en la db
        document = busqueda_en_db(question)
        if not document:
            return "No se encontraron resultados relevantes para tu pregunta."

        # Genera la respuesta final utilizando el documento relevante
        response = prompt_final(question,document)
        return response 
    except Exception as e:
        return f"Hubo un error al procesar la pregunta: {str(e)}"