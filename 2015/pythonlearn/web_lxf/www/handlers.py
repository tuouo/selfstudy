#!/usr/bin/envpython3
# -*- coding: utf-8 -*-
' url handlers'

import logging; logging.basicConfig(level = logging.INFO)
import re, time, json, hashlib, base64, asyncio
from coroweb import get, post
from models import User, Comment, Blog, next_id
from apis import  APIValueError, APIResourceNotFoundError, Page
from config import configs

import markdown2
from aiohttp import web

COOKIE_NAME = 'awesession'
_COOKIE_KEY = configs.session.secret

def check_admin(request):
    if request.__user__ is None or not request.__user__.admin:
        raise APIPermissionError()

def get_page_index(page_str):
    p = 1
    try:
        p = int(page_str)
    except ValueError as e:
        pass
    if p < 1:
        p = 1
    return p

def user2cookie(user, max_age):
     '''
     Generate cookie str by user.
     '''
     expires = str(int(time.time() + max_age))
     s = '%s-%s-%s-%s' % (user.user_id, user.password, expires, _COOKIE_KEY)
     L = [user.user_id, expires, hashlib.sha1(s.encode('utf-8')).hexdigest()]
     return '-'.join(L)

def text2html(text):
    lines = map(lambda s: '<p>%s</p>' % s.replace('&', '&amp;').replace('<', '&lt;').replace('>', '&gt;'), filter(lambda s: s.strip() != '', text.split('\n')))
    return ''.join(lines)

@asyncio.coroutine
def cookie2user(cookie_str):
    '''
    Parse cookie and load user when cookie is valid.
    '''
    if not cookie_str:
        return None
    try:
        L = cookie_str.split('-')
        if len(L) != 3:
            return None
        uid, expires, sha1 = L
        if int(expires) < time.time():
            return None
        user = yield from User.find(uid)
        if user is None:
            return None
        s = '%s-%s-%s-%s' % (uid, user.password, expires, _COOKIE_KEY)
        if sha1 != hashlib.sha1(s.encode('utf-8')).hexdigest():
            logging.info('invalid sha1 when decode')
            return None
        user.password = '******'
        return user
    except Exception as e:
        logging.exception(e)
        return None



@get('/test')
def test(request):
    logging.info('findAll, /test')
    users = yield from User.findAll()
    return {
        '__template__': 'test.html',
        'users': users
    }

@get('/')
def index(request):
    story = "The quick brown fox jumps over the lazy dog."
    test1 = "Lorem ipsum dolor sit amet,consectetur adipisicing elit,"
    test2 = "sed do eiusmod tempor incididunt ut labore et dolore magna aliqua."
    test3 = "Ut enim ad minim veniam,quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat."
    test4 = "Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur."
    test5 = "Excepteur sint occaecat cupidatat non proident,sunt in culpa qui officia deserunt mollit anim id est laborum."
    blogs = [
        Blog(blog_id ='1', name = 'Story', summary = story, created_at = time.time() - 12000000),
        Blog(blog_id ='2', name = 'test1', summary = test1, created_at = time.time() - 240000),
        Blog(blog_id ='3', name = 'test2', summary = test2, created_at = time.time() - 3600),
        Blog(blog_id ='4', name = 'test3', summary = test3, created_at = time.time() - 720),
        Blog(blog_id ='5', name = 'test4', summary = test4, created_at = time.time() - 600),
        Blog(blog_id ='6', name = 'test5', summary = test5, created_at = time.time() - 12)
    ]
    return {
        '__template__': 'blogs.html',
        'blogs': blogs
    }

@get('/api/all')
def api_get_user(*, page = '1'):
    users = yield from User.findAll(orderBy = 'created_at desc')
    for u in users:
        u.password = '******'
    return dict(user = users)

@get('/api/users')
def api_get_users(*, page = '1'):
    page_index = get_page_index(page)
    num = yield from User.findNumber('count(user_id)')
    p = Page(num, page_index)
    if num == 0:
       return dict(page = p, users=())
    users = yield from User.findAll(orderBy = 'created_at desc', limit = (p.offset, p.limit))
    for u in users:
        u.password = '******'
    return dict(page = p, users = users)

