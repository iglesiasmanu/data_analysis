#import libraries to create the database on sqlalchemy use to describe object
from os import path
from sqlalchemy import (create_engine,
                        Column,
                        String,
                        Integer,
                        Boolean,
                        Table,
                        ForeignKey)

#file base light weight for under one terabyte
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy.ext.declarative import declarative_base

#sqlite as DB>> show by designating the sqlite as file extension
database_filename = "twitter.sqlite3"

#standard DB manipulation to create right path to file
directory = path.abspath(path.dirname(__file__))
database_filepath = path.join(directory, database_filename)

#use file path  as engine to collect data
engine_url = "sqlite:///{}".format(database_filepath)
engine = create_engine(engine_url)

#our database clase are going to inherit from the listed class
Base = declarative_base(bind = engine)
#create a configure session class
Session = sessionmaker(bind = engine, autoflush = False)
#create session
session = Session()

hashtag_tweet = Table("hashtag_tweet", Base.metadata,
    Column("hashtag_id", Integer, ForeignKey("hashtag.id"), nullable =  False),
        Column("tweet_id", Integer, ForeignKey("tweets.id"), nullable = False))


class Tweet(Base):
    __tablename__ = "tweets"
    id = Column(Integer, primary_key = True)
    tid = Column(String(100), nullable = False)
    tweet = Column(String(300), nullable = False)
    user_id = Column(Integer, ForeignKey("user.id"))
    coordinates = Column(String(50), nullable = True)
    user = relationship("User", backref = "tweets")
    create_at = Column(String(100), nullable = False)
    favorite_count = Column(Integer)
    in_reply_to_screen_name = Column(String)
    in_reply_to_status_id = Column(Integer)
    in_reply_to_user_id = Column(Integer)
    lang = Column(String)
    quoted_status_id = Column(Integer)
    retweet_count = Column(Integer)
    source = Column(String)
    is_retweet = Column(Boolean)
    hashtags = relationship("Hashtag",
                            secondary = "hashtag_tweet",
                            back_populates = "tweets")
    
    def User(Base):
        return "<Tweet {}".format(self.id)

class User(Base):
    __tablename__ = "user"
    id = Column(Integer, primary_key = True)
    uid = Column(String(50), nullable = False)
    name = Column(String(100), nullable = False)
    screen_name = Column(String)
    created_at = Column(String)
    #nullable
    description = Column(String)
    followers_count = Column(Integer)
    friends_count = Column(Integer)
    statuses_count = Column(Integer)
    favorites_count = Column(Integer)
    listed_count = Column(Integer)
    geo_enabled = Column(Boolean)
    lang = Column(String)

    def __repr__(self):
        return "<User {}>".format(self.id)

class Hashtag(Base):
    __tablename__ = "hashtags"
    id = Column(Integer, primary_key = True)
    text = Column(String(200), nullable = False)
    tweet1 = relationship("Tweet",
                          secondaryjoin = "hashtag_tweet",
                          back_populates = "hashtags")

    def __rep__(self):
        return "<Hashtag {}>".format(self.text)

#Initiatate Data Base
def init_db():
    Base.metadata.create_all()

#just check that is not actually a file and initiate data base
if not path.isfile(database_filepath):
        init_db()



