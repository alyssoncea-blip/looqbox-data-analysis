# Looqbox Data Challenge - Entrega Parcial (Etapas 1 e 2)

## Contexto

Esta entrega cobre as duas primeiras etapas do plano:

1. Introducao tecnica do desafio
2. Consultas SQL para responder perguntas estrategicas de negocio

O banco utilizado e o MySQL `looqbox-challenge`, contendo dados de produtos, vendas e cadastro de lojas.

## Objetivo tecnico desta etapa

- Garantir consultas SQL claras, auditaveis e reutilizaveis
- Adotar padrao de projeto real com:
  - separacao por arquivo/objetivo
  - schema qualificado
  - alias padronizados
  - ordenacao deterministica
- Permitir execucao independente de cada consulta por times de dados/analytics

## Escopo das consultas

As consultas desta etapa respondem:

1. Quais sao os 10 produtos mais caros
2. Quais secoes pertencem aos departamentos BEBIDAS e PADARIA
3. Qual foi o total de vendas (em $) por Area de Negocio no primeiro trimestre de 2019

Os scripts SQL estao em `sql/part1/`.
