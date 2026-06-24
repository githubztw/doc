"""
Python多线程实战示例（适用3.12+）
包含5个典型应用场景及最佳实践
"""
import threading
import concurrent.futures
import queue
import time
import os
from typing import List, Dict, Any
from dataclasses import dataclass
END_MARKER = object()
# 场景1：并行处理多个文件（I/O密集型）
def process_file(file_path: str, result_lock: threading.Lock) -> None:
    """
    模拟文件处理任务，演示资源锁的使用
    """
    # 模拟耗时操作（如解析大文件）
    time.sleep(0.1)
    
    with result_lock:
        print(f"[{threading.current_thread().name}] 处理完成: {os.path.basename(file_path)}")

def parallel_file_processing(file_list: List[str]) -> None:
    lock = threading.Lock()
    with concurrent.futures.ThreadPoolExecutor(max_workers=4) as executor:
        futures = [executor.submit(process_file, f, lock) for f in file_list]
        for future in concurrent.futures.as_completed(futures):
            future.result()

# 场景2：生产者-消费者模式（任务队列）
@dataclass
class Task:
    id: int
    data: Any

def producer(task_queue: queue.Queue, num_tasks: int, consumer_count: int) -> None:
    """生产者线程：生成待处理任务"""
    try:
        for i in range(num_tasks):
            task = Task(i, f"Data-{i}")
            task_queue.put(task)  # 队列满时会自动阻塞
            time.sleep(0.05)
    finally:
        # 发送与消费者数量相等的结束标记
        for _ in range(consumer_count):
            task_queue.put(END_MARKER)

def consumer(task_queue: queue.Queue) -> None:
    """消费者线程：处理任务"""
    try:
        while True:
            task = task_queue.get()
            if task is END_MARKER:
                print(f"[{threading.current_thread().name}]') 结束")
                break
            try:
                if isinstance(task, Task):  # 添加类型检查
                   print(f"[{threading.current_thread().name}] 处理任务 {task.id}: {task.data}")
                else:
                   print(f"收到非任务对象: {type(task)} - {task}")
            except AttributeError as e:
                    print(f"无效任务对象: {task} | 错误: {str(e)}")
            finally:
                # 标记任务完成，从队列中数据
                task_queue.task_done()
            time.sleep(0.1)

    finally:
        # 标记任务完成
        task_queue.task_done()  

def run_producer_consumer():
    """任务队列演示"""
    task_queue = queue.Queue(maxsize=10)
    consumer_count = 2
    
    # 创建并启动消费者（设置为守护线程）
    # 通过列表推导式生成了指定数量的消费者线程，并为每个线程设置了目标函数、参数和名称
    consumers = [
        threading.Thread(target=consumer, args=(task_queue,), name=f"Consumer-{i+1}")
        for i in range(consumer_count)
    ]
    for t in consumers:
        t.start()

    # 创建并启动生产者（传递consumer_count而不是consumers列表）
    producer_thread = threading.Thread(
        target=producer,
        args=(task_queue, 10, consumer_count),
        name="Producer"
    )
    producer_thread.start()

    # 等待生产者完成
    producer_thread.join()
    
    # 等待所有任务处理完成
    task_queue.join()

# 场景3：线程安全计数器（共享资源保护）
class SafeCounter:
    """带锁保护的计数器（演示线程安全）"""
    def __init__(self):
        self._value = 0
        self._lock = threading.Lock()
    
    def increment(self) -> None:
        with self._lock:
            self._value += 1
    
    @property
    def value(self) -> int:
        with self._lock:
            return self._value

def test_counter() -> None:
    """多线程计数器压力测试"""
    counter = SafeCounter()
    threads = []
    
    def worker():
        for _ in range(1000):
            counter.increment()
    
    # 创建10个线程同时修改计数器
    for _ in range(10):
        t = threading.Thread(target=worker)
        threads.append(t)
        t.start()
    
    for t in threads:
        t.join()
    
    print(f"最终计数: {counter.value} (预期: 10000)")

# 场景4：定时任务调度
class Scheduler:
    """简易定时任务调度器"""
    def __init__(self):
        self._timer = None
        self._is_running = False
    
    def _run_task(self, interval: int, task_func) -> None:
        if self._is_running:
            task_func()
            self._timer = threading.Timer(interval, self._run_task, args=(interval, task_func))
            self._timer.start()
    
    def start(self, interval: int, task_func) -> None:
        """启动定时任务"""
        if not self._is_running:
            self._is_running = True
            self._run_task(interval, task_func)
    
    def stop(self) -> None:
        """停止定时任务"""
        self._is_running = False
        if self._timer:
            self._timer.cancel()

# 场景5：Web请求批处理（模拟）
def batch_web_requests(urls: List[str], timeout: float = 5.0) -> Dict[str, str]:
    """使用线程池批量请求"""
    from collections import defaultdict
    results = defaultdict(str)
    lock = threading.Lock()
    
    def fetch(url: str):
        try:
            # 模拟网络请求（实际应使用requests库）
            time.sleep(0.1)
            with lock:
                results[url] = "OK"
        except Exception as e:
            with lock:
                results[url] = f"Error: {str(e)}"
    
    with concurrent.futures.ThreadPoolExecutor() as executor:
        future_to_url = {
            executor.submit(fetch, url): url
            for url in urls
        }
        for future in concurrent.futures.as_completed(future_to_url, timeout=timeout):
            future.result()
    
    return results

if __name__ == "__main__":
    # 执行示例
    print("=== 文件处理演示 ===")
    files = [f"data/file_{i}.txt" for i in range(5)]
    parallel_file_processing(files)
    
    print("\n=== 生产者-消费者演示 ===")
    run_producer_consumer()
    
    print("\n=== 线程安全计数器测试 ===")
    test_counter()
    
    print("\n=== 定时任务演示 ===")
    def print_time():
        print(f"定时任务执行于: {time.strftime('%H:%M:%S')}")
    
    scheduler = Scheduler()
    scheduler.start(1, print_time)
    time.sleep(3)
    scheduler.stop()
    print("定时任务已停止")

    print("\n=== Web请求批处理演示 ===")
    urls = ["https://example.com/1", "https://example.com/2"]
    print(batch_web_requests(urls))
