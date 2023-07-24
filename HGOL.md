# HGOL
Endianness: big  
Reverse engineered by [JaanDev](https://github.com/JaanDev)

## Main
* `LOGH`: `str`. 4 character code. Flipped because of endianness
* `ver`: `u32`
* `joints`: `JOINTS`
* `T`: `T`
* `INV_WT`: `T`
* `jointIxs`: `IXS`
* `pointsOfInterest`: `POI`
* `poiIxs`: `IXS`
* if `ver >= 0xA`:
    * `unk`: `STR32`
* if `ver >= 6`:
    * `layerMetaData`: 
        * `size`: `u32`
        * `size` times:
            * `type`: `u8`
            * `jointIndex`: `u8`
            * `specialIndex`: `u16`
            * if `ver >= 8`:
                * `layer`: `u8`
* `layers`: `LAYERS`
* if `ver >= 3`:
    * `shadowData`: `SHADOW_DATA`
* `sphereRadius`: `f32`
* `sphereYoff`: `f32`
* `min`: `f32[3]`
* `max`: `f32[3]`
* `cylinderYoff`: `f32`
* `cylinderHeight`: `f32`
* `cylinderRadius`: `f32`
* `lodBoundary`: `f32`
* if `ver >= 4`:
    * `topLodRemapTable`: `IXS`
    * `lodRemapTable`: `IXS`
* if `ver >= 5`:
    * `modelRenderScale`: `f32`
* if `ver >= 6`:
    * `lodSpecialRemapTable`:
        * `size`: `u32`
        * `val`: `i16[size]`
* if `ver >= 9`:
    * `krawlyLod`: `u8`

## JOINTS
* `size`: `u32`
* `size` times:
    * `u`: `u32`
    * `orient`: `f32[16]`
    * `locatorOffset`: `f32[3]`
    * `parentIdx`: `u8`
    * `flags`: `u8`

## T
* `size`: `u32`
* `size` times:
    * `val`: `f32[16]`

## IXS
* `size`: `u32`
* `val`: `u8[size]`

## POI
* `size`: `u32`
* `size` times:
    * `u`: `u32`
    * `offset`: `f32[16]`
    * `parentJointIdx`: `u8`

## LAYERS
* `size`: `u32`
* `size` times:
    * if `ver < 6`:
        * if `ver >= 2`:
            * `u`: `u32`
        * `GobjSpecialIndices`: `SPECIAL_INDICES`
        * `skinGobjSpecialIdx`: `u32`
        * `blendGobjSpecialIndices`: `SPECIAL_INDICES`
        * `blendSkinGobjSpecialIdx`: `u32`
    * else
        * `u`: `u32`
        * `metaDataIndex`: `u16`
        * `numRigids`: `u16`
        * `numSkins`: `u16`

## SPECIAL_INDICES
* `size`: `u32`
* `val`: `u32[size]`

## SHADOW_DATA
* `size`: `u32`
* `size` times:
    * `ellipsoids`:
        * `size`: `u32`
        * `size` times:
            * `centre`: `f32[3]`
            * `x_axis`: `f32[3]`
            * `y_axis`: `f32[3]`
            * `z_axis`: `f32[3]`
    * `cylinders`:
        * `size`: `u32`
        * `size` times:
            * `centre`: `f32[3]`
            * `x_axis`: `u32[4]`. Not sure about these but im unable to check. It may be `f32`
            * `y_axis`: `f32[3]`
            * `z_axis`: `u32[4]`
    * `shadowMeshes`:
        * `size`: `u32`
        * `size` times:
            * `normals`:
                * `size`: `u32`
                * `size` times:
                    * `val`: `u32[4]`. May be `f32`
            * `verts`:
                * `size`: `u32`
                * `size` times:
                    * `val`: `u32[4]`. May be `f32`
    * `joint`: `u8`