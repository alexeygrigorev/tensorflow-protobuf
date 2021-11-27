with open('.version') as f_in:
    TF_VERSION = f_in.read().strip()

__version__ = TF_VERSION
