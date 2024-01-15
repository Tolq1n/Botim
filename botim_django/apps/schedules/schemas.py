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

