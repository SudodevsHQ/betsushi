from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import declarative_base, sessionmaker
from starlette.config import Config
Base = declarative_base()


class AsyncDatabaseSession:
    def __init__(self):
        self._session = None
        self._engine = None
        self.config = Config(".env")
        self.password = self.config.get("POSTGRES_PASSWORD", cast=str)

    def __getattr__(self, name):
        return getattr(self._session, name)

    async def init(self):
        host = self.config.get('POSTGRES_HOST', cast=str,  default='localhost')
        self._engine = create_async_engine(
            f"postgresql+asyncpg://root:{self.password}@{host}/indipe",
            echo=True,
        )

        self._session = sessionmaker(
            self._engine, expire_on_commit=False, class_=AsyncSession
        )()

    async def create_all(self):
        async with self._engine.begin() as conn:
            await conn.run_sync(Base.metadata.create_all)


async_db_session = AsyncDatabaseSession()
