# BNDS
Endianness: big  
Reverse engineered by [JaanDev](https://github.com/JaanDev)

## Main
* `SNDB`: `str`. 4 character code
* `ver`: `u32`
* `numSpheres`: `u32`
* `numBounds`: `u32`
* `spheres`: `BOUNDS`
* `bounds`: `BOUNDS`


## BOUNDS
* `size`: `u32`
* `size` times:
    * `data`: `f32[4]`