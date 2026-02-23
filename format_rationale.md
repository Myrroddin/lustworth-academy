# Format Rationale for Lustworth Academy

## Why WebP Instead of ASIF?

- **Ren'Py Version Compatibility:** ASIF requires Ren'Py 8.1+, but WebP works with older versions, ensuring broader compatibility.
- **Tooling and Workflow:** WebP is widely supported by image editors and conversion tools, while ASIF has limited external tooling.
- **Platform and Browser Support:** WebP is a web standard and works well for web builds; ASIF is Ren'Py-specific and not supported outside the engine.
- **Animation Needs:** ASIF is best for simple animations, but Lustworth Academy's assets do not require this; WebP's compression is sufficient.
- **Testing and Stability:** WebP is mature and stable; ASIF is newer and may have unaddressed edge cases.

## Why OGG Instead of MP3?

- **Licensing:** OGG is open and free, while MP3 has had patent/licensing restrictions.
- **Quality and Compression:** OGG generally provides better quality at similar or smaller file sizes, especially at lower bitrates.
- **Ren'Py and Engine Support:** OGG is natively supported and preferred by Ren'Py, ensuring smooth playback.
- **Cross-Platform Consistency:** OGG works reliably across all Ren'Py-supported platforms.
