
# Python Learning Resources

## Courses

{% for course in courses -%}
- {{ course.title }} {% if 'url' in course -%} [link]({{ course.url }}) {%- endif %}
    {% for key, value in course.items() -%}
        {%- if key not in ['title', 'url'] %}
            {{ key }}: {{ value }}
        {%- endif -%}
    {%- endfor %}

{% endfor %}
