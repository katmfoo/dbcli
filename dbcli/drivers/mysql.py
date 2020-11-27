import drivers.base
import mysql.connector

class Driver(drivers.base.Driver):

    def connect(self, host="localhost", user="root", password="", port=3306):
        self.connection = mysql.connector.connect(
            host=host,
            user=user,
            password=password,
            port=port
        )

    def execute(self, command):

        cursor = self.connection.cursor()

        try:
            cursor.execute(command)

            if cursor.description is not None:
                result = cursor.fetchall()
                headers = tuple([i[0] for i in cursor.description])
                return drivers.base.ExecutionResponse(headers=headers, result=result, rowcount=cursor.rowcount)
            else:
                return drivers.base.ExecutionResponse(rowcount=cursor.rowcount)
        except Exception as e:
            error_message = str(e)
            return drivers.base.ExecutionResponse(success=False, error_message=error_message)
