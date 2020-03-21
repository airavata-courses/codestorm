FROM node:current-slim

WORKDIR /usr/src/RESTGateway
COPY package.json .
RUN npm install
RUN npm install jsonwebtoken

EXPOSE 4000
CMD [ "npm", "start" ]

COPY . .