@get('/real')
def indexReal(*, page = '1'):
    page_index = get_page_index(page)
    num = yield from Blog.findNumber('count(blog_id)')
    page = Page(num)
    if num == 0:
        blogs = []
    else:
        blogs = yield from Blog.findAll(orderBy = 'created_at dsec', limit = (page.offset, page.limit))
    return {
        '__template__': 'blogs.html',
        'page': page,
        'blogs': blogs
    }

@get('/blog/{blog_id}')
def get_blog(blog_id):
    blog = yield from Blog.find(blog_id)
    comments = yield from Blog.findAll('blog_id = ?', [blog_id], orderBy = 'created_at desc')    
    for c in comments:
        c.html_content = text2html(c.content)
    blog.html_content = markdown2.markdown(blog.content)
    return {
        '__template__': 'blogs.html',
        'blog': blog,        
        'comments': comments
    }

@get('/register')
def register():
    return {
        '__template__': 'register.html'
    }

_RE_EMAIL = re.compile(r'^[a-z0-9\.\-_]+\@[a-z0-9\-_]+(\.[a-z0-9\-\_]+){1,4}$')
_RE_SHA1 = re.compile(r'^[0-9a-f]{40}$')
@post('/api/users')
def api_register_user(*, email, name, password):
    logging.info('---------------in api_register_user.')
    if not name or not name.strip():
        raise APIValueError('name')
    if not email or not _RE_EMAIL.match(email):
        raise APIValueError('email')
    if not password or not _RE_SHA1.match(password):
        raise APIValueError('_RE_SHA1')
    users = yield from User.findAll('email=?',  [email])
    if len(users) > 0:
        raise APIError('register:failed', 'email', 'Email is already in use.')
    uid = next_id()
    sha1_password = '%s:%s' % (uid, password)
    user = User(user_id = uid, name = name.strip(), email = email,
     password = hashlib.sha1(sha1_password.encode('utf-8')).hexdigest(),
     image = 'http://www.gravatar.com/avatar/%s?d=mm&s=120' % hashlib.md5(email.encode('utf-8')).hexdigest())
    yield from user.save()
    # make session cookie:
    r = web.Response()
    r.set_cookie(COOKIE_NAME, user2cookie(user, 86400), max_age = 86400, httponly = True)
    user.password = '******'
    r.content_type = 'application/json'
    r.body = json.dumps(user, ensure_ascii = False).encode('utf-8')
    return r

@get('/signin')
def signin():
    return {
        '__template__': 'signin.html'
    }

@get('/signout')
def signout(request):
    referer = request.headers.get('Referer')
    r = web.HTTPFound(referer or '/')
    r.set_cookie(COOKIE_NAME, '-deleted-', max_age = 0, httponly = True)
    logging.info('user signed out.')
    return r

@post('/api/authenticate')
def authenticate(*, email, password):
    logging.info('In authenticate.')
    if not email:
        raise APIValueError('email', 'Invalid email.')
    if not password:
        raise APIValueError('password', 'Invalid password.')
    users = yield from User.findAll('email=?', [email])
    if len(users) == 0:
        raise APIValueError('email', 'Email not existt.')
    user = users[0]

    sha1 = hashlib.sha1()
    sha1.update(user.user_id.encode('utf-8'))
    sha1.update(b':')
    sha1.update(password.encode('utf-8'))
    if user.password != sha1.hexdigest():
        raise APIValueError('password', 'Invalid password.')
    # Authenticate is ok, then set cookie
    r = web.Response()
    r.set_cookie(COOKIE_NAME, user2cookie(user, 86400), max_age = 86400, httponly = True)
    user.password = '******'
    r.content_type = 'application/json'
    r.body = json.dumps(user, ensure_ascii = False).encode('utf-8')
    return r


@get('/manage/')
def manage():
    return 'redirect:/manage/comments'

@get('/manage/comments')
def manage_comments(*, page = '1'):
    return {
        '__template__': 'manage_comments.html',
        'page_index': get_page_index(page)
    }

