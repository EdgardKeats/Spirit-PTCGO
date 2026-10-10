FROM python:3.13.0-slim

WORKDIR /app

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# 🧠 Performance tweaks for tight memory containers
ENV PYTHONMALLOC=malloc

# 🛠️ Add system dependencies needed to compile packages from source
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    gcc \
    && rm -rf /var/lib/apt/lists/*

COPY requirements.txt .

RUN pip install --no-cache-dir --upgrade pip \
    && pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 8000
EXPOSE 39389

CMD ["python", "-m", "spirit.main"]
