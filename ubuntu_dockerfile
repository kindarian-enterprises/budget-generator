FROM ubuntu:20.04

RUN apt-get update -y && \
    DEBIAN_FRONTEND=noninteractive TZ=Etc/UTC \
    apt-get install -y python3-pip python3-dev wkhtmltopdf


# We copy just the requirements.txt first to leverage Docker cache
COPY . /budget-generator

WORKDIR /budget-generator

RUN pip install -r requirements.txt

ENTRYPOINT [ "python3" ]

CMD ["wsgi.py"]
