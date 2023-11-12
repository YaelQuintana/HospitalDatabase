import psycopg2
import jinja2

# Connect to the database
##Se usara ese usuario y contrasenna../
conn = psycopg2.connect(
    database="hospitaldb",
    user="hospitaladmin",
    password="1234",
    host="localhost",
    port=5432
)
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

# Print or save the HTML as needed
print(html)

# Close the database connection
conn.close()