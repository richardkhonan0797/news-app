# News-App

An app to show news from different countries. The source of the news is from News-API.

## Installation

1. Install pipenv:

```bash
sudo apt install pipenv
```

2. Create a new project using python 3.8:

```bash
pipenv --python 3.8
```

3. Install all the dependencies in requirements.txt into the virtual environment:

```
pipenv install -r requirements.txt
```

4. Activate the project's virtual environment:

```
pipenv shell
```

5. Execute the run script:

```
python run.py
```




## Endpoints

```
{{URL}} = change to your url.
```


### Register User

#### An endpoint to register a new user.

* URL
`{{URL}}/users/register`


* Method
`POST`

* Request Body
    ```JSON
    {
        "username": "username",
        "password": "password"
    }
    ```

* Success Response
    * Code : 201
    ```JSON
    { "message": "Account created successfully, a confirmation link has been sent to your email."}
    ```

* Error Response
    * Code : 400, If user already exists.
    ```JSON
    { "message": "A user with that username already exists."}
    ```
    
    * Code : 400, If email already exists.
    ```JSON
    { "message": "A user with that email already exists."}
    ```

    * Code : 400, If email format is wrong.
    ```JSON
    { "message": "Please input valid email format."}
    ```

    * Code : 500, If server error.
    ```JSON
    { "message": "Internal server error."}
    ```

### Login User

#### An endpoint to get access token and refresh token.

* URL
`{{URL}}/users/login`


* Method
`POST`

* Request Body
    ```JSON
    {
        "username" = "username",
        "password" = "password"
    }
    ```

* Success Response
    * Code : 200
    ```JSON
    { "access_token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJodHRwczovL2V4YW1wbGUuYXV0aDAuY29tLyIsImF1ZCI6Imh0dHBzOi8vYXBpLmV4YW1wbGUuY29tL2NhbGFuZGFyL3YxLyIsInN1YiI6InVzcl8xMjMiLCJpYXQiOjE0NTg3ODU3OTYsImV4cCI6MTQ1ODg3MjE5Nn0.CA7eaHjIHz5NxeIJoFK9krqaeZrPLwmMmgI_XiQiIkQ",
    "refresh_token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJodHRwczovL2V4YW1wbGUuYXV0aDAuY29tLyIsImF1ZCI6Imh0dHBzOi8vYXBpLmV4YW1wbGUuY29tL2NhbGFuZGFyL3YxLyIsInN1YiI6InVzcl8xMjMiLCJpYXQiOjE0NTg3ODU3OTYsImV4cCI6MTQ1ODg3MjE5Nn0.CA7eaHjIHz5NxeIJoFK9krqaeZrPLwmMmgI_XiQiIkQ"
    }

    * This is just an example of access token and refresh token
    ```

* Error Response
    * Code : 400, If user not activated.
    ```JSON
    { "message": "You have not activated your account, please check your email <example@email.com>."}
    ```
    
    * Code : 401, If invalid credentials is given.
    ```JSON
    { "message": "You have invalid credentials."}
    ```

### Confirm user

#### An endpoint to change user activation status.

* URL
`{{URL}}/users/confirm/<hash value>`


* Method
`GET`

* Header
    ```JSON
    {"Content-Type": "text/html"}
    ```

* Success Response
    * Code : 200
    `Returns an html page informing the user that the account has been activated.`

* Error Response
    * Code : 404, If hash doesn't exists.
    ```JSON
    { "message": "User not found."}
    ```
### Logout user

#### An endpoint to revoke access token.

* URL
`{{URL}}/users/logout`

* Method
`DELETE`

* Header
    ```JSON
    {"Authorization": "Bearer <access_token>"}
    ```

* Success Response
    * Code : 200
    ```JSON
    {"message": "Successfully logged out.}
    ```

### Get news

#### An endpoint to get news based on country and category.

* URL
`{{URL}}/confirm/<country>/<category>`


* Method
`GET`

* Header
    ```JSON
    {"Authorization": "Bearer <access_token>"}
    ```

* Success Response
    * Code : 200
    ```JSON
    [
        {
            "title": "Mobil Bekas Rp 30 Jutaan Buat Keluarga, Selain Dapat Suzuki Carry Futura, Ini Pilihan Lainnya - GridOto.com",
            "publishedAt": "2020-04-02T05:26:18Z",
            "id": 141,
            "country": "id",
            "content": "GridOto.com -Mobil bekas jenis Multi Purpose Vehicle (MPV) banyak diminati di Indonesia.\r\nSelain terkenal dengan sebutan mobil keluarga, sesuai dengan namanya kendaraan ini begitu praktis karena dapat difungsikan menjadi mobil penumpang.\r\nSebelum banyak digun… [+1625 chars]",
            "category": "business",
            "urlToImage": "https://imgx.gridoto.com/crop/0x26:640x461/700x465/filters:watermark(file/2017/gridoto/img/watermark.png,5,5,60)/photo/2019/09/14/1261833884.jpg",
            "url": "https://www.gridoto.com/read/222087013/mobil-bekas-rp-30-jutaan-buat-keluarga-selain-dapat-suzuki-carry-futura-ini-pilihan-lainnya?page=all",
            "source_id": null,
            "description": "Mobil bekas jenis Multi Purpose Vehicle (MPV) banyak diminati di Indonesia,terkenal dengan sebutan mobil keluarga",
            "author": "Rudy Hansend",
            "source_name": "Gridoto.com"
        },
        {
            "title": "Takut Data Bocor, SpaceX Larang Pakai Zoom Kala Corona - CNN Indonesia",
            "publishedAt": "2020-04-02T05:18:28Z",
            "id": 142,
            "country": "id",
            "content": "Jakarta, CNN Indonesia -- Perusahaan manufaktur roket, SpaceX melarang penggunaan aplikasi konferensi video Zoom karena masalah privasi dan keamanan data dalam aplikasi.Pengumuman ini disampaikan perusahaan melalui memo perusahaan yang dikirimkan lewat email.… [+1612 chars]",
            "category": "business",
            "urlToImage": "https://awsimages.detik.net.id/visual/2018/02/07/7fabd35b-289f-497b-9c51-932286c9ac96_169.jpeg?w=650",
            "url": "https://www.cnnindonesia.com/teknologi/20200402114452-185-489510/takut-data-bocor-spacex-larang-pakai-zoom-kala-corona",
            "source_id": null,
            "description": "Larangan SpaceX pada aplikasi Zoom kala corona disebut karena perusahaan roket AS itu lagi mengembangkan teknologi penting bagi keamanan nasional.",
            "author": null,
            "source_name": "Cnnindonesia.com"
        }
    ]
    ```

* Error Response
    * Code : 400, If the news are updating.
    ```JSON
    {"message": "Please come back in 10 minutes. Updating the news."}
    ```

## Built With
- [Flask](https://flask.palletsprojects.com/en/1.1.x/): a micro web framework.
- [News-API](https://newsapi.org/): A JSON API for live news and blog articles.

