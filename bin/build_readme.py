#!/usr/bin/env python

import os

from jinja2 import Template
import yaml


README_TEMPLATE = 'readme_template.md'
SCRIPT_DIR = os.path.dirname(__file__)
DATA_DIR = os.path.join(SCRIPT_DIR, '../data')


def get_context():
    yaml_files = [fn for fn in os.listdir(DATA_DIR) if fn.endswith('.yaml')]
    context = {}
    for yaml_file in yaml_files:
        with open(os.path.join(DATA_DIR, yaml_file)) as f:
            context[yaml_file[:-5]] = yaml.load(f)
    return context


def main(template_file=README_TEMPLATE):
    with open(os.path.join(SCRIPT_DIR, template_file)) as f:
        template = Template(f.read())
    print (template.render(**get_context()))


if __name__ == '__main__':
    main()
