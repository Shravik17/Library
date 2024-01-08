import time
import mysql.connector as mysql

def main_menu():
    c=input('''press '𝐪' for 𝐋𝐢𝐛𝐫𝐚𝐫𝐲 𝐌𝐚𝐧𝐚𝐠𝐞𝐫\npress '𝐰' for 𝐂𝐨𝐦𝐦𝐚𝐧𝐝 𝐋𝐢𝐧𝐞 𝐂𝐥𝐢𝐞𝐧𝐭\ntype '𝐄𝐱𝐢𝐭' to 𝐄𝐱𝐢𝐭\n> ''')
    if c=='q':
        for i in '\n'*35+'─'*80:
            print(i,end='')
            time.sleep(0.01)
        for i in '\n𝐋𝐢𝐛𝐫𝐚𝐫𝐲 𝐌𝐚𝐧𝐚𝐠𝐞𝐫:\n':
            print(i,end='')
            time.sleep(0.1)
        library_manager()
    elif c=='w':
        command_line()
    elif c=='exit':
        exit





def command_line():
    con=mysql.connect(host='localhost',user='root',password='1234')
    cur=con.cursor()
    con.autocommit=True
    print('''\n𝘾𝙤𝙢𝙢𝙖𝙣𝙙 𝙇𝙞𝙣𝙚 𝘾𝙡𝙞𝙚𝙣𝙩:\n '𝘦𝘹𝘪𝘵' 𝘧𝘰𝘳 𝘔𝘢𝘪𝘯 𝘔𝘦𝘯𝘶\n''')
    while True:
        c=input('''𝘴𝘲𝘭>>''')
        if c=='exit':
            print()
            con.disconnect()
            main_menu()
            break
        else:
            try:
                cur.execute(c)
                for i in cur:
                    print(i)
            except:
                print('𝐄𝐫𝐫𝐨𝐫')

