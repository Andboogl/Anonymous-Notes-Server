"""Note ID generation module"""


from random import choice


def generate_note_id() -> str:
    """Generate note id"""
    note_id_len = choice([45, 46, 47, 48, 49, 50])
    symbols = 'qwertyuiopasdfghjklzxcvbnm1234567890'
    result = ''

    for _ in range(note_id_len):
        result += choice(symbols)

    return result
