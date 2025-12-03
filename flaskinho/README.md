## Flask: using your basic resources

```sh
> Rodar Servidor
- make run

> Início Rápido
- poetry init -n (ou poetry new .)
- poetry add flask markupsafe flask-sqlalchemy

> Problemas com a Venv?
- poetry env remove python
- poetry install
- source venv/bin/activate
- crítico: rm -rf ./* (apaga tudo)

> Informações Importantes
- markupsafe.escape → impede a alteração de parâmetros pela URL e previne ataques.
- render_template → usa o Jinja2 para renderizar arquivos .html dentro da pasta templates.
- Para adicionar imagens, crie uma pasta static/

> Filtros Jinja2
- Documentação: https://tedboy.github.io/jinja2/templ14.html

> Depuração:
- caso tenha problemas com o banco de dados:
    - 1. apague qualquer arquivo remanescente
    - 2. abra o interpretador python no terminal
    - 3. digite: from main import app, db
                 with app.app_context():
                 db.create_all()
- lembre de colocar os arquivos(.html) dentro da pasta templates para funcionar e estéticos(.png, .css) em static
- crie a pasta instance para ficar o arquivo do bd
```