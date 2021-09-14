<!--
*** Thanks for checking out the Best-README-Template. If you have a suggestion
*** that would make this better, please fork the repo and create a pull request
*** or simply open an issue with the tag "enhancement".
*** Thanks again! Now go create something AMAZING! :D
-->



<!-- PROJECT SHIELDS -->
<!--
*** I'm using markdown "reference style" links for readability.
*** Reference links are enclosed in brackets [ ] instead of parentheses ( ).
*** See the bottom of this document for the declaration of the reference variables
*** for contributors-url, forks-url, etc. This is an optional, concise syntax you may use.
*** https://www.markdownguide.org/basic-syntax/#reference-style-links
-->

<!-- PROJECT LOGO -->
<br />
<p align="center">
    <img src="readmeImages/med.png" alt="Logo" width="250" height="auto">

  <h1 align="center">Online Pharmaceutical product distribution System for Pharmac (PVT).Ltd.</h1>

  <p align="center">
    Project overview and installation instructions
    <br />
    <a href="https://github.com/othneildrew/Best-README-Template"><strong>Explore the docs »</strong></a>
    <br />
    <br />
    <a href="https://github.com/othneildrew/Best-README-Template">View Demo</a>
    ·
    <a href="https://github.com/othneildrew/Best-README-Template/issues">Report Bug</a>
    ·
    <a href="https://github.com/othneildrew/Best-README-Template/issues">Request Feature</a>
  </p>
</p>



<!-- TABLE OF CONTENTS -->
<details open="open">
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
    <!--<li><a href="#roadmap">Roadmap</a></li>-->
    <li><a href="#contributing">Contributing</a></li>
    <li><a href="#license">License</a></li>
    <li><a href="#acknowledgements">Acknowledgements</a></li>
    <li><a href="#contributors">Contributors</a></li>
  </ol>
</details>



<!-- ABOUT THE PROJECT -->
## About The Project

