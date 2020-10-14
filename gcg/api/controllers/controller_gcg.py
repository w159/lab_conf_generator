from datetime import datetime

from gcg.api.controllers import ControllerResult
from gcg.core import Genesis, Task


def controller_gcg(json_data, store_aws=False, **kwargs):
    config_gen = Genesis()

    task = Task.new(data=json_data, name=kwargs.get("name"))

    config_gen.add_task(task)
    config_gen.generate(
        store_aws=store_aws,
        aws_access_key=kwargs.get("aws_access_key"),
        aws_secret_key=kwargs.get("aws_secret_key"),
        lab_name=kwargs.get("lab_name")
    )

    return ControllerResult(data=task.rendered_data, result=True, msg="Successful", status=200)


def controller_gcg_v2(data, **kwargs):
    store_aws = kwargs.get("store_aws", False)
    store_local = kwargs.get("store_local", False)
    name = kwargs.get("name")
    lab_name = kwargs.get("lab_name", f'GCG_{str(datetime.now().strftime("%m_%d_%Y"))}')
    template_type = kwargs.get("template_type")
    description = kwargs.get("description")
    save_location = kwargs.get("save_location")

    genesis = Genesis()

    task = Task(
        data=data,
        template_type=template_type,
        name=name,
        description=description
    )

    genesis.generate_config_from_task(
        task=task,
        lab_name=lab_name,
        store_aws=store_aws,
        store_local=store_local,
        save_location=save_location
    )

    return ControllerResult(data=task.rendered_data, result=True, msg="Successful", status=200)


pass
