
def get_room(list_to_extract_room_from: list, sid: str) -> str:
    """ It is because, sio.rooms(sid) -> return list that contains room and sid. """
    try:
        list_to_extract_room_from.remove(sid)
    except ValueError:
        if not isinstance(list_to_extract_room_from, list):
            raise ValueError(f"{list_to_extract_room_from.__class__} is not instance of type list")
        elif not len(list_to_extract_room_from):
            raise ValueError(f"{list_to_extract_room_from=}. It must contain at least 1 element")
    return list_to_extract_room_from[0]
