# BCSH
Endianness: big  
Reverse engineered by [JaanDev](https://github.com/JaanDev)

## Main
* `HSCB`: `4CC`
* `ver`: `u32`
* `entryCount`: `u32`
* `entryCount` times:
    * `platform`: `u32`
    * `configHash`: `u32`
    * if `ver < 8`:
        * `vertexProgramSize`: `u32`
        * `pixelProgramSize`: `u32`
        * `vertexProgramData`: `vertexProgramSize bytes`
        * `pixelProgramData`: `pixelProgramSize bytes`
    * else
        * `vertexProgramHash`: `u32`
        * `pixelProgramHash`: `u32`
        * `vertexProgram`: `PROGRAM_DATA`
        * `pixelProgram`: `PROGRAM_DATA`
* if `ver >= 9`:
    * `dummyInt`: `u32`

## PROGRAM_DATA
* `platform`: `u32`
* `bytecodeHash`: `u32`
* `programSize`: `u32`
* `data`: `programSize bytes`