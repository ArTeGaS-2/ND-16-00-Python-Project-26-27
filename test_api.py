from openai import OpenAI

API_KEY = "YOUR_OPENAI_API_KEY"
client = OpenAI(api_key=API_KEY)

response = client.responses.create(
    model="gpt-5.6-luna",
    input="Якщо все працює, напиши мені один з куплетів пісні групи Цвинтар.",
    reasoning={"effort":"medium"},
    store=False
)
print(response.output_text)