def library_manager():
    con=mysql.connect(host='localhost',user='root',password='1234')
    cur=con.cursor()
    con.autocommit=True

    
    def filecheck():
        cur.execute('show databases')
        l=[]
        for i in cur:l=l+list(i)
        if 'library' not in l:
            if input('  library database not found would you like to create new? 𝐲/𝐧')=='y':
                cur.execute('create database library')
            else:main_menu()
        cur.execute('use library');cur.execute('show tables');l=[]
        for i in cur:l=l+list(i)
        if l!=['book', 'borrowed_book', 'borrower', 'onsite_book', 'ordered']:
            for i in ['''CREATE TABLE `book` (`Name` varchar(20) NOT NULL,`ISBN` int NOT NULL,`Author` varchar(20) NOT NULL,`Type` varchar(20) DEFAULT '-',`Status` varchar(20) NOT NULL,PRIMARY KEY (`ISBN`))''','''CREATE TABLE `borrowed_book` (`Name` varchar(20) NOT NULL,`ISBN` int NOT NULL,`Borrower` varchar(20) NOT NULL,`Borrow_Date` date NOT NULL,PRIMARY KEY (`Borrower`))''','''CREATE TABLE `borrower` (`Name` varchar(20) NOT NULL,`Number` int NOT NULL,`Book_Name` varchar(20) DEFAULT '-',`Borrow_Date` date DEFAULT NULL,PRIMARY KEY (`Number`))''','''CREATE TABLE `onsite_book` (`Name` varchar(20) NOT NULL,`ISBN` int NOT NULL,`Author` varchar(20) NOT NULL,`Type` varchar(20) DEFAULT '-',`Locale` int NOT NULL,PRIMARY KEY (`locale`),UNIQUE KEY `ISBN` (`ISBN`))''','''CREATE TABLE `ordered` (`Name` varchar(20) NOT NULL,`ISBN` int NOT NULL,`Author` varchar(20) NOT NULL,`Type` varchar(20) DEFAULT '-',`Status` varchar(20) NOT NULL,PRIMARY KEY (`ISBN`))''']:
                try:cur.execute(i)
                except:continue
        lib_menu()

                

    def lib_menu():
        global tb,tc,c
        tb={'q':'Book','w':'Borrower','e':'Onsite_book','r':'Borrowed_book','t':'Ordered'}
        tc={'Book':'Name ISBN Author Type Status','Borrower':'Name Number Book_Name Borrow_Date','Onsite_book':'Name ISBN Author Type Locale','Borrowed_book':'Name ISBN Borrower Borrow_Date','Ordered':'Name ISBN Author Type Status'}
        c=input('''   press '𝐪' for 𝐀𝐥𝐥 𝐁𝐨𝐨𝐤𝐬\n   press '𝐰' for 𝐀𝐥𝐥 𝐁𝐨𝐫𝐫𝐨𝐰𝐞𝐫𝐬\n   press '𝐞' for 𝐈𝐧 𝐋𝐢𝐛𝐫𝐚𝐫𝐲 𝐁𝐨𝐨𝐤𝐬\n   press '𝐫' for 𝐁𝐨𝐫𝐫𝐨𝐰𝐞𝐝 𝐁𝐨𝐨𝐤𝐬\n   press '𝐭' for 𝐎𝐫𝐝𝐞𝐫𝐞𝐝 𝐁𝐨𝐨𝐤𝐬\n   type '𝐁𝐚𝐜𝐤' to 𝐆𝐨 𝐁𝐚𝐜𝐤\n──>''')
        print(f'\n {tb[c]} selected:\n')
        if c=='back':
            main_menu()
        else:
            cur.execute(f'''select * from {tb[c]}''')
            for i in cur:print('│'+'─'*50+'│\n  ',i,'\n','│'+'─'*50+'│',sep='')
            rec()




    def rec():
        c2=input(f'''press '𝐪' to 𝐒𝐞𝐚𝐫𝐜𝐡 𝐀 {tb[c]}\npress '𝐰' to 𝐀𝐝𝐝 𝐀 {tb[c]}\npress '𝐞' to 𝐑𝐞𝐦𝐨𝐯𝐞 𝐀 {tb[c]}\npress '𝐭' to 𝐒𝐡𝐨𝐰 𝐀𝐥𝐥\ntype '𝐁𝐚𝐜𝐤' to 𝐆𝐨 𝐁𝐚𝐜𝐤\n>''')
        print()
        if c2=='q':
            c2=input('enter values to search by in the format: parameter=value and/or parameter=value\n>')
            if c2:cur.execute(f'''select * from {tb[c]} where {c2}''')
            else:cur.execute(f'''select * from {tb[c]}''')
            for i in cur:print(f'\n{tb[c]} whose({c2}):\n│'+'─'*50+'│\n  ',i,'\n','│'+'─'*50+'│',sep='')
            rec()
        elif c2=='w':
            vals=()
            for i in tc[tb[c]].split():
                print(i+':')
                vals=vals+(input('>'),)
            try:cur.execute(f'''insert into {tb[c]} values {vals}''');print('│'+'─'*50+'│\n  ',vals,' was added','\n','│'+'─'*50+'│',sep='')
            except:print(f'''{vals} could not be added''')
            
            rec()
        elif c2=='e':
            c2=input(f'enter values of {tb[c]} you want to delete: parameter=value and/or parameter=value\n>')
            try:cur.execute(f'''delete from {tb[c]} where {c2}''');print('│'+'─'*50+'│\n  ',f'values with ({c2}) have been removed','\n','│'+'─'*50+'│',sep='')
            except:print('│'+'─'*50+'│\n  ',f'''could not delete ({c2}) from {tb[c]}''','\n','│'+'─'*50+'│',sep='')
            rec()
        elif c2=='t':
            print(f'All records in {tb[c]}:')
            cur.execute(f'select * from {tb[c]}')
            for i in cur:print('│'+'─'*50+'│\n  ',i,'\n','│'+'─'*50+'│',sep='')
            rec()
        elif c2=='back':
            lib_menu()
    filecheck()
        
            
          
    
    
main_menu()
    
    



