# This file is used to test TensorBoard
from torch.utils.tensorboard import SummaryWriter

writer = SummaryWriter("logs")

for x in range(100):
    writer.add_scalar("y = x^2", x**2, x)

writer.close()