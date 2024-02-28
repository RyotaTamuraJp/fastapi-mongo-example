from db.session import client, get_db
from fastapi import FastAPI

app = FastAPI(
    title="FastAPI Sample",
)


@app.on_event("shutdown")
def shutdown_event():
    client.close()


@app.get("/", status_code=200)
def root():
    return "成功！"


@app.post("/box", status_code=200)
def post_item_in_box(item: str):
    # dbというデータベースを取得
    db = get_db()
    # データベースにデータを追加
    result = db["box"].insert_one({"item": item})
    return {"id": str(result.inserted_id)}


@app.get("/box", status_code=200)
def get_items_in_box():
    # dbというデータベースを取得
    db = get_db()
    # データベースからデータを取得
    items = db["box"].find()
    # データを整形
    results = [{"id": str(item["_id"]), "item": item["item"]} for item in items]
    return results
