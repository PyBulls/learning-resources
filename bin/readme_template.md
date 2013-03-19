
# Python Learning Resources

A collection of resources for learning the Python programming language!

## General Resources

{% for resource in general_resources -%}
- [{{ resource.title }}]({{ resource.url }})
{% endfor %}

## Courses

{% for course in courses -%}

- {% if 'url' in course -%}
    [{{ course.title }}]({{ course.url }})
{% else -%}
    {{ course.title }}
{%- endif %}
{%- for key, value in course.items() -%}
    {%- if key not in ['title', 'url'] %}
        {{ key }}: {{ value }}
    {%- endif -%}
{%- endfor %}

{% endfor %}

## Texts

{% for text in texts -%}

- {% if 'url' in text -%}
    [{{ text.title }}]({{ text.url }})
{% else -%}
    {{ text.title }}
{%- endif %}
{%- for key, value in text.items() -%}
    {%- if key not in ['title', 'url'] %}
        {{ key }}: {{ value }}
    {%- endif -%}
{%- endfor %}

{% endfor %}
