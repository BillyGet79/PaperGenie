from fastapi import APIRouter

from interface.schemas.base_response import BaseResponse

router = APIRouter(prefix="/hello")


@router.get("/", summary="项目介绍")
def hello():
    data = "欢迎使用 PaperGenie —— 一个面向科研工作者的智能论文知识系统。该项目支持导入学术论文（PDF 或元数据），通过大语言模型（LLM）进行结构化解析与详细介绍生成。同时，系统会将论文向量化处理，并构建语义索引，使得模型具备跨论文、跨主题的研究理解与问答能力。PaperGenie 致力于打造一个可交互、可协作、可拓展的科研知识 Wiki 平台，助力科研人员更高效地掌握文献与洞察研究趋势。"
    return BaseResponse.success(data=data)
