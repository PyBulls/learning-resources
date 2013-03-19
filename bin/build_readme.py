#!/usr/bin/env python

import os

from jinja2 import Template
import yaml


README_TEMPLATE = Template("""

# Python Learning Resources

## Courses

{% for course in courses -%}
- {{ course.title }}
{% endfor %}

""")


def get_context():
    yaml_files = [fname for fname in os.listdir('data') if fname.endswith('.yaml')]
    context = {}
    for yaml_file in yaml_files:
        with open(os.path.join('data', yaml_file)) as f:
            context[yaml_file[:-5]] = yaml.load(f)
    return context


def main():
    print README_TEMPLATE.render(**get_context())


if __name__ == '__main__':
    main()
