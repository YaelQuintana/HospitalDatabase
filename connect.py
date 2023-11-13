from flask import Flask, render_template, request, send_file, jsonify
from psycopg2 import connect, extras
import jinja2

app = Flask(__name__)

###testeo


# Connect to the database
conn = connect(
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
    conn = get_connection()
    cursor = conn.cursor(cursor_factory= extras.DictCursor)


    cursor.execute("SELECT * FROM staff")
    result = cursor.fetchall()
    
    cursor.close()
    conn.close()

    return jsonify(result)

@app.get("/")
def home():
    return send_file('static/index.html')


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
#conn.close()