"""
Explanation in post
https://geekjob.tech/how-to-make-something-like-php-in-python-part-1-3d7818ec0b60
"""

a = type("stdClass", (), {
    "foo": 123,
    "bar": lambda x: x + 1
})

print(a.bar(a.foo)) # 124
print(type(a)) # <class 'type'>
