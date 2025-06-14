import os

import yaml
from pydantic import BaseModel

from infrastructure.utils.local_path_utils import get_root_path


class DatabaseConfig(BaseModel):
    url: str


class AppConfig(BaseModel):
    port: int

class Config(BaseModel):
    database: DatabaseConfig
    app: AppConfig


def load_config():
    root_path = get_root_path()
    config_path = os.path.join(root_path, 'config.yml')
    with open(config_path, encoding='utf-8') as f:
        config_dict = yaml.load(f, Loader=yaml.FullLoader)
    return Config(**config_dict)


_config = load_config()


def get_config() -> Config:
    return _config
