from sqlalchemy.orm import sessionmaker
from data_base_lesson import OurDataStructure, engine


Session = sessionmaker(bind=engine)
session = Session()

first = OurDataStructure("My_first_record", 20000)
session.add(first)
session.commit()

second = OurDataStructure("New_second", 55000)
session.add(second)
session.commit()

pr = session.query(OurDataStructure).get(1) #iesko pirmo iraso lenteleje kurio id1

print(pr)

pr.price = 500
pr.name = "Antanas"
session.commit()

print(pr)

session.delete(pr)

pr_all = session.query(OurDataStructure).all()

print(pr_all)