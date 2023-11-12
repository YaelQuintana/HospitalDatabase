from flask import Flask, render_template, request, send_file
import psycopg2
import jinja2

app = Flask(__name__)

###testeo


# Connect to the database
conn = psycopg2.connect(
    database="hospitaldb",
    user="cryms",
    password="1234",
    host="localhost",
    port=5432
)

def get_connection():
    return conn

@app.get("/api/staff")
def get_staff():
    conn = get_connection(cursor_factory=psycopg2.extras.DictCursor)
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM staff")
    result = cursor.fetchall()

    cursor.close()
    conn.close()

#@app.get("/")
#def home():


##@app.get("/")
##def home():
##    conn = get_connection()
##    cursor = conn.cursor()
##    cursor.execute("SELECT * FROM staff")
##
##    result = cursor.fetchone()
##
##    print(result)
##
##    return 'Hello world'

if __name__ == "__main__":
    app.run(debug=True)


# Query the database


#@app.route("/", methods=["POST", "GET"])
#def display_table():
#    cursor.execute("SELECT name, status FROM staff")
#    results = cursor.fetchall()
#    return render_template("staff.html", data=results)

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