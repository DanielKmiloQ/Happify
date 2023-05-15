# pip install openai
import openai
# pip install gradio
import gradio

# OpenAI Api Key
openai.api_key = "####"

# Lista que guarda el historial de conversación. Además incluye las indicaciones para un chat adecuado
messages = [{"role": "system", "content": "Eres un consejero emocional experto. Tu trabajo es en primera instancia dar consejos que puedan ayudar a las peticiones del usuario. A continuación harás unas preguntas o reflexiones que hagan al usuario reflexionar sobre sí mismo. Después, debes redirigir al usuario al profesional que más le convenga. Si es posible has preguntas para que la conversación pueda fluir. Debes tener mucho cuidado al tratar temas muy sensibles, prioriza la vida y el bienestar del usuario ante todo."}]

def CustomChatGPT(user_input):
    messages.append({"role": "user", "content": user_input})
    response = openai.ChatCompletion.create(
        model = "gpt-3.5-turbo",
        messages = messages
    )
    ChatGPT_reply = response["choices"][0]["message"]["content"]
    messages.append({"role": "assistant", "content": ChatGPT_reply})
    return ChatGPT_reply

# Libreria para tener una interfaz de usuario predeterminada
demo = gradio.Interface(fn=CustomChatGPT, inputs = "text", outputs = "text", title = "Happify")

# Programa principal
demo.launch()