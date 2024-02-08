"""Module to work with notes"""


from typing import Union
from loguru import logger
from note_id import generate_note_id


class Notes:
    """Class to work with notes"""
    def __init__(self) -> None:
        self.notes = {}

    def create_note(self,
                    name: str,
                    content: str) -> str:
        """Create new note"""
        note_id = generate_note_id()

        while note_id in self.notes.keys():
            note_id = generate_note_id()

        data_to_add = {'name': name, 'content': content}
        self.notes[note_id] = data_to_add
        logger.info(f'Created new note. Data: {data_to_add}, id: {note_id}')
        return note_id

    def read_note(self, note_id: str) -> Union[None, dict]:
        """Read note"""
        if self.notes.get(note_id, None):
            logger.info(f'Readed note. ID: {note_id}')
            return self.notes.pop(note_id)
