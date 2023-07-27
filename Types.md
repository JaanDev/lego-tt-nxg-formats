# Types

`f32` = `float`  
`u8` = `unsigned char`  
`i8` = `char`  
`u16` = `unsigned short`  
`i16` = `short`  
`u32` = `unsigned int`  
`i32` = `int`

`type[n]` = `type`, `n` times
`str(n)` = `str` of length `n`

`4CC` = `str(4)`. 4 character code. Used to indicate new blocks. It is also flipped if endianness is big

## STR16
* `len`: `u16`
* `data`: `str(len)`

## STR32
* `len`: `u32`
* `data`: `str(len)`