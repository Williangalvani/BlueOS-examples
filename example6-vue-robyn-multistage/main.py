from robyn import Robyn
from robyn.responses import serve_file, serve_html

app = Robyn(__name__)

@app.get("/hello")
async def root():
    return "Hello from the Robyn backend!"

@app.get("/")
async def root():
    return serve_html("dist/index.html")

@app.get("/register_service")
def register_service():
    return serve_file("src/register_service")

@app.get("/assets/:path")
async def serve_static_assets(path_params):
    path = path_params["path"]
    return serve_file(f"dist/assets/{path}")


def main():
    app.start(host="0.0.0.0", port=8123)


if __name__ == "__main__":
    main()
