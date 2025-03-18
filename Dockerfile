FROM python:3.9-slim
WORKDIR /app
COPY ip-tool.py .
RUN apt-get update && apt-get install -y iproute2
RUN chmod +x ip-tool.py
CMD ["python3", "ip-tool.py", "--report"]
