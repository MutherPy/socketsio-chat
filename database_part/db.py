import typing as t


class DBMock:
    def __init__(self):
        self.base = dict()
        self.users = dict()

    async def __aenter__(self):
        return self

    async def __aexit__(self, exc_type, exc_val, exc_tb):
        for room, members in self.base.items():
            if not members:
                self.base.pop(room)

    def _create_room(self, room: str) -> dict:
        self.base[room] = {}
        return self.base[room]

    async def get_room_members(self, room: str) -> t.Union[dict, None]:
        return self.base.get(room)

    async def add_room_member(self, room: str, sid: str, username: str) -> str:
        _room = await self.get_room_members(room)
        if not _room:
            self._create_room(room)[sid] = username
            _room = await self.get_room_members(room)
        else:
            _room[sid] = username
        return _room[sid]

    async def get_member(self, room: str, sid: str) -> t.Union[str, None]:
        members = await self.get_room_members(room)
        if isinstance(members, dict):
            return members.get(sid)
        return None

    async def remove_member(self, room: str, sid: str) -> t.NoReturn:
        members = await self.get_room_members(room)
        members.pop(sid)

    def get_user(self, username: str, password: str) -> str:
        user = self.users.get(username)
        if not user:
            self.users[username] = password
            user = username
        return user

    def proof_user(self, user: str) -> bool:
        return user in self.users


db = DBMock()
