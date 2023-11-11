from flask import Flask, render_template
import psycopg2
import jinja2

app = Flask(__name__)

# Connect to the database
conn = psycopg2.connect(
    database="hospitaldb",
    user="cryms",
    password="1234",
    host="localhost",
    port=5432
)
cursor = conn.cursor()

# Query the database


@app.route("/", methods=["POST", "GET"])
def display_table():
    cursor.execute("SELECT name, status FROM staff")
    results = cursor.fetchall()
    return render_template("staff.html", data=results)

## Pass data to HTML template
#template = jinja2.Template("""
#<!DOCTYPE html>
#<html>
#<body>
#
#  <h1>Staff Status</h1>
#
#  <table>
#    {% for row in data %}
#    <tr>
#      <td>{{row[0]}}</td>
#      <td>{{row[1]}}</td>
#    </tr>
#    {% endfor %}
#  </table>
#  
#</body>
#</html>
#""")
#
#html = template.render(data=results)

# Print or save the HTML as needed
#print(html)

#Display in application




#if __name__ == "__main__":
#    app.run(debug=True)

# Close the database connection
conn.close()