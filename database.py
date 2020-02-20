from sqlalchemy import Column, String
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from operator import itemgetter

import tools

engine = create_engine('postgres://dmczbhctvkojep:ae78857d6f501f59543e1543fbcf83f71e74d9d80a84a3d96342255e5be170a2'
                       '@ec2-54-247-96-169.eu-west-1.compute.amazonaws.com:5432/d97rubvmja9mhj')


Base = declarative_base()


class Markets(Base):
    __tablename__ = 'paris_market'
    enseigne = Column(String, primary_key=True)
    lat = Column(String)
    long = Column(String)


def get_nearest_markets(user_lat, user_lng):
    """
        :param user_lat: User latitude
        :param user_lng: User longitude
        :return: 20 nearest markets from user in a perimeter of 300 meters
    """
    Session = sessionmaker(bind=engine)
    session = Session()
    markets_result = session.query(Markets).all()
    result = []

    for market in markets_result:
        if not market.lat or not market.long:
            continue
        market_longitude = float(market.long)
        market_latitude = float(market.lat)
        distance = tools.get_distance(user_lat, user_lng, market_latitude, market_longitude)
        if distance <= 300:  # perimeter of 300
            name = market.enseigne
            result.append(tools.get_element_as_json(name.strip(), distance, market_latitude, market_longitude))

    result = sorted(result, key=itemgetter('distance'))
    return result[:20]

