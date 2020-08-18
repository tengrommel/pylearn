import torch
import time

if __name__ == '__main__':
    print(torch.__version__)
    print(torch.cuda.is_available())
    a = torch.randn(10000, 1000)
    b = torch.randn(1000, 2000)

    t0 = time.time()
    c = torch.matmul(a, b)
    t1 = time.time()
    print(a.device, t1 - t0, c.norm(2))

    device = torch.device('cuda')
    a = a.to(device)
    b = b.to(device)

    # 第一运行中会有初始化的功能
    t0 = time.time()
    c = torch.matmul(a, b)
    t2 = time.time()
    print(a.device, t2 - t0, c.norm(2))

    t0 = time.time()
    c = torch.matmul(a, b)
    t2 = time.time()
    print(a.device, t2 - t0, c.norm(2))
