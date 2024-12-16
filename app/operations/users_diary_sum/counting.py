from sqlalchemy import select

from app.entities.products.classes import Product

from app.entities.users_diary.models import UserDiary as UserDiaryDB
from app.entities.diary.models import Diary as DiaryDB

from app.database.connect import AsyncSession


async def update_users_diary(
    data: DiaryDB,
    product: Product,
    session: AsyncSession,
):
    query = await session.execute(select(UserDiaryDB).where(UserDiaryDB.day == data.day,
                                                            UserDiaryDB.user_id == data.user_id))
    result = query.scalar_one_or_none()
    
    if result is None:

        new_record = UserDiaryDB(
            user_id=data.user_id,
            day=data.day,
            sum_proteins=(data.count / 100) * product.proteins,
            sum_fats=(data.count / 100) * product.fats,
            sum_carbohydrates=(data.count / 100) * product.carbohydrates,
            sum_calories=(data.count / 100) * product.calories,
        )
        
        session.add(new_record)
    else:
        result.sum_proteins+=(data.count / 100) * product.proteins
        result.sum_fats+=(data.count / 100) * product.fats
        result.sum_carbohydrates+=(data.count / 100) * product.carbohydrates
        result.sum_calories+=(data.count / 100) * product.calories

    await session.commit()

    return result or new_record

        