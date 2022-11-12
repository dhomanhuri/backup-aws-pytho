# start by pulling the python image

FROM python:3.10-slim-buster


WORKDIR /python-docker
RUN apt update -y
RUN apt install libgl1-mesa-glx -y
RUN apt-get install -y libglib2.0-0 libsm6 libxrender1 libxext6
COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt --no-cache-dir

COPY . .

CMD [ "python3", "-m" , "flask", "run", "--host=0.0.0.0"]