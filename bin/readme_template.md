
# Python Learning Resources

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
