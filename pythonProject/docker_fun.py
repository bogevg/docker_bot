from docker.models.containers import Container
from docker.models.images import Image
from docker import DockerClient, errors

def get_all_cont(client: DockerClient) -> list[Container]:
    arr_cont = client.containers.list(all=True)
    return arr_cont

def get_cont_id_by_name(client: DockerClient, name:str)-> str:
    try:
        cont = client.containers.get(name)
    except errors.NotFound :
        return "not exist"
    return cont.id

def get_cont_name_by_id(client: DockerClient, id:str)-> str:
    try:
        cont = client.containers.get(id)
    except errors.NotFound :
        return "not exist"
    return cont.name


def start_cont_by_id_or_name(client: DockerClient, cont_id: str) -> str:
    try:
        cont = client.containers.get(cont_id)
        cont.start()
    except errors.NotFound:
        return "not exist"
    return "контейнер запущен"

def run_cont_by_image(client: DockerClient, name_image: str):
    try:
        cont = client.containers.run(name_image, detach= True)
        name_cont = cont.name
    except errors.NotFound:
        return "not exist"
    except errors.BuildError:
        return "build error"
    except:
        return "error"
    return f'контейнер создан под именем {name_cont}'




def restart_cont_by_id_or_name(client: DockerClient, cont_id: str) -> str:
    try:
        cont = client.containers.get(cont_id)
        cont.restart()
    except errors.NotFound:
        return "not exist"
    return "контейнер перезапущен"


def stop_cont_by_id_or_name(client: DockerClient, cont_id: str) -> str:
    try:
        cont = client.containers.get(cont_id)
        cont.stop()
    except errors.NotFound:
        return "not exist"
    return "контейнер остановлен"



def remove_cont_by_id_or_name(client: DockerClient, cont_id: str) -> str:
    try:
        cont = client.containers.get(cont_id)
        cont.remove()
    except errors.NotFound:
        return "not exist"
    return "контейнер удален"





