# TXGH
Endianness: big  
Reverse engineered by [JaanDev](https://github.com/JaanDev)

## Main
* `HGXT`: `4CC`
* `version`: `u32` ; It is assumed to be `0xA`
* `tids`: `TIDS` ; texture ids?
* `textures`: `TEXTURES`

## TIDS
* `ROTV`: `4CC`
* `size`: `u32`
* `size` times:
    * `data`: `u32` ; Unknown as all of them were 0 in all files i've checked

## TEXTURES
* `ROTV`: `4CC`
* `size`: `u32`
* `size` times:
    * `unknown`: `u8[16]`
    * `name`: `STR32`
    * `index`: `u16`
    * `type`: `u8`
    * `flags`: `u8`