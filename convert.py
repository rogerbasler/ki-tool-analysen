
import markdown

with open('wochenanalyse-kw01-2026.md', 'r') as f:
    text = f.read()

html = markdown.markdown(text, extensions=['tables'])

with open('index.html', 'w') as f:
    f.write('''
<!DOCTYPE html>
<html>
<head>
<title>Wöchentliche KI-Tool-Analyse KW 01/2026</title>
<link rel="stylesheet" href="style.css">
</head>
<body>
<div class="container">
''')
    f.write(html)
    f.write('''
</div>
</body>
</html>
''')
