from aiogram.fsm.state import StatesGroup, State


class UserStates(StatesGroup):
    user_choice_button = State()
    user_choice_city = State()
