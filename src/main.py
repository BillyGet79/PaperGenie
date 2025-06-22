from contextlib import asynccontextmanager

from fastapi import FastAPI, Request
from starlette.responses import JSONResponse
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())

from infrastructure.db.database import create_db_and_tables
from infrastructure.error.custom_error import CustomException
from infrastructure.utils.log_utils import logger
from interface.schemas.base_response import BaseResponse
from interface.routers.hello_router import router as hello_router
from interface.routers.repository_test_router import router as repository_test_router


@asynccontextmanager
async def lifespan(app: FastAPI):
    # Initialize resources here if needed
    create_db_and_tables()
    yield
    # Cleanup resources here if needed


app = FastAPI(
    title="Paper Genie API",
    description="Paper Genie 项目接口文档",
    version="v25.0.0",
    lifespan=lifespan
)

prefix = "/api/paper-genie-open/v1"

app.include_router(hello_router, prefix=prefix, tags=["hello"])
app.include_router(repository_test_router, prefix=prefix, tags=["repository_test"])


@app.exception_handler(CustomException)
async def custom_exception_handler(request: Request, exc: CustomException):
    logger.error(request, exc)
    return JSONResponse(
        status_code=500,
        content=BaseResponse.error(code=exc.code, message=exc.message).__dict__,
    )


@app.exception_handler(Exception)
async def exception_handler(request, exc: Exception):
    return JSONResponse(
        status_code=500,
        content=BaseResponse.internal_error().__dict__,
    )


def log_error(request: Request, exc: Exception):
    method = request.method
    url = request.url
    query_params = request.query_params
    logger.error(f"{method}: {url}, query_params: {query_params}, error: {exc.__str__()}")


if __name__ == '__main__':
    import uvicorn

    print("http://127.0.0.1:49336/docs")
    uvicorn.run("main:app", host="127.0.0.1", port=49336)
