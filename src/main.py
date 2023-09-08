import uvicorn
from fastapi import FastAPI
from prometheus_fastapi_instrumentator import Instrumentator

from src.core.events.infra.logging.customlogging import logging_config

app = FastAPI()
instrumentator = Instrumentator().instrument(app).expose(app)


@app.get('/')
def index():
    return {'message': 'Hello World!'}


if __name__ == '__main__':
    try:
        uvicorn.run(app, host='0.0.0.0', port=8000, log_config=logging_config)
        print('server running...')
    except Exception as e:
        print(f'Error: {e}')


# import uvicorn
# from sqlalchemy import create_engine
# from fastapi import FastAPI
# from prometheus_client import multiprocess
# from prometheus_client import make_asgi_app, CollectorRegistry, Counter
# from prometheus_fastapi_instrumentator import Instrumentator

# from src.core.events.domain.entities.partner import Partner
# from src.core.events.domain.entities.customer import Customer
# from src.core.events.infra.database.repositories.repositories import (
#     PartinerSqlAlchemyRepository,
#     CustomerSqlAlchemyRepository
# )

# from src.core.events.infra.logging.customlogging import logging_config

# from src.settings import Settings

# engine = create_engine(Settings().DATABASE_URL)
# # logger = configure_logger(__name__)

# app = FastAPI()

# instrumentator = Instrumentator().instrument(app)

# # couter_requests = Counter('requests_total', 'Total number of requests')

# # @app.get('/metrics')
# # def make_metrics_app():
# #     couter_requests.inc()
# #     registry = CollectorRegistry()
# #     multiprocess.MultiProcessCollector(registry)
# #     return make_asgi_app(registry=registry)


# # metrics_app = make_metrics_app()
# # app.mount("/metrics", metrics_app)

# @app.on_event("startup")
# async def _startup():
#     instrumentator.expose(app)

# @app.get('/')
# def index():
#     # logs = configure_logger("Página raiz acessada")
#     # print('\n')
#     # print('#############################')
#     # print(logs)
#     # print('#############################')
#     # print('\n')
#     # couter_requests.inc()
#     return {'message': 'Hello World!'}

# if __name__ == '__main__':
#     try:
#         # #############################################################################
#         # repository = PartinerSqlAlchemyRepository()
#         # partner_entity = Partner(name='Partner 97')
#         # partner = repository.add(partner_entity)
#         # # partner = repository.find_by_id('827f1d4e-e194-474b-9801-3018bf42d2c1')
#         # # partner = repository.find_all()
#         # # partner = repository.delete('827f1d4e-e194-474b-9801-3018bf42d2c1')
#         # print(partner)

#         # #############################################################################
#         # customer_repository = CustomerSqlAlchemyRepository()
#         # customer_entity = Customer(cpf='12345678901', name='Customer 97')
#         # customer = customer_repository.find_all()
#         # customer = customer_repository.find_by_id('f533a7ea-e574-4322-9990-ce6d88698dc5')
#         # customer = customer_repository.delete('f533a7ea-e574-4322-9990-ce6d88698dc5')
#         # print(customer)
#         # index()
#         uvicorn.run(app, host="0.0.0.0", port=8000, log_config=logging_config)
#     except Exception as e:
#         print(f'Error: {e}')
