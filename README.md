# Documentação em Projetos de Software — Artefatos do TCC (IntegraTech)

Repositório de apoio ao Trabalho de Conclusão de Curso **"Documentação em Projetos de Software: análise do impacto da gestão documental na manutenibilidade de sistemas"**, do Bacharelado em Sistemas de Informação da Faculdade Impacta (2026).

Autores: Ana Caroline Alonso, Ewerton Costa, Lucas Penhoela e Vinicius Costa.
Orientador: Prof. Me. Gilberto Alves Pereira.

## O que há aqui

| Pasta | Conteúdo |
|---|---|
| `docs/modelos/` | Modelos de documentação técnica no padrão *Docs-as-Code* (README de serviço, ADR, runbook, documentação de API, guia de onboarding) |
| `docs/guias/` | Diretrizes de adoção: fluxo de revisão por pares, *Definition of Done* documental, convenções de escrita |
| `.github/workflows/` | *Pipeline* de integração contínua que valida e publica a documentação a cada *pull request* |
| `dados/` | Instrumento de coleta (questionário), distribuição das respostas por questão e perfil dos respondentes |
| `scripts/` | *Script* de análise estatística que reproduz as tabelas e gráficos da Seção 4 do trabalho |
| `mkdocs.yml` | Configuração do site de documentação (MkDocs + Material) |

## Como usar os modelos em um projeto

1. Copie a pasta `docs/`, o arquivo `mkdocs.yml` e o `.markdownlint-cli2.yaml` para a raiz do repositório do seu projeto.
2. Copie `.github/workflows/docs.yml` para habilitar a validação automática em cada *pull request*.
3. Adote o `PULL_REQUEST_TEMPLATE` para que toda alteração de código declare o impacto na documentação.
4. Publique com `mkdocs gh-deploy` ou deixe o *workflow* fazer isso ao mesclar na `main`.

## Reproduzindo a análise da pesquisa de campo

```bash
pip install -r scripts/requirements.txt
python scripts/analise.py
```

O *script* lê `dados/frequencias.csv` e reproduz a Tabela 2 (média, mediana, desvio-padrão e distribuição percentual por questão) e o Gráfico 1 da Seção 4.

## Licença

Templates e scripts: [MIT](LICENSE). Dados da pesquisa: [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/), consolidados por questão conforme descrito em `dados/README.md`.

## Como citar

Veja `CITATION.cff`.
