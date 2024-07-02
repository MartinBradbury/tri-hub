# trihub API
![amiresponsive](/assets/responsive.png)
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

- The trihub [frontend repository](https://github.com/MartinBradbury/trihub)

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

### User Model (from django.contrib.auth.models)
- **Fields**: `id`, `username`, `password`, `created_at`, `updated_at`
- **Functionality**: Manages user authentication and basic information.
- **Impact**: Provides essential authentication functionality, ensuring users can securely log in and access their accounts.
- **Example**: Users can register, log in, and have their authentication details securely stored.

## Database Design

### Entity-Relationship Diagram

The Entity-Relationship Diagram (ERD) provides a visual representation of the database's structure. It helps in planning and illustrating the SQL tables and the relationships between them. The ERD is an essential part of the database design that shows the entities, their attributes, and the types of relationships among the entities.

![trihub api ERD](/assets/trihub-apiERD.png)

**Relationships**

1. User
  - One-to-One: User.id → Profile.owner
  - One-to-Many: User.id → Post.owner
  - One-to-Many: User.id → Comment.owner
  - Many-to-Many (through Follower): User.id → Follower.owner
  - Many-to-Many (through Follower): User.id → Follower.followed
  - Many-to-Many (through Like): User.id → Like.owner
  - One-to-Many: User.id → Contact.owner


2. Profile
  - One-to-One: Profile.owner → User.id

3. Post
  - Many-to-One: Post.owner → User.id
  - One-to-Many: Post.id → Comment.post
  - Many-to-Many (through Like): Post.id → Like.post

4. Comment
  - Many-to-One: Comment.owner → User.id
  - Many-to-One: Comment.post → Post.id

5. Like
  - Many-to-One: Like.owner → User.id
  - Many-to-One: Like.post → Post.id

6. Follower
  - Many-to-One: Follower.owner → User.id
  - Many-to-One: Follower.followed → User.id

7. Event
  - One-to-Many: Event.id → Performance.event

8. Performance
  - Many-to-One: Performance.owner → User.id

9. Goal
   - One-to-One: Goal.id → User.id

10. Training Plan
   - One-to-One: TrainingPlan.id → User.id

## Technologies

### Language

- [Python](https://www.python.org/) serves as the back-end programming language.

### Frameworks, libraries and dependencies used in the backend part of the project.

#### Django Dependencies

1. Django (Django==5.0.6):
    - Website: https://www.djangoproject.com
    - Description: Django is a high-level Python web framework that encourages rapid development and clean, pragmatic design. Built by experienced developers, it takes care of much of the hassle of web development, so you can focus on writing your app without needing to reinvent the wheel.

2. django-allauth (django-allauth==0.54.0):
    -  Website: https://django-allauth.readthedocs.io/en/latest/
    - Description: django-allauth provides an easy-to-use interface for authentication using various providers like Google, Facebook, Twitter, etc., and also supports traditional username/password authentication.

3. django-ckeditor (django-ckeditor==6.7.1):
    - Website: https://ckeditor.com/docs/ckeditor4/latest/builds/ckfinder.html
    - Description: CKEditor for Django is a rich text editor integrated with Django admin. It allows users to input formatted text easily through a WYSIWYG interface.

4. django-cloudinary-storage (django-cloudinary-storage==0.3.0):
    - Website: https://pypi.org/project/django-cloudinary-storage/
    - Description: This package integrates Cloudinary storage backend with Django models, allowing for easy image and file uploads to Cloudinary.

5. django-cors-headers (django-cors-headers==4.3.1):
    - Website: https://github.com/adamchainz/django-cors-headers
    - Description: A Django App for handling Cross Origin Resource Sharing (CORS). It simplifies the process of setting up CORS for your Django application.

6. django-filter (django-filter==24.2):
    - Website: https://django-filter.readthedocs.io/en/stable/
    - Description: Provides a simple way to create filters for Django QuerySets. It's useful for creating complex queries based on user input.

7. django-js-asset (django-js-asset==2.2.0):
    - Website: https://github.com/codingeek/django-js-assets
    - Description: A Django app to manage JavaScript assets. It helps in organizing and managing JavaScript files in a Django project.

8. djangorestframework (djangorestframework==3.15.1):
    - Website: https://www.django-rest-framework.org
    - Description: Django REST Framework is a powerful and flexible toolkit for building Web APIs. It makes it easy to build APIs that don't require Django templates and allows for easy integration with other libraries.

9. djangorestframework-simplejwt (djangorestframework-simplejwt==5.3.1):
    - Website: https://jpadilla.github.io/django-rest-framework-simplejwt/
    - Description: Simple JWT is a JSON Web Token authentication plugin for the Django REST Framework. It provides token-based authentication out of the box.

#### Other Dependencies

1. asgiref (asgiref==3.8.1):
    - Website: https://asgiref.readthedocs.io/en/stable/
    - Description: AsgiRef is a collection of utilities for working with ASGI servers and applications. It provides a common interface for interacting with asynchronous server gateways.

2. cloudinary (cloudinary==1.40.0):
    - Website: https://cloudinary.com/documentation/python_integration
    - Description: Cloudinary is a cloud-based service that provides an end-to-end image and video management solution including uploads, storage, manipulations, optimizations, and delivery.

3. dj-database-url (dj-database-url==2.2.0):
    - Website: https://pypi.org/project/dj-database-url/
    - Description: dj-database-url is a small utility for parsing DATABASE_URL from environment variables and returning a dictionary suitable for passing to Django’s DATABASES setting.

4. dj-rest-auth (dj-rest-auth==2.1.9):
    - Website: https://dj-rest-auth.readthedocs.io/en/latest/
    - Description: dj-rest-auth is a set of Django apps that provides authentication views and serializers for Django Rest Framework.

5. gunicorn (gunicorn==22.0.0):
    - Website: https://gunicorn.org
    - Description: Gunicorn 'Green Unicorn' is a Python WSGI HTTP Server for UNIX. It's a pre-fork worker model ported from Ruby's Unicorn server.

6. oauthlib (oauthlib==3.2.2):
    - Website: https://oauthlib.readthedocs.io/en/latest/
    - Description: OAuthLib is a generic library to implement OAuth1 and OAuth2 protocols. It provides a set of classes and methods to simplify the process of implementing these protocols.

7. pillow (pillow==10.3.0):
    - Website: https://pillow.readthedocs.io/en/stable/
    - Description: Pillow is a fork of PIL (Python Imaging Library) aiming to add some user-friendly features.

8. psycopg2 (psycopg2==2.9.9):
    - Website: https://www.psycopg.org/docs/
    - Description: Psycopg2 is a PostgreSQL database adapter for Python. It provides a simple and efficient way to interact with PostgreSQL databases.

9. PyJWT (PyJWT==2.8.0):
    - Website: https://pyjwt.readthedocs.io/en/latest/
    - Description: PyJWT is a Python library which allows you to encode, decode, and verify JSON Web Tokens (JWT).

10. python3-openid (python3-openid==3.2.0):
    - Website: https://openid.net/developers/libraries/python-openid/
    - Description: python3-openid is a Python library for OpenID authentication. It allows users to authenticate via OpenID providers such as Google, Yahoo, etc.

11. pytz (pytz==2024.1):
    - Website: http://pytz.sourceforge.net/
    - Description: pytz brings the Olson tz database into Python. This allows accurate and cross platform timezone calculations.

12. requests-oauthlib (requests-oauthlib==2.0.0):
    - Website: https://requests-oauthlib.readthedocs.io/en/latest/
    - Description: requests-oauthlib is a library that combines the power of Requests and OAuthlib to provide a higher level API for making authenticated HTTP requests.

13. sqlparse (sqlparse==0.5.0):
    - Website: https://sqlparse.readthedocs.io/en/latest/
    - Description: sqlparse is a non-validating SQL parser for Python. Its goal is to be fully compatible with Python’s sqlite3 module.

## Testing and Issues

Information about how the project was tested & Issues encountered, please refer to the [trihub, TESTING.md](https://github.com/MartinBradbury/trihub)

## Deployment


### Version Control

The site was created using the Gitpod editor and pushed to github to the remote repository ‘trihub’.
The following git commands were used throughout development to push code to the remote repo:

- `git add <file>` - This command was used to add the file(s) to the staging area before they are committed.
- `git commit -m “commit message”` - This command was used to commit changes to the local repository queue ready for the final step.
- `git push` - This command was used to push all committed code to the remote repository on github.


### Heroku


### To deploy the project to Heroku, I took the following steps


Create a new workspace in your preferred IDE, in our case it was [Gitpod](https://www.gitpod.io/docs/introduction/getting-started), and set up the new trihub api project. Use [Django REST framwork](https://www.django-rest-framework.org/) guide. 

**Project Settings**

- Include https://<your_app_name>.herokuapp.com in the ALLOWED_HOSTS and CSRF_TRUSTED_ORIGINS lists inside the settings.py file.
- Make sure that the environment variables (DATABASE_URL, SECRET_KEY, and CLOUDINARY_URL) are correctly set to os.environ.get("<variable_name>")
- Make sure that DEBUG is set to false.
- If making changes to static files or apps, make sure to run collectstatic or migrate as needed.
- Commit and push to the repository.

**Requirements**

- Create a plain file called Procfile without any file suffix, at the root level of the project.
  - Add to the Procfile and save.
    - `release: python manage.py makemigrations && python manage.py migrate`
    - `web: gunicorn drf_api.wsgi`
- In your IDE terminal, type pip3 freeze local > requirements.txt to create the requirements.
- (Optional) Create a runtime.txt and type python-3.11.9 (or whichever version you use)
- Commit and push these files to the project repository.

 **Deployment to Heroku**

- In your heroku account, select New and then Create New App.
- Give it a unique name related to your project, choose the correct region for where you are located.
- Create app
- Goto 'Settings' tab and the Config Vars. For Heroku to be able to process and render the project, you must define some environment variables:
  - Add DATABASE_URL variable and assign it a link to your database
  - Add SECRET_KEY variable and assign it a secret key of your choice
  - Add CLOUDINARY_URL variable and assign it a link to your Cloudinary
  - Add ALLOWED_HOST variable and assign it the url of the deployed heroku link
  - Add CLIENT_ORIGIN variable and assign it the url of your deployed frontend app
  - Add CLIENT_ORIGIN_DEV variable and assign it the url of your local development client

- Continue to the 'Deploy' tab. 
  - Select GitHub as the 'deployment method'.
  - Confirm connection to git hub by searching for the correct repository and then connecting to it.
  - To manually deploy project click 'Deploy Branch'. 
      - Don't forget to ensure Debug is false for final deployment
  - Once built a message will appear saying: Your app was successfully deployed. 
  - Click the view button to view the deployed page making a note of it's url.


### Github


### >How to Clone the Repository


Cloning a GitHub repository creates a local copy on your machine, allowing you to sync between the two locations. Here are the steps:


- Log in (or sign up) to GitHub.
- Navigate to the GitHub Repository you want to clone to use locally.
- Click on the code button
- Select whether you would like to clone with HTTPS, SSH or GitHub CLI and copy repository link to the clipboard.
- Open the terminal in your code editor of choice (git must be installed for the nextcoming steps)
- Change the current working directory to the location you want to use for the cloned directory.
- Type 'git clone' into the terminal and then paste the link you copied previously. Press enter.
- If you are working in VSCode, create a virtual environment with command: `python3 -m venv .venv` 
- Agree to select as workspace folder. 
- Move to the virtual environment with command: `source .venv/bin/activate`
- Import all dependencies with command: `pip3 install -r requirements.txt`
- Create an 'env.py' file in the main directory.
- Enter key data, such as: SECRET_KEY, CLIENT_ORIGIN_DEV, CLOUDINARY_URL, DATABASE_URL and ['DEV'] = '1'
- Check that both the virtual environment and env.py are named in the .gitignore file.
- Check it's all working by running the server, use command: `python3 manage.py runserver`

### How to Fork the Repository

Most commonly, forks are used to either propose changes to someone else's project or to use someone else's project as a starting point for your own idea. In order to protect the main branch while you work on something new, essential when working as part of a team or when you want to experiment with a new feature, you will need to fork a branch.


- Log in (or sign up) to Github.
- Go to the selected repository.
- Click the Fork button in the top right corner and select create a fork.
- One can change the name of the fork and add description
- Choose to copy only the main branch or all branches to the new fork.
- Click Create a Fork. A repository should appear in your GitHub

## Credits

### Content


In the creation of TriHub, a broad spectrum of resources has been leveraged to guarantee the platform's strength, ease of use, and interactivity. The following compilation encompasses pivotal documentation, blog posts, tutorials, and manuals that have significantly contributed to the development of its backend infrastructure:

- **Bootstrap**: Extensively used for styling and responsive design, making the site accessible on a variety of devices - [Bootstrap documentation](https://getbootstrap.com/).
- **Django**: As the backbone of our platform, Django's comprehensive documentation has been crucial for backend development - [Django documentation](https://docs.djangoproject.com/en/5.0/).

- **Sources of inspiration and guidance in general**:
  - This resources is only available to enrolled students at The Code Institute:
  - The Code Institute Diploma in Full Stack Software Development (Advanced Front-End) Walk-through project Django REST framework (backend)

### Acknowledgement

Please see the [frontend README](https://github.com/MartinBradbury/trihub/blob/main/README.md).
