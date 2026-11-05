---
titulo: ADR-0001 — Adotar Docs-as-Code para a documentação técnica
responsavel: time de engenharia
ultima_revisao: 2026-11-05
status: aceito
---

# ADR-0001 — Adotar Docs-as-Code para a documentação técnica

## Contexto

A documentação está fragmentada entre *wiki*, ferramentas de chat e documentos avulsos, frequentemente desatualizada em relação ao código. A pesquisa de campo que motivou este repositório indicou forte reconhecimento do valor da documentação para *onboarding* e redução de retrabalho, mas baixa priorização durante as Sprints.

## Decisão

Manter a documentação técnica em Markdown, no mesmo repositório do código, submetida ao mesmo fluxo de *pull request*, revisão por pares e integração contínua, publicada automaticamente com MkDocs.

## Alternativas consideradas

| Alternativa | Vantagens | Desvantagens | Motivo da rejeição |
|---|---|---|---|
| Wiki corporativa separada | fácil de editar | descola do código; sem revisão; sem histórico vinculado | principal causa da dessincronização observada |
| Documentos em editor de texto | familiar | sem versionamento real; difícil de buscar | não escala |

## Consequências

**Positivas:** documentação versionada junto com a mudança que a motivou; revisão obrigatória; validação automática de links e formato; histórico auditável.

**Negativas / riscos aceitos:** exige disciplina no PR; curva inicial para quem não usa Git; conteúdo voltado a usuário final pode exigir outro canal.
