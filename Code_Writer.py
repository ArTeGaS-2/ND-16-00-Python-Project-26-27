from openai import OpenAI
API_KEY = "YOUR_OPENAI_API_KEY"
client = OpenAI(api_key=API_KEY, max_retries=0)
MODEL = "gpt-5.6-luna"
INSTRUCTION = "Ти Python-розробник для текстової RPG в форматі. " \
            "Ти маєш створювати і редагувати скрипти і промпти викликів моделей."

def ask(context):
    return client.responses.create(
        model=MODEL,
        instructions=INSTRUCTION,
        input=context,
        reasoning={"effort": "xhigh"},
        store=False
    )
task = input("Задача: ")
context = [{"role": "user", "content": task}]
response = ask(context)
print(response.output_text)