"""Server"""


from socket import socket
from threading import Thread
from pickle import loads, dumps
from loguru import logger
from notes import Notes


class Server:
    """Server"""
    def __init__(self,
                 ip: str,
                 port: int) -> None:
        self.server_socket = socket()
        self.server_socket.bind((ip, port))
        self.server_socket.listen(0)
        self.notes = Notes()

        self.connections_handler()

    def connections_handler(self) -> None:
        """Connections handler"""
        while True:
            try:
                user = self.server_socket.accept()[0]
                Thread(target=self.user_handler,
                       args=(user,),
                       daemon=True).start()

            except:
                pass

    @logger.catch
    def user_handler(self, user_socket: socket) -> None:
        """User handler"""
        try:
            data = user_socket.recv(9000)
            data = loads(data)  # Decryption
            logger.info(f'User request: {data}')

            # Request to create a note
            # ['create_note', name, content]
            if data[0] == 'create_note':
                note_id = self.notes.create_note(data[1], data[2])
                note_id = dumps(note_id)  # Encryption
                user_socket.send(note_id)

            # Request to read a note
            # ['read_note', id]
            elif data[0] == 'read_note':
                note_data = self.notes.read_note(data[1])
                note_data = dumps(note_data)  # Encryption
                user_socket.send(note_data)

        except:
            pass
