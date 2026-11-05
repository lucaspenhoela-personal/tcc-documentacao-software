---
titulo: Fluxo de revisão por pares da documentação
responsavel: time de engenharia
ultima_revisao: 2026-11-05
status: vigente
---

# Fluxo de revisão por pares da documentação

A documentação segue o mesmo ciclo de vida do código:

```text
branch → alteração em docs/ → pull request → CI valida → revisão por par → merge → publicação
```

## Regras

1. **Mesmo PR.** Alterações de comportamento, interface, configuração ou infraestrutura devem incluir a atualização da documentação correspondente no mesmo *pull request*. O template de PR obriga o autor a declarar isso.
2. **Revisor diferente do autor.** Pelo menos uma aprovação de outra pessoa da equipe. Para ADRs, a aprovação deve vir de alguém com responsabilidade técnica sobre o componente afetado.
3. **O CI é bloqueante.** Links quebrados, Markdown fora do padrão ou *build* do site com falha impedem o *merge*.
4. **Revisão leve, frequente.** Prefira PRs pequenos de documentação a grandes revisões trimestrais. Um ajuste de três linhas feito no dia da mudança vale mais que um manual reescrito seis meses depois.

## O que o revisor verifica

- [ ] O texto reflete o comportamento atual do código (não o planejado).
- [ ] Um desenvolvedor novo conseguiria seguir as instruções sem perguntar a ninguém.
- [ ] Termos, nomes de serviços e variáveis conferem com o código.
- [ ] Não há informação sensível (segredos, dados pessoais, IPs internos).
- [ ] A data de `ultima_revisao` foi atualizada.
