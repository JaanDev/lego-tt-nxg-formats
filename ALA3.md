# ALA3
Endianness: big  
Reverse engineered by [JaanDev](https://github.com/JaanDev)

## Main
* `3ALA`: `4CC`
* `ver`: `u32`
* `instAnimBlocks`:
    * `len`: `u32`
    * `len` times:
        * `mtx`: `f32[16]`
        * `Tfactor`: `f32`
        * `Tfirst`: `f32`
        * `Tinterval`: `f32`
        * `localTime`: `f32`
        * `playing`: `u8`
        * `backwards`: `u8`
        * `waiting`: `u8`
        * `repeating`: `u8`
        * `oscillate`: `u8`
        * if `ver >= 3`:
            * `textAnimLock`: `u8`
        * `Fparam1`: `f32`
        * `prevEvalTime`: `f32`
        * `animIdx`: `u16`
        * `stateanimIdx`: `u32`
        * `instanceIdx`: `u16`
        * if `ver >= 2`:
            * `bsobj_ix`: `u16`
* `stateAnims`:
    * `len`: `u32`
    * `len` times:
        * `endFrame`: `u16`
        * `frames`:
            * `len`: `u32`
            * `vals`: `f32[len]`
        * `states`:
            * `len`: `u32`
            * `vals`: `u8[len]`
* `instAnimData`:
    * `len`: `u32`
    * `len` times:
        * `animHeaderVersion`: `u32`
        * `numNodes`: `u16`
        * `numFrames`: `u16`
        * `curveGroupSize`: `u16`
        * `originalNumFramesOLD`: `u16`
        * `numCurves`: `u16`
        * `firstFrameOLD`: `u16`
        * `endFrames`: `u8`
        * `numShortIntegers`: `u8`
        * `fixedUp`: `u8`
        * `miscFlags`: `u8`
        * `totalNumFrames`: `u16`
        * `constantBase`: `f32`
        * `constantScale`: `f32`
        * if `miscFlags & 0x80`: ; uhh ig?
            * `compressionRatio`: `f32`
            * `firstFrame`: `f32`
        * if `animHeaderVersion >= 0x414E4941`:
            * `keysNeeded`: `u32`
        * else
            * `keyItems`:
                * `len`: `u32`
                * `val`: `u16[len]`
        * ; 0x003A4C9A hobbiton
        * if `animHeaderVersion >= 0x414E4944`:
            * `fConstants`:
                * `size`: `u32`
                * `data`: `f32[size]`
            * `unk`: `STR32`
        * `constants`:
            * `size`: `u32`
            * `data`: `u16[size]`
        * `keyTypes`:
            * `size`: `u32`
            * `data`: `u16[size]`
        * `curveScalesMins`:
            * `size`: `u32`
            * `size` times:
                * `scale`: `f32`
                * `min`: `f32`
        * `tangentKeys`:
            * `size`: `u32`
            * `data`: `u8[size]`
        * `curvesetFlags`:
            * `size`: `u32`
            * `data`: `u8[size]`
        * if `animHeaderVersion < 0x414E4941`:
            * ; idk
        * else
            * if `keysNeeded > 0`:
                * ; 0x003A4CD3 hobbiton
                * ; scary stuff going here that i will not be able to implement using this script unfortunately :(