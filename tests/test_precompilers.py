import pytest
from django.conf import settings


@pytest.fixture
def django_settings():
    settings.configure()
    settings.STATIC_ROOT = "/statics"
    settings.STATIC_URL = "/static/"


def test_babel_compiler(django_settings):
    # import here to make sure that Django settings have been configured
    from django_compressor_js.precompilers import BabelCompiler

    babel_compiler = BabelCompiler(
        """const myFunc = name => {
    return `Hello ${name}`;
}"""
    )
    transpiled_code = babel_compiler.input()

    assert transpiled_code
    assert (
        transpiled_code
        == """"use strict";

var myFunc = function myFunc(name) {
    return "Hello " + name;
};"""
    )
