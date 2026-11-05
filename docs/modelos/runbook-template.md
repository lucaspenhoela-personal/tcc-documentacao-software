---
titulo: Runbook — <Nome do serviço>
responsavel: <time>
ultima_revisao: AAAA-MM-DD
status: vigente
---

# Runbook — <Nome do serviço>

## Contexto rápido

- O que o serviço faz: <uma frase>
- Impacto se cair: <quem é afetado e como>
- Dependências críticas: <lista>

## Verificação de saúde

```bash
curl -s https://<host>/health
```

Dashboard: <link> — Alertas: <link>

## Procedimentos

### Implantar nova versão

1.
2.

### Reverter (rollback)

1.
2.

### Reiniciar

1.

## Diagnóstico de incidentes

| Sintoma | Causa provável | Ação |
|---|---|---|
| Erro 5xx em massa | | |
| Fila acumulando | | |
| Latência alta | | |

## Acionamento

- Plantão: <como contatar>
- Escalonamento: <próximo nível>

## Histórico de incidentes

| Data | Resumo | Post-mortem |
|---|---|---|
| | | |
