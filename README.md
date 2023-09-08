
# documentação/projeto em desenvolvimento...
# Projeto de Vendas de Ingresso

O projeto é voltado para estudo e simula um sistema de vendas de ingressos. Nele, um cliente pode comprar e pagar por ingressos para eventos, garantindo seu assento no respectivo evento.

## Declaração da Visão do Domínio

- O modelo deve permitir que **clientes comprem ingressos** de eventos utilizando **apenas cartão de crédito**.
- Deve-se garantir que **não haja conflitos** de lugares.
- A **validação do ingresso** no evento deve ser rápida e sempre disponível.
- **Parceiros** devem ter a capacidade de criar eventos e determinar lugares.
- Pagamentos realizados pelos clientes devem ser devidamente representados entre o parceiro e a organização do evento.
- O modelo deve considerar as diferentes visões de usuários, incluindo **administradores**, **parceiros** e **clientes**.
- Deve ser possível a pesquisa de eventos e o registro de compras feitas pelos clientes. Além disso, o parceiro deve ser capaz de gerenciar seus eventos, atualizar informações e gerenciar os assentos disponíveis.

## Entidades e Agregados

- **Customer**: Representa o cliente que deseja adquirir ingressos para um evento.
- **Event**: Detalha o evento para o qual os ingressos são vendidos.
- **Event_Section**: Define diferentes seções dentro de um evento (por exemplo, áreas VIP, áreas normais).
- **Event_Spot**: Indica um lugar ou assento específico dentro de uma seção do evento.
- **Partner**: Representa entidades ou indivíduos que organizam e disponibilizam eventos.

## Design e Implementação

O projeto é fundamentado no **Domain-Driven Design (DDD)**, garantindo uma clara separação e definição das entidades e agregados.

## Bibliotecas e Ferramentas

- **Python**: Versão 3.11.
- **Frameworks e Bibliotecas**:
  - fastapi
  - sqlalchemy
  - alembic
  - pydantic-settings
  - pytest
  - pytest-cov
  - python-json-logger
  - taskipy
  - blue
  - ruff
  - isort
- **Observabilidade**:
  - prometheus-client


## Bibliotecas e Ferramentas
- **Métricas**:
  - **Prometheus**: Biblioteca para coleta de métricas.
  - **Grafana**: Ferramenta para visualização de métricas.
- **Tracing**:
- **Logs**:


## Manutenção e Suporte
Este projeto consiste apenas em estudo e NÃO possui manutenção e suporte.

## Contribuição
Este projeto consiste apenas em estudo e NÃO aceita contribuições.

## Licença
Este projeto consiste apenas em estudo e NÃO possui licença.
