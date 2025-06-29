from setuptools import setup, find_packages

setup(
    name="paper-genie",
    version="0.1.0",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    include_package_data=True,
    install_requires=[
        "fastapi>=0.95.0",
        "uvicorn>=0.2.0",
        "sqlmodel>=0.0.8",
        "pymilvus>=2.3.3",
        "openai>=1.0.0",
        "pyyaml>=6.0",
        "python-dotenv>=1.0.0",
        "starlette>=0.27.0",
        "pytest>=7.0",  # 可选：用于测试
    ],
    extras_require={
        "dev": [
            "pytest>=7.0",
            "black>=23.0",
            "isort>=5.0",
            "mypy>=1.0",
        ],
    },
    entry_points={
        "console_scripts": [
            "run-app=main:main",
        ],
    },
    author="BillyGet",
    author_email="GYFwork@aliyun.com",
    description="Paper Genie - A RAG-based paper Q&A and Wiki generation system",
    long_description=open("README.md", encoding="utf-8").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/BillyGet79/PaperGenie",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.9',
)
