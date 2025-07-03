from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import asyncio
from async_demo import hello_world

# 创建FastAPI应用实例
app = FastAPI(title="异步函数演示API", description="使用FastAPI调用异步函数的示例")

# 添加CORS中间件，允许前端页面访问
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # 允许所有来源，生产环境中应该限制
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
async def root():
    """根路径，返回欢迎信息"""
    return {"message": "欢迎使用异步函数演示API！"}


@app.get("/hello")
async def call_async_function():
    """调用异步函数的端点"""
    print("收到API请求，开始调用异步函数...")
    
    # 调用async_demo.py中的hello_world函数
    result = await hello_world()
    
    return {
        "message": "异步函数调用成功",
        "result": result,
        "status": "completed"
    }


@app.get("/hello-multiple/{count}")
async def call_async_multiple_times(count: int):
    """多次调用异步函数的端点"""
    if count > 10:
        return {"error": "调用次数不能超过10次"}
    
    results = []
    for i in range(count):
        print(f"第 {i+1} 次调用异步函数...")
        result = await hello_world()
        results.append(f"第{i+1}次: {result}")
    
    return {
        "message": f"成功调用异步函数 {count} 次",
        "results": results,
        "total_calls": count
    }


