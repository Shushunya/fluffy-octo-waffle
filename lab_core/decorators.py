import functools
from datetime import datetime

# TODO: make env file and add there the log file
# TODO: make is_promotable(self) method and call it in decorator
def log_calls(func):
    from context import FileLogger
    @functools.wraps(func)
    def wrapper(self, *args, **kwargs):
        func_name = func.__name__
        date = datetime.now()
        log_text = f"{date}     {func_name}    {repr(self)}\n"
        result = func(self, *args, **kwargs)
        with FileLogger() as f:
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
