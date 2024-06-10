#IMDb Clone Project
Overview
This project is an IMDb clone built using Django. The application allows users to browse movies, actors, and leave comments and ratings. Users can also search for movies and actors and add movies to their watchlist. This README provides an overview of the design, data model, assumptions made during development, and problems encountered.

Table of Contents
Overview
Design
Data Model
Assumptions
Problems Encountered
Installation
Usage
Contributing
License
Design
Frontend
The frontend of the application is built using HTML, CSS, and Bootstrap for responsive design. The search functionality includes real-time suggestions implemented with JavaScript.

Backend
The backend is built with Django, which provides a robust framework for handling the database, views, and forms. The application follows the Model-View-Template (MVT) architecture pattern.

Features
Home Page: Displays a list of movies.
Movie Detail Page: Shows detailed information about a movie, including a list of actors, user comments, and ratings.
Actor Detail Page: Shows detailed information about an actor.
User Authentication: Users can register, login, and logout.
Search: Users can search for movies and actors with real-time suggestions.
Watchlist: Users can add movies to their watchlist.
Comments and Ratings: Authenticated users can leave comments and ratings on movies.
Data Model
Models
User: Django's built-in User model is used for authentication.
Profile: Extends the User model to include additional information.
Movie: Stores movie details such as title, description, rating, popularity, views, image, and trailer.
Actor: Stores actor details such as name, nickname, and image.
MovieActor: Represents a many-to-many relationship between movies and actors, with an additional field for the role name.
Comment: Stores user comments on movies.
Watchlist: Stores movies added to a user's watchlist.
Rank: Stores user ratings for movies.
Relationships
User-Profile: One-to-one relationship.
Movie-Actor: Many-to-many relationship through the MovieActor model.
User-Comment: One-to-many relationship.
User-Watchlist: Many-to-many relationship.
User-Rank: Many-to-many relationship with unique constraints.
Assumptions
User Authentication: Only authenticated users can leave comments and ratings.
Search Functionality: Real-time suggestions are provided when the user types at least three characters.
Rating Scale: Movies can be rated on a scale of 1 to 10.
Image and Video Storage: Movie images and trailers are stored in the static directory for simplicity.
Popularity Calculation: Movie popularity is calculated based on the number of views.
Problems Encountered
Foreign Key Constraint Issues: Encountered issues with foreign key constraints when deleting and populating the database. Resolved by ensuring the correct order of operations.
Real-time Search Suggestions: Initially, search suggestions were not very intuitive. Improved by providing suggestions for both movies and actors.
Form Handling in Templates: Faced challenges with displaying and processing forms in templates. Ensured forms were correctly passed and processed in views.
Database Migrations: Encountered issues with missing or inconsistent migration files. Resolved by manually creating and applying migrations.
Frontend Responsiveness: Ensured the application was fully responsive by using Bootstrap and custom CSS
