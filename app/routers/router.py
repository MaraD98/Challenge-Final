from fastapi import APIRouter, HTTPException, status
from app.controllers.rag import RAG_answer
from app.models.schemas import Question,ResponseModel

router = APIRouter()

@router.post("/chat", response_model=ResponseModel, status_code= status.HTTP_201_CREATED, description="Genera una respuesta a la pregunta proporcionada.")
async def chat_endpoint(question: Question):
    """
    Endpoint para procesar preguntas y generar una respuesta.
    """
    # Validación de entrada
    if not question.question.strip():
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="La pregunta no puede estar vacía.")
    # Lógica de respuesta
    response = RAG_answer(question.question)
    return {"response": response}