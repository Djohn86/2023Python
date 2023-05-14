from jinja2 import Template

# 1

# menu = [
#     {'link': '/index', 'sel': 'Главная'},
#     {'link': '/news', 'sel': 'Новости'},
#     {'link': '/about', 'sel': 'О компании'},
#     {'link': '/shop', 'sel': 'Магазин'},
#     {'link': '/contacts', 'sel': 'Контакты'}
# ]
#
# body = """<ul>
# {% for i in menu -%}
#     {% if  i.link == '/index' -%}
#         <li><a href = "{{ i.link }}" class = "active">{{ i.sel }}</a></li>
#     {%- else -%}
#         <li><a href = "{{ i.link }}">{{ i.sel }}</a></li>
#     {%- endif %}
# {% endfor -%}
# </ul>"""
#
# tm = Template(body)
# msg = tm.render(menu=menu)
#
# print(msg)


# 2

html = """
{%- macro body(x, type = '', name = '', placeholder = '') -%}
    <input type = "{{ type }}" name = "{{ name }}" placeholder = "{{ placeholder }}">
{%- endmacro %}

<p>{{ body('a1', type = 'text', name = 'firstname', placeholder = 'Имя') }}</p>
<p>{{ body('a2', type = 'text', name = 'lastname', placeholder = 'Фамилия') }}</p>
<p>{{ body('a3', type = 'text', name = 'address', placeholder = 'Адрес') }}</p>
<p>{{ body('a4', type = 'tel', name = 'phone', placeholder = 'Телефон') }}</p>
<p>{{ body('a5', type = 'email', name = 'email', placeholder = 'Почта') }}</p>
"""

tm = Template(html)
msg = tm.render()

print(msg)
