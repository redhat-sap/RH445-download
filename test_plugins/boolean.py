from __future__ import absolute_import, division, print_function

__metaclass__ = type


def boolean(value):
    """Return True if value is a Python bool (ansible-core 2.14+ compatible)."""
    return isinstance(value, bool)


class TestModule(object):
    """Jinja tests used by community.sap_launchpad, missing in ansible-core 2.12."""

    def tests(self):
        return {
            "boolean": boolean,
        }
