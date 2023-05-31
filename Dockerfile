FROM python:3.9

ADD main.py city.py .

RUN pip install requests python-dotenv

CMD ["python", "main.py"]
