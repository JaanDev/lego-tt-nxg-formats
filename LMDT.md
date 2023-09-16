# LMDT
Endianness: big  
Reverse engineered by [JaanDev](https://github.com/JaanDev)  
Lightmap data

## Main
* `TDML`: `4CC`
* `ver`: `u32`
* `size`: `u32`
* `size` times:
    * `type`: `u32`
    * `meshInstanceID`: `u32`
    * `localTID`: `u32[4]`
    * if `ver >= 2`:
        * `localTID`: `u32`
    * `UVOffsets`: `f32[2]`
    * `UVScales`: `f32[2]`