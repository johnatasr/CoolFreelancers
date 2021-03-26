# Coolfrela

Plataforma de busca de freelancers via Rest.

## Requisitos

* Docker
* Python 3.7 >

## Iniciando

Passos para configurar o projeto com docker:

1. `cd` na pasta do projeto
2. `docker-compose up --build`

Caso não deseje o uso de docker:
1. `Inicie um virtual env`
2. `python manage.py runserver`

O projeto por padrão estará em localhost:8000 pelo enpoint http://localhost:8000/freelancers/send-freelance

## Como usar

```
curl --request POST \
  --url http://localhost:8000/freelancers/send-freelance \
  --header 'Content-Type: application/json' \
  --data '{
  "freelance": {
    "id": 42,
    "user": {
      "firstName": "Hunter",
      "lastName": "Moore",
      "jobTitle": "Fullstack JS Developer"
    },
    "status": "new",
    "retribution": 650,
    "availabilityDate": "2018-06-13T00:00:00+01:00",
    "professionalExperiences": [
      {
        "id": 4,
        "companyName": "Okuneva, Kerluke and Strosin",
        "startDate": "2016-01-01T00:00:00+01:00",
        "endDate": "2018-05-01T00:00:00+01:00",
        "skills": [
          {
            "id": 241,
            "name": "React"
          },
          {
            "id": 270,
            "name": "Node.js"
          },
          {
            "id": 370,
            "name": "Javascript"
          }
        ]
      },
      {
        "id": 54,
        "companyName": "Hayes - Veum",
        "startDate": "2014-01-01T00:00:00+01:00",
        "endDate": "2016-09-01T00:00:00+01:00",
        "skills": [
          {
            "id": 470,
            "name": "MySQL"
          },
          {
            "id": 400,
            "name": "Java"
          },
          {
            "id": 370,
            "name": "Javascript"
          }
        ]
      },
      {
        "id": 80,
        "companyName": "Harber, Kirlin and Thompson",
        "startDate": "2013-05-01T00:00:00+01:00",
        "endDate": "2014-07-01T00:00:00+01:00",
        "skills": [
          {
            "id": 370,
            "name": "Javascript"
          },
          {
            "id": 400,
            "name": "Java"
          }
        ]
      }
    ]
  }
}'
```

- Envie o cURL acima por uma requisição POST 
- O retorno virá da seguinte forma: 

```
{
  "freelance": {
    "id": 42,
    "computedSkills": [
      {
        "id": 241,
        "name": "React",
        "durationInMonths": 28
      },
      {
        "id": 270,
        "name": "Node.js",
        "durationInMonths": 28
      },
      {
        "id": 370,
        "name": "Javascript",
        "durationInMonths": 60
      },
      {
        "id": 400,
        "name": "Java",
        "durationInMonths": 40
      },
      {
        "id": 470,
        "name": "MySQL",
        "durationInMonths": 32
      }
    ]
  }
}

```

