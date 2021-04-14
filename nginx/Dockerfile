#FROM nginx
##RUN apt-get install openssl
##RUN mkdir /etc/openssl
##RUN openssl req -x509 -nodes -newkey rsa:2048 -days 365 -keyout  /etc/openssl/mykey.key -out /etc/openssl/cert.crt -subj /C=UA/ST=KH/L=[]/O=./CN=localhost
#RUN rm /etc/nginx/conf.d/default.conf
#COPY conf/nginx.conf /etc/nginx/conf.d
#COPY /static /static

FROM ubuntu:18.04
RUN apt-get update -y
RUN apt-get install software-properties-common -y
RUN add-apt-repository ppa:nginx/stable -y
RUN apt-get update -y
RUN apt-get install nginx -y
RUN add-apt-repository ppa:certbot/certbot
RUN apt-get update -y
RUN apt-get install certbot python-certbot-nginx -y
RUN echo "\ndaemon off;" >> /etc/nginx/nginx.conf
RUN chown -R www-data:www-data /var/lib/nginx

EXPOSE 80 443

ARG DOMAIN=localhost
ARG EMAIL=example@gmail.com

COPY docker-entrypoint.sh /etc/nginx
RUN chmod +x /etc/nginx/docker-entrypoint.sh

#RUN certbot certonly --webroot --webroot-path=/var/www/html --email ${EMAIL} --agree-tos \
#    --no-eff-email -d ${DOMAIN} -d www.${DOMAIN}

#COPY ../front /etc/nginx/front
WORKDIR /etc/nginx
#ADD conf/nginx.conf /sites-available/${DOMAIN}
#RUN ln -s /sites-available/${DOMAIN} /sites-enabled/${DOMAIN}
#COPY conf/nginx.conf /conf.d

VOLUME ["/etc/letsencrypt"]
ENTRYPOINT ["/etc/nginx/docker-entrypoint.sh"]