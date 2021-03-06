from sqlalchemy import update as sqlalchemy_update
from sqlalchemy.future import select

from src.database.database import async_db_session


class Crud:
    @classmethod
    async def create(cls, **kwargs):
        async_db_session.add(cls(**kwargs))
        await async_db_session.commit()

    @classmethod
    async def update(cls, id, **kwargs):
        query = (
            sqlalchemy_update(cls)
            .where(cls.id == id)
            .values(**kwargs)
            .execution_options(synchronize_session="fetch")
        )

        await async_db_session.execute(query)
        await async_db_session.commit()

    @classmethod
    async def update_by_user_id(cls, id, **kwargs):
        query = (
            sqlalchemy_update(cls)
            .where(cls.user_id == id)
            .values(**kwargs)
            .execution_options(synchronize_session="fetch")
        )

        await async_db_session.execute(query)
        await async_db_session.commit()

    @classmethod
    async def get(cls, id):
        query = select(cls).where(cls.id == id)
        results = await async_db_session.execute(query)
        try: 
            results = await async_db_session.execute(query)
            print(results)
            return results.scalars().first()
        except Exception as e:
            return None


    @classmethod
    async def get_by_user_id(cls, id):
        query = select(cls).where(cls.user_id == id)
        results = await async_db_session.execute(query)
        try: 
            results = await async_db_session.execute(query)
            print(results)
            return results.scalars().first()
        except Exception as e:
            return None
        

    @classmethod
    async def fetch_transactions(cls, id):
        query = select(cls).where(cls.user_id == id).order_by(cls.created_at.desc())
        results = await async_db_session.execute(query)
        
        return results.all()

