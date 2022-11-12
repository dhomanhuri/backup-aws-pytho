sudo docker build -t ersa-app:latest .
sudo docker run -d -p 5000:5000 --name ersa ersa-app:latest
