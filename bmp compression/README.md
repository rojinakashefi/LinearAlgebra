# BMP compression

We tried to compress bmp images using SVD formula:

![](https://github.com/rojinakashefi/LinearAlgebra/blob/main/bmp%20compression/svd.png)

Since sigma matrix is decreasing so when we get downer their values get near to zero and we can not condiser them in our calculation:


![](https://github.com/rojinakashefi/LinearAlgebra/blob/main/bmp%20compression/svd-k.png)

For example if our Input image is : 

<img src="https://github.com/rojinakashefi/LinearAlgebra/blob/main/bmp%20compression/images/2.bmp" title="" alt="" width="266">

with k = 10 :

<img src="https://github.com/rojinakashefi/LinearAlgebra/blob/main/bmp%20compression/new_images/k%3D10-2.jpg" title="" alt="" width="266">

with k = 50 :

<img src="https://github.com/rojinakashefi/LinearAlgebra/blob/main/bmp%20compression/new_images/k%3D50-2.jpg" title="" alt="" width="272">

with k = 150 :

<img src="https://github.com/rojinakashefi/LinearAlgebra/blob/main/bmp%20compression/new_images/k%3D150-2.jpg" title="" alt="" width="274">

with k = 250 :

<img src="https://github.com/rojinakashefi/LinearAlgebra/blob/main/bmp%20compression/new_images/k%3D250-2.jpg" title="" alt="" width="280">

----

you can check my notes for svd in [here](https://github.com/rojinakashefi/LinearAlgebra/blob/main/bmp%20compression/SVD.pdf).
