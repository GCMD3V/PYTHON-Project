FROM python:3.11

# Instala pacotes do sistema necessários para bibliotecas como OpenCV, PyQt5, TTS etc
RUN apt-get update && apt-get install -y \
    ffmpeg \
    espeak \
    libglib2.0-0 \
    libsm6 \
    libxext6 \
    libxrender-dev \
    libpulse-dev \
    libasound2 \
    && apt-get clean

# Cria diretório de trabalho
WORKDIR /app

# Copia arquivos do projeto
COPY requirements.txt .

# Instala dependências do Python
RUN pip install --upgrade pip && \
    pip install -r requirements.txt

# Copia o projeto para o contêiner
# O diretório /app/app deve conter o arquivo main.py e outros arquivos do projeto
COPY ./app /app/app

# Comando para iniciar o servidor FastAPI
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
