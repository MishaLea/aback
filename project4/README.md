Smiling Coast Apartments
 
This wesite is specifically targetting a niche market of tourists/ long term vacationers/ex-patriates visiting the Gambia. And the featurers included allow the user to make/amend cancel bookings direct through the site. 
Table on Contents
User Experience
-	Site Goals/ Initial Requirements
-	User Stories
-	Agile Methodology
-	Wireframes
-	UX Design
-	Features
-	Testing HTML, CSS, Javascript, Python and Django
-	Fixed Bugs
-	Deployment
-	Credits

UX Design 

Strategy: 
Site Goals
This website will include several specific features including: 
1)	Home page with basic features such as: 
-	navigation links which direct the user across the web application. 
-	Pictures and a description of the apartments 
-	Footer with social media links 
2)	Bookings page with the following deatures: 
-	Main cover image
-	Booking information including links to contact us. 
-	Booking form including additional user friednly features a) availabilty checker b)  booking facility c) cancellation and d) edit booking features. 
-	Header including nav links/logo and footer with social media links. 
3)	Sign In/Login/Log Out Pages.  
-	All with authentication features that provides correct data for entry and also confrmation to user. 
-	Footer on bottom of sign in page. Also includes link to login if already registered and the logout page will direct the user back to the home page. 
4)	Special Features: 
-	Message/Notification from admin informing of certain conditions: email already in use, wrong characters used, wrong password etc.. 

User Stories
As a User, 
-	I would like a clear understanding of the web app and easy navigation throughout the pages. 
-	I would like a clear and easy to understand spec of the accommodation
-	I would like the Web App Contact info available and easy to make booking/s with the option to amend or delete bookings.  
-	 I would like to know when my email is submitted that the registration was successful. 
-	I would like to know if I can log out efficiently. 

Business Objectives: 
With rental properties booming in The Gambia and 3rd party companies having much of the control over marketing privately owned accommodation. It has come to my attention that the benefit of handling your own bookings and web application allows the user/potential guests the ability to have a secure and accesible form of booking that is direct with the property.. This benefits both the owner and users as it removes any 3rd party services/charges and allows us to create a safe and secure environment for our user. 
This inturn offers trust to the user and a straightforward approach to bookings including the options to cancel and to amend bookings. 

Scope:
Functional Specifications

Standard Features to include: 
-	Navigation links as well as footer with social media links on home and bookings page. The Sign in and log in form pages will have a footer but no nav links on top of page. 
-   The home page will include 3 different room options including price and specific view request. Each room has a link which will redirect to the bookings form page. 
-	The bookings page will include links for contact us as well as T&C’s. 
-	On the bookings page will also include a form that allows the user to make/edit/cancel a booking. As well as confirm any unavailable dates. 
-	The Sign in page will allow the user the option to register with us for special offers and discounts for future bookings. 
-	A link will be provided for those already registered and wishing to log in. 
-	The log in form will have a secure authorisation process to make sure the correct email, username etc is provided in order to sign in safely. 
-	For any error in submitting the forms, a notificatoin message will show the user what the problem is and how to fix it. 

Content Requirements to include:  
-	Images of accommdation
-	Brief introduction to what the property provides the guests
-	A tropical colour pallete to enhance the propeties features. 
-	Easy to find and well designed web app to allow for good UX design

Structure: 
-	The home screen will have one or two main images just under the navigation bar. Followed by a brief paragraph on the apartments and what is provided. Below this will be a few images to show the aesthestics of the apartments and finally, the footer will include 3 social media links. Facebook, insta and Youtube.  
-	The bookings page will start off with an medium/large sized image leading in to the information regarding bookings and links to Contact Us and Terms and Conditions. This leads in to the booking form, with the footer ending the 2nd browser page. 
-	The Sign/Up and Login pages will look similar with same layout. A footer will be on the lower section of both pages with links to either login on sign up page or log out on log in page. 


Surface: 

Colour Pallete:
The colours I chose all correlate together and can be used interchangebly. For simplcity, the main theme is the dark blue is the background colour for the body with Ivory being used for borders and most text. 



Typography: 
For the majority of the text content, im using Josefin Sans (italic) with Sans Sarif as back up. For the Booking Form, I wanted to create a standout section that still corresponds with the overall appeal of the design, by using Mouse Memoirs in the Booking Form only. 
I imported the fonts from google fonts to css. 

Icons
The icon used throughout the web app are provided by fontawesome. This was included in the HTML pages. 

Pictures: 
All pictures have been utilised via pixels.

Django 
Created Django – Project name: Project4 
-	In project, created 2 separate, independent apps – Accounts & Rooms. 
-	Accounts App – focuses on user login, signup and similar authentication features. 
-	Room App – focuses on listing rooms, adding rooms and amending bookings. 
-	High Level Architecture

Accounts App: 
-	I wanted a system in which we could authenticate if a user is valid based on email/password. 
-	Django’s default authentication is username and password, so in order to get around that – we override the user table which Django provides. 
-	To do this, a new table was created in models.py. 
-	Also added extra functions to create users and superusers. (Helper Functions) 
-	By doing this, we override default behaviour and our system now authenticates. 
-	We created 2 routes in urls.py (in accounts directory)
-	URL Patterns are: 
1)	Login route
2)	Signup route
-	In routes, I wrote logic for each route, so they know what to do. 
-	For that, 2 functions were created – one for login and one for signup. 
Login Function 
-	Authenticate login Checks if request is POST and either extracts email & password from post and authorises using predetermined method. 
-	Backend.py shows auth method and get user method.  
-	When written it will call method and logic checks if valid or not. 
Logic on line 19 will direct to home page. If not correct, will redirect to login page. 

Similar for sign up 
Authenticate by overriding Django predetermined templates. 

In Rooms
Created multiple routes;
-add.rooms		add new room
-get_rooms		search room info
-get_all_rooms		list all rooms

Have written methods in views.py

New table called ‘rooms’ in models.py inc room no, prices etc…

Initial Testing: 
n/a


Fixed Bugs: 
n/a


Deployment: 
Heroku deployment 


Credits:
pixels.com used for the images on the browser. 
fontawesome.come used for icons. 
fontgoogle used for font style.