from voluptuous import Schema, Required, PREVENT_EXTRA

create_user_schema = Schema(
    {
        "name": str,
        "job": str,
        "id": str,
        "createdAt": str
    },
    required=True,
    extra=PREVENT_EXTRA
)

update_user_schema = Schema(
    {
        "name": str,
        "job": str,
        "updatedAt": str
    },
    required=True,
    extra=PREVENT_EXTRA
)

get_single_user_schema = Schema(
    {
        "data": {
                "id": int,
                "email": str,
                "first_name": str,
                "last_name": str,
                "avatar": str
            },
            "support": {
                "url": str,
                "text": str
            }
    },
    required=True,
    extra=PREVENT_EXTRA
)

successful_register_user_schema = Schema(
    {
        "id": int,
        "token": str
    },
    required=True,
    extra=PREVENT_EXTRA
)