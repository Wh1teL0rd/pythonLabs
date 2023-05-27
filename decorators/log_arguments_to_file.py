import functools


def log_arguments_to_file(file_path):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            with open(file_path, 'a') as file:
                file.write(f"{func.__name__}: ")
                for arg_name, arg_value in kwargs.items():
                    file.write(f"{arg_name}={arg_value} ")
                file.write('\n')
            return func(*args, **kwargs)
        return wrapper
    return decorator
