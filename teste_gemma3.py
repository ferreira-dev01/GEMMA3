# import ollama
import sys
sys.stdout.reconfigure(encoding="utf-8")
# # 127.0.0.1:11434: bind:
# #http://localhost:3000/
# # inicia o cliente
# #client = ollama.Client()
# client = ollama.Client(host='127.0.0.1:11434')

# # prompt com contexto
# contexto = """

# """

# instrucao = """
# qual a capital do  equador?
# """

# prompt = f"Contexto: {contexto}\n\nInstrução: {instrucao}" # define prompt

# response = client.generate(model="gemma3:12b", prompt=prompt) # alimento modelo com prompt

# # imprime a resposta
# print("Resposta do Gema 3:", response.response)


# import pycurl

# def process_header(header_line):
#     print(header_line.decode('utf-8').strip())

# c = pycurl.Curl()
# c.setopt(c.URL, 'http://127.0.0.1:11434')
# c.setopt(c.HEADERFUNCTION, process_header)
# c.setopt(c.NOBODY, 1)
# c.perform()
# c.close()



# import pycurl
# from io import BytesIO

# buffer = BytesIO()
# c = pycurl.Curl()
# c.setopt(c.URL,  'http://127.0.0.1:11434')
# c.setopt(c.FOLLOWLOCATION, 1)
# c.setopt(c.WRITEDATA, buffer)
# c.perform()
# c.close()
# response = buffer.getvalue()
# print(response.decode("utf-8"))


# import ollama
# response = ollama.chat(model='gemma3:12b', messages=[
#   {
#     'role': 'user',
#     'content': ' quanto é 5 mais 3?',
#   },
# ])
# print(response['message']['content'])

# import ollama

# # Use the generate function for a one-off prompt
# result = ollama.generate(model='gemma3:12b', prompt='QUAL é sua versão?')
# print(result['response'])

# from ollama import chat

# conversation = [
#     {"role": "user", "content": "Hello, how are you?"}
# ]
# reply = chat(model='gemma3:12b', messages=conversation)
# print(reply.message.content)

import requests

SERVER_URL = "http://127.0.0.1:11434/api/generate" # add your server ip
model = "gemma3:12b"  # or "deepseek"
prompt="qual a capital do estado de minas gerais que fica no pais brasil? "
payload = {
    "model": model,
    "prompt": prompt,
    "stream": False
}

response = requests.post(SERVER_URL, json=payload)
response_json = response.json()  # Convert response to dictionary
print(response_json.get("response", "Key 'response' not found"))