

from openai import OpenAI

#Paste your API key from openai inside
client = OpenAI(api_key="")


def personal_assistant(prompt: str) -> str:

    #Sends your answer to chat gpt

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "Είσαι ένας προσωπικός βοηθός απαντάει φιλικά και σύντομα, το όνομα σου είναι πίπης"},
            {"role": "user", "content": prompt}
        ]
    )

    answer = response.choices[0].message.content
    # Return the answer to main.py
    return answer
