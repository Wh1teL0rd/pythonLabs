import functools
import inspect


def log_arguments_to_file(file_path):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(self, *args, **kwargs):
            with open(file_path, 'a') as file:
                file.write(f"{func.__name__}: ")
                signature = inspect.signature(func)
                bound_args = signature.bind(self, *args, **kwargs)
                for name, value in bound_args.arguments.items():
                    if name != 'self':
                        file.write(f"{name}={value}, ")
                file.write('\n')
            return func(self, *args, **kwargs)
        return wrapper
    return decorator
