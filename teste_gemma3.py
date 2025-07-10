import ollama
#  127.0.0.1:11434: bind:
# inicia o cliente
client = ollama.Client()

# prompt com contexto
contexto = """
    aja como professor.
"""

instrucao = """
        responda a pergunta. quais foram as capitais do brasil?
"""

prompt = f"Contexto: {contexto}\n\nInstrução: {instrucao}" # define prompt

response = client.generate(model="gemma3:12b", prompt=prompt) # alimento modelo com prompt

# imprime a resposta
print("Resposta do Gema 3:", response)