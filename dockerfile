# Usa imagem oficial do Python
FROM python:3.13-slim

# Define diretório de trabalho no container
WORKDIR /app

# Copia requirements e instala dependências
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copia todo o código para dentro do container
COPY . .

# Expõe a porta (Railway precisa disso)
EXPOSE 8080

# Comando para rodar a aplicação
CMD ["python", "teste.py"]