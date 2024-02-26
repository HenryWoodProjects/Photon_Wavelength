This is a bit of code I wrote to calculate the wavelength of a photon emitted from a hydrogen atom when the single electron transitions from a quantum state of higher energy to a quantum state of lower energy.

The code itself is relatively basic but I am uploading it to GitHub as I defined a function that rounds numbers correctly which I'm quite proud of.

As you may know, Python has the Round() function but it does not work properly. When python rounds a number exactly half way between two integers (for example 2.5), it rounds to the nearest even number so if you were to type...


a = round(2.5)
print(a)


...it would print "2" when you should get "3". I was also unable to get the function to work on numbers written in standard form (a x10^n) so I created a function that would work.
