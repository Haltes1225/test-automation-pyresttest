# How to run:

```
docker-compose up -d

docker-compose down -v --remove-orphans ; docker-compose up -d --build ; docker-compose logs -f
```

# How to test:

```
docker-compose run --rm backend ./tests.sh
```