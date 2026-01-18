FROM python:3.12-slim

# Prevent Python from buffering stdout (useful for logs)
ENV PYTHONUNBUFFERED=1

WORKDIR /app

# System dependencies for:
# - cv2 (libgl1, libglib)
# - tkinter (tk)
# - matplotlib backends
RUN apt-get update && apt-get install -y \
    libgl1 \
    libglib2.0-0 \
    tk \
    && rm -rf /var/lib/apt/lists/*

# Install Python dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy project files
COPY . .

# Run the GUI
CMD ["python", "src/main.py"]
