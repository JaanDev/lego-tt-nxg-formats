# EdStream
Endianness: little

## Main
* `StreamInfo`: `BLOCKINFO`
* `ver`: `u32`. probably version but im not sure as there are no names for this format. it is assumed to be > 22
* `TypeList`: `BLOCKINFO`
* `len`: `u32`
* `len` times:
    * `Type`: `BLOCKINFO`
    * `name`: `STR32`
    * `size`: `u32`. Size of the type in bytes. (or `i32`?)
* `ClassList`: `BLOCKINFO`
* `len`: `u32`
* `len` times:
    * `Class`: `BLOCKINFO`
    * `className`: `STR32`
    * `while any property left`:
        * `blockSize`: `u32`
        * `propertyName`: `STR32`
        * if `propertyName == "Version"`:
            * `version`: `u32`
        * elif `propertyName == "Types"`:
            * `size`: `u32`
            * `size` times:
                * `index`: `u32`. index of the type from TypeList
                * `typeName`: `STR32`
                * `unk1`: `u32`
                * `unk2`: `u32`
                * `unk3`: `u32`
                * `unk4`: `i32`
        * elif `propertyName == "Params"`:
            * `count`: `u32`
        * elif `propertyName == "Components"`:
            * `len`: `u32`
            * `len` times:
                * `Component`: `BLOCKINFO`
                * `name`: `STR32`. Of max len 128
                * `unk`: `u32`
* `count`: `u32`
* `count` times:
    * `OLST`: `BLOCKINFO`
    * `unk`: `u16`
    * if `ver > 23`:
        * `len`: `u32`
    * else
        * `len`: `u16`
    * `len` times:
        * `MOBJ`: `BLOCKINFO`
        * if `ver < 25`:
            * `unk`: `u32`
        * else
            * `unk`: `u16`
        * `unk`: `u8`. skip 1 byte for some reason
        * todo

## BLOCKINFO
* `size`: `u32`. Size of the block (including this value)
* `name`: `STR32`