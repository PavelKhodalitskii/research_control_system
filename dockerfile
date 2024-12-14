FROM python:3.10.12

RUN apt-get update

WORKDIR /rcs_backend
COPY . /rcs_backend/

RUN pip install -r requirments.txt

ENV PYTHONUNBUFFERED=1
EXPOSE 8000

ENTRYPOINT ["tail"]
CMD ["-f","/dev/null"]