import sys

import jinja2
import yaml

def generate_html(template: str, config: str) -> str:
    cfg = yaml.load(open(config), Loader=yaml.Loader)
    return jinja2.Environment().from_string(template).render(cfg)
    

if __name__ == "__main__":
    print(generate_html(
        sys.stdin.read(),
        sys.argv[1]
    ))
