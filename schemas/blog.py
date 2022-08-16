def blogEntity(item) -> dict:
    return {
        "id":str(item["_id"]),
        "title":item["title"],
        "content":item["content"],
        "author":item["author"],
        "upvote":int(item["upvote"]),
        "downvote":int(item["downvote"])
    }

def blogsEntity(entity) -> list:
    return [blogEntity(item) for item in entity]