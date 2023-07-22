# VFXL
Endianness: big
Reverse engineered by [JaanDev](https://github.com/JaanDev)

## Main
* `LXFV`: `str`. 4 char code
* `ver`: `u32`
* `vfxName`: `STR16`
* `ledFileName`: `STR16`
* `mtx`: `f32[16]`
* if `ver >= 2`:
    * `radius`: `f32`
    * `fuzzySearch`: `u8`
    * `nxgOnly`: `u8`