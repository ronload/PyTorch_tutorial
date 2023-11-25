# This file is used to test `tensor` data type
import torch

test = torch.tensor(1)
test = torch.Tensor(1)

print(torch.tensor(0))
# create a tensor and initialize as 0
# [[0, 0, 0],
#  [0, 0, 0]]
print(torch.zeros(2, 3))

# create a tensor and initialize as 1
# [[1, 1, 1],
#  [1, 1, 1]]
print(torch.ones(2, 3))

# 0D tensor(scalar)
t1 = torch.tensor(
    ([1, 2, 3], [3, 4, 5]),
    dtype=torch.int64,
    device=torch.device("cpu"),
    requires_grad=False
)
print(t1.shape)
print(t1.dtype)  # dtype is default as `torch.int64`
print(t1.ndim)
print(t1.size())

# create a
print(torch.randint(0, 10, (2, 3)))