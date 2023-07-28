# MESH
Endianness: big  
Reverse engineered by [JaanDev](https://github.com/JaanDev)  
Credits to the original author of [this](https://github.com/JamesFrancoe/TTGames-Extraction-Tools)

## Main
* `HSEM`: `4CC`
* `ver`: `u32`. It is assumed to be `>= 0x30`
* `ROTV`: `4CC`
* `len`: `u32`
* `len` times:
    * `vbs`: `VBS`
    * `fastBlendVBS`: `VBS`
    * `unk`: `UNK`
    * `ibOffset`: `u32`
    * `ibCount`: `u32`
    * `ibBase`: `u32`
    * `primType`: `u16`
    * `vbUsedCount`: `u32`
    * `vbInstBits`: `u32`
    * `skinMtxMap`:
        * `size`: `u32`
        * `data`: `u8[size]`
    * `unk`:
        * `unk`: `u32`
        * if `unk > 0`:
            * idk
    * `editorData.optFlags`: `u32`
    * `editorData.centreExtents[0]`: `16 bytes`
    * `editorData.centreExtents[1]`: `16 bytes`
    * `densityDiscDiameter`: `f32`
    * `depthBits`: `u32`
    * `unk`: `VERTEX_SOMETHING`
    * `byteOffset`: `u32`
    * `depthVbUsedCount`: `u32`
    * `unk`: `UNK`
    * `depthIbBase`: `u32`
    * `depthIbOffset`: `u32`
    * `depthIbBase`: `u32`

## VBS
* `size`: `u32`
* `size` times:
    * `data`: `VERTEX_SOMETHING`
    * `byteOffset`: `u32`

## UNK
* `unk`: `u32`. Maybe size? But this is not used anyway
* `flags`: `u32`
* `count`: `u32`
* `size`: `u32`
* `data`: `size * count bytes`

## VERTEX_SOMETHING
* `unk`: `u32`
* `flags`: `u32`
* `count`: `u32`
* `attribs`: `ATTRIBS`
* Now the size in bytes of each vertex entry is calculated based on the `valVarType`s. The vertex size is equal to `sum([(4 * (type == 6) + 4) if (type > 4) else (4 * type) for type in valVarTypes])`
* `count` times:
    * for `val` in `attribs.valVarTypes`:
        * `entry`: `(4 * (val == 6) + 4) if (val > 4) else (4 * val) bytes`