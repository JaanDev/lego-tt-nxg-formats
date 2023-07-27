# DLGT
Endianness: big  
Reverse engineered by [JaanDev](https://github.com/JaanDev)

## Main
* `TGLD`: `4CC`
* `ver`: `u32`
* if `ver <= 1`:
    * `lightCount`: `u32`
* `size`: `u32`
* `lightDescs`: `LIGHT[size]`

## LIGHT
* `light`: `LIGHT_NXG`
* `transform`: `64 bytes`

## LIGHT_NXG
* `common`: `LIGHT_COMMON`
* `deferredBoundingBoxes`:
    * `usedBits`: `u8`
    * `num` = `4u32` if `ver >= 0x17` else `6u32`
    * `i` = `0u32`
    * `num` times:
        * this one is tricky. it only reads if `((*(&usedBits + (i >> 3)) >> (i & 7)) & 1) != 0`. so it doesnt read in most cases, for example when `usedBits = 0`
        * `data`: `DEFER_BB`
        * `i` = `i + 1`
* `numRayTracedShadowRays`: `u32`
* `realTimeMethod`: `u32`
* if `ver < 0x23`:
    * `splitMethod`: `u32`
* `shadowProjectionMethod`: `u32`
* `shadowMapRangeInGame[SMR_SHADOW_RANGE_0]`: `f32`
* `shadowMapRangeInGame[SMR_SHADOW_RANGE_1]`: `f32`
* `shadowMapRangeInGame[SMR_SHADOW_RANGE_2]`: `f32`
* `shadowMapRangeInGame[SMR_SHADOW_RANGE_3]`: `f32`
* `shadowMapRangeInGame[SMR_SHADOW_RANGE_4]`: `f32`
* if `ver >= 0x23`:
    * `shadowFalloffStartInGame`: `f32`
    * `shadowFalloffRangeInGame`: `f32`
    * `shadowBiasInGame`: `f32`
    * `shadowSplitMethodInGame`: `u32`
* if `ver >= 0x19`:
    * `shadowMapRangeCutscene[SMR_SHADOW_RANGE_0]`: `f32`
    * `shadowMapRangeCutscene[SMR_SHADOW_RANGE_1]`: `f32`
    * `shadowMapRangeCutscene[SMR_SHADOW_RANGE_2]`: `f32`
    * `shadowMapRangeCutscene[SMR_SHADOW_RANGE_3]`: `f32`
    * `shadowMapRangeCutscene[SMR_SHADOW_RANGE_4]`: `f32`
    * `haveCustomCutsceneShadowRanges`: `u8`
    * if `ver >= 0x23`:
        * `shadowFalloffStartCutscene`: `f32`
        * `shadowFalloffRangeCutscene`: `f32`
        * `shadowBias`: `f32`
        * `shadowSplitMethodCutscene`: `u32`
* if `ver >= 0x20`:
    * `focusSpotShadowsFromMaya`: `u8`
* if `ver >= 0x1A`:
    * `focusSpotShadowsInGame`: `u8`
    * `focusSpotShadowsCutscenes`: `u8`
* if `ver >= 0x1B`:
    * `castShadowsFromFrontFaces`: `u8`
* if `ver >= 0x1D`:
    * `downwardsCubeShadowsOnly`: `u8`
* if `ver >= 0x21`:
    * `occluderPixelThreshold[0]`: `f32`
    * `occluderPixelThreshold[1]`: `f32`
    * `occluderPixelThreshold[2]`: `f32`
    * `occluderPixelThreshold[3]`: `f32`
* `enableDynamicCascadeSizes`: `u8`
* `dynamicCascadesStartDistance`: `f32`
* `dynamicCascadesEndDistance`: `f32`
* `dynamicCascadesEndFactor`: `f32`
* if `ver >= 0x1C`:
    * `dynamicCascadesCount`: `u32`
* if `ver < 0x23`:
    * `falloff`: `f32`
* if `ver < 0x13`:
    * `shadowFalloffEnd`: `f32`
* elif `ver < 0x23`:
    * `falloff`: `f32`
* if `ver < 0x23`:
    * `shadowBias`: `f32`
* if `ver >= 0x14`:
    * `shadowBiasDoubleSided`: `f32`
* `shadowIntensity`: `f32`
* `softShadowsEnabled`: `u8`
* `softShadowsFixedSpread`: `f32`
* `softShadowsSpreadRatio`: `f32`
* `softShadowsSampleCount`: `u32`
* `softShadowOverlap`: `f32`
* if `ver >= 0x1E`:
    * `softShadowsSpreadRatioEnabled`: `u8`
    * `softShadowsFixedSpread2`: `f32`
    * if `ver < 0x1F`:
        * `unk`: `STR32`
    * `enableDynamicCascadeSizesInGame`: `u8`
    * `enableDynamicCascadeSizesCutscenes`: `u8`
* `shadowNoiseEnabled`: `u8`
* `shadowNoiseScale`: `f32`
* `shadowNoiseIntensity`: `f32`
* if `ver >= 0x18`:
    * `castShadowsFromSpecials`: `u8`
    * `castShadowsFromTerrain`: `u8`
    * `onlyCastShadowsIfPlayerIsInVolume`: `u8`

## LIGHT_COMMON
* if `ver >= 0x1E`:
    * `name`: `STR16`
* else:
    * `name`: `STR32`
* `enabled`: `u8` (`bool`)
* if `ver >= 0x16`:
    * `layer`: `u32`
* `shapeType`: `u32`
* if `ver >= 0x12`:
    * `emitterShape`: `u32`
* `shadingModel`: `u32`
* `falloff`: `u32`
* `importance`: `u32`
* `platform`: `u32`
* `directDiffuseMode`: `u32`
* `bouncedDiffuseMode`: `u32`
* `specularMode`: `u32`
* if `ver >= 0x22`:
    * `godRays`: `u32`. (or `f32` ?)
    * `effectIntensity`: `f32`
* if `ver >= 0x24`:
    * `godRaysFalloff`: `f32`
* if `ver >= 0x29`:
    * `lensFlare`: `u8` (`bool`)
* if `ver >= 0x12`:
    * if `ver >= 0x15`:
        * if `ver < 0x1E`:
            * `serializeMtx`: `64 bytes`
    * else
        * `x`: `12 bytes`. I really dont know why but it reads 12 bytes in the code
        * `y`: `12 bytes`
        * `z`: `12 bytes`
        * `w`: `12 bytes`
    * `emitterSize`: `12 bytes`
* else
    * `serializeMtx[3]`: `12 bytes`
    * `serializeMtx[2]`: `12 bytes`
    * `serializeMtx[1]`: `12 bytes`
    * `sourceRadius`: `f32`
* if `ver >= 0x2A`:
    * `lensFlareIntensity`: `f32`
    * `coronaIntensity`: `f32`
    * `GodRayIntensity`: `f32`
* `colour`: `12 bytes`
* `linearColour`: `12 bytes`
* `secondaryColourLinear`: `12 bytes`
* if `ver >= 0x2B`:
    * `secondaryColour`: `12 bytes`
* if `ver >= 0x1F`:
    * `unk`: `STR32`
* `ambientFactor`: `f32`
* `diffuseFactor`: `f32`
* `specularFactor`: `f32`
* `shadowIntensity`: `f32`
* if `ver >= 0x2C`:
    * `isNegativeLight`: `u8`
* `LSVHotSpot`: `u8`
* `falloffStart`: `f32`
* `spotFarClip`: `f32`
* if `ver >= 0x13`:
    * `lightFalloffStart`: `f32`
    * `lightFalloffRange`: `f32`
* `TID`: `u32`. (`i32` ?)
* `spotFovY_Degrees`: `f32`
* `spotFovY_Cos`: `f32`
* `spotInnerFovY_Degrees`: `f32`
* `spotInnerFovY_Cos`: `f32`
* `spotNearClip`: `f32`
* if `ver >= 0x28`:
    * `falloffFactor`: `f32`
* `spotAspectRatio`: `f32`
* `spotNegativeDistance`: `f32`

## DEFER_BB
* `_00`: `f32`
* `_01`: `f32`
* `_02`: `f32`
* `_03`: `f32`
* `_10`: `f32`
* `_11`: `f32`
* `_12`: `f32`
* `_13`: `f32`
* `_20`: `f32`
* `_21`: `f32`
* `_22`: `f32`
* `_23`: `f32`
* `_30`: `f32`
* `_31`: `f32`
* `_32`: `f32`
* `_33`: `f32`