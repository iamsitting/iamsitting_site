FROM node

WORKDIR /app/frontend
COPY libraries /app/frontend/libraries
COPY webpack /app/frontend/webpack
COPY package.json /app/frontend/package.json
RUN npm install

EXPOSE 3000
CMD ["/usr/local/bin/node", "webpack/server.js"]

