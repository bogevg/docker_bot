from aiogram.fsm.state import State, StatesGroup


class DockerStates(StatesGroup):
    get_all_cont = State()
    get_cont_id_by_name = State()
    start_cont_by_id = State()
    restart_cont_by_id = State()
    stop_cont_by_id = State()
    remote_cont_by_id = State()
    create_image_by_df = State()
    get_all_images = State()
