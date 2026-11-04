# Validation

Target: Horizon 998b1d8301928c0559a0f368809860a30d6d9e53 (Minecraft 26.3).
Transformer: horizon-mixins e8cd0aa38cffef49cb2e088ef716baa107148c02.
Local environment: Windows x86_64, Rust 1.99.1.

- Six standalone Rust tests pass: sprite face selection, layered sprites, custom/invalid geometry fallback,
  configuration, disabled-mod shadow behavior, and horizontal/vertical camera-facing math.
- Clippy on all standalone targets passes with warnings denied.
- Rustfmt passes for every injected Rust source file.
- The final `.hnmod` is accepted by Horizon's actual `horizon_mods::index::native::Bundle::read` loader.
- Two independent package runs produce identical bytes; ZIP integrity and source-only entries pass.
- The real pinned mixin tool accepts and applies all three injections and both modules to a pristine
  export of the pinned Horizon revision.
- Full modded Horizon gameplay library compile check passes with `cargo check -p horizon-client --lib --no-default-features --locked` (Windows).
- In-game visual testing and FPS benchmarks have not been run: prepared Minecraft assets are unavailable.

The archive contains source only. Installing it asks the Horizon launcher to compile native Rust code into
an instance-specific game build. This prerelease is not a prebuilt game executable.
