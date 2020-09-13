# pytorch

# 自动求导

# 回归问题

# 神经网络

手写识别

- *Recap*
    - H1 = relu(XW1 + b1)
    - H2 = relu(H1W2 + b2)
    - H3 = relu(H2W3 + b3)

- *steps*
    - load data
    - Build Model
    - Train
    - Test

How to denote string

- One-hot
    - [0,1,0,0,...]
- Embedding
    - Word2vec
    - glove

uninitialized

- Torch.empty()

- Torch.FloatTensor(d1, d2, d3)

- Torch.IntTensor(d1, d2, d3)

# rand/rand_like, randint

# 转置 t()

# transpose 转置

# premute 压入

＃ Broadcasting 

- Expand
- without copying data

Key idea

- Insert 1 dim ahead
- Expand dims with size 1 to same size 
- Feature maps: [4, 32, 14, 14]
- Bias: [32, 1, 1] => [1, 32, 1, 1] => [4, 32, 14, 14]

# Merge or split
> 拼接与拆分
- Cat
- Stack
- Split(按长度)
- Chunk(按数量)


Math operation

dim keepdim

How to search for minima
