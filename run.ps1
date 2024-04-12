docker run --rm -it `
    --name docker_portfolio `
    -p 8501:8501 `
    -v .:/app `
    dbraun0/streamlit-portfolio:latest