# django-compressor-js

Instead of running an extra node.js process watching for changes in your Javascript, this precompiler for `django-compressor` will convert any ES6 code into ES5 automagically.

# Install
1. `pip install django-compressor-js`
2. Add precompiler (`text/es6` can be anything, but it has to match the script type in the template)
```
COMPRESS_PRECOMPILERS = (
    ("text/es6", "django_compressor_js.precompilers.BabelCompiler"),
)
```
3. Add to HTML template
```
{% compress js %}
	<script src="{% static 'js/test-es6-code.js' %}" type="text/es6"></script>
{% endcompress %}
```

# Cache compiled files
To prevent the compressor from precomiling your JavaScript on every request, you can use the [COMPRESS_CACHEABLE_PRECOMPILERS](https://django-compressor.readthedocs.io/en/stable/settings/#django.conf.settings.COMPRESS_CACHEABLE_PRECOMPILERS) settings in development:
```python
CACHES["compressor"] = {
    "BACKEND": "django.core.cache.backends.locmem.LocMemCache",
    "LOCATION": "unique-snowflake",
}
COMPRESS_CACHEABLE_PRECOMPILERS = ("text/es6",)
COMPRESS_CACHE_BACKEND = "compressor"
```
If you change the content of the file it will get re-compiled, but otherwise it will skip it.

# Caveats
Most ES6 syntax seems to work pretty well, but requiring modules doesn't import correctly. Also, this approach adds some latency when compressing on the fly (i.e. `COMPRESS_OFFLINE = False`).

# Run tests
`poetry run pytest`

# Credits
- [duktape](https://github.com/svaarala/duktape/)
- [dukpy](https://github.com/amol-/dukpy)
- [django-compressor](https://pypi.org/project/django-compressor/)
