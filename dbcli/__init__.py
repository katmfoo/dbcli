from prompt_toolkit import PromptSession
import drivers.mysql

def main():
    session = PromptSession()

    mysql = drivers.mysql.Driver()
    mysql.connect(port=6101);

    while True:
        try:
            text = session.prompt('> ')
            result = mysql.execute(text)

            if result.success:
                if result.result is not None:
                    if result.rowcount > 0:
                        if result.headers:
                            print(result.headers)
                        for row in result.result:
                            print(row)
                    print('Success, %s rows retrieved' % result.rowcount)
                else:
                    if result.rowcount > 0:
                        print('Success, %s rows affected' % result.rowcount)
                    else:
                        print('Success')
            else:
                print('Error: %s' % result.error_message)
        except EOFError:
            break
        except KeyboardInterrupt:
            break

if __name__ == "__main__":
    main()
