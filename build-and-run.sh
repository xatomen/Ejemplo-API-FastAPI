docker build . -t example-api
docker run -d -p 8000:8000 example-api