@get('/manage/blogs')
def manage_blogs(*, page = '1'):
    return {
        '__template__': 'manage_blogs.html',
        'page_index': get_page_index(page)
    }

@get('/manage/blogs/create')
def manage_create_blog():
    return {
        '__template__': 'manage_blog_edit.html',
        'blog_id': '',
        'action': '/api/blogs'
    }

@get('/manage/blogs/edit')
def manage_edit_blog(*, blog_id):
    return {
        '__template__': 'manage_blog_edit.html',
        'blog_id': blog_id,
        'action': '/api/blogs/%s' % blog_id
    }

@get('/manage/users')
def manage_users(*, page = '1'):
    return {
        '__template__': 'manage_users.html',
        'page_index': get_page_index(page)
    }

@get('/api/comments')
def api_comments(*, page = '1'):
    page_index = get_page_index(page)
    num = yield from Comment.findNumber('count(comment_id)')
    p = Page(num, page_index)
    if num == 0:
        return dict(age = p, comments = ())
    comments = yield from Comment.findAll(orderBy = 'created_at desc', limit = (p.offset, p.limit))
    return dict(page = p, comments = comments)

@post('/api/blogs/{comment_id}/comments')
def api_create_comment(comment_id, request, *, content):
    user = request.__user__
    if user is None:
        raise APIPermissionError("Signin, Please.")
    if not content or not content.strip():
        raise APIValueError("No content.")
    blog = yield from Blog.find(comment_id)
    if blog is None:
        raise APIResourceNotFoundError("Blog")
    comment = Comment(blog_id = blog.blog_id, user_id = user.user_id, user_name = name, user_image = user.image, content = content.strip())
    yield from comment.save()
    return comment

@post('/api/comments/{comment_id}/delete')
def api_delete_comments(comment_id, request):
    check_admin(request)
    c = yield from Comment.find(comment_id)
    if c is None:
        raise APIResourceNotFoundError('Comment')
    yield from c.remove()
    return dict(comment_id = comment_id)

@get('/api/blogs')
def api_blogs(*, page = '1'):
    page_index = get_page_index(page)
    num = yield from Blog.findNumber('count(blog_id)')
    p = Page(num, page_index)
    if num == 0:
       return dict(page = p, blogs = ())
    blogs = yield from Blog.findAll(orderBy = 'created_at desc', limit = (p.offset, p.limit))
    return dict(page = p, blogs = blogs)

@get('/api/blogs/{blog_id}')
def api_get_blog(*, blog_id):
    blog = yield from Blog.find(blog_id)
    return blog

@post('/api/blogs')
def api_create_blog(request, *, name, summary, content):
    check_admin(request)
    if not name or not name.strip():
        raise APIValueError('name', 'name cannot be empty.')
    if not summary or not summary.strip():
        raise APIValueError('summary', 'summary cannot be empty.')
    if not content or not content.strip():
        raise APIValueError('content', 'content cannot be empty.')
    blog = Blog(user_id = request.__user__.user_id, user_name = request.__user__.name, user_image = request.__user__.image, name=name.strip(), summary=summary.strip(), content=content.strip())
    yield from blog.save()
    return blog

@post('/api/blogs/{blog_id}')
def api_update_blog(blog_id, request, *, name, summary, content):
    check_admin(request)
    blog = yield from Blog.find(blog_id)
    if not name or not name.strip():
        raise APIValueError('name', 'name cannot be empty.')
    if not summary or not summary.strip():
        raise APIValueError('summary', 'summary cannot be empty.')
    if not content or not content.strip():
        raise APIValueError('content', 'content cannot be empty.')
    blog.name = name.strip()
    blog.summary = summary.strip()
    blog.content = content.strip()
    yield from blog.update()
    return blog

@post('/api/blogs/{blog_id}/delete')
def api_delete_blog(request, *, blog_id):
    check_admin(request)
    blog = yield from Blog.find(blog_id)
    yield from blog.remove()
    return dict(blog_id = blog_id)