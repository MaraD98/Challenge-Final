from pydantic import BaseModel

#Clase para manejar los enlaces y metada
class LinkMetadata:
    def __init__(self, url, description, date_accessed):
        self.url = url
        self.description = description
        self.date_accessed = date_accessed


# Modelo de entrada
class Question(BaseModel):
    question: str

# Modelo de salida
class ResponseModel(BaseModel):
    response: str