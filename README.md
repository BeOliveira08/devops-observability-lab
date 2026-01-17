# Monitoring App – Observability & DevOps Lab

Este projeto demonstra práticas modernas de **DevOps**, **Observabilidade** e **Engenharia de Software** usando uma aplicação Flask instrumentada.

## 🎯 Objetivo

Demonstrar:
- Observabilidade com Prometheus e Grafana
- Containerização com Docker e Docker Compose
- Automação com Makefile
- CI/CD com GitHub Actions
- Boas práticas de código, testes e segurança

## 🧱 Arquitetura

```mermaid
graph TD
    User --> FlaskApp
    FlaskApp --> Prometheus
    Prometheus --> Grafana
