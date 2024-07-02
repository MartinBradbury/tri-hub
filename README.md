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
- **Fields**: `id`, `owner`, `post`, `content`, `created_at`, `updated_at`
- **Functionality**: Stores comments made by users on posts.
- **Impact**: Facilitates engagement and community interaction by allowing users to comment on each other's posts.
- **Example**: Users comment on a friend's post to share their thoughts and reactions, fostering discussions.

### Follower Model
- **Fields**: `id`, `owner`, `followed`, `created_at`, `updated_at`
- **Functionality**: Stores follower relationships between users.
- **Impact**: Enables users to follow each other, creating a personalized feed based on followed users' posts.
- **Example**: User A follows User B to see User B's posts in their feed, fostering engagement and community building.

### Goals Model
- **Fields**: `id`, `owner`, `event_date`, `created_at`, `updated_at`,
`content`, `plan_length`, `hours_per_week`, `completed`
- **Functionality**: Stores goal date for the user that will be used to filter and generate a personalised training plan.
- **Impact**: Enables users to create a goal for their next event and generate a training plan for the event based on their plan length requirement and how many hours per week they can train.
- **Example**: User A creates a goal date, selected hours per week and length of plan and then get provided with a custom training plan for those specifications.

### Like Model
- **Fields**: `id`, `owner`, `post`, `created_at`, `updated_at`
- **Functionality**: Stores likes on posts by users.
- **Impact**: Provides a way for users to express appreciation for content, increasing user interaction and engagement.
- **Example**: A user likes a friend's post, which may also increase the visibility of popular content through likes.

### Performances Model
- **Fields**: `id`, `owner`, `event`, `time`, `completed_date`,
`content`
- **Functionality**: Stores performances created by authenticated users.
- **Impact**: Provides a way for users to share their performances at different triathlon events along with their experiences of the envent.
- **Example**: A user creates a performance for a specific event. The performance is then shared in a list of all the other perofrmances from all the users.

### Event Model in Performances
- **Fields**: `id`, `title`, `description`, `distance`,
- **Functionality**: Stores event data for users to select from when adding a performance.
- **Impact**: Provides a way for admin to create events for users to select from when creating a performance. 
- **Example**: Admin creates an event. When the user goes to add the event to their performance, the event title appears in the drop down.


### Post Model
- **Fields**: `id`, `owner`, `title`, `content`, `created_at`, `updated_at`, `category`
- **Functionality**: Stores posts created by users.
- **Impact**: Central to the content-sharing functionality, allowing users to create and share posts with their followers.
- **Example**: A user creates a new post with a photo from their recent trip and assigns it to the 'Travel' category.

### Profile Model
- **Fields**: `id`, `owner`, `created_at`, `updated_at`, `first_name`, `last_name`, `date_of_birth`, `email`, `gender`, `fitness_level`, `image`, `content`,
- **Functionality**: Stores user profile information.
- **Impact**: Enhances user profiles by allowing customization, making the platform more personalized and engaging.
- **Example**: A user uploads a profile picture and writes a short bio to make their profile more attractive to other users.

### Training Plan Model
- **Fields**: `id`, `owner`, `created_at`, `updated_at`, `plan_level`, `hours_available`, `weeks_available`, `content`, `notes`, `complete`,
- **Functionality**: Stores training plans created by site admin.
- **Impact**: Enables users to get a custom built training plan based on their hours available and weeks available set in their goal.
- **Example**: A user creates a specific goal, the training plan that meets their creteria is generated for the user to see.
