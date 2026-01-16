<!DOCTYPE html>
<html lang="el">
<head>
    <meta charset="UTF-8">
    <title>Login</title>
    <link rel="stylesheet" href="{{ url_for('static', filename='style.css') }}">
</head>
<body>

<div class="container">
    <h1>Welcome ✨</h1>

    <form method="POST">
        <input type="text" name="user" placeholder="Username" required>
        <button type="submit">Enter</button>
    </form>

    {% if msg %}
        <div class="message {{ 'success' if 'Καλώς' in msg or 'Καλημέρα' in msg else 'error' }}">
            {{ msg }}
        </div>
    {% endif %}
</div>

</body>
</html>
