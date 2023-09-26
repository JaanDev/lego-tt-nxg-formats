# GHG and GSC
This is the file structure for .gsc and .ghg files  
Reverse engineered by [JaanDev](https://github.com/JaanDev)

## Main
* `RESH_size`: `u32` ; size of the RESH block
* `idk`: `8 bytes` ; some 4CC codes
* `header`: `RESH`
* `unk`: `4 bytes` ; idk why but it has those 4 bytes after the RESH, i am pretty sure those are just filler
* `unk`: `u32`
* `02UN`: `4CC`
* `fileVer`: `u32` ; the version of the file
* `info`: `INFO` ; INFO block (see [INFO.md](INFO.md))
* if `fileVer >= 0x3D`:
    * `hasSeparateTextureFiles`: `u8`
* `ntbl`: `NTBL` ; NTBL block (see [NTBL.md](NTBL.md))
* `unk`: `u32`
* `txgh`: `TXGH` ; TXGH block (see [TXGH.md](TXGH.md))
* if `fileVer >= 0x14`:
    * `splines`:
        * `ROTV`: `4CC`
        * `size`: `u32`
        * `size` times:
            * if `fileVer >= 0xC`:
                * `u`: `u32`
            * else
                * `nameIdx`: `u16`
            * `points`:
                * `size`: `u32`
                * `data`: `VEC3F[size]`
* else
    * ; idk
* if `fileVer >= 0x36`:
    * `vfxLocatorSet`:
        * `ROTV`: `4CC`
        * `size`: `u32`
        * `data`: `VFXL[size]` ; VFXL block (see [VFXL.md](VFXL.md))
* if `fileVer >= 0x14`:
    * `instanceIxs`:
        * `ROTV`: `4CC`
        * `size`: `u32`
        * `data`: `u16[size]`
* else
    * ; idk
* `bnds`: `BNDS` ; BNDS block (see [BNDS.md](BNDS.md))
* `unk`: `u32`
* `meshes`: `MESH` ; MESH block (see [MESH.md](MESH.md))
* `unk`: `u32`
* `materials`: `UMTL` ; UMTL block (see [UMTL.md](UMTL.md))
* `unk`: `u32`
* `lightmapData`: `LMDT` ; LMDT block (see [LMDT.md](LMDT.md))
* `unk`: `u32`
* `cpus`: `CPUS` ; CPUS block (see [CPUS.md](CPUS.md))
* `disp`: `DISP` ; DISP block (see [DISP.md](DISP.md))
* if `fileVer < 0x38`:
    * ; idk
* if `fileVer >= 0x14`:
    * `texAnims`:
        * `ROTV`: `4CC`
        * `size`: `u32`
        * `size` times:
            * `layerIdx`: `u8`
            * `mtlIdx`: `u32`
            * `scriptnameIdx`: `u32`
            * `tidsIdx`: `u32`
            * `numTids`: `u32`
    * `texAnimsTids`:
        * `ROTV`: `4CC`
        * `size`: `u32`
        * `data`: `u16[size]`
* else
    * ; idk
* `tanb`: `TANB` ; TANB block (see [TANB.md](TANB.md))
* `playbackFPS`: `f32`
* `unk`: `u32`
* `ala3`: `ALA3` ; ALA3 block (see [ALA3.md](ALA3.md))
* `port`: `PORT` ; PORT block (see [PORT.md](PORT.md))
* if `fileVer >= 0x10`:
    * `unk`: `u32`
    * `pins`: `PINS` ; PINS block (see [PINS.md](PINS.md))
* `bscb`: `BSCB` ; BSCB block (see [BSCB.md](BSCB.md))
* if `fileVer >= 0x33`:
    * `occluders`: `OCCB` ; OCCB block (see [OCCB.md](OCCB.md))
* `ivol`: `IVOL` ; IVOL block (see [IVOL.md](IVOL.md))
* if `fileVer >= 0xE`:
    * `ivl5`: `IVL5` ; IVL5 block (see [IVL5.md](IVL5.md))
* if `fileVer >= 0x14`:
    * `charData`:
        * `ROTV`: `4CC`
        * `size`: `u32`
        * `hgol`: `HGOL[size]` ; HGOL block (see [HGOL.md](HGOL.md))
* if `fileVer >= 0xB`:
    * `unk`: `u32`
    * if `unk != 0`: ; uhh i think it is supposed to work like that :P
        * `wiiMesh`: `WMSH`
* if `fileVer >= 0x11`:
    * `looseTextures`: `u8`
* if `fileVer >= 0xC`:
    * `meta`: `META` ; META block (see [META.md](META.md))
* if `fileVer >= 0x12`:
    * `unk`: `u32`
    * if `unk != 0`: ; uhh i think it is supposed to work like that :P
        * ; the following hasnt been checked
        * ; looks like its a legacy deprecated MESH format  
        `legacyMesh`: `LEGACY_MESH`
* if `fileVer >= 0x13`:
    * `useSingleLodAnim`: `u8`
* if `fileVer >= 0x35`:
    * `discipline`: `u8`
* if `fileVer >= 0x37`:
    * `numBlendShapes`: `u32`
* ; here goes dds textures data

## LEGACY_MESH
* `version`: `u32`
* `numPatches`: `u32`
* `numMeshes`: `u32`
* `patchArray`:
    * `size`: `u32`
    * `size` times:
        * `meshID`: `u32`
        * `numInstances`: `u32`
        * `numTris`: `u32`
        * `feathers`: `u8`
        * `segments`: `u32`
        * `specularSharpness`: `f32`
        * `baseAlpha`: `f32`
        * `tipAlpha`: `f32`
        * `antiAliasAlphaMul`: `f32`
        * `edgeAlpha`: `f32`
        * `translucency`: `f32`
        * `translucencySpread`: `f32`
        * `selfShadowing`: `f32`
        * `baseColor`: `COL3F`
        * `tipColor`: `COL3F`
        * `baseAmbientColor`: `COL3F`
        * `tipAmbientColor`: `COL3F`
        * `specularColor`: `COL3F`
        * `instanceArray`:
            * `size`: `u32`
            * `size` times:
                * `points`: `64 bytes` ; unsure about its type
                * `baryCoords`: `f32[3]`
                * `attraction`: `f32`
                * `uv`: `f32[2]`
                * `baseWidth`: `f32`
                * `tipWidth`: `f32`
                * `curveIDs`: `u32[3]`
                * `curveWeights`: `u8[4]`
        * `triArray`:
            * `size`: `u32`
            * `size` times:
                * `numInstances`: `u32`
                * `instanceOffset`: `u32`
                * `triID`: `u32`
* `meshArray`:
    * `size`: `u32`
    * `size` times:
        * `meshID`: `u32`
        * `numTris`: `u32`
        * `numVerts`: `u32`
        * `numBlendShapes`: `u32`
        * `triArray`:
            * `size`: `u32`
            * `size` times:
                * `vertIDs`: `u32[3]`
        * `vertArray`:
            * `size`: `u32`
            * `size` times:
                * `position`: `16 bytes` ; VEC4F ?
                * `normal`: `16 bytes` ; VEC4F ?
                * `tangent`: `16 bytes` ; VEC4F ?
                * `uv`: `f32[2]`
                * `boneWeights`: `f32[4]`
                * `boneIndices`: `u8[4]`
                * `uvSeam`: `u8`
        * `blendArray`:
            * `size`: `u32`
            * `size` times:
                * `stride`: `u32`
                * `numOffsets`: `u32`
                * `vertOffsetArray`:
                    * `size`: `u32`
                    * `vals`: `size * 16 bytes` ; VEC4F[size]? no one knows