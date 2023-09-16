# IVL4
Endianness: big  
Reverse engineered by [JaanDev](https://github.com/JaanDev)

## Main
* `4LVI`: `4CC`
* `ver`: `u32`
* `bounds[0]`: `12 bytes`
* `bounds[1]`: `12 bytes`
* `maxDepth`: `u8`
* `sampleArray`:
    * `size`: `u32`
    * `size` times:
        * `directLights`: `DIRECT_LIGHTS[2]`
        * `NuSHQuad3`:
            * `v`: `12 bytes[9]`
* `treeNodes`:
    * `size`: `u32`
    * `size` times:
        * `sampleIndex`: `u16[8]`. (`NuLSVNode`)
* `lights`: `DLGT` ; (if `ver == 2`, there is no `DLGT` version or 4 char code)
* if `ver >= 4`:
    * `nextGen`: `u8`. (`bool`)
* if `ver >= 5`:
    * `compactSampleArray`:
        * `size`: `u32`
        * `size` times:
            * `directLights`: `DIRECT_LIGHTS[2]`
            * `UInt`: `u32` ; (yes its literally called like that in the game)

## DIRECT_LIGHTS
* `lightID`: `u32`
* `shadowFactor`: `f32`