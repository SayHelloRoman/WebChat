from typing import NoReturn
import asyncio
import asyncpg
import json
import os


async def main() -> NoReturn:
    with open("../ConfigDB.json") as f:
        conn = await asyncpg.connect(
            **json.load(f)
        )

    await conn.execute('''
    CREATE TABLE message(
    id SERIAL,
    content text
    );
    ''')

    await conn.close()


if __name__ == "__main__":
    asyncio.get_event_loop().run_until_complete(main())