# PINS
Endianness: big  
Reverse engineered by [JaanDev](https://github.com/JaanDev)  
This block hasnt been checked and may contain mistakes

## Main
* `SNIP`: `4CC`
* `ver`: `u32`
* `roomInstances`:
    * `len`: `u32`
    * `len` times:
        * `instances`:
            * `len`: `u32`
            * `val`: `u16[len]`