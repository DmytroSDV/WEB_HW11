from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from source.models.models import User
from source.schemas.user import UserSchema

async def get_users(limit: int, offset: int, db: AsyncSession):
    search = select(User).offset(offset).limit(limit)
    users = await db.execute(search)
    return users.scalars().all()


async def get_user(user_id: int, db: AsyncSession):
    search = select(User).filter_by(id=user_id)
    user = await db.execute(search)
    return user.scalar_one_or_none()


async def create_user(body: UserSchema, db: AsyncSession):
    user = User(**body.model_dump(exclude_unset=True))
    db.add(user)
    await db.commit()
    await db.refresh(user)
    return user


async def update_user(user_id: int, body: UserSchema, db: AsyncSession):
    search = select(User).filter_by(id=user_id)
    result = await db.execute(search)
    user = result.scalar_one_or_none()
    if search:
        search.title = body.title
        search.description = body.description
        search.completed = body.completed
        await db.commit()
        await db.refresh(search)
    return  search


async def delete_user(user_id: int, db: AsyncSession):
    search = select(User).filter_by(id=user_id)
    user = await db.execute(search)
    user = user.scalar_one_or_none()
    if user:
        await db.delete(user)
        await db.commit()
    return user
