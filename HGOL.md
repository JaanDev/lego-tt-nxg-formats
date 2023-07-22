# HGOL
Endianness: big
Reverse engineered by [JaanDev](https://github.com/JaanDev)
this is probably wrong

## Main
* `LOGH`: `str`. 4 character code. Flipped because of endianness
* `ver`: `u32`
* `joints`: `JOINTS`
* `T`: `T`
* `INV_WT`: `T`
* `jointIxs`: `IXS`
* `pointsOfInterest`: `POI`

## JOINTS
* `size`: `u32`
* `size` times:
    * `unk`: `u32`
    * `orient`: `f32[16]`
    * `locatorOffset`: `f32[3]`
    * `parentIdx`: `u8`
    * `flags`: `u8`

## T
* `size`: `u32`
* `size` times:
    * `unk`: `f32[16]`

## IXS
* `size`: `u32`
* `unk`: `u8[size]`

## POI
* `unk`: `u32`
* `offset`: `f32[16]`
* `parentJointIdx`: `u8`
* `size`: `u32`
* 