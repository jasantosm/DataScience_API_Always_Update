from datetime import date
from enum import unique
from sqlalchemy import Column, Integer, String, Text, Float

from .database import Base

class Article(Base):
    __tablename__ = "articles"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(300), nullable=False)
    subtitle = Column(String(300), nullable=False)
    article_date = Column(String(50), nullable=False)
    image_url = Column(String(200), nullable=True)
    category_id = Column(Integer)
    body = Column(Text, nullable=False)
    article_url = Column(String(200), unique=True, nullable=False)
    journal_id = Column(Integer)
    scraping_date = Column(String(50), nullable=False)
    

class ScrapingStats(Base):
    __tablename__ = "scraping_stats"

    id = Column(Integer, primary_key=True, index=True)
    response_count = Column(Integer, nullable=False)
    start_time = Column(String(50), nullable=False)
    finish_time = Column(String(50), nullable=False)
    memory_usage_max = Column(Integer, nullable=False)
    total_articles_added = Column(Integer, nullable=False)
    scraping_date = Column(String(50), nullable=False)

