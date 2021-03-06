"""Index view"""

from orion import encode

class IndexResource(object):
    """Controller for index resource"""

    def on_get(self, req, res):
        """Handle GET method"""
        result = {
            'status': 0,
            'msg': 'Hello'
        }
        res.body = encode.encode(result)
