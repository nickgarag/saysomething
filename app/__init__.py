from flask import Flask
from opentelemetry import trace
from opentelemetry.exporter import jaeger
from opentelemetry.sdk.trace import TracerProvider
from opentelemetry.sdk.trace.export import ConsoleSpanExporter, SimpleExportSpanProcessor, BatchExportSpanProcessor
from logging.config import dictConfig

dictConfig({
    'version': 1,
    'formatters': {'default': {
        'format': '{"date_time": %(asctime)s, "log_level": %(levelname)s, "module": %(module)s, %(message)s}',
    }},
    'handlers': {'wsgi': {
        'class': 'logging.StreamHandler',
        'stream': 'ext://flask.logging.wsgi_errors_stream',
        'formatter': 'default'
    },
     'console': {
      'class': 'logging.StreamHandler',
      'stream': 'ext://sys.stdout',
      'formatter': 'default'
    }},
    'root': {
        'level': 'INFO',
        'handlers': ['console']
    }
})



app = Flask(__name__)
app.config.from_object("config.Config")

trace.set_tracer_provider(TracerProvider())
jaeger_exporter = jaeger.JaegerSpanExporter(
    service_name=app.config['SERVICE_NAME'],
    agent_host_name=app.config['AGENT_HOST_NAME'],
    agent_port=app.config['AGENT_PORT'],
)

trace.get_tracer_provider().add_span_processor(
    BatchExportSpanProcessor(jaeger_exporter)
)
tracer = trace.get_tracer(__name__)

from app import routes