FROM python:3.12

WORKDIR /app
COPY . .

RUN pip install -r requirements.txt
RUN reflex export --frontend-only --no-zip

CMD ["reflex", "run", "--env", "prod", "--backend-only", "--loglevel", "debug"]
