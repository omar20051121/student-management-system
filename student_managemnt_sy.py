import csv
import sqlite3


def check_db():
    global conn, curser, exsist
    db = None
    exsist = False

    while True:
        db_exsist = input("Do you want to access a previous database (y/n): ").lower()

        if db_exsist in ["yes", "y", "ya"]:
            while True:
                Perivous_db = input("Enter previous DB name (without .db): ")
                if ".db" in Perivous_db:
                    print("Invalid input")
                else:
                    db = Perivous_db
                    exsist = True
                    break
            break

        elif db_exsist in ["no", "n"]:
            while True:
                new_db = input("Enter new DB name (without .db): ")
                if ".db" in new_db:
                    print("Invalid input")
                else:
                    db = new_db
                    exsist = False
                    break
            break

        else:
            print("Invalid, type (y/n)")

    conn = sqlite3.connect(db + ".db")
    curser = conn.cursor()


def files_maker():
    file_name = input("File name: ")

    while True:
        try:
            fieldElements = int(input("Number of attributes: "))
            break
        except ValueError:
            print("Invalid number")

    field_attributes = [0] * fieldElements

    for i in range(len(field_attributes)):
        while True:
            found = False
            field_attributes[i] = input(f"Attribute_{i+1}: ")

            for c in field_attributes[i]:
                if c.isalpha():
                    found = True
                    break
            else:
                print("Invalid name")

            if found:
                break

    students_number = int(input("Number of records: "))

    with open(file_name + ".csv", "w", newline="") as file_DB:
        writer = csv.DictWriter(file_DB, fieldnames=field_attributes)
        writer.writeheader()

        row = [{attr: "" for attr in field_attributes} for _ in range(students_number)]

        for i in range(students_number):
            for attr in row[0].keys():
                row[i][attr] = input(f"{attr} for {file_name}_{i+1}: ")

        writer.writerows(row)

    return field_attributes, file_name


def tables_maker(field_attributes):
    table_name = input("Table name: ")

    table = ", ".join(
        f"{attr} " + (
            "INTEGER PRIMARY KEY" if attr == "id"
            else "INTEGER" if "_id" in attr
            else "INTEGER" if attr in ["age", "phone", "credits"]
            else "TEXT"
        )
        for attr in field_attributes
    )

    create_table_query = f"CREATE TABLE IF NOT EXISTS {table_name} ({table})"
    curser.execute(create_table_query)

    return table_name


def load_csv_to_db(file_name, table_name, field_attributes):
    with open(file_name + ".csv", "r") as file_DB:
        reader = csv.DictReader(file_DB)

        columns = ", ".join(field_attributes)
        placeholders = ", ".join("?" for _ in field_attributes)

        insert_query = f"INSERT INTO {table_name} ({columns}) VALUES ({placeholders})"

        for row in reader:
            values = [row[attr] for attr in field_attributes]
            curser.execute(insert_query, values)


def show_table(table_name):
    curser.execute(f"SELECT * FROM {table_name}")
    rows = curser.fetchall()

    print("\nData inside table:")
    for row in rows:
        print(row)


def db_features():
    pass


def main():
    check_db()

    while True:
        try:
            files_n = int(input("How many tables/files: "))
            break
        except ValueError:
            print("Invalid number")

    for _ in range(files_n):
        field_attributes, file_name = files_maker()

        print("Good job, file created successfully\n")

        table_name = tables_maker(field_attributes)

        load_csv_to_db(file_name, table_name, field_attributes)

        show_table(table_name)

    conn.commit()
    conn.close()


if __name__ == "__main__":
    main()









# import csv
# import sqlite3

# def check_db():
#     global conn, curser, exsist
#     db = None
#     exsist = False

#     while True:
#         db_exsist = input("do you want to access a previous database (y/n): ").lower()

#         if db_exsist in ["yes", "y", "ya"]:
#             while True:
#                 Perivous_db = input("type the name of the previous database without .db: ")
#                 if ".db" in Perivous_db:
#                     print("Invalid input")
#                 else:
#                     db = Perivous_db
#                     exsist = True
#                     break
#             break

#         elif db_exsist in ["no", "n"]:
#             while True:
#                 new_db = input("type the name of the new database without .db: ")
#                 if ".db" in new_db:
#                     print("Invalid input")
#                 else:
#                     db = new_db
#                     exsist = False
#                     break
#             break

#         else:
#             print("Invalid, Please type (y/n)")

#     conn = sqlite3.connect(db + ".db")
#     curser = conn.cursor()


# def files_maker():
#     file_name = input("what's the file name: ")

#     while True:
#         try:
#             fieldElements = int(input("File attributes count: "))
#             break
#         except ValueError:
#             print("Invalid number")

#     field_attributes = [0] * fieldElements

#     for i in range(len(field_attributes)):
#         while True:
#             found = False
#             field_attributes[i] = input(f"Attribute_{i+1}: ")

#             for c in field_attributes[i]:
#                 if c.isalpha():
#                     found = True
#                     break
#             else:
#                 print("Invalid name")

#             if found:
#                 break

#     students_number = int(input("How many records: "))

#     with open(file_name + ".csv", "w", newline="") as file_DB:
#         writer = csv.DictWriter(file_DB, fieldnames=field_attributes)
#         writer.writeheader()

#         row = [{attr: "" for attr in field_attributes} for _ in range(students_number)]

#         for i in range(students_number):
#             for attr in row[0].keys():
#                 row[i][attr] = input(f"{attr} for {file_name-'s'}_{i+1}: ")

