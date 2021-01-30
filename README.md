# Static FOLDER
This is where the CSS files and JavaScript Files go.
They are then able to be included in the "HTML" files through:

- `<link rel="stylesheet" href="{{ url_for('static', filename='css/site.css') }}?v=1" />`
- `<script src="{{ url_for('static', filename='js/site.js') }}?v=1"></script>`

The version numbers allow the cache to be reset when a file is edited
