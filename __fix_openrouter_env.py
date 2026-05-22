from pathlib import Path

p = Path(r"d:\Full_stack_GenAI\Repo\Full-Stack-GenAI\Class-16-16-May-2026\access-diff-llm-mmllm.ipynb")
text = p.read_text(encoding="utf-8")
old = '''<VSCode.Cell id="#VSC-c488f2c3" language="python">\nfrom dotenv import load_dotenv\nload_dotenv()  # loads .env from workspace root\nOPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY")\nif OPENROUTER_API_KEY:\n    print("API key found in .env file.")\n    os.environ["OPENROUTER_API_KEY"] = OPENROUTER_API_KEY\nprint("API key set successfully.")\nprint(OPENROUTER_API_KEY)\n</VSCode.Cell>'''
new = '''<VSCode.Cell id="#VSC-c488f2c3" language="python">\nimport os\nfrom dotenv import load_dotenv, find_dotenv\n\ndotenv_path = find_dotenv(usecwd=True)\nif dotenv_path:\n    load_dotenv(dotenv_path=dotenv_path, override=True)\n    print(f"Loaded .env from: {dotenv_path}")\nelse:\n    print("No .env file found.")\n\nfor key in ("OPENAI_API_KEY", "OPENROUTER_API_KEY"):\n    value = os.getenv(key)\n    if value:\n        os.environ[key] = value\n    print(f"{key} configured: {bool(value)}")\n</VSCode.Cell>'''
if old not in text:
    raise SystemExit("OLD block not found")
p.write_text(text.replace(old, new), encoding="utf-8")
print("patched")
