from asyncpg.connection import Connection

from .AsyncObject import Aobject

from typing import Optional

class Message(Aobject):
    async def __init__(self, conn: Optional[Connection], content: Optional[str]):
        await conn.execute(
            "INSERT INTO message(content) VALUES($1)",
            content.split(":")[1]
        )