#         writer.writerows(row)

#     return field_attributes


# def tables_maker(field_attributes):
#     table_name = input("Table name: ")

#     table = ", ".join(
#         f"{attr} " + (
#             "INTEGER PRIMARY KEY" if attr == "id"
#             else "INTEGER" if "_id" in attr
#             else "INTEGER" if attr in ["age", "phone", "credits"]
#             else "TEXT"
#         )
#         for attr in field_attributes
#     )

#     create_table_query = f"CREATE TABLE IF NOT EXISTS {table_name} ({table})"
#     curser.execute(create_table_query)


# def db_features():
#     pass


# def main():
#     check_db()

#     if exsist:
#         pass
#     else:
#         pass

#     while True:
#         try:
#             files_n = int(input("How many files/tables: "))
#             break
#         except ValueError:
#             print("Invalid number")

#     for _ in range(files_n):
#         field_attributes = files_maker()
#         print("Good job")
#         tables_maker(field_attributes)

#     conn.commit()
#     conn.close()


# if __name__ == "__main__":
#     main()



# import csv
# import sqlite3



# def check_db():
#     global conn,curser,exsist
#     db=None
#     exsist=False
#     while True:
#         db_exsist=input("do you want to access a perivous database (y/n)")
#         db_exsist=db_exsist.lower()
#         if db_exsist in ["yes","y","ya"]:
#             while True:
#                   Perivous_db=input("type the name of the perivous database you would like to access without .db extintion? ")
#                   if ".db" in db:
#                      print("Invalid input, please type a database name without .db extintion")
#                   else:
#                      exsist=True
#                      break
#             break
#         elif db_exsist in["no","n"]:
#             while True:
#                     new_db=input("type the name of the new database you would like to access without .db extintion? ")
#                     if ".db" in db:
#                        print("Invalid input, please type a database name without .db extintion")
#                     else:
#                        exsist=True
#                        break
#             break
#         else:
#             print("Invalid, Please type (y/n)")


#     conn=sqlite3.connect(db+".db")
#     curser=conn.cursor()


# def files_maker():
#     file_name=input("what's the file name you would like: ")
#     # ["id","name","age","gender","email","phone","address"]
#     while(True):
#      try:
#         global fieldElements
#         fieldElements=int(input("File attriputes count: "))
#         break

#      except ValueError:
#         print("Invalid input, please enter a valid number for your file attributes counts")

#     field_attributes=[0]*fieldElements
#     field_attributes_size=len(field_attributes)

#     for i in range(field_attributes_size):
#         while(True):
#             found=False
#             field_attributes[i]=input(f"Attripute name_{i+1}: ")

#             for c in field_attributes[i]:
#                 if c.isalpha():
#                     found=True
#                     break

#             else:
#                 print("Invalid input: please enter a valid name it should contain at least one charecter")
#             if found:
#                 break

#     students_number=int(input("How many elements you want to make a database for? "))

#     with open(file_name + ".csv", "w", newline="") as file_DB:
#         writer=csv.DictWriter(file_DB,fieldnames=field_attributes)
#         writer.writeheader()

#         row=[{attribute: "" for attribute in field_attributes} for _ in range(students_number)]

#         for i in range(students_number):

#             for attribute in row[0].keys():

#                 row[i][attribute]= input(f"Type {attribute} student_{i+1}: ")

#         writer.writerows(row)
#         return(field_attributes)


# def tables_maker(field_attributes, ):

#      table_name=input("What's the table name? ")
#      table= ", ".join(f"{attr} "
#         + ("INTEGER PRIMARY KEY" if attr=="id"
#            else "INTEGER FOREIGN KEY" if "_id" in attr
#            else "INTEGER" if attr in ["age","phone","credits"]
#             else "TEXT" )
#                     for attr in field_attributes)

#      create_table_query=f"Create TABLE IF NOT EXISTS {table_name} ({table})"
#      curser.execute(create_table_query)


# def db_features():



# def main():
#   check_db()
#   if exsist:

#   else:


#   while(True):
#        try:
#           files_n=int(input("How many files do you want to create ""each file has one single table in the database"": "))
#           break
#        except ValueError:
#           print("Invalid input, Please enter a valied number")

#   for _ in range(files_n):
#     field_attributes=files_maker()
#     print("Goodjop, now you competed the filling the file perfectly")
#     print()
#     tables_maker(field_attributes)
#   if __name__=="__main__":
#             main





# with open(file_name +".csv","r+",newline="") as file_DB:
#     rows=list(csv.DictReader(file_DB))

#     for i in range(students_number):

#         for attribute in rows[0].keys():

#             rows[i][attribute]= input(f"Type {attribute} student_{i+1}: ")


#     file_DB.seek(0)

#     writer=csv.DictWriter(file_DB,fieldnames=field_attributes)
#     writer.writeheader()
#     writer.writerows(rows)

# print("Goodjop, now you competed the filling the file perfectly")

# with open(file_name + ".csv", "w", newline="") as file_DB:
#     writer=csv.DictWriter(file_DB,fieldnames=field_attributes)
#     row=list(writer)

#     for i in range(students_number):

#         for attribute in row[0].keys():

#             row[i][attribute]= input(f"Type {attribute} student_{i+1}: ")

#  writer.writerows(row)

# print("Goodjop, now you competed the filling the file perfectly")

# with open(file_name +".csv", newline="") as Students_DB:
#     reader=csv.DictReader(Students_DB)


