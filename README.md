<h1 align="center">Extra Hand</h1>
<h1 align="center"><img src="./assets/img/readme/responsive.PNG" /></h1>

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

[Note about Search Volumes](#searchvolumes)

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

    -   There were several design changes during the development process, but the final site looks very similar with the wireframe. 

    -   Mobile Wireframe - [View](./assets/wireframes/Wireframe_Iphone_X_MP2.pdf)

        <img src="./assets/img/readme/wireframe_iphonex_mp2.PNG" height="400px" />


    -   Ipad Pro Wireframe - [View](./assets/wireframes/Wireframe_IpadPro_MP2.pdf)

        <img src="./assets/img/readme/wireframe_ipadpro_mp2.PNG" height="400px" />


    -   Desktop Wireframe - [View](./assets/wireframes/Wireframe_Desktop_MP2.pdf)

        <img src="./assets/img/readme/wireframe_desktop_mp2.PNG" height="400px" />

    <a name="features"></a>        

    ## Features

    ### Present Features

    #### Features accross all Pages

    -   The website was designed to have the same structure on every pages. On this way the visitor feel comfortable and find her/his way on every page.
        The layout is the following:
        - On the top section there is the Header with Navigation links
        - The middel section is the largest "main" section on every page, which contains the main information.
        - The page is closed with the Footer, which in this case contains only a Copyright text. 

    - [x] **Header**
        - The header can be divided into 2 main section. The first one is the name of the site ("Popular more Popular") without any link, it is just a decoration element. 
        - The second main section is the "navigation" section with 3 navigation items:
            -   About the Game
            -   Game
            -   Contact
    - [x] **Main section**
        - The main section contains the page specific information on every page.
    - [x] **Footer**
        - Always located as the last element of the page. In this project it does not contain any important information not to steal the focus of the visitor.        

    #### Features specific to Pages

    - [x] **Landing page**
        - Hero imnage set to the background, which clearly represents the type of the webpage
        - A smaller window floating over the background, which highlight some topic of the content od the page and call to action
        - If the visitor accept the invitation and take action after clicking the "Learn more" button, gets to the Home page.
    - [x] **About the Game page**
        - This page is the first page, that is shown after the landing page. By seeing this page the visitor gets a short description about the game itslef.
        - The visitor also can see screenshots from the game, so when she/he starts to play they are already familiar with the layout.
        - As a last element on this page the visitor can click on a button, which takes her/him to the Game page and start the game
    - [x] **Game page**
        This Game page is the soul of this site. Visually it is divided into 3 sections:
        - Header element with a question
        - "Start New Game" button, which can be a pushed anytime during the game
        - Score area where the visitor can follow up how many question is used from the total 10 questions and also how many correct and wrong answer has the visitor.
        
        At the end of the game (after answering all the 10 questions), there are 2 modals which can be shown:
        - "Winner" modal:
            This modal is shown if the number of the correct answers larger or equal than the number of the wrong answers. 
        - "Loser" modal: 
            This modal is shown if the number of the correct answers smaller than the number of the wrong answers.
        The modal window also contains text and Smile icons to visulaize if the final result is positiv or negative.
        There is also a section which shows the statistics of the game (number of correct and wrong answers).
    - [x] **Contact page**
        This is the main page for the visitor if she/he wants to contact to the website developer.
        This page is divided into 2 main sections:
        - left side of the section contains a description in which cases the visitor can contact to the developer and also contains:
         - address
         - phone number
         - social media links
         of the developer. 
        - right section contains a contact form, where the visitor can leave her/his name/e-mail and the message.
         this feature is fully set up through the email.js website 
        

    ### Future Features
    This website and game is full of possibilities for future develpments and adding new features. Here are some possible future developments:
    - Adding a feature where the visitor can define the number of the questions her-/himself. 
    - Separate page with a form to uploading data into the database.
    - After a certain number of the database it makes sense to have the possibility to play games based on professions or sex or origin of people.  
