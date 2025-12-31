import os
from groq import Groq

# ------------------------------------------------------------------
# 🚨 PASTE YOUR API KEY HERE
MY_API_KEY = "gsk_..."  
# ------------------------------------------------------------------

class RealLLM:
    def __init__(self):
        if "gsk_" not in MY_API_KEY:
             raise ValueError("🚨 YOU DID NOT PASTE THE KEY IN llm.py!")
        self.client = Groq(api_key="your_api_key")

    def generate(self, system_instruction, user_input):
        try:
            chat_completion = self.client.chat.completions.create(
                messages=[
                    {"role": "system", "content": system_instruction},
                    {"role": "user", "content": user_input}
                ],
                model="llama-3.3-70b-versatile",
                temperature=0.5,
            )
            return chat_completion.choices[0].message.content
        except Exception as e:
            return f"⚠️ API Error: {str(e)}"