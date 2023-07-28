# UMTL
Endianness: big  
Reverse engineered by [JaanDev](https://github.com/JaanDev)  
This file may (but very unlikely) contain mistakes, just because it's so huge. Of course i've still checked it

## Main
* `LTMU`: `4CC`
* `ver`: `u32`
* `numMtls`: `u32`
* `mtls`: `MTLS`
* `haveShaderBlock`: `u8`
* if `haveShaderBlock`:
    * `shader`: `BCSH`
* if `ver >= 0x21`:
    * `storedEngineHash`: `u32`
    * `storedShaderBuilderVersion`: `u32`

## MTLS
* `size`: `u32`
* `size` times:
    * `unk`:
        * `version`: `u32`
        * `shaderType`: `u32`
        * if `ver >= 0x16`:
            * `lightingModel`: `u32`
        * `BRDFMode`: `u32`
        * `fresnelAlphaMode`: `u32`
        * if `ver >= 0x3D && ver != 0x64 && ver != 0x65 && ver != 0x66 && ver != 0x67`:
            * `blendMode`: `u32`
            * `alphaTest`: `u32`
            * `alphaFadeSource`: `u32`
        * `surfaceMapMethod`: `u32`
        * `surfaceMapFormat[0]`: `u32`
        * `surfaceMapFormat[1]`: `u32`
        * if `ver >= 0x7F`:
            * `surfaceMapFormat[2]`: `u32`
        * `surfaceMapFormatVTFN`: `u32`
        * `occlusion`: `u32`
        * `refraction`: `u32`
        * if `ver >= 0x2A`:
            * `reflection`: `u32`
        * `layerBlendDiffuse[0]`: `u32`
        * `layerBlendDiffuse[1]`: `u32`
        * `layerBlendDiffuse[2]`: `u32`
        * if `ver >= 0x30`:
            * `useLayers234OnWii`: `u8`
        * if `ver >= 0x93`:
            * `useWiiTintColours`: `u8`
        * if `ver >= 0x7F`:
            * `layerBlendSpecular[0]`: `u32`
            * `layerBlendSpecular[1]`: `u32`
            * `dummy`: `u32`
            * `layerBlendNormal[0]`: `u32`
            * `layerBlendNormal[1]`: `u32`
            * `dummy`: `u32`
        * `numUVSets`: `u32`
        * `lightmapUVSet`: `u32`
        * if `ver >= 0x19`:
            * `motionBlurVertexType`: `u32`
            * `motionBlurPixelType`: `u32`
        * `motionBlurSamples`: `u8`
        * `numBones`: `u8`
        * `UVSets`: `UVSET[14]`
        * if `ver >= 0x7F`:
            * `UVSets`: `UVSET[2]`
        * if `ver >= 0x1D`:
            * `old_bitangentFlip`: `u8`
        * `materialFlags.tangentSwap`: `u8`
        * `materialFlags.water`: `u8`
        * `materialFlags.nextGenShine`: `u8`
        * `materialFlags.glow`: `u8`
        * `materialFlags.carpaint`: `u8`
        * `materialFlags.fractal`: `u8`
        * `materialFlags.fractalBump`: `u8`
        * `materialFlags.fog`: `u8`
        * if `ver >= 0x33`:
            * `materialFlags.disableVerticalFog`: `u8`
        * `materialFlags.hdrAlpha_diffuse`: `u8`
        * `materialFlags.hdrAlpha_envmap`: `u8`
        * `materialFlags.dapple`: `u8`
        * `materialFlags.smoothspec`: `u8`
        * `materialFlags.blendWrinkles`: `u8`
        * `materialFlags.layer2fxmaps_old`: `u8`
        * `materialFlags.smoothLightmap`: `u8`
        * `materialFlags.rimLight`: `u8`
        * `materialFlags.ignoreExposure`: `u8`
        * `materialFlags.bakedSpecular`: `u8`
        * `materialFlags.semiLit`: `u8`
        * `materialFlags.refractionNearFix`: `u8`
        * `materialFlags.UNUSED1`: `u8`
        * `materialFlags.dontReceiveShadow`: `u8`
        * `materialFlags.lateShader`: `u8`
        * if `ver >= 0x15`:
            * `materialFlags.diffreflmaps`: `u8`
        * if `ver >= 0x20`:
            * `materialFlags.brdf_spec_map`: `u8`
        * if `ver >= 0x26`:
            * `materialFlags.tintable`: `u8`
        * if `ver >= 0x7D`:
            * `materialFlags.generateCubeMap`: `u8`
        * if `ver >= 0x83 && ver != 0x85`:
            * `materialFlags.outputToonShaderData`: `u8`
        * if `ver >= 0x8B`:
            * `materialFlags.disablePerPixelFade`: `u8`
        * `vertexFlags.vertAlbedo`: `u8`
        * `vertexFlags.skinned`: `u8`
        * `vertexFlags.fastBlend`: `u8`
        * `vertexFlags.blendShape`: `u8`
        * `vertexFlags.doPerspDivInVS`: `u8`
        * `vertexFlags.numAlphaLayers`: `u8`
        * `vertexFlags.use2DW`: `u8`
        * `vertexFlags.unTransformed`: `u8`
        * `vertexFlags.waterAmplitude`: `u8`
        * if `ver >= 0x2D`:
            * `vertexFlags.ignoreVertexOpacity`: `u8`
        * if `ver >= 0x3B && ver != 0x64 && ver != 0x65`:
            * `vertexFlags.LODVerticalScale`: `u8`
        * `miscFlags.WiiWater`: `u8`
        * `miscFlags.WiiGlass`: `u8`
        * `miscFlags.OLD_VisViewSpaceNormalZ`: `u8`
        * `miscFlags.OLD_VisTexelDensity`: `u8`
        * `miscFlags.OLD_VisShadowRecieve`: `u8`
        * `miscFlags.OLD_VisComplexity`: `u8`
        * `miscFlags.OLD_VisXRayMode`: `u8`
        * `miscFlags.OLD_VisOverDrawMode`: `u8`
        * if `ver >= 0x20`:
            * `miscFlags.greyAlbedo`: `u8`
        * `miscFlags.motionBlur`: `u8`
        * if `ver < 0x80`:
            * `DEFUNCT_WAS_SupportVTF`: `u8`
        * `miscFlags.UVAnimation`: `u8`
        * `miscFlags.canAlphaBlend`: `u8`
        * `miscFlags.Defunct_Opaque`: `u8`
        * `miscFlags.isDecal`: `u8`
        * `miscFlags.creaseMeshMaterial`: `u8`. Might be a typo (crease -> create) but im not sure
        * if `ver >= 0x20`:
            * `miscFlags.TTAnimationMode`: `u8`
        * if `ver >= 0x2C`:
            * `miscFlags.culled`: `u8`
        * if `ver >= 0x32`:
            * `miscFlags.isDeferredDecal`: `u8`
        * if `ver >= 0x39`:
            * `miscFlags.Defunct_IsGPAA`: `u8`
        * if `ver >= 0x3D && ver != 0x64 && ver != 0x65 && ver != 0x66 && ver != 0x67`:
            * `miscFlags.requiresDiffuseAlphaMultiply`: `u8`
        * `output.colourRT`: `u8`
        * `output.normalRT`: `u8`
        * `output.albedoRT`: `u8`
        * `output.depthAsColourRT`: `u8`
        * Some strange thing here in the code, but it probably does not read: `displayMode`: `u32`
        * `shaderVersion`: `u32`
        * `GPUVendor`: `u32`. what lol
        * if `ver < 0x7B`:
            * `srgb`: `u8`
        * else
            * `colourSpace`: `u32`
        * `bakedLighting`: `u32`
        * if `ver < 0x6A`:
            * if `ver < 0x25`:
                * `5` times:
                    * `discreteLightsType`: `u32`
                    * `castsLight`: `u8`
                    * `castsShadows`: `u8`
            * else
                * `5` times:
                    * `discreteLightsType`: `u32`
                    * `discreteLightsShadingModel`: `u32`
        * else
            * `5` times:
                * `discreteLightsType`: `u32`
                * `discreteLightsShadingModel`: `u32`
                * `discreteLightsSoftShadows`: `u8`
        * `sceneZAccess`: `u32`
        * `shadowZAccess`: `u32`
        * `PCFMethod`: `u32`
        * if `ver >= 0x25`:
            * `glowMode`: `u32`
        * if `ver >= 0x8C`:
            * `rainSplashSurfaceType`: `u32`
        * probably doesnt read: `engineHash`: `u32`
        * if `ver >= 0x6F`:
            * `useTangent2`: `u8`
    * `localTID`: `u32[16]`
    * if `ver >= 0x7F`:
        * `localTID`: `u32[2]`
    * if `ver < 0x90`:
        * `maxAnisotropy`: `u32[10]`
        * `mipmapBias`: `f32[10]`
        * `texAuxData`: `u32[10]`
    * else
        * `numTexAuxEntries`: `u32`
        * `maxAnisotropy`: `u32[numTexAuxEntries]`
        * `mipmapBias`: `f32[numTexAuxEntries]`
        * `texAuxData`: `u32[numTexAuxEntries]`
    * `texAnimData`: `u32[4]`
    * if `ver < 0x23`:
        * `4` times:
            * `temp`: `f32`
            * `temp`: `f32`
    * `unk`: `UV_UNK[4]`
    * `Uint`: `u32[4]`. Yes it's called like that in the code
    * if `ver < 0x31`:
        * `kOpacity`: `f32[4]`
    * `bitangentFlip`: `u8`
    * `kNormal[0]`: `f32`
    * `kNormal[1]`: `f32`
    * if `ver >= 0x7F`:
        * `kNormal[2]`: `f32`
    * `kParallax`: `f32`
    * `kParallaxBias`: `f32`
    * `UInt`: `u32[2]`
    * if `ver >= 0x7F`:
        * `UInt`: `u32`
    * `UInt`: `u32[2]`
    * if `ver >= 0x24`:
        * `UInt`: `u32`
    * `UInt`: `u32`
    * `kRefractiveIndex`: `f32`
    * `kRefractiveThicknessFactor`: `f32`
    * `kGlow`: `f32`
    * if `ver >= 0x1D`:
        * `UInt`: `u32`
    * `kReflectivity`: `f32`
    * `kSpecularCosPower`: `f32`
    * `kEnvironment`: `f32`
    * `kEnvLighting`: `f32`
    * `kEnvAlphaHDR`: `f32`
    * `kFresnel`: `f32`
    * `kFresnelPower`: `f32`
    * `kVTFHeight`: `f32`
    * `kVTFNormal`: `f32`
    * `kVTFOffset`: `f32`
    * `Uint`: `u32[4]`
    * `kCarPaintViewFactor`: `f32`
    * `kCarPaintLightFactor`: `f32`
    * `kBDRFRoughness`: `f32`
    * `kBDRFAnotherSetting`: `f32`. Yes it's like that in the code =)
    * `kDappleDistance`: `f32`
    * if `ver >= 0x17`:
        * `kDappleIntensity`: `f32`
    * `kFractalFrequency`: `f32`
    * `kFractalDiffuse`: `f32`
    * `kFractalSpecular`: `f32`
    * `kFractalLacunarity`: `f32`
    * `kFractalGain`: `f32`
    * `kFractalHeight`: `f32`
    * `kEnvRotationX`: `f32`
    * `kEnvRotationX`: `f32`
    * `kEnvRotationZ`: `f32`
    * `kEnvLightIntensity`: `f32`
    * `kEnvLightSpecular`: `f32`
    * `kEnvFresnel`: `f32`
    * `kEnvFresnelPower`: `f32`
    * `kSpecularBump`: `f32`
    * `kSkinSpread`: `f32`
    * `kShineSpread`: `f32`
    * `kShineStrength`: `f32`
    * if `ver >= 0x28`:
        * `kSubstance`: `f32`
    * if `ver >= 0x70`:
        * `kDepthBias`: `u8`
    * if `ver >= 0x8F`:
        * `kWiiMaxAlphaBias`: `f32`
    * if `ver >= 0x93`:
        * `UInt`: `u32[2]`
    * if `ver >= 0x95`:
        * `kTPageID`: `u16`
    * if `ver >= 0x1A`:
        * if `ver >= 0x3C && ver != 0x64 & ver != 0x65 && ver != 0x66`:
            * `materialName`: `STR16`
        * else
            * `materialName`: `STR32`. <i>Should</i> be the material name
    * if `ver >= 0x18`:
        * `flags`: `u32`
    * if `ver >= 0x81`:
        * `size` = `20`
        * if `ver < 0x8C`:
            * `size` = `19`
        * if `ver > 0x83`:
            * if `ver < 0x88`:
                * `size` = `17`
        * else
            * `size` = `16`
        * if `ver == 0x85`:
            * `size` = `16`
        * `dummyHashArray`: `u32[size * 4]`
        * if `ver < 0x82`:
            * `dummyHashArray`: `u32[size * 3]`
        * else
            * `storedShaderHashPC`: `u32[size * 3]`
        * `dummyHashArray`: `u32[size * 3]`
    * elif `ver >= 0x7D`:
        * `dummyHashArray`: `u32[16 * 4]`
    * elif `ver >= 0x7B`:
        * `dummyHashArray`: `u32[16 * 4]`
    * elif `ver < 0x6A`:
        * if `ver >= 0x1F`:
            * `dummyHashArary`: `u32[8 * 2]`
            * if `ver >= 0x28`:
                * `dummyHashArray`: `u32[8]`
            * if `ver >= 0x64`:
                * `dummyHashArray`: `u32[8]`
            * if `ver >= 0x33`:
                * `dummyHashArray_normalNoFog`: `u32`
                * `dummyHashArray_normalHorizontalOnlyFog`: `u32`
                * `dummyHashArray_normalNoFog`: `u32`
                * `dummyHashArray_normalHorizontalOnlyFog`: `u32`
                * `dummyHashArray_normalNoFog`: `u32`
                * `dummyHashArray_normalHorizontalOnlyFog`: `u32`
                * if `ver >= 0x69`:
                  * `dummyHashArray_normalNoFog`: `u32`
                  * `dummyHashArray_normalHorizontalOnlyFog`: `u32`
    * else
        * `dummyHashArray`: `u32[14 * 4]`
    * if `ver >= 0x29`:
        * `attribs1`: `ATTRIBS`
        * `attribs2`: `ATTRIBS`
    * if `ver >= 0x34`:
        * `shaderVertexStreamDepthMask`: `u32`
    * `fpThroughputPS3`: `f32`
    * `unk`: `u8[3]`
    * if `ver < 0xC`:
        * `unk`: `u8`
    * `unk`: `u8[2]`
    * `renderPlaneID`: `u8`
    * `flags`:
        * if `ver < 0x32`:
            * `old_alpha`: `u8`
            * `filter`: `u8`
            * `unk`: `u8`
            * `utc`: `u8`
            * `vtc`: `u8`
            * `cull`: `u8`
            * `zmode`: `u8`
            * `unk`: `u8`
            * `colour`: `u8`
            * `fill`: `u8`
            * `old_atst`: `u8`
            * `aref`: `u8`
            * `afail`: `u8`
            * `unk`: `u8[6]`
            * `only2d`: `u8`
            * `unk`: `u8[2]`
            * `stencil_shadows`: `u8`
            * `unk`: `u8[4]`
            * `castShadow`: `u8`
            * `old_autoStencil`: `u8`
            * `noprepass`: `u8`
        * else
            * `old_alpha`: `u8`
            * `old_atst`: `u8`
            * `afail`: `u8`
            * `aref`: `u8`
            * `cull`: `u8`
            * `zmode`: `u8`
            * if `ver >= 0x3A && ver != 0x64`:
                * `stencilMode`: `u8`
            * `noprepass`: `u8`
            * `filter`: `u8`
            * `utc`: `u8`
            * `vtc`: `u8`
            * `colour`: `u8`
            * `fill`: `u8`
            * `only2d`: `u8`
            * `stencil_shadows`: `u8`
            * `castShadows`: `u8`
            * `old_autoStencil`: `u8`
            * `colourWriteMask`: `u8`
            * if `ver >= 0x86`:
                * `alwaysUpdateRefraction`: `u8`
            * if `ver >= 0x94`:
                * `sortLast`: `u8`
            * if `ver >= 0x6B`:
                * `alphaTestMode`: `u8`
    * if `ver < 0x31`:
        * `diffuse`: `COL3F`
    * `fx1.u32`: `u32`
    * `fx2.u32`: `u32`
    * `fx3.u32`: `u32`
    * `fx4.u32`: `u32`
    * if `ver < 0x31`:
        * `alpha`: `f32`
    * `localTID`: `u32`
    * if `ver < 0x32`:
        * `fb_mask`: `u32`
    * `fxid`: `u8`
    * `special_id`: `u8`
    * `shortPri16bit`: `u16`
    * `shineSortID`: `u16`
    * `uanmode`: `u8`
    * `vanmode`: `u8`
    * `du`: `f32`
    * `dv`: `f32`
    * `su`: `f32`
    * `sv`: `f32`
    * `Index`: `u32[2]`
    * `isCreaseMeshMaterial`: `u8`
    * `hasVariants`: `u8`
    * `wasSerialized`: `u8`
    * if `ver >= 0x37`:
        * `legoStudMaterial`: `u8`
    * if `ver >= 0x1E`:
        * `maskShadows`: `u8`
        * if `ver >= 0x27`:
            * `sortAfterDeferred`: `u8`
        * else
            * `discardSortAfterDeferred`: `u8`
        * `sortAfterRefraction`: `u8`
        * `skipValidation`: `u8`
    * if `ver >= 0x6B`:
        * `specialDepthSorting`: `u8`
    * if `ver >= 0x6C`:
        * `forceAlphaLightingSupport`: `u8`
    * if `ver >= 0x7A`:
        * `noAutoScreenDoor`: `u8`
    * if `ver >= 0x7D`:
        * `compileLiveCubemapGenShader`: `u8`
    * if `ver != 0x85 && ver >= 0x83`:
        * `compileToonShader`: `u8`
    * if `ver >= 0x91`:
        * `shadowImpostor`: `u8`
    * if `ver >= 0x92`:
        * `shadowsFromFrontFaces`: `u8`
    * if `ver >= 0x96`:
        * `doUntexturedTPage`: `u8`
    * `name_ix`: `u32`
    * if `ver >= 0x1F`:
        * `defaultRenderStage`: `u32`


## UVSET
* `state`: `u32`
* `UVSet`: `u32`

## UV_UNK
* `modeU`: `u8`
* `modeV`: `u8`
* `dU`: `f32`
* `dV`: `f32`
* `speedU`: `f32`
* `speedV`: `f32`