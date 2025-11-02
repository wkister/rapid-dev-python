# DGT0235 — Desenvolvimento Rápido de Aplicações em Python

Tema atual: Tema 4 — Python com Banco de Dados

Resumo das alterações recentes
- Harmonização do arquivo `Tema 4 - Python Com Banco de Dados/gerenciamento_livraria.py`:
  - Normalização de indentação (4 espaços), conversão de tabs para espaços.
  - Adição de docstrings de módulo, classes e funções.
  - Adição de anotações de tipo (typing) simples.
  - Tornada a inserção de dados idempotente (não duplica registros existentes).

Commit de referência (submódulo): 3cae130
Tag criada: `DGT0235-tema4`

Como usar
1. Abra o diretório deste submódulo.
2. Execute o script de exemplo (criará ou usará `livraria.db` na mesma pasta):

```bash
python3 "Tema 4 - Python Com Banco de Dados/gerenciamento_livraria.py"
```

Notas
- O banco SQLite (`livraria.db`) é criado no mesmo diretório do script.
- As inserções de exemplo são feitas apenas se as tabelas estiverem vazias.

Se quiser que eu adicione mais documentação, testes ou um pequeno script de demonstração (ex.: listar livros), diga o que prefere.
