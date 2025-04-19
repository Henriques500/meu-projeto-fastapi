from fastapi import FastAPI, Request
import subprocess

app = FastAPI()

@app.post("/generate")
async def generate(request: Request):
    data = await request.json()  # Recebe parâmetros JSON
    script_path = "./blender_generate.py"  # Caminho do script que será executado

    # Prepara os argumentos
    args = " ".join([f"--{key} {value}" for key, value in data.items()])

    # Executa o Blender com o script
    command = f"blender --background --python {script_path} -- {args}"
    process = subprocess.run(command, shell=True, capture_output=True)

    # Retorna a resposta
    if process.returncode == 0:
        return {"status": "success", "output": process.stdout.decode()}
    else:
        return {"status": "error", "output": process.stderr.decode()}
