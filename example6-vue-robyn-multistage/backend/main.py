from robyn import Robyn, Request
from robyn.responses import serve_file, serve_html

app = Robyn(__name__)

@app.get("/hello")
async def root():
    return "Hello from the Robyn backend!"

@app.get("/")
async def root():
    
    return serve_html("/frontend/index.html")

@app.get("/*extra")
async def serve_static_assets(request: Request):
    extra = request.path_params["extra"]
    print("extra:", extra)
    return serve_file(f"/frontend/{extra}")


def main():
    app.start(host="0.0.0.0", port=8123)


if __name__ == "__main__":
    main()
