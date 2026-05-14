import os
import time
import tiktoken

from ollama import Client
from dotenv import load_dotenv

load_dotenv()


class LLMClient:
    def __init__(self):
        self.model = os.getenv("MODEL_NAME", "gpt-oss:120b")

        self.client = Client(
            host="https://ollama.com",
            headers={
                "Authorization": "Bearer " + os.getenv("OLLAMA_API_KEY", "")
            }
        )

    def contar_tokens(self, texto):
        encoding = tiktoken.get_encoding("cl100k_base")
        return len(encoding.encode(texto or ""))

    def verificar_conexao(self):
        try:
            response = self.client.chat(
                model=self.model,
                messages=[
                    {
                        "role": "user",
                        "content": "Responda apenas OK"
                    }
                ],
                stream=False
            )

            if response["message"]["content"]:
                return True, "Conexão com Ollama Cloud OK"

            return False, "Resposta vazia"

        except Exception as e:
            return False, str(e)

    def chat(self, prompt, system="", temp=0.3, max_tokens=300):
        inicio = time.time()

        try:
            messages = []

            if system:
                messages.append({
                    "role": "system",
                    "content": system
                })

            messages.append({
                "role": "user",
                "content": prompt
            })

            response = self.client.chat(
                model=self.model,
                messages=messages,
                options={
                    "num_predict": max_tokens,
                    "temperature": temp
                },
                stream=False
            )

            fim = time.time()

            resposta = response["message"]["content"].strip()

            tokens_prompt = self.contar_tokens(prompt)
            tokens_resposta = self.contar_tokens(resposta)

            return {
                "resposta": resposta,
                "tokens_prompt": tokens_prompt,
                "tokens_resposta": tokens_resposta,
                "tempo_ms": round((fim - inicio) * 1000, 2),
                "erro": ""
            }

        except Exception as e:
            return {
                "resposta": "",
                "tokens_prompt": self.contar_tokens(prompt),
                "tokens_resposta": 0,
                "tempo_ms": 0,
                "erro": f"Erro API Ollama Cloud: {str(e)}"
            }