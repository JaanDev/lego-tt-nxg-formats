# RESH
Endianness: big  
Reverse engineered by [JaanDev](https://github.com/JaanDev)

## Main
* `HSER`: `4CC`. 4 character code
* `ver`: `u32`
* `unk`: `u32`
* `version`: `u32`
* `filesCount`: `u32`
* `treeCount`: `u32`
* `leafNames`: `STR32`
* `treeCount` times:
    * `childix`: `u16`
    * `sibix`: `u16`
    * `offset`: `u32`
    * `parentix`: `u16`
* `hasHashTable`: `u32`
* if `hasHashTable > 0`:
    * `filesCount` times:
        * `hash`: `u32`
    * `dup_cnt`: `u32`
    * `dup_table`: `STR32`
* `resources`: `RESOURCES`
* if `ver >= 2`:
    * `resourceType`: `u32`
* `accurevStream`: `STR16`
* `accurevTransaction`: `STR16`
* `producedByUserName`: `STR16`
* `projectName`: `STR16`
* `sourceFileName`: `STR16`

## RESOURCES
* `ROTV`: `4CC`
* `size`: `u32`
* `size` times:
    * `t`: `u32`. type?
    * `param`: `u32`
    * `hash`: `u32`
    * `unk`: `u32`
    * `checksum`: `u8[16]`