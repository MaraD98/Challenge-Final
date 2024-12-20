# Sistema de Carga, Búsqueda y Generación de Datos (RAG)

Este proyecto implementa un sistema avanzado de carga, búsqueda y generación de datos utilizando tecnologías como **Cohere**, **ChromaDB** y **procesamiento de texto**. A continuación, se describen las funcionalidades principales y el entorno de configuración necesario.

---

## Funcionalidades Principales

### **1. Carga de Datos Persistentes**
- **Descripción**: Procesa documentos, los divide en fragmentos y genera embeddings para su almacenamiento en una base de datos persistente configurada con **ChromaDB**.
- **Proceso**:
  1. Descarga el contenido de un enlace (documento).
  2. Divide el texto en fragmentos utilizando un `RecursiveCharacterTextSplitter`.
  3. Genera embeddings con **Cohere**.
  4. Guarda los fragmentos y embeddings en una colección de ChromaDB para futuras búsquedas.

---

### **2. Búsqueda de Datos**
- **Descripción**: Permite buscar y recuperar los documentos más relevantes de la base de datos utilizando embeddings.
- **Características**:
  - Genera embeddings de las consultas de los usuarios.
  - Retorna documentos clasificados según su relevancia.

---

### **3. Generación de Respuestas (RAG)**
- **Descripción**: Construye un sistema de **Retrieval-Augmented Generation (RAG)** para responder preguntas basándose en contexto.
- **Funcionamiento**:
  1. Realiza una consulta en la base de datos para encontrar documentos relevantes.
  2. Usa el contenido como contexto para un modelo generador.
  3. Responde en español con un enfoque claro y conciso, centrado en los derechos de las personas con discapacidad.

---

## Tecnologías Utilizadas
- **Cohere**: Generación de embeddings y respuestas.
- **ChromaDB**: Almacenamiento y recuperación eficiente de datos persistentes.
- **BeautifulSoup**: Extracción de contenido de páginas web.
- **Python**: Desarrollo modular y escalable del sistema.

---

## Archivos y Funciones Principales
- **`split_text`**: Divide texto en fragmentos manejables.
- **`get_embeddings`**: Genera embeddings a partir de texto.
- **`process_embeddings_link`**: Procesa enlaces y guarda datos en ChromaDB.
- **`busqueda_en_db`**: Realiza consultas para encontrar documentos relevantes.
- **`RAG_answer`**: Integra búsqueda y generación para responder preguntas.

---

## Requisitos
- **Python**: Versión 3.9+
- **Dependencias**:
  - `langchain`
  - `cohere`
  - `chromadb`
  - `requests`
  - `beautifulsoup4`
  - `dotenv`

---

## Instrucciones de Configuración
1. **Clonar el repositorio**:
   ```bash
   git clone <url_del_repositorio>
   ```

2. **Instalar las dependencias**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Configurar las claves de API**:
   - Crear un archivo `.env` en la raíz del proyecto.
   - Agregar la clave de Cohere:
     ```env
     CO_API_KEY=tu_clave_de_cohere
     ```

4. **Ejecutar el proyecto**:
   ```bash
   python main.py
   ```

---

## Ejemplo de Uso

### **Carga de Datos**
Para procesar un enlace y cargar los datos:
```python
process_embeddings_link("https://www.argentina.gob.ar/normativa/nacional/ley-26378-141317/texto")
```

### **Búsqueda en la Base de Datos**
Para realizar una búsqueda:
```python
resultados = busqueda_en_db("¿Cuáles son los derechos garantizados en esta ley?")
print(resultados)
```

### **Generación de Respuestas**
Para obtener una respuesta basada en el contexto:
```python
respuesta = RAG_answer("Explique los derechos establecidos en la ley 26378.")
print(respuesta)
```
---

# **Documentación de la API: POST /chat**

## **Descripción**
Este endpoint procesa una pregunta proporcionada por el usuario y genera una respuesta utilizando un modelo de Recuperación y Generación Aumentada (RAG). Es útil para consultas relacionadas con los derechos de las personas con discapacidad.

---

## **Detalles del Endpoint**
- **URL:** `/chat`
- **Método HTTP:** `POST`
- **Código de Respuesta:** `201 Created`
- **Descripción:** Genera una respuesta basada en el contexto y la pregunta proporcionada.

---

### **Request**
- **Headers:**  
  - `Content-Type: application/json`

- **Cuerpo del Request:**  
  Debe enviarse un JSON con el siguiente formato:

```json
{
  "question": "¿Cuál es el marco legal para el acceso al trabajo de personas con discapacidad?"
}
```

- **Validaciones:**  
  - El campo `question` no puede estar vacío.
  - Debe ser un string válido.

---

### **Response**
- **Código de Estado:** `201 Created`
- **Cuerpo de la Respuesta:**  
  Un JSON con el siguiente formato:

```json
{
  "response": "El marco legal incluye la Ley 26.378, que garantiza la igualdad de oportunidades en el ámbito laboral para las personas con discapacidad."
}
```

---

### **Errores Comunes**
1. **400 Bad Request:**  
   - Causa: El campo `question` está vacío.  
   - Respuesta:

   ```json
   {
     "detail": "La pregunta no puede estar vacía."
   }
   ```

2. **500 Internal Server Error:**  
   - Causa: Error interno durante el procesamiento de la pregunta.  
   - Respuesta:

   ```json
   {
     "detail": "Error al procesar la pregunta. Inténtalo nuevamente más tarde."
   }
   ```

---

