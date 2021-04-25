# Ontario-Covid-19-QNA-Forum

Sources Of Inspiration

The first inspiration for this project was simply the oppurtunity to take my knowledge of JavaScript, HTML and CSS and be able to apply it to the Python Flask framework, essentially an oppurtunity to learn the Flask framework, Bootstrap styling, Blueprints and the SQLAlchemy ORM for database management all on a Kali Linux environment.

Secondly, working a Co-op term remotely in the Ontario Public Sector during the Covid-19 Pandemic motivated me to use web application development tools to create a platform that allows users access to a forum in response to their queries related to the Covid-19 pandemic.

Lastly, during my Co-op term working as a Student IT Support Officer for the Ontario Public Sector, I had the oppurtunity to learn about accesibility especially in government documents. This motivated me to want to learn how to build an application with a Dark Mode feature to support visual accessibility needs.


What Is This Project?

This web application is a fully featured forum that allows users the ability to post queries regarding the Coronavirus pandemic and have them answered by other users on the forum. Key features include a Dark Mode, the ability to respond to or comment on queries anonymously, the ability to update account details on the fly including being able to add a profile picture, the ability to register and create new user accounts and a dynamic UI that is responsive to differing screen size.

How I Built It

I built this forum by creating a few Blueprints via the Flask framework. I then created HTML pages to populate the routes within those Blueprints and styled them using a mix of CSS and Bootstrap (4.0 and 5.0) elements. Certain features like the Dark Mode toggle were implemented using JavaScript while all database management, including the creation itself of the database was done through the SQLAlchemy ORM.

Challenges I Ran Into

While some features of the application were relatively straightforward to implement like rendering HTML templates, other features like implementing a Dark Mode, performing database queries and even implemnting a comment section were decently challenging. To mitigate some of these issues, I initially created a test route where I would test the implementation of features like a Dark Mode. With the Dark Mode I ran into some trouble flipping between two CSS files and had to properly define a variable linking to the Dark Mode CSS file. I also had to figure out how to store a local variable that would keep the state of the application so that if a user reloaded their page after enabling Dark Mode, the correct CSS file would be retained. The comment or response section also proved difficult as my initial database had become corrupt due to use of old SQLAlchemy commands and so I had to recreate it with the updated version commands in order for it to render properly. Fortunately, with a little research and much trial and error I was able to mitigate much of the challenges I ran into.

Features I'm Proud Of

Personally, I'm quite proud of my Dark Mode implementation, while it's not perfect I'm glad it gets the job done, same can be said for my comment section implementation. Mitigating backened database errors proved especially tricky but with the help of Google and some of the relevent SQLAlchemy documentation I succeeded in developing a working comment section by establishing a relationship between Post models and their associated Comment models.
