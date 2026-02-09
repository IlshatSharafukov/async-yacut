from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, MultipleFileField, URLField
from wtforms.validators import (DataRequired, Optional,
                                ValidationError, Regexp,
                                URL, Length)
from yacut.constants import ALLOWED_CHARS, MAX_SHORT_ID_LENGTH
from yacut.models import URLMap


def validate_custom_id(form, field):
    if field.data:
        if field.data == 'files':
            raise ValidationError(
                'Предложенный вариант короткой ссылки уже существует.'
            )
        if URLMap.query.filter_by(short=field.data).first():
            raise ValidationError(
                'Предложенный вариант короткой ссылки уже существует.'
            )


class URLForm(FlaskForm):
    original_link = URLField(
        'Длинная ссылка',
        validators=[DataRequired(message='Обязательное поле'), URL()]
    )
    custom_id = StringField(
        'Ваш вариант короткой ссылки',
        validators=[
            Optional(),
            Length(max=MAX_SHORT_ID_LENGTH),
            Regexp(
                f'^[{ALLOWED_CHARS}]+$',
                message='Указано недопустимое имя для короткой ссылки'
            ),
            validate_custom_id
        ]
    )
    submit = SubmitField('Создать')


class FileUploadForm(FlaskForm):
    files = MultipleFileField(
        'Файлы',
        validators=[DataRequired(message='Обязательное поле')]
    )
    submit = SubmitField('Загрузить')