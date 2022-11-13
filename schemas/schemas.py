from voluptuous import Schema, Required, PREVENT_EXTRA, All, Length, Any

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


def validate_pantone_value(value):
    part_1, part_2 = value.split('-')
    if len(part_1) == 2 and len(part_2) == 4:
        return True
    else:
        raise ValueError(f'len part_1 "{part_1}" != 2 or len part_2 "{part_2}" != 4 ')


unknown_list_data_field = Schema(
    {
        "id": int,
        "name": str,
        "year": int,
        "color": str,
        "pantone_value": All(str, validate_pantone_value)
    },
    required=True,
    extra=PREVENT_EXTRA,
)

unknown_support = Schema(
    {
        "url": str,
        "text": str
    },
    required=True,
    extra=PREVENT_EXTRA,
)

unknown_list_schema = Schema(
    {
        "page": int,
        "per_page": int,
        "total": int,
        "total_pages": int,
        "data": All([unknown_list_data_field], Length(min=1)),
        "support": unknown_support
    },
    required=True,
    extra=PREVENT_EXTRA,
)