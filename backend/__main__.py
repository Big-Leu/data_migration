import os
import shutil
import uvicorn


def main() -> None:
    uvicorn.run(
        "backend.api.application:get_app",
        workers=1,
        host='127.0.0.1',
        port=8000,
        reload=True,
    )

if __name__ == "__main__":
    main()
