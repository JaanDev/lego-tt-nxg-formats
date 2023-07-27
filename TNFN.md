# TNFN
Endianness: big  
Reverse engineered by [JaanDev](https://github.com/JaanDev)

## Main
* `size`: `u32`. Size of the block
* `unk`: `u32`. It's always (?) 1
* `TNFN`: `4CC`
* `type`: `u32`. 2 for buttons, 3 for fonts
* `version`: `u32`
* `flags`: `u16`
* `size`: `u32`. Idk what it means, but the game seems to ignore this value anyway
* `numChars`: `u32`. Amount of chars in the file
* `unicodeTableSize`: `u32`. Size of the character table
* `height`: `f32`. Height of every char texture (they all have the same height)
* `baseline`: `f32`
* `spaceWidth`: `f32`
* `sendid`: `u32`. Unknown
* `icgap`: `f32`. Unknown
* `posTable`: `POSTABLE`
* `charsTable`: `CHARTABLE`
* `kerning`: `KERNTABLE`
* `texture`: `DDS texture file`

## POSTABLE
* if `type > 2`:
    * `ROTV`: `4CC`
* `size`: `u32`
* `size` times:
    * `x`: `f32`. X coordinate of the texture rect
    * `y`: `f32`. Y coordinate of the texture rect
    * `w`: `f32`. Width of the texture rect

## CHARTABLE
* if `type > 2`:
    * `ROTV`: `4CC`
* `size`: `u32`
* `size` times:
    * `unicodeCodepoint`: `u16`
    * `index`: `u16`. Index of the character (from the posTable)

## KERNTABLE
* if `type > 1`:
    * if `type > 2`:
        * `ROTV`: `4CC`
    * `size`: `u32`
    * `size` times:
        * `charA`: `u16`. Character A
        * `charB`: `u16`. Character B
        * `gap`: `f32`