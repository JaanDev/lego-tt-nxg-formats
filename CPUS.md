# CPUS
Endianness: big  
Reverse engineered by [JaanDev](https://github.com/JaanDev)  
This file may have mistakes (but most likely doesnt) as i was not able to find a file that contains all that info

## Main
* `SUPC`: `str`. 4 char code
* `ver`: `u32`
* if `ver of prev block < 60`:
    * `lodsVersion`: `u32`
* else:
    * `lodsVersion` = `1u32`
* `lods`:
    * `size`: `u32`
    * `size` times:
        * `layers`:
            * `size`: `u32`
            * `size` times:
                * `verts`:
                    * `size`: `u32`
                    * `data`: `f32[3 * size]`
                * `bones`:
                    * `size`: `u32`
                    * `vertIndexes`:
                        * `size`: `u32`
                        * `data`: `u16[size]`
                    * `vertWeights`:
                        * `size`: `u32`
                        * `data`: `u8[size]`
                * `tris`:
                    * `size`: `u32`
                    * `size` times:
                        * `x`: `u16`
                        * `y`: `u16`
                        * `z`: `u16`
                * if `lodsVersion >= 2`:
                    * `colours`:
                        * `size`: `u32`
                        * `val`: `u32[size]`