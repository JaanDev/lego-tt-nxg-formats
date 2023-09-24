# DISP
Endianness: big  
Reverse engineered by [JaanDev](https://github.com/JaanDev)

## Main
* `DISP`: `4CC`
* `ver`: `u32` ; it is assumed to be 15
* `filePath`: `STR32`
* `items`:
    * `ROTV`: `4CC`
    * `size`: `u32`
    * `size` times:
        * `type`: `u8`
        * `id`: `u8`
        * `index`: `u32`
* `clipObjects`:
    * `ROTV`: `4CC`
    * `size`: `u32`
    * `size` times:
        * `unusedLightmapIndex`: `u16`
        * `mtlIndices`:
            * `size`: `u32`
            * `data`: `u32[size]`
        * `itemIndices`:
            * `size`: `u32`
            * `data`: `u32[size]`
* `numClipItems`:
    * `ROTV`: `4CC`
    * `size`: `u32`
    * `data`: `u16[size]`
* `mtlClip`:
    * `ROTV`: `4CC`
    * `size`: `u32`
    * `data`: `u32[size]`
* `clipRange`:
    * `ROTV`: `4CC`
    * `size`: `u32`
    * `data`: `f32[size]`
* `farclip`: `CLIP`
* `PS3Farclip`: `CLIP`
* `specials`:
    * `ROTV`: `4CC`
    * `size`: `u32`
    * `size` times:
        * `nameIdx`: `u32`
        * `mtx`: `64 bytes`
        * `drawMtx`: `64 bytes`
        * `min`: `16 bytes`
        * `max`: `16 bytes`
        * `sphere`: `16 bytes`
        * `clipObjectIdx`: `u32`
        * `flags`: `u32`
        * `clipRange`: `CLIP`
        * `instanceIdx`: `u32`
        * `animIdx`: `u32`
        * `windSpeed`: `u16`
        * `windScale`: `u16`
* `specialGroupNodes`:
    * `ROTV`: `4CC`
    * `size`: `u32`
    * `size` times:
        * `specialIndexes`:
            * `size`: `u32`
            * `data`: `u16[size]`
* `sceneSpecials`: `u8`
* `numInstances`: `u32`
* `specialFlags`:
    * `ROTV`: `4CC`
    * `size`: `u32`
    * `data`: `u8[size]`
* `visibilityFlags`:
    * `ROTV`: `4CC`
    * `size`: `u32`
    * `data`: `size bytes`
* `instFadeBounds`:
    * `ROTV`: `4CC`
    * `size`: `u32`
    * `size` times:
        * `4` times:
            * `fadeDistance`: `f32`
            * `fadeAlpha`: `f32`
        * `fadeFromPivot`: `u8`
* `visualImportance`:
    * `ROTV`: `4CC`
    * `size`: `u32`
    * `data`: `size bytes`
* `animMtls`:
    * `ROTV`: `4CC`
    * `size`: `u32`
    * `data`: `u32[size]`
* `matrixItems`:
    * `size`: `u32`
    * `size` times:
        * `mtx`: `f32[12]`
* `faceOnItems`:
    * `ROTV`: `4CC`
    * `size`: `u32`
    * `size` times:
        * `isFixedUp`: `u32`
        * `type`: `u32`
        * `instances`:
            * `size`: `u32`
            * `size` times:
                * `loc`: `VEC3F`
                * `width`: `f32`
                * `height`: `f32`
                * `colour`: `u32`

## CLIP
* `size`: `u32`
* `data`: `f32[size]`