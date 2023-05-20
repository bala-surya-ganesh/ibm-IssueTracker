FROM python:3.10
WORKDIR /app
ADD . /app
COPY requirments.txt /app
RUN python3 -m pip install -r requirments.txt
EXPOSE 5000
CMD ["python","app.py"]