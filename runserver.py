import uvicorn
from backend.core import cfg

if __name__ == "__main__":
    uvicorn.run(
        "backend.main:app",
        host=cfg["host"],
        port=cfg["port"],
        reload=True,
    )
