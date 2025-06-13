# blog-microservico
```
blog_project/
├── app/
│   ├── models/           # ORM models (User, Post, Comment)
│   ├── schemas/          # Pydantic models (input/output)
│   ├── routes/           # Endpoints separados por entidade
│   ├── services/         # Lógica de negócio
│   ├── core/             # Configs, segurança etc.
│   └── main.py           # Entry point com FastAPI
├── tests/
├── requirements.txt
├── .env
└── README.md
```