<!--[![Product Name Screen Shot][product-screenshot]](https://example.com)-->

Pharmac Distributors Co. (PVT) LTD is a pharmaceutical importer and distributor based in Kandy, providing service to hundreds of pharmacies and dispensaries island wide. They legally source pharmaceutical products, store them under proper conditions before distributing them among authorized sellers. Their goal is to become the largest pharmaceutical distributor in the country. However, their operations are vastly affected by the inefficiency of the manual system currently deployed. Therefore, they have decided to implement an automated system to manage all possible functions and directly connect with the customers to provide more efficient service.

### Built With

This section shows the list of major frameworks that we have used to  built our project . 
* Front-end : [Vue JS 2](https://vuejs.org/)




<p align="center"><a href="https://vuejs.org/" target="_blank"><img src="https://vuejs.org/images/logo.png" width="150"></a></p>



* Back-end : [Laravel 8](https://laravel.com)

<p align="center"><a href="https://laravel.com" target="_blank"><img src="https://raw.githubusercontent.com/laravel/art/master/logo-lockup/5%20SVG/2%20CMYK/1%20Full%20Color/laravel-logolockup-cmyk-red.svg" width="400"></a></p>

* Database : [MySQL](https://www.mysql.com/)

<p align="center"><a href="https://www.mysql.com/" target="_blank"><img src="readmeImages/pngegg.png" width="200"></a></p>



<!-- GETTING STARTED -->
## Getting Started

In order to be fully funtional and uprunning the following should be followed

### Prerequisites

The following applications must be installed
* Xampp server with php version 8.0
* MySQL server
* Latest version of composer installed
* Node Package Manager(npm)
<!--
  ```sh
  npm install npm@latest -g
  ```
-->
### Installation


1. Clone the repository
   ```sh
   git clone https://github.com/salukadev/Pharmac-OMS.git
   ```
2. Install Composer packages
   ```sh
   composer install
   ```
3. Install Node Package manager packages
   ```sh
   npm install
   ```
4. Add `.env` file and copy the content from `.env.example` file   
5. Configure the database in `.env` file
   ```sh
   DB_CONNECTION=mysql
   DB_HOST=127.0.0.1
   DB_PORT=3306
   DB_DATABASE='Your database name'
   DB_USERNAME='Your database username'
   DB_PASSWORD='Your database password'
   ```
7. Generate keys
   ```sh
   php artisan key:generate
   ```
6. Generate migrations
   ```sh
   php artisan migrate
   ```

8. Run development serve
   ```sh
   php artisan optimize
   php artisan serve
   ```
9. For development purposes
   ```sh
   npm run watch
   ```

   Incase of Issue in setting the environment 
    ```sh
   npm install laravel-mix@latest
   ```
 
<!--   ```
7. Enter your API in `config.js`
   ```JS
   const API_KEY = 'ENTER YOUR API';
   ```
   -->





<!-- CONTRIBUTING -->
## Contributing

Contributions are what make the open source community such an amazing place to be learn, inspire, and create. Any contributions you make are **greatly appreciated**.

1. Clone the project <br>`git clone https://github.com/salukadev/Pharmac-OMS.git`
2. Create your Feature Branch<br> `git checkout -b feature/AmazingFeature`
3. Commit your Changes <br>`git commit -m 'Add some AmazingFeature'`
4. Push to the Branch <br>`git push origin feature/AmazingFeature`
5. Open a Pull Request



<!-- LICENSE -->
## License

Distributed under the MIT License. See `LICENSE` for more information.



<!-- CONTACT 
## Contact

Your Name - [@your_twitter](https://twitter.com/your_username) - email@example.com

Project Link: [https://github.com/salukadev/Pharmac-OMS.git](https://github.com/salukadev/Pharmac-OMS.git)
-->

<!-- ACKNOWLEDGEMENTS  -->
## Acknowledgements

<p align="center"><a href="https://www.sliit.lk/" target="_blank"><img src="readmeImages/SLIIT_Logo_Crest.png" width="100"></a></p>

This is a project done for the Information Technology project module of BSc.(Hons.) Degree in Information Technology in Sri Lanka Institute of Information Technology


## Contributors
* IT19188928 - Saluka Udbhasa - [salukadev](https://github.com/salukadev)
* IT19142838 - Esala Senarathna - [Esala-Senarathna](https://github.com/Esala-Senarathna)
* IT19957180 - Danuja Wijerathne - [danuja-wije](https://github.com/danuja-wije)
* IT19955896 - Salitha Tennakoon - [salitha10](https://github.com/salitha10)
* IT19001708 - Parami Lelkada - [pLe98](https://github.com/pLe98)
* IT19987880 - Manoj Rangana - [RanganaPWM](https://github.com/RanganaPWM)
* IT19987712 - Kavindya Perera - [kavindya-perera](https://github.com/kavindya-perera)
* IT19955896 - Ridma Reshan - [ridma11](https://github.com/ridma11)






<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[contributors-shield]: https://img.shields.io/github/contributors/othneildrew/Best-README-Template.svg?style=for-the-badge
[contributors-url]: https://github.com/othneildrew/Best-README-Template/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/othneildrew/Best-README-Template.svg?style=for-the-badge
[forks-url]: https://github.com/othneildrew/Best-README-Template/network/members
[stars-shield]: https://img.shields.io/github/stars/othneildrew/Best-README-Template.svg?style=for-the-badge
[stars-url]: https://github.com/othneildrew/Best-README-Template/stargazers
[issues-shield]: https://img.shields.io/github/issues/othneildrew/Best-README-Template.svg?style=for-the-badge
[issues-url]: https://github.com/othneildrew/Best-README-Template/issues
[license-shield]: https://img.shields.io/github/license/othneildrew/Best-README-Template.svg?style=for-the-badge
[license-url]: https://github.com/othneildrew/Best-README-Template/blob/master/LICENSE.txt
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555
[linkedin-url]: https://linkedin.com/in/othneildrew
[product-screenshot]: images/screenshot.png
