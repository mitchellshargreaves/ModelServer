FROM tiangolo/uwsgi-nginx-flask:python3.6-alpine3.7
RUN apk update
RUN apk add bash nano make automake gcc g++ subversion python3-dev
ENV STATIC_URL /static
ENV STATIC_PATH /var/www/app/static
COPY ./requirements.txt /var/www/requirements.txt
RUN pip install -f https://download.pytorch.org/whl/torch_stable.html -r /var/www/requirements.txt