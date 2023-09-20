# PORT
Endianness: big  
Reverse engineered by [JaanDev](https://github.com/JaanDev)  
This block hasnt been checked and may contain mistakes

## Main
* `TROP`: `4CC`
* `ver`: `u32`
* `portals`:
    * `len`: `u32`
    * `len` times:
        * `pointsIdx`: `u32`
        * `numPoints`: `u16`
        * `planeEqn`: `u32[4]`
        * `leftRoom`: `u16`
        * `rightRoom`: `u16`
        * `id`: `u8`
        * `flags`: `u32`
* `rooms`:
    * `len`: `u32`
    * `len` times:
        * `instancesIdx`: `u32`
        * `planesIdx`: `u32`
        * `portalsIdx`: `u32`
        * `numInstances`: `u16`
        * `numPlanes`: `u8`
        * `numPortals`: `u8`
        * `containsRoom`: `u8`
        * `isNested`: `u8`
        * `isVisible`: `u8`
        * `depth`: `u8`
* `instances`:
    * `len`: `u32`
    * `vals`: `u16[len]`
* `planes`:
    * `len`: `u32`
    * `vals`: `16 bytes[len]`
* `points`:
    * `len`: `u32`
    * `vals`: `VEC3F[len]`
* `portalIndex`:
    * `len`: `u32`
    * `vals`: `u16[len]`