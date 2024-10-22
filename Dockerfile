FROM python:3.9-slim-buster

WORKDIR /

COPY requirements.txt requirements.txt
CMD ["python", "-m" , "pip" , " install"," -i","https://mirrors.tuna.tsinghua.edu.cn/pypi/web/simple"," --upgrade pip"]
RUN pip3 install -r requirements.txt

COPY . .

EXPOSE 8000
LABEL authors="DawnDream"

CMD ["python3", "main.py"]