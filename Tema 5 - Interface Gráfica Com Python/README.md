# Tema 5 — Interface Gráfica com Python

> Pequenos exemplos usados no tema 5 — interfaces gráficas com Python.

Conteúdo principal:

- `01.tkinter.py` — exemplo mínimo com Tkinter.
- `04.kivy.py` — exemplo com Kivy (executar com backend gráfico disponível).
- `05.gtk.py`, `06.qt.py`, `07.wx.py` — exemplos/esboços para outros toolkits (GTK, Qt, wxWidgets).
- `exemplos_tkinter/` — exemplos adicionais com widgets Tkinter (botões, entradas, radio, etc.).
- `banco-grafico/` — integrações entre banco de dados e interfaces gráficas; contém scripts de criação/população de tabelas.
- `postgresql/` — exemplos que usam psycopg2 para PostgreSQL (quando aplicável).

Como executar

- Use Python 3.10+ (ou o interpretador do seu ambiente):

  python3 "01.tkinter.py"

- Para Kivy, instale as dependências e execute `python3 "04.kivy.py"` em um ambiente com display (X11/Wayland). Em servidores sem display, use um framebuffer virtual ou Xvfb para testes.

Notas

- Estes são exemplos de ensino: alguns requerem bibliotecas adicionais (kivy, pyqt, wxpython, psycopg2, Faker). Instale-as via pip conforme necessário.
- Este README foi adicionado automaticamente durante a operação de mesclagem/restauração para documentar o diretório restaurado e evitar exclusões acidentais.

Se quiser, eu já posso commitar este README no repositório (está preparado) e atualizar o repositório pai para apontar para o commit final do submódulo.
