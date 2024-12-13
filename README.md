<h1 align="center">PYTHON MODEL PROCESSING (SIMPLE API)</h1>

## Deskripsi
Merupakan bagian proyek dari Machine Learning DIY yang terkhusus pada proses deployment menggunakan `Framework Flask, Postman, dan Docker`.

## Instalasi
Ensure you have docker dekstop installed
- Clone repository ini
  ```shell
  git clone https://github.com/Capstone-DIY/Machine-Learning.git
  ```
- Masuk ke direktori
  ```shell
  cd Machine-Learning
  code .
  ```
- Pindah branch
  ```shell
  git checkout deployment
  ```
- Buat docker images
  ```shell
  docker build -t ml-diy .
  ```
- Jalankan container
  ```shell
  docker container run -d -p 8080:8080 ml-diy 
  ```

## Menjalankan aplikasi
  Try to run this path in postman and give the form data "text"
  http://127.0.0.1:8080/predict  

<h3 align="center">Thank U for Coming Here!😊</h3>