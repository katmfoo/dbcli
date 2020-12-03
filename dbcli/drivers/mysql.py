from .base import BaseDriver, ExecutionResponse
import mysql.connector

class MySQLDriver(BaseDriver):

    item_singular: str = 'row'
    item_plural: str = 'rows'

    def connect(self, host: str = "localhost", user: str = "root",
                password: str = "", port: int = 3306):
        """Connects to a mysql server.

        :param host: The host to connect to
        :param user: The username to connect with
        :param password: The password to connect with
        :param port: The port to connect with
        """

        self.connection = mysql.connector.connect(
            host=host,
            user=user,
            password=password,
            port=port
        )

    def execute(self, command: str):
        """Executes a mysql query.

        :param command: The query to execute.
        :returns: An `ExecutionResponse`
        """

        cursor = self.connection.cursor()

        try:
            cursor.execute(command)

            # If there is a result set
            if cursor.description is not None:
                result = cursor.fetchall()
                headers = tuple([i[0] for i in cursor.description])
                return ExecutionResponse(headers=headers, result=result, count=cursor.rowcount)
            else:
                # There is no result set
                return ExecutionResponse(count=cursor.rowcount)
        except Exception as e:
            # There was an error executing the query
            error_message = str(e)
            return ExecutionResponse(success=False, error_message=error_message)
