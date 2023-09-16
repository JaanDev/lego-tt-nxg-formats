# KRWL
Endianness: big  
Reverse engineered by [JaanDev](https://github.com/JaanDev)  
Krawly LODs  
This file may contain mistakes as i couldnt find such block

## Main
* `LWRK`: `4CC`
* `ver`: `u32`
* `ROTV`: `4CC` ; Maybe?
* `size`: `u32`
* `size` times:
    * `lodNum`: `u32`
    * `frames`:
        * `ROTV`: `4CC` ; Maybe?
        * `size`: `u32`
        * `size` times:
            * `frameNum`: `u32`
            * todo
            * if `ver >= 3`:
                * `unk`: `u32`
            * `poiMatrices`:
                * `ROTV`: `4CC` ; Maybe?
                * `size`: `u32`
                * `size` times:
                    * `data`: `64 bytes`
            * if `ver >= 2`:
                * `rootTrackMatrix`: `64 bytes`