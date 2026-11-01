# MESH
Endianness: big  
Reverse engineered by [JaanDev](https://github.com/JaanDev)  
Credits to the original author of [this](https://github.com/JamesFrancoe/TTGames-Extraction-Tools)  
With help from [Alub](https://github.com/AlubJ)

## Main
* `HSEM`: `4CC`
* `ver`: `u32` ; `0x30` in LEGO LOTR (PC). A few leftover test files (`old_super_minifig`, `phantom_minifig`, `super_test`, `ufo`, some cutscene props) are `0x2F`
* if `ver >= 0x30`:
    * `ROTV`: `4CC` ; not present in `0x2F` files
* `len`: `u32`
* `len` times:
    * `vbs`: `VERTICES`
    * `fastBlendVBS`: `VERTICES`
    * `indexList`: `INDICES`
    * `ibOffset`: `u32` ; first index of this draw in the shared index buffer (see NOTES)
    * `ibCount`: `u32` ; number of indices of this draw
    * `ibBase`: `u32` ; first vertex of this draw in its vertex buffer; indices are relative to it
    * `primType`: `u16` ; `0` = triangle list (the only value in LOTR)
    * `vbUsedCount`: `u32` ; number of vertices this draw uses (all its indices are `< vbUsedCount`)
    * `vbInstBits`: `u32`
    * `skinMtxMap`:
        * `size`: `u32`
        * `data`: `u8[size]`
    * `dynamicBufferCheck`: ; UNVERIFIED: this layout does not match LOTR files that use it (see NOTES)
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
    * `unk`: `INDICES`
    * `depthIbBase`: `u32`
    * `depthIbOffset`: `u32`
    * `depthIbBase`: `u32`

## VERTICES
* `size`: `u32`
* `size` times:
    * `data`: `VERTEX_SOMETHING`
    * `byteOffset`: `u32`

## INDICES
* `tag`: `u32` ; object tag, see OBJECT TAG
* if `tag == 1`:
    * `flags`: `u32`
    * `count`: `u32`
    * `size`: `u32` ; size in bytes of one index: `2` in all LOTR files (`u16`, big endian)
    * `data`: `size * count bytes`
* if `tag & 0xC0000000 == 0xC0000000`:
    * `unk`: `u32` ; always `1` in LOTR

## VERTEX_SOMETHING
* `tag`: `u32` ; object tag, see OBJECT TAG
* if `tag & 0xC0000000 == 0xC0000000`:
    * `unk`: `u32` ; always `1` in LOTR
* if `tag == 1`:
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

## OBJECT TAG
`INDICES` and `VERTEX_SOMETHING` start with a `u32` tag instead of a size:
* `0`: no object, nothing follows
* `1`: a new object follows inline
* `0xC0000000 | id`: a reference to an object read earlier in the file, followed by one `u32` (always `1` in LOTR) and no data.
  Most entries after the first refer back to the first index buffer this way: all draws of a MESH share one index buffer.

Reading the reference as "non-zero, so data follows" (the previous description) misaligns the rest of the block, which is
why most files could not be read past the first entry.

## NOTES
Checked against all 762 `.ghg` / `.gsc` files of LEGO The Lord of the Rings (PC) with a strict reader that
follows this file and stops on the first mismatch: 663 files read to the end of the MESH block (653 `0x30`, 10 `0x2F`).
* Draws chain through the shared index buffer: each entry's `ibOffset` = previous `ibOffset + ibCount` (6234 of 6234 draws).
* Indices are relative to `ibBase`: every draw's smallest index is `0` and all are `< vbUsedCount`.
* Triangles are counter-clockwise: the face normal `(p1 - p0) x (p2 - p0)` agrees with the stored vertex normals.
* Attribute value encodings, checked against the geometry:
    * `Position`: `vec4Half` with `w = 1.0`, or `vec3Float` (big endian)
    * `Normal`, `Tangent`: `vec4Mini` = unsigned bytes, `x = b / 127.5 - 1` (normals agree with the faces, the signed
      reading does not; tangents decoded this way are perpendicular to the normals)
    * `ColourSet0`: `colour4Char` = R, G, B, A bytes
    * `UVSet1`: `vec2Half`
    * `BlendInd`: `vec4Char` = 4 bone numbers, indices into the draw's `skinMtxMap` (every index with a non-zero
      weight is `< skinMtxMap.size`)
    * `BlendWeight`: `vec4Mini` = 4 unsigned bytes that sum to 255
* 98 of the 99 files that still fail reach an entry with `dynamicBufferCheck > 0` first: every minifig face (expressions)
  and several creatures (bear, cave troll, Gollum, oliphant, wolf, warg, eagle, ...). The pose loop described above does
  not match their data, so that section is still unknown. The other failure is `levels/builder/builderdefault_nxg.gsc`.
