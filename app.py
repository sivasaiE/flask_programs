from flask import Flask,jsonify,json,request
from utils import connection_to_db
import logging
from config import (FLASK_PORT, DEBUG)
import psycopg2
app = Flask(__name__)
# logging.basicConfig(filename=".env",
#                     format='%(asctime)s %(message)s',
#                     filemode='a')
conn, cur = connection_to_db()
emails_in_list=[]
# cur = conn.cursor()
# logger=logging.getLogger()
# logger.setLevel(logging.INFO)

# b = connection_to_db()
# print(b)
# dict_user_data = { }
# @app.route('/')
# def hello():
#     if conn:
#         logger.info('connection established')
#         conn,cur = connection_to_db()
#         return conn,cur
#     logger.info('connection not established')
#     return 'hello world'

# @app.route('/create',methods=['POST'])
#                             #  'GET',
#                             #  'PATCH',
#                             #  'PUT',
#                             #  'DELETE'
# def method():
#     if conn:
#         if request.method=='POST':
#             user = request.get_json()
#             first_name = user['first_name']
#             last_name = user['last_name']
#             email = user['email']
#             password = user['password']
#             cur.execute('select email from details_user100' )
#             emails_in_db = cur.fetchall()
#             print(emails_in_db)
#             # To check email exists ot not
#             for tuple_email in emails_in_db:
#                 if email in tuple_email:
#                     return 'email already present'
            
#             # If not email, create a new row with all objects
#             insertion_to_table ='''insert into details_user100
#                                 (first_name,last_name,email,pwd) 
#                                 values(%s,%s,%s,%s)'''
#             data_to_be_inserted= (first_name,last_name,email,password)
#             cur.execute(insertion_to_table,data_to_be_inserted)
#             conn.commit()
#             return 'Data Inserted'
@app.route('/<email>/<anything>',methods = ['PUT',
                                            'PATCH',
                                            'GET',
                                            'DELETE'])

def more_methods(email,anything):
    if request.method=='GET':
        cur.execute('select email from details_user100')
        emails_in_db = cur.fetchall()
        # type(emails_in_db)
        for emails in emails_in_db:
            if email not in emails:
                return 'user not present'
        data_to_be_returned='select * from user_details100'
        parameters = (email,)
        cur.execute(data_to_be_returned,parameters)
        user_details = cur.fetchall()
        print(user_details)
        conn.commit()
    
    elif request.method=='DELETE':
        cur.execute('select email from details_user100')
        emails_in_db = cur.fetchall()
        # type(emails_in_db)
        for emails in emails_in_db:
            if email not in emails:
                return 'user not present'
        row_to_be_deleted = 'delete from details_user100 where email = %s'
        row_data = (email,)
        cur.execute(row_to_be_deleted,row_data)
        return 'deleted successfully'
    elif request.method=='PATCH':
        # cur.execute('select email from details_user100')
        # emails_in_db = cur.fetchall()
        # # type(emails_in_db)
        # for emails in emails_in_db:
        #     if email not in emails:
                # return 'user not present'
        update_query = 'update details_user100 set last_name =%s where email =%s'
        data_to_be_updated = (anything,email)
        cur.execute(update_query,data_to_be_updated)
        conn.commit()
        return 'successfully updated'

    # elif 
        



    # elif request.method=='PATCH':



               

    return 'no methods match'
        
            
    return 'none'



if __name__ =='__main__':
    app.run(debug=DEBUG, port=FLASK_PORT)

