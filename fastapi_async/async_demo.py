import asyncio
import time


async def hello_world():
    """最简单的异步函数示例"""
    print("开始执行异步函数")
    
    # 模拟异步操作 - 等待1秒
    await asyncio.sleep(1)
    
    print("异步操作完成！")
    return "Hello, World!"


async def main():
    """主函数，用于运行异步函数"""
    print("程序开始")
    
    # 调用异步函数
    result = await hello_world()
    
    print(f"函数返回值: {result}")
    print("程序结束")


# 运行异步程序
if __name__ == "__main__":
    asyncio.run(main()) 