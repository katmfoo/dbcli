from prompt_toolkit import PromptSession
import drivers.mysql

def main():
    session = PromptSession()

    driver = drivers.mysql.Driver()
    driver.connect(port=6101);

    while True:
        try:
            text = session.prompt('> ')
            result = driver.execute(text)

            if result.success:
                item_word: str = driver.get_pluralized_item_name(result.count)
                if result.result is not None:
                    # There is a result set

                    # Print the results
                    if result.headers:
                        print(result.headers)
                    for row in result.result:
                        print(row)

                    # Print a success message
                    if result.count is not None:
                        if result.count > 0:
                            if item_word is not None:
                                print('Success, %s %s retrieved' % (result.count, item_word))
                            else:
                                print('Success')
                        else:
                            print('Empty result set')
                    else:
                        print('Success')
                else:
                    # There is not a result set

                    # Print a success message
                    if result.count is not None and result.count > 0 and item_word is not None:
                        print('Success, %s %s affected' % (result.count, item_word))
                    else:
                        print('Success')
            else:
                # Print error message
                print('Error: %s' % result.error_message)
        except EOFError:
            break
        except KeyboardInterrupt:
            break

if __name__ == "__main__":
    main()
