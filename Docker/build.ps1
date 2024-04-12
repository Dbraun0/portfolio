param (
    [string]$version = "latest"
)

docker build --progress=plain -t dbraun0/streamlit-portfolio:${version} -f Docker/Dockerfile Docker/