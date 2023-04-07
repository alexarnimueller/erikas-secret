# Erikas Secret

Website für Erikas Secret Projekt mit Formular für Reservationen.

### Docker image bauen

```bash
$ docker build -t erikas-secret:latest .
```

### Docker container laufen lassen

```bash
$ docker run -d -p 80:80 --env-file .env erikas-secret
```

http://erikas.ch
