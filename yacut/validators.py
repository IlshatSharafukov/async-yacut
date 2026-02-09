import re
from yacut.constants import ALLOWED_CHARS, MAX_SHORT_ID_LENGTH
from yacut.models import URLMap


def validate_short_id(short_id):
    if not short_id:
        return None

    if short_id == 'files':
        return 'Предложенный вариант короткой ссылки уже существует.'

    if len(short_id) > MAX_SHORT_ID_LENGTH:
        return 'Указано недопустимое имя для короткой ссылки'

    pattern = f'^[{re.escape(ALLOWED_CHARS)}]+$'
    if not re.match(pattern, short_id):
        return 'Указано недопустимое имя для короткой ссылки'

    if URLMap.query.filter_by(short=short_id).first():
        return 'Предложенный вариант короткой ссылки уже существует.'

    return None