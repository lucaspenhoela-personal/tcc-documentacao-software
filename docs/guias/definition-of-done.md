---
titulo: Definition of Done documental
responsavel: time de engenharia
ultima_revisao: 2026-11-05
status: vigente
---

# Definition of Done documental

Uma *user story* ou tarefa só é considerada concluída quando **todos** os itens aplicáveis abaixo forem atendidos. Esta lista deve ser incorporada à *Definition of Done* do time Scrum.

## Para qualquer alteração de código

- [ ] Comentários de código atualizados onde a lógica não é autoexplicativa.
- [ ] README do serviço atualizado se mudou dependência, variável de ambiente, porta ou comando de execução.

## Para alteração de API ou contrato

- [ ] Especificação (OpenAPI/Swagger ou `api-template.md`) atualizada e versionada.
- [ ] Exemplos de requisição/resposta revisados.

## Para decisão de arquitetura

- [ ] ADR criado em `docs/adr/` com contexto, decisão e consequências.

## Para serviço novo ou alteração operacional

- [ ] Runbook criado ou atualizado (como implantar, monitorar, reverter, diagnosticar).
- [ ] Alertas e *dashboards* referenciados no runbook.

## Para encerramento da Sprint

- [ ] Nenhum item de documentação pendente foi "empurrado" para a próxima Sprint sem registro explícito no *backlog* como dívida de documentação.
