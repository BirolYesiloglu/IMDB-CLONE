# myapp/management/commands/populate_db.py
from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from myapp.models import Movie, Comment, Watchlist, Actor, MovieActor
from django.contrib.auth.hashers import make_password
from django.db import connection, transaction

class Command(BaseCommand):
    help = 'Populate the database with sample data'

    @transaction.atomic
    def handle(self, *args, **kwargs):
        # Disable foreign key constraints
        with connection.cursor() as cursor:
            cursor.execute('PRAGMA foreign_keys=OFF')

        # Delete all data
        MovieActor.objects.all().delete()
        Watchlist.objects.all().delete()
        Comment.objects.all().delete()
        Movie.objects.all().delete()
        Actor.objects.all().delete()
        User.objects.all().delete()

        # Reset the sequences
        with connection.cursor() as cursor:
            cursor.execute("DELETE FROM sqlite_sequence WHERE name='myapp_movie'")
            cursor.execute("DELETE FROM sqlite_sequence WHERE name='auth_user'")
            cursor.execute("DELETE FROM sqlite_sequence WHERE name='myapp_comment'")
            cursor.execute("DELETE FROM sqlite_sequence WHERE name='myapp_watchlist'")
            cursor.execute("DELETE FROM sqlite_sequence WHERE name='myapp_actor'")
            cursor.execute("DELETE FROM sqlite_sequence WHERE name='myapp_movieactor'")

        # Insert sample users
        user1 = User.objects.create(username='user1', email='user1@example.com', password=make_password('password1'))
        user2 = User.objects.create(username='user2', email='user2@example.com', password=make_password('password2'))

        # Insert sample movies
        movies = [
            Movie(
                title='Furiosa Bir Mad Max Destanı',
                description='A gripping post-apocalyptic story following the fearless Furiosa on her quest for survival and justice in a barren wasteland.',
                rating=8.5,
                popularity=90,
                image='images/Movie1/Furiosa_Bir_Mad_Max_Destanı_(2024).jpg',
                trailer='trailers/Movie1/Furiosa_Bir_Mad_Max_Destanı_Altyazılı_Fragman.mp4'
            ),
            Movie(
                title='Bridgerton',
                description='Set in the lavish Regency era, Bridgerton follows the powerful Bridgerton family as they navigate love, scandal, and drama in high society.',
                rating=7.5,
                popularity=80,
                image='images/Movie2/Bridgerton_(2020).jpg',
                trailer='trailers/Movie2/Bridgerton_Resmi_Fragman_Netflix.mp4'
            ),
            Movie(
                title='Atlas',
                description='A thrilling adventure that takes you through the legendary journey of Atlas, exploring uncharted territories and battling mythical creatures.',
                rating=9.0,
                popularity=95,
                image='images/Movie3/Atlas_(2024).jpg',
                trailer='trailers/Movie3/ATLAS_Resmi_Fragman_Netflix.mp4'
            ),
            Movie(
                title='İç Savaş',
                description='An intense civil war drama depicting the struggles, sacrifices, and heroism of ordinary people caught in the midst of a devastating conflict.',
                rating=6.5,
                popularity=70,
                image='images/Movie4/İç_Savaş_(2024).jpg',
                trailer='trailers/Movie4/İç_Savaş_Civil_War_Altyazılı_Fragman.mp4'
            ),
            Movie(
                title='Dublör',
                description='A high-stakes action thriller about a stuntman who gets caught in a real-life conspiracy, facing dangerous challenges that blur the line between fiction and reality.',
                rating=7.0,
                popularity=75,
                image='images/Movie5/Dublör_(2024).jpg',
                trailer='trailers/Movie5/Dublör_The_Fall_Guy_Altyazılı_Fragman.mp4'
            ),
            Movie(
                title='Mad Max Fury Road',
                description='An explosive return to the Mad Max franchise, Fury Road delivers relentless action as Max teams up with Furiosa to escape a tyrannical warlord in a desolate wasteland.',
                rating=8.0,
                popularity=85,
                image='images/Movie6/Mad_Max_Fury_Road_(2015).jpg',
                trailer='trailers/Movie6/Mad_Max_Fury_Road_Türkçe_Altyazılı_Fragman.mp4'
            ),
            Movie(
                title='Godzilla Minus One',
                description='In a world recovering from war, a new and more terrifying Godzilla emerges, threatening humanity’s fragile peace and igniting a desperate struggle for survival.',
                rating=6.0,
                popularity=65,
                image='images/Movie7/Godzilla_Minus_One_(2023).jpg',
                trailer='trailers/Movie7/GODZILLA_MINUS_ONE_Official_Trailer_2.mp4'
            ),
            Movie(
                title='Dune Çöl Gezegeni Bölüm İki',
                description='The epic saga continues as Paul Atreides rises to power, navigating political intrigue and treacherous deserts to fulfill his destiny on the planet Arrakis.',
                rating=7.8,
                popularity=88,
                image='images/Movie8/Dune_Çöl_Gezegeni_Bölüm_İki_(2024).jpg',
                trailer='trailers/Movie8/Dune_Çöl_Gezegeni_Bölüm_İki_Dune_Part_Two_Altyazılı_Fragman.mp4'
            ),
            Movie(
                title='Maymunlar Cehennemi Yeni Krallık',
                description='A gripping continuation of the Planet of the Apes saga, where a new generation of apes faces unprecedented challenges and human threats in their quest for a peaceful existence.',
                rating=9.5,
                popularity=98,
                image='images/Movie9/Maymunlar_Cehennemi_Yeni_Krallık_(2024).jpg',
                trailer='trailers/Movie9/Maymunlar_Cehennemi_Yeni_Krallık_Kingdom_of_the_Planet_of_the_Apes_Altyazılı_Fragman.mp4'
            ),
            Movie(
                title='Fallout',
                description='Based on the popular video game series, Fallout brings to life a post-apocalyptic world where survivors navigate the ruins of civilization and face constant threats from mutated creatures and hostile factions.',
                rating=5.5,
                popularity=60,
                image='images/Movie10/Fallout_(2024).jpg',
                trailer='trailers/Movie10/Fallout_Resmi_Fragman.mp4'
            ),
            Movie(
                title='Eric',
                description='A heartfelt drama that explores the journey of Eric, a young man with a troubled past, as he seeks redemption and purpose through unexpected relationships and challenges.',
                rating=8.3,
                popularity=89,
                image='images/Movie11/Eric_(2024).jpg',
                trailer='trailers/Movie11/Eric_Resmi_Fragman_Netflix.mp4'
            ),
            Movie(
                title='Shôgun',
                description='An epic historical drama based on the best-selling novel, Shôgun follows the adventures of an English navigator shipwrecked in feudal Japan, as he navigates a complex web of power, honor, and survival.',
                rating=7.2,
                popularity=78,
                image='images/Movie12/Shôgun_(2024).jpg',
                trailer='trailers/Movie12/Shōgun_Resmi_Fragman_Disney.mp4'
            ),
            Movie(
                title='Rekabet',
                description='A gripping tale of ambition and rivalry, Rekabet explores the intense competition between two business tycoons, where personal and professional conflicts lead to dramatic consequences.',
                rating=6.8,
                popularity=73,
                image='images/Movie13/Rekabet_(2024).jpg',
                trailer='trailers/Movie13/Rekabet_Türkçe_Altyazılı_Fragman.mp4'
            ),
            Movie(
                title='Esaretin Bedeli',
                description='A timeless classic about hope, friendship, and perseverance, Esaretin Bedeli follows the story of Andy Dufresne, a banker wrongfully imprisoned, as he navigates the harsh realities of Shawshank prison.',
                rating=8.7,
                popularity=92,
                image='images/Movie14/Esaretin_Bedeli_(1994).jpg',
                trailer='trailers/Movie14/The_Shawshank_Redemption_OFFICIAL_TRAILER.mp4'
            ),
            Movie(
                title='Yıldızlararası',
                description='A visually stunning and emotionally powerful sci-fi epic, Yıldızlararası explores humanity’s quest for survival through space exploration, where a team of astronauts travel through a wormhole in search of a new home.',
                rating=9.1,
                popularity=97,
                image='images/Movie15/Yıldızlararası_(2014).jpg',
                trailer='trailers/Movie15/Interstellar_Yıldızlararası_Fragman.mp4'
            ),
            Movie(
                title='Oppenheimer',
                description='A historical drama that delves into the life of J. Robert Oppenheimer, the brilliant physicist whose work on the Manhattan Project led to the creation of the atomic bomb, changing the course of history forever.',
                rating=5.8,
                popularity=63,
                image='images/Movie16/Oppenheimer_(2023).jpg',
                trailer='trailers/Movie16/Oppenheimer_Altyazılı_Fragman.mp4'
            )
        ]

        Movie.objects.bulk_create(movies)

        # Insert sample actors
        actors = [
            Actor(name='Anya Taylor-Joy', nickname='The Queen’s Gambit Star', image='images/actors/anya_taylor_joy.jpg'),
            Actor(name='Chris Hemsworth', nickname='Thor', image='images/actors/chris_hemsworth.jpg'),
            Actor(name='Nicola Coughlan', nickname='Derry Girl', image='images/actors/nicola_coughlan.jpg'),
            Actor(name='Claudia Jessie', nickname='Eloise Bridgerton', image='images/actors/claudia_jessie.jpg'),
            Actor(name='Jennifer Lopez', nickname='JLo', image='images/actors/jennifer_lopez.jpg'),
            Actor(name='Simu Liu', nickname='Shang-Chi', image='images/actors/simu_liu.jpg'),
            Actor(name='Kirsten Dunst', nickname='Kiki', image='images/actors/kirsten_dunst.jpg'),
            Actor(name='Wagner Moura', nickname='Pablo', image='images/actors/wagner_moura.jpg'),
            Actor(name='Ryan Gosling', nickname='Ken', image='images/actors/ryan_gosling.jpg'),
            Actor(name='Emily Blunt', nickname='Mary Poppins', image='images/actors/emily_blunt.jpg'),
            Actor(name='Tom Hardy', nickname='Eddie Brock', image='images/actors/tom_hardy.jpg'),
            Actor(name='Charlize Theron', nickname='Furiosa', image='images/actors/charlize_theron.jpg'),
            Actor(name='Minami Hamabe', nickname='Minami', image='images/actors/minami_hamabe.jpg'),
            Actor(name='Ryunosuke Kamiki', nickname='Kamiki', image='images/actors/ryunosuke_kamiki.jpg'),
            Actor(name='Timothée Chalamet', nickname='Timmy', image='images/actors/timothee_chalamet.jpg'),
            Actor(name='Zendaya', nickname='Daya', image='images/actors/zendaya.jpg'),
            Actor(name='Owen Teague', nickname='Owen', image='images/actors/owen_teague.jpg'),
            Actor(name='Freya Allan', nickname='Freya', image='images/actors/freya_allan.jpg'),
            Actor(name='Ella Purnell', nickname='Ella', image='images/actors/ella_purnell.jpg'),
            Actor(name='Aaron Moten', nickname='Aaron', image='images/actors/aaron_moten.jpg'),
            Actor(name='Benedict Cumberbatch', nickname='Benedict', image='images/actors/benedict_cumberbatch.jpg'),
            Actor(name='Gaby Hoffmann', nickname='Gaby', image='images/actors/gaby_hoffmann.jpg'),
            Actor(name='Cosmo Jarvis', nickname='Cosmo', image='images/actors/cosmo_jarvis.jpg'),
            Actor(name='Anna Sawai', nickname='Anna', image='images/actors/anna_sawai.jpeg'),
            Actor(name='Mike Faist', nickname='Mike', image='images/actors/mike_faist.jpg'),
            Actor(name='Josh OConnor', nickname='Josh', image='images/actors/josh_oconnor.jpg'),
            Actor(name='Tim Robbins', nickname='Tim', image='images/actors/tim_robbins.jpg'),
            Actor(name='Morgan Freeman', nickname='Morgan', image='images/actors/morgan_freeman.jpg'),
            Actor(name='Matthew McConaughey', nickname='Matthew', image='images/actors/matthew_mcconaughey.jpg'),
            Actor(name='Anne Hathaway', nickname='Anne', image='images/actors/anne_hathaway.jpg'),
            Actor(name='Jessica Chastain', nickname='Jessica', image='images/actors/jessica_chastain.jpg'),
            Actor(name='Cillian Murphy', nickname='Cillian', image='images/actors/cillian_murphy.jpg'),
            Actor(name='Matt Damon', nickname='Matt', image='images/actors/matt_damon.jpg'),
            Actor(name='Robert Downey Jr.', nickname='RDJ', image='images/actors/robert_downey_jr.jpg'),
        ]

        Actor.objects.bulk_create(actors)

        # Link actors to movies with roles
        furiosa = Movie.objects.get(title='Furiosa Bir Mad Max Destanı')
        anya_taylor_joy = Actor.objects.get(name='Anya Taylor-Joy')
        chris_hemsworth = Actor.objects.get(name='Chris Hemsworth')
        MovieActor.objects.create(movie=furiosa, actor=anya_taylor_joy, role_name='Furiosa')
        MovieActor.objects.create(movie=furiosa, actor=chris_hemsworth, role_name='Dementus')

        bridgerton = Movie.objects.get(title='Bridgerton')
        nicola_coughlan = Actor.objects.get(name='Nicola Coughlan')
        claudia_jessie = Actor.objects.get(name='Claudia Jessie')
        MovieActor.objects.create(movie=bridgerton, actor=nicola_coughlan, role_name='Penelope Featherington')
        MovieActor.objects.create(movie=bridgerton, actor=claudia_jessie, role_name='Eloise Bridgerton')

        atlas = Movie.objects.get(title='Atlas')
        jennifer_lopez = Actor.objects.get(name='Jennifer Lopez')
        simu_liu = Actor.objects.get(name='Simu Liu')
        MovieActor.objects.create(movie=atlas, actor=jennifer_lopez, role_name='Atlas Shepherd')
        MovieActor.objects.create(movie=atlas, actor=simu_liu, role_name='Harlan Shepherd')

        ic_savas = Movie.objects.get(title='İç Savaş')
        kirsten_dunst = Actor.objects.get(name='Kirsten Dunst')
        wagner_moura = Actor.objects.get(name='Wagner Moura')
        MovieActor.objects.create(movie=ic_savas, actor=kirsten_dunst, role_name='Lee')
        MovieActor.objects.create(movie=ic_savas, actor=wagner_moura, role_name='Joel')

        dubler = Movie.objects.get(title='Dublör')
        ryan_gosling = Actor.objects.get(name='Ryan Gosling')
        emily_blunt = Actor.objects.get(name='Emily Blunt')
        MovieActor.objects.create(movie=dubler, actor=ryan_gosling, role_name='Colt Seavers')
        MovieActor.objects.create(movie=dubler, actor=emily_blunt, role_name='Jody Moreno')

        mad_max_fury_road = Movie.objects.get(title='Mad Max Fury Road')
        tom_hardy = Actor.objects.get(name='Tom Hardy')
        charlize_theron = Actor.objects.get(name='Charlize Theron')
        MovieActor.objects.create(movie=mad_max_fury_road, actor=tom_hardy, role_name='Max Rockatansky')
        MovieActor.objects.create(movie=mad_max_fury_road, actor=charlize_theron, role_name='Imperator Furiosa')

        godzilla_minus_one = Movie.objects.get(title='Godzilla Minus One')
        minami_hamabe = Actor.objects.get(name='Minami Hamabe')
        ryunosuke_kamiki = Actor.objects.get(name='Ryunosuke Kamiki')
        MovieActor.objects.create(movie=godzilla_minus_one, actor=minami_hamabe, role_name='Noriko Oishi')
        MovieActor.objects.create(movie=godzilla_minus_one, actor=ryunosuke_kamiki, role_name='Koichi Shikishima')

        dune_cöl_gezegeni = Movie.objects.get(title='Dune Çöl Gezegeni Bölüm İki')
        timothee_chalamet = Actor.objects.get(name='Timothée Chalamet')
        zendaya = Actor.objects.get(name='Zendaya')
        MovieActor.objects.create(movie=dune_cöl_gezegeni, actor=timothee_chalamet, role_name='Paul Atreides')
        MovieActor.objects.create(movie=dune_cöl_gezegeni, actor=zendaya, role_name='Chani')

        maymunlar_cehennemi = Movie.objects.get(title='Maymunlar Cehennemi Yeni Krallık')
        owen_teague = Actor.objects.get(name='Owen Teague')
        freya_allan = Actor.objects.get(name='Freya Allan')
        MovieActor.objects.create(movie=maymunlar_cehennemi, actor=owen_teague, role_name='Noa')
        MovieActor.objects.create(movie=maymunlar_cehennemi, actor=freya_allan, role_name='Nova')

        fallout = Movie.objects.get(title='Fallout')
        ella_purnell = Actor.objects.get(name='Ella Purnell')
        aaron_moten = Actor.objects.get(name='Aaron Moten')
        MovieActor.objects.create(movie=fallout, actor=ella_purnell, role_name='Lucy MacLean')
        MovieActor.objects.create(movie=fallout, actor=aaron_moten, role_name='Maximus')

        eric = Movie.objects.get(title='Eric')
        benedict_cumberbatch = Actor.objects.get(name='Benedict Cumberbatch')
        gaby_hoffmann = Actor.objects.get(name='Gaby Hoffmann')
        MovieActor.objects.create(movie=eric, actor=benedict_cumberbatch, role_name='Eric')
        MovieActor.objects.create(movie=eric, actor=gaby_hoffmann, role_name='Gaby')

        shogun = Movie.objects.get(title='Shôgun')
        cosmo_jarvis = Actor.objects.get(name='Cosmo Jarvis')
        anna_sawai = Actor.objects.get(name='Anna Sawai')
        MovieActor.objects.create(movie=shogun, actor=cosmo_jarvis, role_name='John Blackthorne')
        MovieActor.objects.create(movie=shogun, actor=anna_sawai, role_name='Lady Mariko')

        rekabet = Movie.objects.get(title='Rekabet')
        mike_faist = Actor.objects.get(name='Mike Faist')
        josh_oconnor = Actor.objects.get(name='Josh OConnor')
        zendaya = Actor.objects.get(name='Zendaya')
        MovieActor.objects.create(movie=rekabet, actor=mike_faist, role_name='Jonathan')
        MovieActor.objects.create(movie=rekabet, actor=josh_oconnor, role_name='Alexander')
        MovieActor.objects.create(movie=rekabet, actor=zendaya, role_name='Zara')

        esaretin_bedeli = Movie.objects.get(title='Esaretin Bedeli')
        tim_robbins = Actor.objects.get(name='Tim Robbins')
        morgan_freeman = Actor.objects.get(name='Morgan Freeman')
        MovieActor.objects.create(movie=esaretin_bedeli, actor=tim_robbins, role_name='Andy Dufresne')
        MovieActor.objects.create(movie=esaretin_bedeli, actor=morgan_freeman, role_name='Ellis Boyd "Red" Redding')

        yildizlararasi = Movie.objects.get(title='Yıldızlararası')
        matthew_mcconaughey = Actor.objects.get(name='Matthew McConaughey')
        anne_hathaway = Actor.objects.get(name='Anne Hathaway')
        jessica_chastain = Actor.objects.get(name='Jessica Chastain')
        MovieActor.objects.create(movie=yildizlararasi, actor=matthew_mcconaughey, role_name='Cooper')
        MovieActor.objects.create(movie=yildizlararasi, actor=anne_hathaway, role_name='Amelia Brand')
        MovieActor.objects.create(movie=yildizlararasi, actor=jessica_chastain, role_name='Murph')

        oppenheimer = Movie.objects.get(title='Oppenheimer')
        cillian_murphy = Actor.objects.get(name='Cillian Murphy')
        emily_blunt = Actor.objects.get(name='Emily Blunt')
        matt_damon = Actor.objects.get(name='Matt Damon')
        robert_downey_jr = Actor.objects.get(name='Robert Downey Jr.')
        MovieActor.objects.create(movie=oppenheimer, actor=cillian_murphy, role_name='J. Robert Oppenheimer')
        MovieActor.objects.create(movie=oppenheimer, actor=emily_blunt, role_name='Kitty Oppenheimer')
        MovieActor.objects.create(movie=oppenheimer, actor=matt_damon, role_name='Leslie Groves')
        MovieActor.objects.create(movie=oppenheimer, actor=robert_downey_jr, role_name='Lewis Strauss')

        # Re-enable foreign key constraints
        with connection.cursor() as cursor:
            cursor.execute('PRAGMA foreign_keys=ON')

        self.stdout.write(self.style.SUCCESS('Database populated successfully'))