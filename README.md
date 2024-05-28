<h1 align="center" id="title">Insight-Guard</h1>

<p align="center"><img src="https://socialify.git.ci/Younus-Saberi/Insight-Guard/image?description=1&amp;font=Raleway&amp;forks=1&amp;issues=1&amp;language=1&amp;name=1&amp;owner=1&amp;pattern=Signal&amp;pulls=1&amp;stargazers=1&amp;theme=Dark" alt="project-image"></p>


# Insight Guard

A Chronic eye disorder called glaucoma leading to irreversible blindness by damaging the optic
nerve of the eye. It is provoked due to exalted intraocular pressure inside the eye. Detecting glaucoma is the
most challenging process in case of open angle glaucoma (OAG) due to lack of initial symptoms.We have developed a Full Stack Application called Insight Guard to detect the disease with the help of the Machine Learning and Image Processing Library OpenCV



## Installation

Clone the project locally

```bash
  git clone https://github.com/Younus-Saberi/Insight-Guard
```
### Change the Directory to Backend
```bash
cd Backend
```
Create a Python Virtual Enviorment
```bash
python -m venv .venv
```
Activate the Enviorment in Windows
```bash
source .venv/Scripts/activate
```
Run the Backend Django Server
```bash
python manage.py runserver
```
### Chnage to Frontend Directory
Install the Dependancies
```bash
npm install
```
Run the server up
```bash
npm run dev
```



## Run Locally through Docker

Clone the project

```bash
  git clone https://github.com/Younus-Saberi/Insight-Guard
```

Go to the project directory

```bash
  cd Insight-Guard
```

Run the Docker Compose File

```bash
  docker compose up 
```



## Tech Stack

**Client:** React, Redux, TailwindCSS

**Server:** Django, Python, AWS


## API Reference

#### Get all items

```http
  POST /api/predict
```

| Body Parameter | Type     | Description                |
| :-------- | :------- | :------------------------- |
| `image` | `Form-Fields` | **Required**. image |

#### Get item

```http
  GET /api/cdr/
```

| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `iamge_id`      | `int` | **Required**. Id of Image to Compute |




## Screenshots

![App Screenshot](https://via.placeholder.com/468x300?text=App+Screenshot+Here)


## Environment Variables

To run this project, you will need to add the following environment variables to your .env file

`Google Gemini API_KEY`

`Google OAuth API_KEY`

`AWS_SECERT_KEY`

`AWS_ACCESS_KEY`

`AWS_BUCKET_NAME`


## Support

For support, email younussaberi@gmail.com 


## Documentation

[Documentation](https://ijcrt.org/papers/IJCRT2403694.pdf)


## License

[MIT](https://choosealicense.com/licenses/mit/)



TASK LIST
- [x] Make Basic File upload.
- [x] Make validation before upload.
- [x] Refactor image after upload.
- [x] Make model predict.
- [x] Draw Eclipse with Opencv2.
- [x] Upload image to s3.

- Download our ML model using the link [here](https://drive.google.com/file/d/19NnGMA99WZls7KM4sJ7jArz7dFzXJKnF/view?usp=drive_link)
- List of Model Folder in [Google Drive](https://drive.google.com/drive/folders/1jX9-Ckk1CHz3q4eT8JAesepXoGVXiCqt?usp=sharing)
- List of Resource Materials [here](https://github.com/Younus-Saberi/GlaucomaDetection/tree/master/resources)
