from __future__ import print_function

import json
import os
import multiprocessing

workers_per_core_str = os.getenv("WORKERS_PER_CORE", 4)
cores_count = os.getenv("CORES_COUNT",multiprocessing.cpu_count())
host = os.getenv("HOST", "0.0.0.0")
port = os.getenv("PORT", "8010")
bind_env = os.getenv("BIND", None)
use_loglevel = os.getenv("LOG_LEVEL", "info")
if bind_env:
    use_bind = bind_env
else:
    use_bind = "{host}:{port}".format(host=host, port=port)
try:
    workers_per_core = int(workers_per_core_str)
    cores_count = int(cores_count)
except ValueError as e:
    raise e from None

workers_count = workers_per_core * cores_count
assert workers_count > 0

# Gunicorn config variables
loglevel = use_loglevel
workers = workers_count
bind = use_bind
keepalive = 120
errorlog = "-"

# For debugging and testing
log_data = {
    "loglevel": loglevel,
    "workers": workers,
    "bind": bind,
    # Additional, non-gunicorn variables
    "workers_per_core": workers_per_core,
    "host": host,
    "port": port,
}
print(json.dumps(log_data))