# MESH
Endianness: big  
Reverse engineered by [JaanDev](https://github.com/JaanDev)  
this file is probably wrong

## Main
* `HSEM`: `str`. 4 character code
* `ver`: `u32`. It is assumed to be `>= 0x30`
* `ROTV`: `str`
* `len`: `u32`
* `len` times:
    * `vbs`: `VBS`
    * `fastBlendVBS`: `VBS`
    * `unk`:
        * `unk`: `u32`
        * `flags`: `u32`
        * `count`: `u32`
        * `size`: `u32`
        * `dataPtr`: `size * count bytes`
    * `ibOffset`: `u32`
    * `ibCount`: `u32`
    * `ibBase`: `u32`
    * `primType`: `u32`
    * `vbUsedCount`: `u32`
    * `vbInstBits`: `u32`
    * `skinMtxMap`:
        * `size`: `u32`
        * `data`: `u8[size]`
    * `unk`:
        * `unk`: `u32`
        * `id`: `u32`
        * help

## VBS
* `size`: `u32`
* `size` times:
    * `unk`: `u32`
    * `flags`: `u32`
    * `count`: `u32`
    * `nbAttribs`: `u32`
    * `nbAttribs` times:
        * `tempInt`: `u8`
        * `attribBits`: `u16`