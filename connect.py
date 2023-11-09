import psycopg2
import jinja2

# Connect to the database
conn = psycopg2.connect(database="mydatabase", user="myuser", password="mypassword", host="localhost", port=5432)
cursor = conn.cursor()

# Query the database 
cursor.execute("SELECT name, status FROM staff")
results = cursor.fetchall()

# Pass data to HTML template
template = jinja2.Template("""
<!DOCTYPE html>
<html>
<body>

  <h1>Staff Status</h1>

  <table>
    {% for row in data %}
    <tr>
      <td>{{row[0]}}</td>
      <td>{{row[1]}}</td>
    </tr>
    {% endfor %}
  </table>
  
</body>
</html>
""")

html = template.render(data=results)

print(html)

conn.close()