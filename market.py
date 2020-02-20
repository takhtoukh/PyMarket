import database as db


def nearest_markets(user_lat, user_long):
    markets_json = db.get_nearest_markets(user_lat, user_long)
    return markets_json


if __name__ == '__main__':
    print(nearest_markets(48.862430, 2.336210))
    print(nearest_markets(48.887972, 2.355366))
    print(nearest_markets(48.882102, 2.305584))
    print(nearest_markets(48.861327, 2.283955))
    print(nearest_markets(48.873974, 2.355280))
    print(nearest_markets(48.850709, 2.399219))
    print(nearest_markets(48.832600, 2.349636))
    print(nearest_markets(48.830453, 2.372295))
