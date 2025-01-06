from model import Model
from config import opts

print(f"Data directory being used: {opts.data_dir}")

if __name__ == '__main__':
    model = Model(opts)
    model.test()

