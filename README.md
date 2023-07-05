# Webcounter Project
Simple Python Webcounter with redis server

## Requirements

- Docker account: 
- Gitlab account: 
- 
## Project tree

```
webcounter
 ┣ webcounter
 ┃ ┣ static
 ┃ ┃ ┗ main.css
 ┃ ┣ templates
 ┃ ┃ ┗ index.html
 ┃ ┣ __init__.py
 ┃ ┣ __main__.py
 ┃ ┗ redis_helper.py
 ┣ tests
 ┃ ┣ test_redis.py
 ┃ ┗ test_webcounter.py
 ┣ .gitignore
 ┣ Dockerfile
 ┣ LICENSE
 ┣ README.md
 ┣ jmeter-webcounter-tests.jmx
 ┣ k8s-webcounter-deployment.yaml
 ┣ requirements-tests.txt
 ┗ requirements.txt
```

---
## Developer tasks

### Local run

    $ python -m webcounter

### Local test
    
    $ python -m pytest tests/

### Integration tests

    docker run --name tests -it -v $PWD:/app  -w /app --rm justb4/jmeter -JURL=$(hostname -i) -n -t jmeter-webcounter-tests.jmx

### Coverage Report

    coverage run --source=webcounter -m pytest tests
    coverage report -m

### Cyclomatic complexity
    radon  cc -a -s webcounter/

### Pyinstruments benchmark

    pyinstrument webcounter/redis_helper.py

---
## Manual server operations

### Build
    docker build -t <docker-id>/webcounter:latest .

### Run Dependencies
    docker run -d  -p 6379:6379 --name redis --rm redis:alpine

### Deploy
    docker run -d --rm -p 80:5000 --name webcounter --link redis -e REDIS_URL=redis <docker-id>/webcounter:latest

---
## Cluster operations with docker

### Push to docker repository

    docker login 
    docker push <docker-id>/webcounter:latest

### Create a docker swarm cluster

    docker swarm init

### Deploy stack app 

    docker stack deploy --compose-file docker-compose.yml app

### Verify project up and running

    docker stack ps app

---
## Kubernetes operations

kubectl apply -f webcounter-deployment.yaml 
kubectl port-forward svc/webcounter-service 8080:5000

curl localhost:8080