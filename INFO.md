# INFO
Endianness: big  
Reverse engineered by [JaanDev](https://github.com/JaanDev)

## Main
* `ver`: `u32`
* `OFNI`: `str`. 4 character code
* `unk`: `u32`
* `author`: `STR32`
* `date`: `STR32`
* if `ver >= 0x3D`:
    * `hasSeparateTextureFiles`: `u8`