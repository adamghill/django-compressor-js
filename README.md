# django-compressor-js

Instead of running an extra node.js process watching for changes in your Javascript, this precompiler for `django-compressor` will convert any ES6 code into ES5 automagically.

# Install
1. `pip install django-compressor-js`
1. Add precompiler (`text/es6` can be anything, but it has to match the script type in the template)
```
COMPRESS_PRECOMPILERS = (
    ("text/es6", "django_compressor_js.precompilers.BabelCompiler"),
)
```
1. Add to HTML template
```
{% compress js %}
	<script src="{% static 'js/test-es6-code.js' %}" type="text/es6"></script>
{% endcompress %}
```

# Caveats
Most ES6 syntax seems to work pretty well, but requiring modules doesn't import correctly. Also, this approach adds some latency when compressing on the fly (i.e. `COMPRESS_OFFLINE = False`).

# Run tests
`poetry run pytest`

# Credits
`dukpy` and `django-compressor` for doing all the hard things.
