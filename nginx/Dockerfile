FROM nginx

WORKDIR /etc/nginx

EXPOSE 80

COPY src/nginx.conf /etc/nginx/conf.d/default.conf

CMD ["nginx", "-g", "daemon off;"]