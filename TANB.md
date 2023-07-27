# TANB
Endianness: big  
Reverse engineered by [JaanDev](https://github.com/JaanDev)  
this file may be wrong as i was not able to compare it with the decomp. could not find any such block

## Main
* `BNAT`: `4CC`
* `ver`: `u32`
* `animBlocks`:
    * `size`: `u32`
    * `size` times:
        * `mtlNameHash`: `u32`
        * `animID`: `u16`
        * if `ver == 3`:
            * `mtlInxTemp[0]`: `u16`
            * `mtlInxTemp[1]`: `u16`
            * `mtlInxTemp[2]`: `u16`
            * `mtlInxTemp[3]`: `u16`
        * else
            * `val`: `u16[8]`
            * `val`: `u8[8]`
            * `val`: `u8[8]`
        * `tids`:
            * `size`: `u32`
            * `val`: `i16[size]`
        * `numTidsArray`:
            * `size`: `u32`
            * `val`: `u16[size]`
        * `curveList`:
            * `size`: `u32`
            * `size` times:
                * `result`: `u32`
                * `firstFrame`: `u16`
                * `numFrames`: `u16`
                * `animActive`: `u8`
                * `postAnimCycling`: `u8`
                * `preAnimCycling`: `u8`
                * `updateFlag`: `u8`
                * `attributeID`: `u8`
        * `unk`: `u32`
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
        * if `endFrames < 0`:
            * `compressionRatio`: `f32`
            * `firstFrame`: `f32`
        * if `animHeaderVersion >= 0x414E4941`:
            * `keysNeeded`: `u32`
        * else:
            * `keyItems`:
                * `size`: `u32`
                * `val`: `i16[size]`
        * if `animHeaderVersion >= 0x414E4944`
            * `fConstants`:
                * `size`: `u32`
                * `val`: `f32[size]`
            * `unk`: `STR32`
        * `constants`:
            * `size`: `u32`
            * `val`: `u16[size]`
        * `keyTypes`:
            * `size`: `u32`
            * `val`: `u16[size]`
        * `curveScalesMins`:
            * `size`: `u32`
            * `size` times:
                * `scale`: `f32`
                * `min`: `f32`
        * `tangentKeys`:
            * `size`: `u32`
            * `val`: `u8[size]`
        * `curvesetFlags`:
            * `size`: `u32`
            * `val`: `u8[size]`
        * some weird stuff going here
        * idk im too lazy to decomp it
        * without even knowing if the above is correct or not
        * its on 0x196F70 without base in lego lotr binary in case someone wants to RE