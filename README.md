
# Recipe Bot 

 Authors: Aryan Vinod, Harshini Sarraff, Bhavna Ramkumar, Sahithi Matta
  Authors: <[Harshini Sarraff](https://github.com/harshinisarraff)> <[Aryan Vinod](https://github.com/AyeItsVinny)> <[Sahithi Matta](https://github.com/smatt023)> <[Bhavna Ramkumar](https://github.com/bhavnaramkumar1)>

## Project Description

  * As college students who struggle to make meals and can find recipes in an easy way. We think this project will be helpful to those who are very busy such as college students.
  * This idea is also very unique because we are implementing AI into something simple such as a cook book we are combining new technology into something that has been popular for a very long time.
 * For this project we plan on using Python for the backend and HTML, CSS, and Javascript for the frontend. We plan on using Visual Studio Code and Github.
   
* Chatbot features:
  
  * if users are unsure on what they want to cook they can click a chatbot button at the bottom of the home page
  * users can enter specific ingredients they currently have and based on that the ai chat bot can provide different food options
  * users can also enter flavors they are craving and based on that the ai chat bot can provide different food options
  * API; we are incorporating a chat gpt API for the custom input for the chatbot.
  * there is a nav bar with login/signup/signout

 > ## Phase II

## User Interface Specification

### Navigation Diagram
 <img width="727" alt="Screen Shot 2024-03-14 at 12 13 27 PM" src="[https://github.com/cs100/final-project-hsarr001-avino008-bramk002-smatt023/assets/156261894/73d7d255-651b-4b38-aec2-65c8e996f66](https://github.com/smatta27/recipe-bot/blob/main/navigationimg.png?raw=true)f">



### Screen Layouts
<img width="812" alt="Screen Shot 2024-03-14 at 3 34 49 AM" src="https://github.com/cs100/final-project-hsarr001-avino008-bramk002-smatt023/assets/151404736/a8e87dc2-2f17-4e19-8663-ba41bb15f766">


## Class Diagram
 ![Cs_final_project-2](https://github.com/cs100/final-project-hsarr001-avino008-bramk002-smatt023/assets/156261894/20f33a0b-164f-4a7b-b1ac-b31e2b8b7bd2)
 
![Cs_final_project-3](https://github.com/cs100/final-project-hsarr001-avino008-bramk002-smatt023/assets/156261894/d657efa3-de69-44f1-a4fe-6b80f7845361)

![Cs_final_project-4](https://github.com/cs100/final-project-hsarr001-avino008-bramk002-smatt023/assets/156261894/baea1e41-4ae8-4f09-9104-5cd70ac74b06)


 > ## Phase III

 ## User Interface Specification

## Class Diagram
![Cs_final_project-2](https://github.com/cs100/final-project-hsarr001-avino008-bramk002-smatt023/assets/156261894/582084a7-01dd-4c35-ab71-7a2167c899ac)

 In this diagram, I discarded the searchbar class and simply combined with the chatbot class to create a universal AI that can carry out all the required functions of our program. For the searchbot class, I applied the SRP principle because each class to has specific role in the chatbot AI and did not want to put multiple functions into one class, so the searchbot is divided into recipe which contains the specifc characteristics for the recipe, and the searchbar(html/css) itself. This also utilizes the ISP principle as there is no unused methods or interfaces being used for any of the classes in the diagram. Each function and class exist purely towards the functionality of the program and none of it will go unused or unutilizewd in the final project. This diagram also utilizes the OCP principle as the print functions inside Recipe could be extended in a way to print more information without modifying its already existing methods. These principles assisted with keeping the code more organized and made it to be not be dependant on a singular interface or class, so that the program would still function properly.
![Cs_final_project-3](https://github.com/cs100/final-project-hsarr001-avino008-bramk002-smatt023/assets/156261894/7cca7f6e-0db7-48ec-9b47-fe108552f62f)

 
 In this diagram, I designed the homepage in a similar manner as I did in the previous page, however, I took out variables and functions that were not necessary and linked the homepage to other necessary pages such as the chatbot and the sidebar. The SRC principle was utilized as sidebar contains its own responsibilities shown on the side portion of the homepage and homepage is like a coordinator to the sidebar and the chatbot page. The homepage has it's own specific role which is to potray a captivating layout that contains the sidebar and the chatbot button. If there were extended classes to the homepage, it would not affect its main function which would be to showcase the sidebar and the chabot page which adheres to the OCP principle. Even if certain functions or classes were added to the homepage, it would not affect its functionality and the program would run as usual. These principles assisted with keeping the code more organized and made it to be not be dependant on a singular interface or class, so that the program would still function properly.
![Cs_final_project-4](https://github.com/cs100/final-project-hsarr001-avino008-bramk002-smatt023/assets/156261894/96b97f05-7fe7-41d1-8549-b26f96693761)


In this diagram, I designed the sidebar in a similar manner as I did in the chatbot class. I used similar principles as the chatbot class such as the SRP principle as it only contains one key responsibility which is to showcase and link the subcategories onto the sidebar. If additional uses were added to the sidebar for extension, it would not affect the overall function of the sidebar which is to showcase and link said subcategories. There's not an excessive amount of code in this class and each class specifies its functions without including variables or functions that are not necesssary for this layout. These principles assisted with keeping the code more organized and made it to be not be dependant on a singular interface or class, so that the program would still function properly.

 
 > ## Final deliverable

 ## Screenshots
> <img width="227" alt="Screenshot 2024-03-14 at 10 40 00 AM" src="https://github.com/cs100/final-project-hsarr001-avino008-bramk002-smatt023/assets/141898541/e887d67b-3cce-4a32-8113-bfdfa4b879d5">

* This is what the folders in the vs code has to look like so it would properly run. All html files have to be umder templates folder and the css files under the static folder. Lastly, the chatbot.py should be outside of these two folders like shown above. 
<img width="821" alt="Screenshot 2024-03-14 at 10 40 42 AM" src="https://github.com/cs100/final-project-hsarr001-avino008-bramk002-smatt023/assets/141898541/4acd6a78-b9cb-411c-ad6d-3171a3857507">

* For the website to run click on the chat.py and click the play button in the corner(the triangle button)

<img width="821" alt="Screenshot 2024-03-14 at 10 41 25 AM" src="https://github.com/cs100/final-project-hsarr001-avino008-bramk002-smatt023/assets/141898541/dd17b4a8-ac9b-4124-9f86-292089ee122c">
<img width="1440" alt="Screenshot 2024-03-14 at 10 42 11 AM" src="https://github.com/cs100/final-project-hsarr001-avino008-bramk002-smatt023/assets/141898541/1690950d-4dbe-432b-bc3c-a0574c2a9fff">

* Once you hit the run button, it would generate a http link. Copy the link in your web browser
  
<img width="1440" alt="Screenshot 2024-03-14 at 10 42 35 AM" src="https://github.com/cs100/final-project-hsarr001-avino008-bramk002-smatt023/assets/141898541/be50313b-1007-4fb8-876e-6c49397c6ebf">

* Now you should be able to see our website. There is a navbar in the side the leads us to diffrent pages. One to sign up if you do not have a account and one to login in if you do. The infomation will be stored in a firebase. There is an about us page and a log out page. 

 ## Installation/Usage

* download python 3.12.2
* In VSC code terminal type the command: (pip3 install Flask)
* In VSC code terminal type the command: (pip3 install pyrebase4)
* In VSC In VSC code terminal type the command: (pip3 install pytest)
* Install HTML and CSS on VSC
  
 ## Testing
 <img width="1089" alt="Screen Shot 2024-03-14 at 7 41 21 PM" src="https://github.com/cs100/final-project-hsarr001-avino008-bramk002-smatt023/assets/156261894/c28febff-5e9e-4c05-a405-80b3ddc5278b">
 <img width="1189" alt="Screen Shot 2024-03-14 at 7 42 06 PM" src="https://github.com/cs100/final-project-hsarr001-avino008-bramk002-smatt023/assets/156261894/4ea5efd1-8187-4ad2-9cdd-121831162562">
 <img width="1188" alt="Screen Shot 2024-03-14 at 7 51 53 PM" src="https://github.com/cs100/final-project-hsarr001-avino008-bramk002-sm
  <img width="1183" alt="Screen Shot 2024-03-14 at 7 52 09 PM" src="https://github.com/cs100/final-project-hsarr001-avino008-bramk002-smatt023/assets/156261894/6bbbfc6e-51df-4d9d-906b-751b27194644">
att023/assets/156261894/11ea5068-faa0-4b9f-8dc0-2d9a48b0fed6">
<img width="1183" alt="Screen Shot 2024-03-14 at 7 52 09 PM" src="https://github.com/cs100/final-project-hsarr001-avino008-bramk002-smatt023/assets/156261894/188119c1-1924-43b8-9c14-10053a58ae47">

<img width="1072" alt="Screen Shot 2024-03-14 at 7 52 26 PM" src="https://github.com/cs100/final-project-hsarr001-avino008-bramk002-smatt023/assets/156261894/8539aa64-1668-4886-8f99-031524e8a9ed">

