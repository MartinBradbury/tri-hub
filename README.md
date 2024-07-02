# trihub API
![amiresponsive]()
<br>
<br>

## Purpose of the project 

The purpose of TriHub is to make the ultimate destination for all things triathlon. TriHub is designed to bring together triathletes of all abilities, fostering a vibrant community where everyone can share, learn, and grow together. My platform offers a unique blend of features tailored to meet the diverse needs of its members, whether you're a seasoned pro or just starting your triathlon journey.

I want TriHub to foster the power of community. My platform allows users to share images and comments, creating a space where triathletes can connect, inspire, and motivate each other. Whether you've just completed your first sprint or are gearing up for an Ironman, their voice matters here. Users can share their triumphs, challenges, and insights to build a supportive network that goes beyond the finish line.

Performance tracking is at the heart of TriHub. Users can log their performances, analyse their progress, and set new goals with my intuitive tools. Users who are looking to improve, TriHub offers customizable training plans designed to fit your schedule and ability level. Tailor your training to reach your peak performance, whether you're aiming for a personal best or simply enjoying the journey.
<br>
<br>
The trihub API serves as the backend service for the trihub Application, [view live site here](https://trihub-e2e28f386783.herokuapp.com/).

<hr>

## General Details

This is the API for the trihub backend application. Detailed information about strategy, structure, skeleton, ux, testing and open issues are found in the frontend repository README and TESTING information.

- The Pixavibe [frontend repository](https://github.com/MartinBradbury/trihub)

## Database and Model

In the development environment, trihub uses SQLite, which is simple to set up and ideal for development and testing. For the production environment, PostgreSQL is used due to its robustness, scalability, and advanced features suitable for handling a live web application.

## Models in trihub api

### Comment Model
- **Fields**: `id`, `owner`, `post_`, `content`, `created_at`, `updated_at`
- **Functionality**: Stores comments made by users on posts.
- **Impact**: Facilitates engagement and community interaction by allowing users to comment on each other's posts.
- **Example**: Users comment on a friend's post to share their thoughts and reactions, fostering discussions.
