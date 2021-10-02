FROM nginx

RUN apt update -y && apt install -y python3 python3-pip
RUN pip3 install psutil jinja2
RUN rm /etc/nginx/conf.d/default.conf
WORKDIR /opt
COPY ./nginx .
COPY ./param.conf /etc/nginx/conf.d

RUN python3 get_param.py
#CMD ["python3", "get_param.py"] #заставить ЭТО работать (не выполянется скрипт)