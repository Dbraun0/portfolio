.PHONY: $(MAKECMDGOALS)

VERSION = latest

build: 
	docker build -t dbraun0/streamlit-portfolio:$(VERSION) -f Docker/Dockerfile Docker/