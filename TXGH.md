# TXGH
Endianness: big  
Reverse engineered by [JaanDev](https://github.com/JaanDev)

maybe not done?

## Main
* `unknown`: `u32`. It was 1 in all files i've checked
* `HGXT`: `str`. 4 character code. Flipped because of endianness
* `version`: `u32`. It is assumed to be `0xA`
* `tids` (texture ids?): `TIDS`
* `textures`: `TEXTURES`

## TIDS
* `ROTV`: `str`. Block indicator
* `size`: `u32`
* `size` times:
    * `data`: `u32`. Unknown as all of them were 0 in all files i've checked

## TEXTURES
* `ROTV`: `str`. Block indicator
* `size`: `u32`
* `size` times:
    * `unknown`: `u8[16]`
    * `name`: `STR32`
    * `index`: `u16`
    * `type`: `u8`
    * `flags`: `u8`