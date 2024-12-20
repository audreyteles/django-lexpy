# Django Lexpy - v0.1.2-beta


![PyPI](https://img.shields.io/pypi/v/django-lexpy?color=blue&style=flat-square)
![PyPI - Downloads](https://img.shields.io/pypi/dm/django-lexpy?color=blue&style=flat-square)

[![Published on Django Packages](https://img.shields.io/badge/Published%20on-Django%20Packages-0c3c26)](https://djangopackages.org/packages/p/django-lexpy/)

This is a package that helps you organize your texts in several languages in a simple way.

## Install


```bash
pip install django-lexpy
```

## Configure


### settings.py

```python
INSTALLED_APPS = [
    'django_lexpy'
]
```
Check that the desired language is correct:
```python
LANGUAGE_CODE = 'en-us'
```

Run your project:
```bash
python manage.py runserver
```

---
So a folder with your desired language was created:
```bash
lang
└── en_us
    ├── __init__.py
    └── main.py
```

The `main.py` looks like:

```python
messages = {
    "message.test": "This is a test message.",
}
```

## Load lexpy


Load lexpy in your template and use the tag:
```html
{% load lexpy %}
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Title</title>
</head>
<body>
{% lexpy 'message.test' %}
</body>
</html>
```

The tag consists of the prefix “message.” followed by the short key of the message that has been defined in your message file:

```python
{% lexpy 'message.welcome' %}
```

## Organazing


you no longer have to go through your entire project to find your “messages”/texts, centralize them in one place:

```python
# yourproject/lang/en_us/main.py

messages = {
    "message.test": "This is a test message.",
    "message.welcome": "Welcome to my website.",
    "message.help": "Do you need some help?",
}
```

## Internationalization and localization


In addition to organizing your texts, you can simplify the translations without 'strings as keys' in `.po` file:
```python
# path/to/python/file.py:123
msgid "Welcome to my site."
msgstr "Bem-vindo ao meu site"
```

Now you have short keys:
```python
# yourproject/lang/en_us/main.py

messages = {
    "message.test": "This is a test message.",
    "message.welcome": "Welcome to my website.",
}
```
---
Another language:

```python
# yourproject/lang/pt_BR/main.py

messages = {
    "message.test": "Isso é uma mensagem de teste.",
    "message.welcome": "Bem-vindo ao meu site.",
}
```

## Replacing Fields in Messages

You can also define fields in your message and replace them with dynamic values.

```python
# yourproject/lang/en_us/main.py
messages = {
    "message.welcome": "Hi {name}, welcome to my website.",
}
```
 And in your template you can:

```html
{% load lexpy %}
...
{% lexpy 'message.welcome' name="Foobar" %}
...
```

Then you can see it on your website:
```
Hi Foobar, welcome to my website.
```


> **Unnamed fields are also supported**
> 
> ```python
> #yourproject/lang/en_us/main.py
> messages = {
>    "message.welcome": "Hi {}, welcome to my website.",
> }
> ```
> ```html
> {% load lexpy %}
> ...
> {% lexpy 'message.welcome' "Foobar" %}
> ...
> ```


