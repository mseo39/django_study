from faker import Faker

myfake = Faker()
#한국어로 출력하고 싶으면 myfake = Faker('ko_kr')
# Faker의 메소드를 통해 어떤 종류의 가짜 데이터를 뽑아낼지 설정 가능

# myfake.seed(seed번호)
#seed 번호= 각각의 가짜 데이터의 데이터번호
Faker.seed(1)


print(myfake.name())
print(myfake.address())
print(myfake.text())
print(myfake.state())
print(myfake.sentence())
print(myfake.random_number())