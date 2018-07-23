
"""falsk modules which help us to to include app path and 
render the html page on the browser"""
from flask import Flask, render_template, request
#importing sqlite3 database for storing our data
import sqlite3 as sql
import sqlite3
#including app
app = Flask(__name__)
#sepcifying the app and render on the html page
@app.route('/')
def home():
   return render_template('home.html')
#connecting to the database
conn = sqlite3.connect('database.db')
print("Opened database successfully")

#Task3 Creating the integrity constraints
conn.execute('CREATE TABLE product(name TEXT, pdesc TEXT, qty TEXT, price TEXT)' primary key(name))
print ("Table created successfully")
conn.close()
app=Flask(__name__)


#Task2 Adding new records
@app.route('/enternew')
def new_product():
   return render_template('product.html')
@app.route('/addrec',methods = ['POST', 'GET'])

"""for inserting the values into the table and by
fetching the form controls """
def addrec():
   if request.method == 'POST':
      try:
         nm = request.form['nm']
         pdesc = request.form['pdesc']
         qty = request.form['qty']
         price = request.form['price']
         #Importing the initial data set into product SQL Database
         with sql.connect("database.db") as con:
            cur = con.cursor()
            cur.execute("INSERT INTO product(name,pdesc,qty,price)VALUES (?,?,?,?)"
                        ,(nm,pdesc,qty,price) )
            
            con.commit()
            msg = "Record successfully added"
      except:
         con.rollback()
         msg = "error in insert operation"
      
      finally:
         return render_template("result.html",msg = msg)
         con.close()
#displaying the table data on the browser which is on list
@app.route('/list')
def list():
   con = sql.connect("database.db")
   con.row_factory = sql.Row
#creating the cursor command to run sql statements
   cur = con.cursor()
   cur.execute("select * from product")
   
   rows = cur.fetchall();

#Task1 Importing the intial data set into the database file
   file = open('productdetails.txt','w+')
   file.write(rows.encode('utf-8', 'ignore'))
   return render_template("list.html",rows = rows)
@app.route('/')
def home():
   return render_template('home.html')
if __name__ == '__main__':
   app.run(debug = True)
   file = open('productdetails.txt','w+')
   file.write(rows)
   
