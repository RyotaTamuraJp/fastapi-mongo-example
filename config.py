from pydantic import Field
from pydantic_settings import BaseSettings


class DBConfig(BaseSettings):
    DB_USERNAME: str = Field(description="DBのユーザ名")
    DB_PASSWORD: str = Field(description="DBのパスワード")
    DB_HOST: str = Field(description="DBのホスト名")
    DB_PORT: str = Field(description="DBのポート番号")


db_config = DBConfig()
