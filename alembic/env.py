import os
import sys
from logging.config import fileConfig

from sqlalchemy import engine_from_config 
from sqlalchemy import pool

from alembic import context

# Add the root directory to the Python path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# Next, we import our models
from src.data_processing.models.database import (Base, SentimentEnum, Tweet,
                                                 MarketSentiment, Token, TokenSentiment,
                                                 Network, NetworkSentiment, Influencer)
from config.settings import DATABASE_URL

# this is the Alembic Config object
config = context.config

# Interpret the config file for Python logging
if config.config_file_name is not None: 
    fileConfig(config.config_file_name)

target_metadata = Base.metadata 

def run_migrations_offline():
    url = DATABASE_URL
    context.configure(
        url=url,
        target_metadata=target_metata,
        literal_binds=True,
        dialect_opts={"paramstyle": "named"},
    )

    with context.begin_transaction():
        context.run_migrations()

def run_migrations_online():
    configuration = config.get_section(config.config_ini_section)
    configuration["sqlalchemy.url"] = DATABASE_URL
    connectable = engine_from_config(
        configuration,
        prefix="sqlalchemy.",
        poolclass=pool.NullPool,
    )

    with connectable.connect() as connection:
        context.configure(
            connection=connection,
            target_metadata=target_metadata
        )

        with context.begin_transaction():
            context.run_migrations()

if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()
