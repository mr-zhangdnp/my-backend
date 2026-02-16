from fastapi import FastAPI

# 创建FastAPI应用实例
app = FastAPI()

# 定义一个最简单的根路径路由
@app.get("/")
async def root():
    return {"message": "FastAPI后端运行证明奥里给"}

# 一个模拟登录的接口，用于小程序测试
@app.get("/test")
async def test_api():
    return {"status": "success", "data": "这是一个测试接口，用于小程序对接"}