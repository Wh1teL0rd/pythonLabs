import logging


def logged(custom_exception, mode):
    def decorator(func):
        def wrapper(*args, **kwargs):
            try:
                return func(*args, **kwargs)
            except custom_exception as e:
                if mode == "console":
                    logging.basicConfig(level=logging.INFO)
                    logging.error(e)
                elif mode == "file":
                    logging.basicConfig(level=logging.INFO, filename="exception.log", filemode="a")
                    logging.error(e)
                else:
                    raise ValueError("Invalid logging mode. Please choose 'console' or 'file'.")
        return wrapper
    return decorator
