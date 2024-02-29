from flask import Flask, render_template, request, url_for, flash, redirect, abort
import sqlite3

app = Flask(__name__)

#Helper function for establishing a connection to the database
def getDbConnection():
    connection = sqlite3.connect('database.db')
    connection.row_factory = sqlite3.Row
    return connection

#Actual function that displays a webpage
@app.route("/")
def display():
    connection = getDbConnection()
    data = connection.execute('SELECT * FROM data').fetchall()
    connection.close()
    return render_template('home.html', searchName="", data=data)

#Adds user to the database and refreshes the page to show the change
@app.route('/insert', methods = ['POST'])
def insert():
    if request.method == 'POST':
        name = request.form['name']
        id = request.form['id']
        points = request.form['points']

        connection = sqlite3.connect('database.db')
        cursor = connection.cursor()
        cursor.execute("INSERT INTO data (user, id, points) VALUES (?, ?, ?)", (name, id, points))
        
        connection.commit()
        connection.close()
        return redirect(url_for('display'))

#Updates existing user information
@app.route('/update', methods = ['GET', 'POST'])
def update():
    if request.method == 'POST':
        entryNum = request.form['entryNum']
        print(entryNum)
        name = request.form['name']
        id = request.form['id']
        points = request.form['points']

        connection = getDbConnection()
        connection.execute('UPDATE data SET user = ?, id = ?, points = ? WHERE entryNum = ?', 
                            (name, id, points, entryNum))
        connection.commit()
        connection.close()
        return redirect(url_for('display'))

@app.route('/delete/<entryNum>/', methods = ['GET', 'POST'])
def delete(entryNum):
    connection = getDbConnection()
    connection.execute('DELETE FROM data WHERE entryNum = ?', (entryNum,))
    connection.commit()
    connection.close()
    return redirect(url_for('display'))

#Using template to print the array instead of making an entirely new thing
@app.route('/search', methods = ['POST'])
def search():
    if request.method == 'POST':
        connection = getDbConnection()
        name = request.form.get('searchName')
        searchName = "%" + name + "%"
        data = connection.execute('SELECT * FROM data WHERE user LIKE ?', (searchName,)).fetchall()
        connection.close()
        return render_template('home.html', searchName=name, data=data)

if __name__ == "__main__":
    app.run(debug=True)
