# Flask

📌 **Install Flask**

`pip install Flask`


> **Create a folder with any name.**
> 

📌 **Step 1:**
**Inside the folder create a file `app.py`. Insert the following code.**

```python
from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=True)
```

📌 **Step 2**:
**Create a `templates` folder inside `root` folder. Inside the `templates` folder create `base.html` file. Now, insert the following code.**

```python
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>
        {% block head %} {% endblock %}
    </title>
</head>
<body>
    {% block body %} {% endblock %}
</body>
</html>
```

📌 **Step 3:**

**Inside the `templates` folder create `index.html` file. Now, insert the following code.**

```python
{% extends "base.html" %}

{% block head %}
    MYTE: Flask Introduction
{% endblock %}

{% block body %}
    Hello, from the index page..!
{% endblock %}
```


📌 **Step 4:**
**Run The Application.**

```powershell
python app.py
```