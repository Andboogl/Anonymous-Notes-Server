"""Main module. Runs server"""


from loguru import logger
from server import Server


# Logger settings
logger.add(
    sink='logs/now.log',
)


def get_user_data() -> tuple:
    """Get user data"""
    try:
        server_ip = input('Enter server IP: ')
        server_port = int(input('Enter server port: '))
        return server_ip, server_port

    except ValueError:
        print('Server port must be an integer')
        return get_user_data()


def main() -> None:
    """This function runs server"""
    try:
        server_ip, server_port = get_user_data()
        Server(server_ip, server_port)

    except Exception as error:
        logger.error(f'Error while running server: {error}')
        print('Check server ip and port')
        main()


if __name__ == '__main__':
    main()
