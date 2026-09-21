from __future__ import absolute_import, division, print_function

__metaclass__ = type


def boolean(value):
    """Return True if value is a Python bool (ansible-core >= 2.16)."""
    return isinstance(value, bool)


def is_true(value):
    """Return True only for the Python singleton True (ansible-core >= 2.16)."""
    return value is True


def is_false(value):
    """Return True only for the Python singleton False (ansible-core >= 2.16)."""
    return value is False


def integer(value):
    """Return True if value is an int, excluding bool (ansible-core >= 2.16)."""
    return isinstance(value, int) and not isinstance(value, bool)


def is_float(value):
    """Return True if value is a float (ansible-core >= 2.16)."""
    return isinstance(value, float)


class TestModule(object):
    """Jinja tests used by community.sap_launchpad, missing in ansible-core 2.12."""

    def tests(self):
        return {
            "boolean": boolean,
            "true": is_true,
            "false": is_false,
            "integer": integer,
            "float": is_float,
        }
