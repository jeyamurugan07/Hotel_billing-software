from django.shortcuts import render
import mysql.connector
from django.db import connection
from django.http import JsonResponse
import json
def loginpage(request):
    if request.method == 'POST':
        login=request.POST
        username=login['username']
        password=login['password']
        cursor = connection.cursor()
        cursor.execute("select * from form where username='"+username+"' and password='"+password+"' ")
        a = cursor.fetchall()
        count = cursor.rowcount
        if count == 1:
            return render(request,'homepage.html')
        elif count> 1:
            return 'more then one user'
        else:
         
            return render(request, "loginpage.html")
    else:
         return render(request, "loginpage.html")

def stocklist(request):
    cursor = connection.cursor()
    cursor.execute('SELECT * FROM stocklist')
    mydb = cursor.fetchall()
    connection.commit()
    cursor.close()
    return render(request,'stocklist.html', {'data':mydb})

def stock(request):
        if request.method == 'POST':
            no = request.POST["no"]
            itemname = request.POST["itemname"]
            itemcode =request.POST["itemcode"]
            rate = request.POST["rate"]
            quantity = request.POST["quantity"]
            amount =request.POST["amount"]
            cursor = connection.cursor()
            cursor.execute(""" INSERT INTO stocklist VALUES (%s, %s, %s,%s,%s,%s)""",
                        (no, itemname, itemcode, rate, quantity, amount))
            cursor = connection.cursor()
            cursor.execute('SELECT * FROM stocklist')
            mydb = cursor.fetchall()
            connection.commit()
            cursor.close()
            return render(request,'stocklist.html', {'data':mydb})
        return render(request,'stock.html')
def delete(no_data):
    if request.method=='GET':
        cur = mysql.connection.cursor()
        cur.execute("DELETE FROM stocklist WHERE no=%s", (no_data,))
        mysql.connection.commit()
        return redirect(url_for('stocklist'))
    else:
        return render(request,'stocklist.html')

def bill(request):
        cur = connection.cursor()
        cur.execute('SELECT * FROM stocklist')
        mydb =cur.fetchall()
        connection.commit()
        cur.close()
      
        result1=json.dumps(mydb)
        context={
            'data':mydb,
            'result':result1
        }
        return render(request,'bill.html', context)




        
    # return render(request,"bill.html")

   # if request.method == 'POST':
    #     id = request.POST['id']
    #     name = request.POST['name']
    #     email = request.POST['email']
    #     cursor = connection.cursor()
    #     cursor.execute(''' INSERT INTO emplyoee VALUES(%s,%s,%s)''', (id, name, email))
    #     connection.commit()
    #     cursor.close()
    #     return render(request,"aa.html")
    # else:
    #     return render (request,"aa.html")