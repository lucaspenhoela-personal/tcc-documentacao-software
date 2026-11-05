---
titulo: Convenções de escrita
responsavel: time de engenharia
ultima_revisao: 2026-11-05
status: vigente
---

# Convenções de escrita

- **Idioma:** português; termos técnicos consagrados em inglês (*deploy*, *rollback*, *pull request*) em itálico na primeira ocorrência.
- **Formato:** Markdown (CommonMark). Um arquivo por assunto. Nome de arquivo em `kebab-case`.
- **Cabeçalho obrigatório** em todo documento (o CI verifica):

```markdown
---
titulo: Nome do documento
responsavel: time-ou-pessoa
ultima_revisao: AAAA-MM-DD
status: rascunho | vigente | obsoleto
---
```

- **Diagramas** em Mermaid dentro do próprio Markdown, para que sejam versionados e revisados como texto.
- **Links** sempre relativos dentro de `docs/`. Links externos devem apontar para a versão/documentação oficial.
- **Segredos nunca** entram na documentação. Use `<VARIAVEL>` como marcador.
- **Documento obsoleto** não é apagado: recebe `status: obsoleto` e um aviso no topo apontando o substituto.
