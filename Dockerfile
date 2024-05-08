FROM surnet/alpine-python-wkhtmltopdf:3.7.3-0.12.5-small

RUN apk add --update --no-cache gcc alpine-sdk linux-headers

RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app

COPY ./app .
COPY app.ini .
RUN pip3 install -r requirements.txt
RUN pip3 install uwsgi

RUN echo -e "uwsgi\nuwsgi" | adduser uwsgi

EXPOSE 45380
CMD ["uwsgi", "--ini", "app.ini"]
