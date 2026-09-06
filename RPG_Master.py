from pathlib import Path # Шляхи до файлів
import json # Збереження даних
from openai import OpenAI # Звернення до моделей AI

API_KEY = "ключ"
client = OpenAI(api_key=API_KEY)

MODEL = "gpt-5.6-luna"
HISTORY_FILE = Path("history.json")
STATE_DIR = Path(".rpg_state")
MEMORY_FILE = STATE_DIR / "gm_memory.txt"
MAX_HISTORY_MESSAGES = 100

INSTRUCTIONS = (
    "Ти Game Master текстової RPG.\n"
    "Керуй світом, NPC, описами, діалогами, наслідками дій і розвитком сюжету.\n"
)