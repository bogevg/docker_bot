from docker.models.containers import Container
from docker.models.images import Image
from docker import DockerClient

def get_all_cont(client: DockerClient) -> list[Container]:
    arr_cont = client.containers.list(all=True)
    return arr_cont

def get_cont_id_by_name(client: DockerClient, name:str)-> int:
    cont = client.containers.get(name)
    if cont:
        return cont.id
    else:
        return -1

def get_cont_name_by_id(client: DockerClient, id:str)-> int:
    cont = client.containers.get(id)
    if cont:
        return cont.name
    else:
        return "not exist"

def start_cont_by_id(client: DockerClient, cont_id: str) -> str:
    cont = client.containers.get(cont_id)
    if cont:
        cont.start()
        return "контейнер запущен"
    else:
        return "такого контейнера нет"

def restart_cont_by_id(client: DockerClient, cont_id: str) -> str:
    cont = client.containers.get(cont_id)
    if cont:
        cont.restart()
        return "контейнер перезапущен"
    else:
        return "такого контейнера нет"

def stop_cont_by_id(client: DockerClient, cont_id: str) -> str:
    cont = client.containers.get(cont_id)
    if cont:
        cont.stop()
        return "контейнер остановлен"
    else:
        return "такого контейнера нет"


def remote_by_name(client: DockerClient, cont_id: str) -> str:
    cont = client.containers.get(cont_id)
    if cont:
        cont.start()
        return "контейнер удален"
    else:
        return "такого контейнера нет"


def create_image_by_df(client: DockerClient, path_df: str, path: str, name: str):
    image, build_logs = client.images.build(path = path, dockerfile =path_df, tag = name)

def get_all_cont(client: DockerClient) -> list[Image]:
    arr_images = client.images.list()
    return arr_images


