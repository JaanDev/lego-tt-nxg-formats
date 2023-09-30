# MESH
Endianness: big  
Reverse engineered by [JaanDev](https://github.com/JaanDev)  
Credits to the original author of [this](https://github.com/JamesFrancoe/TTGames-Extraction-Tools)  
With help from [Alub](https://github.com/AlubJ)

## Main
* `HSEM`: `4CC`
* `ver`: `u32` ; It is assumed to be `>= 0x30`
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
    * `dynamicBufferCheck`:
        * `dynamicBufferCheck`: `u32`
        * if `dynamicBufferCheck > 0`:
            * `unk`: `u32`
            * `poseCount` = `0`
            * `test`: `u32`
            * while `test != 0`:
               * `poseCount` = `poseCount + 1`
               * `unk`: `u32`
               * `test`: `u32`
            * `len` poseCount:
               * `poseVertexCount`: `u32`
               * `data`: `poseVertexCount * 12 bytes`
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
* `unk`: `u32` ; Maybe size? But this is not used anyway
* `flags`: `u32`
* `count`: `u32`
* `size`: `u32`
* `data`: `size * count bytes`

## VERTEX_SOMETHING
* `unk`: `u32`
* if `unk != 0`:
    * `flags`: `u32`
    * `count`: `u32`
    * `attribs`: `ATTRIBS`
    * Now the size in bytes of each vertex entry is calculated based on the `valVarType`s. The vertex size is equal to `sum([(4 * (type == 6) + 4) if (type > 4) else (4 * type) for type in valVarTypes])`
    * `count` times:
        * for `val` in `attribs.valVarTypes`:
            * `entry`: `(4 * (val == 6) + 4) if (val > 4) else (4 * val) bytes`

## VERTEX ATTRIBUTES
|Position|Attribute|
|---|---|
|`0`|`Position`|
|`1`|`Normal`|
|`2`|`ColourSet0`|
|`3`|`Tangent`|
|`4`|`ColourSet1`|
|`5`|`UVSet1`|
|`6`|`Unknown`|
|`7`|`UVSet2`|
|`8`|`Unknown`|
|`9`|`BlendInd`|
|`10`|`BlendWeight`|
|`11`|`Unknown`|
|`12`|`LightDirSet`|
|`13`|`LightColSet`|

## VERTEX TYPES
|ID|Type|Size|
|---|---|---|
|`0`|`nothing`|`0`|
|`2`|`vec2Float`|`8`|
|`3`|`vec3Float`|`12`|
|`4`|`vec4Float`|`16`|
|`5`|`vec2Half`|`4`|
|`6`|`vec4Half`|`8`|
|`7`|`vec4Char`|`4`|
|`8`|`vec4Mini`|`4`|
|`9`|`colour4Char`|`4`|
