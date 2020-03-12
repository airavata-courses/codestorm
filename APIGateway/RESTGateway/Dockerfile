FROM node:current-slim

WORKDIR /usr/src/RESTGateway
COPY package.json .
RUN npm install

EXPOSE 4000
CMD [ "npm", "start" ]

COPY . .