import os

class Config:
    DEBUG = os.getenv('DEBUG', 'False').lower() in ('true', '1', 't')
    SECRET_KEY = os.getenv('SECRET_KEY', 'your-secret-key')
    DATABASE_URI = os.getenv('DATABASE_URI', 'sqlite:///ecs.db')
    MQTT_BROKER_URL = os.getenv('MQTT_BROKER_URL', 'localhost')
    MQTT_BROKER_PORT = int(os.getenv('MQTT_BROKER_PORT', 1883))

class DevelopmentConfig(Config):
    DEBUG = True
    DATABASE_URI = 'sqlite:///dev_ecs.db'

class ProductionConfig(Config):
    DEBUG = False
    DATABASE_URI = os.getenv('DATABASE_URI', 'sqlite:///ecs.db')

config = {
    'development': DevelopmentConfig,
    'production': ProductionConfig,
}