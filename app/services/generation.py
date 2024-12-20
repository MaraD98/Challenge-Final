from app.utils.utils import co

#Construcción del Módulo de Generación
def prompt_final(question, document):
    try:
        # Crear el prompt para el modelo
        system_prompt = f""" 
                Eres un experto en los derechos de las personas con discapacidad.
                
                Tu tarea consiste en:
                - Responder a las preguntas basandote en el contexto, sin añadir información no relevante.
                - Dar una respuesta con un enfoque conciso y claro, en menos de 1 parrafo.
                - Responder en tercera persona siempre.
                - Responde siempre en español, sin importar en qué idioma se haga la pregunta.

                ###
                Contexto:
                {document}

                ###
                Pregunta:
                {question}

                ###
                Respuesta: str
                """
        # Llamada al modelo
        response = co.generate(
                model="command-r-plus-08-2024",
                prompt=system_prompt,
                max_tokens=200,  
                temperature=0.2,
                seed=2323
            )
        # Retornar la respuesta generada
        return response.generations[0].text
    except Exception as e:
        return f"Error al generar la respuesta: {str(e)}"