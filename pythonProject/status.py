from aiogram.fsm.state import State, StatesGroup


class DockerStates(StatesGroup):
    get_cont_id_by_name = State()
    get_cont_name_by_id = State()
    start_cont = State()
    build_cont = State()
    restart_cont = State()
    stop_cont = State()
    remote_cont = State()
