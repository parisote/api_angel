# API PROYECTO ANGEL

FastAPI + GraphQL

## Instalacion

```bash
pip install -r requirements.txt
```

## Configuracion de env

Crear file .env en el root del proyecto con la variable BASE para la conexion de [sqlalchemy](https://pypi.org/project/SQLAlchemy/)

```bash
BASE=mysql+pymysql://user:password@host:port/db
```

## Generar model

Generar model de sqlalchemy con [sqlacodegen](https://pypi.org/project/sqlacodegen/)

```bash
sqlacodegen mysql+pymysql://user:password@host:port/db --outfile models.py
```

Ese file pegarlo dentro de src/models.

## Licencia
[MIT](https://github.com/parisote/api_angel/blob/develop/LICENSE.md)
