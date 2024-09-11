sudo docker build -t ersa-app:latest .
sudo docker run -d -p 5000:5000 -v /root/backup-aws-pytho/upload/:/python-docker/upload --name ersa ersa-app:latest
