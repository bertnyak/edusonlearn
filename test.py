def add(a, b, c, d=100):
    print(f'1 - {a}\n2 - {b}\n3 - {c}\n4 - {d}')
add(5, 3,4)

def process(user_code, language, problem_id, company_id, attempts):
    ...
process(
    user_code='select * from users',
    language='SQL',
    problem_id=115,
    company_id=1,
    attempts=3,
)
def foo(*args, **kwargs):
    print(args)
    print(kwargs)
foo(5, 3, 'string', n=5,d=3,s='s')


def get_user_info(num, **kwargs):
    name = kwargs.get('name', 'Без имени')
    email = kwargs.get('email', 'Без почты')
    print(f' Пользователь')