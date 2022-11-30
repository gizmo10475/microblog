from prometheus_flask_exporter.multiprocess import GunicornInternalPrometheusMetrics

def child_exit(serverr, worker):
    GunicornInternalPrometheusMetrics.mark_process_dead_on_child_exit(worker.pid)