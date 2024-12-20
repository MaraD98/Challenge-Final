from app.services.retrieval import busqueda_en_db
from app.services.generation import prompt_final
#from services.validation import get_cached_response

#Integracion de los modulos
def RAG_answer(question):
    """
    Genera una respuesta amable y estructurada basada en la consulta.

    Parámetros:
        question (str): Pregunta del usuario.

    Retorna:
        str: La respuesta generada o un mensaje amable si ocurre algo inesperado.
    """
    try:
        # Busca el documento más relevante en la db
        document = busqueda_en_db(question)
        if not document:
            return "Lo siento, no encontré información relevante para tu consulta. ¿Te gustaría intentar con otra pregunta?"

        # Genera la respuesta final utilizando el documento relevante
        response = prompt_final(question,document)

        # Validar y retornar respuesta cacheada
        #return get_cached_response(question, response)
        return response
    except Exception as e:
        return f"Lo siento, hubo un problema al procesar tu pregunta. Por favor, intenta nuevamente o contacta con soporte. Detalle del error: {str(e)}"
    


