from server import mongo_connection


def get_user_friends(user_list):
    users = mongo_connection.db.yelp_users.find({'user_id': {"$in": user_list}}, {'friends': 1, 'user_id': 1})
    edges = []
    for user in users:
        friends = user['friends']
        user_id = user['user_id']
        for friend in friends:
            edges.append((user_id, friend))
            edges.append((friend, user_id))

    edges = list(set(edges))

    return edges


def get_users_for_business(business_id):
    user_list = []
    reviews = mongo_connection.db.yelp_reviews.find({'business_id': business_id}, {"user_id": 1})
    tips = mongo_connection.db.yelp_tips.find({'business_id': business_id}, {"user_id": 1})

    for user in reviews:
        user_list.append(user['user_id'])
    for user in tips:
        user_list.append(user['user_id'])

    user_list = list(set(user_list))
    return user_list
