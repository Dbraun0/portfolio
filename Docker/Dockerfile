ARG VERSION=latest

FROM dbraun0/streamlit:${VERSION}

RUN pip install --upgrade pip && \
    pip install --no-cache-dir streamlit-vis-timeline 

WORKDIR /app

ENTRYPOINT ["streamlit", "run", "/app/Home.py", "--server.port=8501", "--server.address=0.0.0.0"]