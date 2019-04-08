import pymysql


class ConnectDB:
    def CheckUser(self, result, credentials):
        self.result = result
        self.credentials = credentialss
        try:
            db = pymysql.connect(
                        credentials["dbhost"],
                        credentials["dbuser"],
                        credentials["dbpass"],
                        credentials["dbname"],
                        credentials["dbport"])
            cursor = db.cursor()
            query = cursor.execute("select * from name \
                                    where name = '{}'".format(result['name']))
            if query > 0:
                status = {
                   "status": "User already exist!"
                }
                return status

            else:
                insert = "insert into name values\
                         ('{}','{}','{}')".format(result['name'],
                                                  result['color'],
                                                  result['animal'])
                cursor.execute(insert)
                db.commit()
                status = {
                         "status": "Success"
                        }
                return status

        except Exception as e:
            print("Error: to save in db ", e)
            status = {
                "status": e
                    }
            return status

    def queryAll(self, credentials):
        self.credentials = credentials
        try:
            db = pymysql.connect(
                        credentials["dbhost"],
                        credentials["dbuser"],
                        credentials["dbpass"],
                        credentials["dbname"],
                        credentials["dbport"])
            cursor = db.cursor()
            cursor.execute("select * from name ")
            return cursor.fetchall()

        except Exception as e:
            print("Error on query: ", e)
            return e
