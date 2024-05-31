from rest_framework.schemas.coreapi import AutoSchema, coreapi, coreschema, ManualSchema



list_schedule_schema = AutoSchema(manual_fields=[
    coreapi.Field(
        name='weekday_id',
        required=True,
        description="Week day ID",
        type='int',
        location='form',
        schema=coreschema.String()
    ),
    coreapi.Field(
        name='user_id',
        required=True,
        description="User ID",
        type='int',
        location='form',
        schema=coreschema.String()
    ),
])

create_schedule_schema = AutoSchema(manual_fields=[
    coreapi.Field(
        name='user',
        required=True,
        description="Telegram ID",
        type='int',
        location='form',
        schema=coreschema.Integer()
    ),
    coreapi.Field(
        name='weekday',
        required=True,
        description="weekday ID",
        type='int',
        location='form',
        schema=coreschema.Integer()
    ),
    coreapi.Field(
        name='daykind',
        required=True,
        description="daykind ID",
        type='int',
        location='form',
        schema=coreschema.Integer()
    ),
    coreapi.Field(
        name='subject',
        required=False,
        description="subject",
        type='str',
        location='form',
        schema=coreschema.String()
    ),
    coreapi.Field(
        name='teacher',
        required=False,
        description="teacher",
        type='str',
        location='form',
        schema=coreschema.String()
    ),
    coreapi.Field(
        name='room',
        required=False,
        description="room",
        type='str',
        location='form',
        schema=coreschema.String()
    ),
    coreapi.Field(
        name='lesson_type',
        required=False,
        description="lesson_type",
        type='str',
        location='form',
        schema=coreschema.String()
    ),
])

