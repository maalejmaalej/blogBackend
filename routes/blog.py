from typing import Optional
from fastapi import APIRouter

from models.blog import Blog
from config.db import conn
from schemas.blog import blogEntity, blogsEntity
from bson.objectid import ObjectId

blog = APIRouter()

@blog.get('/blog')
async def findBlogs(search: Optional[str]= ''):
    if search != '':
        return blogsEntity(conn.testblog.testblogs.find({"$or":[{"content":{"$regex" :search }},{"title":{"$regex" :search }},{"author":{"$regex" :search }}]}))
    else:
        return blogsEntity(conn.testblog.testblogs.find())

@blog.get('/blog/{id}')
async def findBlog(id):
    return blogEntity(conn.testblog.testblogs.find_one({"_id":ObjectId(id)}));

@blog.post('/blog')
async def createBlog(blog: Blog):
    conn.testblog.testblogs.insert_one(dict(blog))
    return blogsEntity(conn.testblog.testblogs.find())


@blog.put('/blog/{id}')
async def updateBlog(id, blog:Blog):
    conn.testblog.testblogs.find_one_and_update({"_id":ObjectId(id)},{
        "$set": dict(blog)
    })
    return blogEntity(conn.testblog.testblogs.find_one({"_id":ObjectId(id)}))