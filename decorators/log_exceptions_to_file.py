import functools


def log_exceptions_to_file(file_path):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            try:
                return func(*args, **kwargs)
            except Exception as e:
                with open(file_path, 'a') as file:
                    file.write(f"Method: {func.__name__}, Exception: {type(e).__name__}\n")
                raise
        return wrapper
    return decorator
