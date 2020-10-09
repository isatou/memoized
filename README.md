# memoized


## How to Setup

- pull the repo
- make a clone of the `docker-compose-vars-template.env` called `docker-compose-vars.env` and update the value
- start the docker stack, run `make up`
- apply db migrations , run `make migrate `
- setup front end, cd into memoized_frontend and run `npm install`
- build the front end, run `yarn build`
- enjoy the project at `http://localhost:8001`