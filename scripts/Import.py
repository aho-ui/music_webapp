
# import csv
# import mongoengine
# from music.models import Artist # < 


# mongoengine.connect(db="music", host="localhost", port=27017)

# with open('Data/artist.csv', newline='', encoding='utf-8') as csvfile:
#     reader = csv.DictReader(csvfile)
#     for row in reader:
#         Artist(
#             name=row['name'],
#             bio=row['bio']
#         ).save()

# print("Import completed.")

# to run vvvvv
# exec(open("scripts/import.py").read())


from music.factories import ArtistFactory, UserFactory, SongFactory, RecommendationFactory

for _ in range(10):
    UserFactory()

for _ in range(50):
    ArtistFactory()

for _ in range(20):
    SongFactory()

for _ in range(50):
    RecommendationFactory()