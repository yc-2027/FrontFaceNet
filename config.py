import argparse
import os

def str2bool(x):
    return x.lower() in ('true')

parser = argparse.ArgumentParser('FrontFaceNet')

# naming / file handling
parser.add_argument('--model_name', default='FrontFaceNet', help='segmentation models')
parser.add_argument('--data_dir', default='./datasets/uprightnet15/', help='point clouds dataset folder')
parser.add_argument('--model_dir', default='./models/', help='training models log folder')
parser.add_argument('--model_file', default='model.pth', help='pretrained network models file')
#parser.add_argument('--gpu_idx', type=str, default='0,1,2')

# training parameters
parser.add_argument('--epoch',  default=1, type=int, help='number of epoch in training')
parser.add_argument('--batch_size', type=int, default=128, help='batch size in training')
parser.add_argument('--seed', type=int, default=-1, help='manual seed')
parser.add_argument('--learning_rate', default=0.001, type=float, help='learning rate in training')
parser.add_argument('--weight_decay', type=float, default=1e-4, help='weight decay (L2 penalty) of Adam optimizer')
parser.add_argument('--decay_rate', type=float, default=0.01, help='decay rate of learning rate')
parser.add_argument('--no_decay', type=str2bool, default=False)

# models hyperparameters
parser.add_argument('--alpha', default=0.1, type=float, help='coefficient of fitting residual loss function')
parser.add_argument('--num_points', type=int, default=2048)
parser.add_argument('--sym_op', type=str, default='max', help='symmetry operation')

parser.add_argument('--restore', action='store_true')

opts = parser.parse_args()
