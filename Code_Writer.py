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
        store=False,
        tools=TOOLS,
        parallel_tool_calls=False,
        include=["reasoning.encrypted_content"]
    )

def describe_tool(name, description, properties):
    return {
        "type": "function",
        "name": name,
        "description": description,
        "parametrs": {
            "type": "object",
            "propetries": properties,
            "request": list(properties),
            "additionalProperties": False
        }, "strict": True
    }

TOOLS = [describe_tool("list_files",
                       "Показати Python-файли нашої гри",
                       {})]

task = input("Задача: ")
context = [{"role": "user", "content": task}]
response = ask(context)
for item in response.output:
    print(
        item.type,
        getattr(item, "name", ""),
        getattr(item, "argumets", ""))