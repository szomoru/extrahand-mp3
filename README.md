<h1 align="center">Extra Hand</h1>
<h1 align="center"><img src="docs/test/amirespinsive_extrahand.JPG" /></h1>

:point_right: <a href="https://szomoru.github.io/extrahand-mp3/">Live Website</a> :point_left:

:point_right: <a href="https://github.com/szomoru/extrahand-mp3">Github Repository</a> :point_left:
 
 ## About

This website was created to fullfill the requirements of Code Institute 3rd Milstone Project. The main focus of this project is database handling and manipulation through a website. The main goal to maintain a dtabase connected to the website with full CRUD functionality. 
The main purpose of this website to bring together people who needs help and with people who willing to help. This website is based on membership. Registered account required to use the full functionality of the website eg register tasks that we would liket to have someone to help with and also apply to help someone with something. There is no limitation in the audiance, because everyone can be in a situation when needs help. Or is in a situation when can help. 
As a first step this site is created for private persons, but later it is possible to involve professionals and company accounts. 
This site was not built for earning money, but the possibility is given. While it is for private persons, ads placed on the site can genarate some income, later on when companies join the and offer professional solutions some commission can be earned as well. 


## Table of Contents

[User Experience (UX)](#UX)

[Features](#features)

[Technologies Used](#technologies)

[JavaScripts](#scripts)

[Testing](#testing)

[Deployment](#deployment)

[Credits](#credits)


<a name="UX"></a>

## User Experience (UX)

-   ### User stories

    -   #### First Time Visitor Goals

        1. As a First Time Visitor, I want to easily understand the content of the webpage and the aim of the site.
        2. As a First Time Visitor, I want Register for an Account
        3. As a First Time Visitor, I want to be able to easily navigate through the site and get an overal picture about the site structure.
        4. As a First Time Visitor, I want to see their social media availability, where i can get more information about the site or organisation / person behind that.
        5. As a first Time Visitor i want to see clearly what content available for without registration and what requires registration. 

    -   #### Returning Visitor Goals

        1. As a Returning Visitor, I want to be able to login with my previously registered credentials.
        2. As a Returning Visitor, I want to be able to register request for help.
        3. As a Returning Visitor, I want to be able to apply to help someone else.
        4. As a Returning Visitor, I want to be able to update my profile information.
        5. As a Returning Visitor, I want to be able to edit my help request information.
        6. As a Returning Visitor, I want to be able to delete my registered requests.
        7. As a Returning Visitor, I want to be able to browse among all regitered tasks.

    -   #### Admin Goals
        As the admin i want to be able to delete any of the registered tasks.

-   ### Design

    -   #### Colour Scheme
        This website was built on a startbootstrap template, called business-casual (https://startbootstrap.com/theme/business-casual).
        The base of selection of this template is the calm, simple, but professional look of the site. It is stylish but very well represent the serious message of the website. Help eachother ...
        The basic colors follow through the whole website. Some of the basic colors:
        - #f6e1c5 mainly used as a bright background of a section
        - rgba(47, 23, 15, 0.9) mainly used the beckground of the navbar and the footer
        - #e6a756 mainly color of the buttons (which is not submit or cancel)
        - sisimple red and green color used for cancel and submit buttons
        - light grey, light blue and yellow colors are used as information colors these colors comming from bootstrap just like the danger, info, warning bootstrap names


    -   #### Typography
        - The fonts are also comming from the business-casual startbootstrap template (https://startbootstrap.com/theme/business-casual). Me as a developer has not changed it at all, i have not added or removed fonts.
    
    -   #### Imagery
        -   This site at this stage does not use many images. There is one huge image as a background image of the whole site on everypages. This image symbolise the supportive attitude to eachother. there is only one more picture except that on the about page which is just a smaller section of a bigger world famous painting (Michaelangelo - The Creation of Adam).

-   ### Wireframes

    -   There were several design changes during the development process, but the final site looks very similar with the wireframe. The wireframe does not contain any colorscheme, because when it was done it was already known that template will be used, but still was not decided which one. On the following pictures the wireframes are introduced by htmls. Each image contain a desktop, tablet, and phone size wireframe.  

    -   index.html

        <img src="docs/wireframe/indexhtml.png" height="400px" />


    -   register.html 

        <img src="docs/wireframe/registerhtml.png" height="400px" />


    -   login.html 

        <img src="docs/wireframe/loginhtml.png" height="400px" />

    -   profile.html 

        <img src="docs/wireframe/profilehtml.png" height="400px" />

    -   profile_alltask.html 

        <img src="docs/wireframe/profile_alltaskhtml.png" height="400px" />

    -   profile_new_task.html 

        <img src="docs/wireframe/profile_newtaskhtml.png" height="400px" />

    -   profile_edit_task.html 

        <img src="docs/wireframe/profile_edittaskhtml.png" height="400px" />

    -   profile_mytasks.html 

        <img src="docs/wireframe/profile_allmytaskhtml.png" height="400px" />

    -   about.html 

        <img src="docs/wireframe/abouthtml.png" height="400px" />

    -   contact.html 

        <img src="docs/wireframe/contacthtml.png" height="400px" />

    <a name="features"></a>        

    ## Features

    ### Present Features

    #### Features accross all Pages

    -   The website was designed to have the same structure on every pages. On this way the visitor feel comfortable and find her/his way on every page.
        The layout is the following:
        - On the top section there is the Header with Navigation links
        - The middel section is the largest "main" section on every page, which contains the main information. This middel section is also very well separated visually. 
        - The page is closed with the Footer, which in this case contains only a Copyright text and the year. 

    - [x] **Header**
        - The header contains the title of the site (Extra Hand)
        - The second section is the "navigation" section with varried number of menupoints. The NAvigation bar is a sticky navigation, so by scrolling up the page the navigations are always visible. The folowing cases are possible based on authorization:
            -   Basic state no user logged in:
                - Home
                - Login/Register
                - About
                - Contact
            -   User logged in:
                - All Tasks
                - Add New Task
                - Tasks By Me
                - Profile
                - Logout
                - Contact
            -   Admin is logged in:
                - All Tasks
                - Profile
                - Contact

    - [x] **Main section**
        - The main section contains the page specific information on every page.
    - [x] **Footer**
        - Always located as the last element of the page. In this project it does not contain any important information not to steal the focus of the visitor.        

    #### Features specific to Pages

    - [x] **Index page**
        - Hero imnage set to the background, which clearly represents the type of the webpage
        - A smaller window floating over the background, which highlight some topic of the content od the page and call to action
        - If the visitor accept the invitation and take action after clicking the "Learn more" button, gets to the Home page.
    - [x] **Register page**
        - the user can register and get her/his own account to use full potential of the site
    - [x] **Login page**
        - This page is the first page, that is shown after the landing page. By seeing this page the visitor gets a short description about the game itslef.
        - The visitor also can see screenshots from the game, so when she/he starts to play they are already familiar with the layout.
        - As a last element on this page the visitor can click on a button, which takes her/him to the Game page and start the game
    - [x] **About page**
        This page contain some real life cases when the visitor should use this page and a short description about the purpose of the site.
    - [x] **Contact page**
        This is the main page for the visitor if she/he wants to contact to the website developer.
        The visitor can get information about the following:
         - address
         - phone number
         - social media links
         of the developer.
    - [x] **Profile page**
        - This is the first page that the visitor see when she/he successfully identified her-/him-self through a username and password on the login page.
        - This page contains the profile information which was given during the registration process
        - The user has possibility to update this information except the username and password 
    - [x] **Profile all task page**
        - This page has several functions. As a basic the user see all the registered tasks in the database.
        - Through the search function the user can filter up the displayed tasks. The user can search by keywords, which is compared with the Task name and Task description fields.
        - On an individual task, the user can get further information:
            - Orange task header background:
                - The task was registered buy someone else and noone has applied for that yet. 
                - Apply button still active for the user
                - the user cannot edit or delete it
            - Orange task header background with a light blue background text: I HAVE APPLIED:
                - the task was created by someone else and the user applied to help with the task
                - Apply button replaced by the contact info of the task creator
                - user cannot Edit or Delete it
            - Grey task header background with the text of: NOT AVAILABLE FOR YOU:
                - The task has been created by someone else, but it has already been taken by someone else
                - Apply button deactivated for the user
                - the user cannot Edit or Delet it
            - Green task header background
                - the iuser created the task, but noone has applied for it yet
                - the user CAN Edit or Delete it
            - Green task header background with yellow background text HELP SHOWED UP:
                - the user created the task and someone has already applied to help
                - the user can see the volunteer contact information
                - the user CAN Edit or Delete it
        - [x] **Profile New task page**
            - the user can register a new task
        - [x] **Profile Edit task page**
            - the user can edit an already existing task content. The task must be created the user
        - [x] **Profile Apply task page** 
            - the user apply for a task through this page. The user can add further information to the help requier eg. desired contact information
        - [x] **Profile All My Task page**
            - the user can see only the following task in 2 separate sections:
                - the user created help requests
                - the user applications to help
        - [x] **Error handling pages**
            -   404: Page not found
            -   505: Internal server Error
        

    ### Future Features

    There is a lot of potential in this webpage. The focus this time was that the functionalities working properly, so the following features can be added in the future:
    -   Applying more icons and symbols for better UX
    - Automatic e-mail notification to the right persons if the status of one of the task is changed. 
    - Adding a parallel section where professional companies can search for possible clients among the help seekers. 

    <a name="technologies"></a> 

    ## Technologies Used

    ### Languages Used

    - [HTML5](https://developer.mozilla.org/en-US/docs/Web/Guide/HTML/HTML5)
    - [CSS3](https://developer.mozilla.org/en-US/docs/Archive/CSS3#:~:text=CSS3%20is%20the%20latest%20evolution,flexible%20box%20or%20grid%20layouts.)
    - [JavaScript](https://developer.mozilla.org/en-US/docs/Web/JavaScript)
    - [Python](https://www.python.org/)

    ### Workspace

    - [Gitpod](https://gitpod.io/) was used as a virtual IDE workspace to build this site.

    ### Version Control

    - [Git](https://git-scm.com/) was used for version control by utilizing the Gitpod terminal to add and commit to Git and push to GitHub.
    - [GitHub](https://github.com/) is used to store the code for this project after being pushed from Git.

    ### Wireframing

    - [Balsamiq](https://balsamiq.com/) was used to create the wireframes during the design process.

    ### Responsive Design

    - [Am I Responsive Design](http://ami.responsivedesign.is/)

    ### Site Design

    - [Font Awesome](https://fontawesome.com/) was used on all pages to add the icons.
    - [Google Fonts](https://fonts.google.com/) was used to import the _Bangers_ font used within the site.
    - [Favicon.io](https://favicon.io/favicon-generator/)

    ### Database Design Technologies

    - [MongoDB](https://www.mongodb.com/) was used to store the contents of the database, and allow full CRUD functionality.
    - [Flask-PyMongo](https://flask-pymongo.readthedocs.io/en/latest/) was used to connect this Python / Flask app to MongoDB.

    ### Frameworks, Libraries and Others

    - [Heroku](https://www.heroku.com) was used to deploy the live site.
    - [Google DevTools](https://developer.chrome.com/docs/devtools/) was used to check site responsiveness, and as a general debugger.
    - [MaterializeCss](https://www.materializecss.com) was used to design attractive, functional webpage with CSS, Javascript, Html created UI library 
    - [Lighthouse](https://developers.google.com/web/tools/lighthouse/) was used to check the site's Performance, Accessibility, Best Practices, and SEO.
    - [Flask](https://flask.palletsprojects.com/en/2.0.x/) was used to help create the templating for this site.
    - [Bootstrap](https://getbootstrap.com/) was used to create a beautiful, responsive website.
    - [jQuery](https://jquery.com/) was used to make the DOM traversal easier within the JavaScript.
    - [Jinja](https://jinja.palletsprojects.com/en/3.0.x/) was used to auto-populate the site with the contents of the database.
    - [RandomKeygen](https://randomkeygen.com/) was used to generate a strong `SECRET_KEY`.
    - [pip](https://pip.pypa.io/en/stable/) was used to install the required dependancies for this site.
    - [dnspython](https://pypi.org/project/dnspython/) was used to provide access to DNS.
    

    ### Testing

    - [W3C Markup Validation Service](https://validator.w3.org/) was used to test that the HTML is valid.
    - [W3C CSS Validation Service](http://jigsaw.w3.org/css-validator/) was used to test that the CSS is valid.
    - [JSHint](https://jshint.com/) was used to test that the JavaScript is valid.
    - [PEP8](http://pep8online.com/) was used to validate the python syntax.

<a name="scripts"></a>

## JavaScript

- ### script.js:
    this javascript file contains all the functions which is running the materializecss functions

<a name="testing"></a>

## Testing

The W3C Markup Validator and W3C CSS Validator Services were used to validate every page of the project to ensure there were no syntax errors in the project.

-   [W3C Markup Validator](https://jigsaw.w3.org/css-validator/#validate_by_input) 

    -   index.html                PASSED    [Result]()
    -   login.html                 PASSED    [Result]()
    -   register.html             PASSED    [Result]()
    -   profile.html            PASSED    [Result]()
    -   profile_alltask.html                PASSED    [Result]()
    -   profile_new_task.html                 PASSED    [Result]()
    -   profile_edit_task.html             PASSED    [Result]()
    -   profile_apply_task.html            PASSED    [Result]()
    -   profile_mytasks.html                PASSED    [Result]()
    -   about.html                 PASSED    [Result]()
    -   contact.html             PASSED    [Result]()
    -   404.html            PASSED    [Result]()
    -   500.html            PASSED    [Result]()
    -   base.html            PASSED    [Result]()


-   [W3C CSS Validator](https://jigsaw.w3.org/css-validator/#validate_by_input) 

    -   style.css                 PASSED 
        
    :point_right: <a href="http://jigsaw.w3.org/css-validator/check/referer">
        <img style="border:0;width:88px;height:31px"
            src="http://jigsaw.w3.org/css-validator/images/vcss-blue"
            alt="Valid CSS!" />
    </a> :point_left: Results

### Testing User Stories from User Experience (UX) Section

-   #### First Time Visitor Goals

    1. As a First Time Visitor, I want to easily understand the content of the webpage and the aim of the site.
        1. right on the index page there are 2 main expressions, which targets the topic of the website
        2. the tasks in the database section on the main page also gives a short insight what is waiting for the user inside
        3. the about navigation menu also gives a description
    2. As a First Time Visitor, I want Register for an Account
        1. to register to the website can happen by clicking on the register button on the main page
        2. by clicking on the Login/register menupoint the user can get to the register form as well
    3. As a First Time Visitor, I want to be able to easily navigate through the site and get an overal picture about the site structure.
        1. There are not many menupoints outside of the member are, so nthing complicated to have a good overview.
        2. At the user are  the navigation is a sticky navbar so even the user has to scroll away because of the contetnt, it will be always visible where the user can go
    4. As a First Time Visitor, I want to see their social media availability, where i can get more information about the site or organisation / person behind that.
        1. on the contact page all these informations are available
        2. the content page available in the member area and outside the member area as well
    5. As a first Time Visitor i want to see clearly what content available for without registration and what requires registration. 
        1. right on the main page all the data which is available without registration is shown. Mor info accessable only with registration

-   #### Returning Visitor Goals

    1. As a Returning Visitor, I want to be able to login with my previously registered credentials.
        - on the main page there is the Login / Register menupoint. By clicking on that the user get to the login page, where can fill in the previously registered credentials, if the login name and the password were given correctly, theuser gets into the user area. If there was a problem, the user get a flash message
    2. As a Returning Visitor, I want to be able to register request for help.
        - in the member area there is a separate menupoint where the user can register a request for help through a form
    3. As a Returning Visitor, I want to be able to apply to help someone else.
        - in the member area the user can see all the available tasks. Can also search among them. All available (understand not taken) task has an active apply button. If the task is not available, the Apply button is deactivated
    4. As a Returning Visitor, I want to be able to update my profile information.
        - after logging into the member area the first page that the user see is the profile page. by just simply modifying the data in the fields and by clicking on the Update Profile button the previously given data can be overwritten, Note: every registered data can be updated except the username and password
    5. As a Returning Visitor, I want to be able to edit my help request information.
        - in the member area the user can edit and delete the tasks that were created by herself/himself. it can be done on the All Tasks page or under the Tasks by Me menupoint by just simply clicking on the Edit button
    6. As a Returning Visitor, I want to be able to delete my registered requests.
        - in the member area the user can edit and delete the tasks that were created by herself/himself. it can be done on the All Tasks page or under the Tasks by Me menupoint by just simply clicking on the Delete button
    7. As a Returning Visitor, I want to be able to browse among all regitered tasks.
        - in the member area under the All Tasks menupoin all the registered tasks i nthe system are visible. The user can simply scroll down or search for specific keywords in the search input field. The search function search for wirds in the task name and the task description 

-   #### Admin Goals
    As the admin i want to be able to delete any of the registered tasks.
        - as an admin the only thing you can change is to delete any of the registered tasks. The registration can happen by anyone

### Further Testing

-   The Website was tested on Google Chrome, Internet Explorer, Microsoft Edge browsers.
-   The website was viewed on a variety of devices such as Desktop, Laptop, iPhoneSE, iPhone 6 & iPhone 11 Pro.
-   A large amount of testing was done to ensure that all pages were linking correctly.

### Functional Testing
-   During the development process and after that there were several tests carried out to validate the links. All external and internal links were tested several times.

### Known Bugs
At this point there are no known bugs but during the development process in the testing periods some bug has been detected. They were the following: 
-   the main problems were communication between the database flask. By reinstalling the libraries the problems were solved. If not it turned out Github had problems
-   during edit features the database data were not overwriten or were overwriten with no data. The problem mainly was that in the python snippet wrong addressing wer used


<a name="deployment"></a>

## **Deployment**

### Requirements for Deployment

* Python
* MongoDB account and database
* GitHub account
* Heroku account

### Initial Deployment

* MONGO_DBNAME - This is the name of the database you need to connect to in MongoDB.

* MONGO_URI - This can be found on the MongoDB website by following these steps:
    * In the clusters tab of your database, click connect on the associated cluster.
    * Click 'Connect', then 'Connect your application'.
    * Copy the string, then substitute the password (from Database access NOT your MongoDB password) and change "myFirstDB" to your MONGO_DBNAME.

* SECRET_KEY - This is a custom string set up to keep sessions secure. I recommend using a 'Fork Knox' level password generated by [RandomKeygen](https://randomkeygen.com/).

* This site was deployed to Heroku by following these steps:

    1. Heroku needs to be told what the requirements are for this project, so go into your GitPod terminal, and create files to explain the requirements by using the following commands:
        * `pip3 freeze --local > requirements.txt`
        * `echo web: python run.py > Procfile` - Ensure there is no blank line after the contents of this file
    2. Push these changes to your repository.
    3. Ensure you have a .gitignore file in your repository, and if not, create one.
    4. Add `env.py` and `__pycache__/` into your .gitignore file, and save the file. This is to avoid any sensitive information being added into your repository.
    5. Create an env.py file, and add the following information to it, updating the '## x ##' values with your own values:

        ``` python
        import os

        os.environ.setdefault("IP", "0.0.0.0")
        os.environ.setdefault("PORT", "5000")
        os.environ.setdefault("SECRET_KEY", " ## YOUR SECRET_KEY ## ")
        os.environ.setdefault("MONGO_URI", " ## YOUR MONGO_URI ## ")
        os.environ.setdefault("MONGO_DB", " ## YOUR MONGO_DBNAME ## ")
        ```

    6. Login or sign up to [Heroku](https://www.heroku.com).
    7. Select 'Create New App' in the top right of your dashboard.
    8. Choose a unique app name, and select the region closest to you, before clicking 'Create App'.
    9. Go to the 'Deploy' tab, find 'Deployment Method' and select 'GitHub'.
    10. Search to find your GitHub repository, and click 'Connect'. Don't enable automatic deployment yet, as this can cause errors.
    11. Go to the 'Settings' tab, find 'Config Vars', and click 'Reveal Config Vars'.
    12. Enter key value pairs that match those in your env.py file, displayed like this :

        | Key | Value |
        |---|---|
        | IP | 0.0.0.0 |
        | PORT | 5000 |
        | MONGO_DBNAME | ## YOUR DATABASE NAME ## |
        | MONGO_URI | ## YOUR MONGO_URI ## |
        | SECRET_KEY | ## YOUR SECRET_KEY ## |

    13. Go to the 'Deploy' tab, and click 'Enable Automatic Deployment'.
    14. In 'Manual Deploy', choose which branch you'd like to deploy from (I chose 'master' branch, this is also known as 'main').
    15. Click 'Deploy Branch' to deploy your app onto the Heroku servers.
    16. Once the app has finished building, click 'Open App' to open your site.

### How to Fork it

1. Login or Sign Up to [GitHub](www.github.com).
2. On GitHub, go to [szomoru/extrahand-mp3](https://github.com/szomoru/extrahand-mp3).
3. In the top right, click "Fork".
4. You will need to create an env.py file with your own values, and create a MongoDB database with the data keys and types as shown above.
5. You will also need to install all of the project requirements. This can be done using the command:
    * `pip3 install -r requirements.txt`
6. Type `python3 app.py` in your GitPod terminal to run your local site of this project.

### Making a Local Clone

1. Log in to [GitHub](https://www.github.com) and locate the [Repository](https://github.com/szomoru/extrahand-mp3) for this site.
2. Under the repository name, above the list of files, click "Code".
3. Here you can either Clone or Download the repository.
4. You should clone the repository using HTTPS, clicking on the icon to copy the link.
5. Open Git Bash.
6. Change the current working directory to the new location, where you want the cloned directory to be.
7. Type `git clone`, and then paste the URL that was copied in Step 4.
    * `git clone https://github.com/szomoru/extrahand-mp3.git`
8. Press Enter, and your local clone will be created.
9. You will need to create an env.py file with your own values, and create a MongoDB database with the data keys and types as shown above.
10. You will also need to install all of the project requirements. This can be done using the command:
    * `pip3 install -r requirements.txt`.
11. Type `python3 app.py` in your Gitpod terminal to run your local site of this project.

Alternatively, if using Gitpod, you can click below to create your own workspace using this repository.

[![Open in Gitpod](https://gitpod.io/button/open-in-gitpod.svg)](https://gitpod.io/#https://github.com/szomoru/extrahand-mp3)


<a name="credits"></a>

## Credits

### Code

-   [Bootstrap4](https://getbootstrap.com/docs/4.4/getting-started/introduction/): Bootstrap Library used throughout the project mainly to make site responsive using the Bootstrap Grid System.

-   [W3Schools](https://www.w3schools.com/): I have used their content many times to understand CSS and HTML, JavaScript and learned a lot from their content

-   [Froggy](https://flexboxfroggy.com/): I have used this cute educator site to understand better the flexbox method

-   [CSS tricks](https://css-tricks.com/): I have also learned a lot and found interesting topics on the CSS-tricks website

-   [Stackoverflow community](https://stackoverflow.com/): I have read a lot of forums and got a lot of hints how to continue when i was stucked.

### Content

-   All content was written by the developer -Gergely Vig. 
- I have used the following documents as a support and inspiration for the README.md file:
    - Code Institute [SampleREADME](https://github.com/Code-Institute-Solutions/SampleREADME)
    - Code Institute [README Template](https://github.com/Code-Institute-Solutions/readme-template)
    - [Markdown Cheatsheet](https://github.com/adam-p/markdown-here/wiki/Markdown-Cheatsheet#code)
    - [Mastering Markdown](https://guides.github.com/features/mastering-markdown/)
    - [Gergely Vig](https://github.com/szomoru/MP1-Bodyweight)
    - [Carla Buongiorno](https://github.com/CarlaBuongiorno/The-Collector)
    

### Media

-   All used images have been taken from wikipedia page:
    

### Acknowledgements

-   My Mentor for helpful feedback.
-   Thanks to my family specially my wife who taken over our 4 kids while i was doing my studies. 
