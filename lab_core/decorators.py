import functools
from datetime import datetime

# TODO: make env file and add there the log file
# TODO: make is_promotable(self) method and call it in decorator
def log_calls(func):
    from lab_core.context import FileLogger
    @functools.wraps(func)
    def wrapper(self, *args, **kwargs):
        func_name = func.__name__
        date = datetime.now()
        log_text = (
            f"[{date.strftime('%Y-%m-%d %H:%M:%S')}] "
            f"CALL: {func_name} | "
            f"OBJECT: {repr(self)}"
            "\n"
        )
        result = func(self, *args, **kwargs)
        log_path = getattr(self, "_log_path", "logs.txt")
        with FileLogger(path=log_path) as f:
            f.write(log_text)
        return result
    return wrapper

def requires_publications(minimum=10):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(self, *args, **kwargs):
            pubs_check = self.publications >= minimum
            exp_check = self.experience_years > 5
            has_field = self.field != "unknown"
            if pubs_check and exp_check and has_field:
                result = func(self, *args, **kwargs)
            else:
                raise ValueError("Scientist is required to have more expertise.")
            return result
        return wrapper
    return decorator
