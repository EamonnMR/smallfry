# smallfry
Very small, exceedingly opinionated static site generator.

Specific opinions:

Your site has only have one page.

You don't want to have to repeat elements; you instead want to use loops.

You like Jinja2

You like Yaml

Install requirements with:

`pip install -r requirements.txt`

Use it like this:

`cat index.j2.html | python smallfry.py config.yml > index.html`

It's just binding a jinja2 template to whatever you stick.in that config file. See the [jinja2 documentation](https://jinja.palletsprojects.com/en/3.1.x/) for how to use jinja2. 
