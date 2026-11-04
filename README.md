# Fast Items for Horizon

An unofficial, independently written native Horizon mod inspired by Noryea's
[Fast Items](https://modrinth.com/mod/fast-items). Noryea did not author or endorse this port.
The original Java mod's source has not been copied or translated; its published behavior is the reference.

## What it does

- Makes dropped item entities face the active camera, including first-person, rear/front third-person and vertical views.
- Removes edge extrusion and the hidden back face from recognized generated item sprite layers. Each visible layer becomes one flat quad. Multi-layer textures (including potion overlays), tint, lighting and glint metadata are preserved.
- Rotates ordinary 3D block items toward the camera while keeping their 3D models.
- Preserves item bobbing, interpolation, stack copies, pickup animation, distance/frustum culling, glow outlines and the existing CPU/GPU rendering paths.
- Optionally disables dropped-item blob shadows. It does not disable shader-pack shadow passes.

Rendering only: inventory icons, held items, item frames, loot, physics and servers keep their normal behavior.
Special/custom 3D models retain their geometry. Because Horizon does not retain a generated-model marker,
flattening conservatively recognizes the standard full-size sprite slab, rather than every resource-pack model.
A custom model geometrically identical to that slab is treated as a sprite.

No performance percentage is promised: a full game benchmark has not been run. The main saving is replacing
sprite perimeter extrusion with one front quad per layer. A bounded cache reuses transformed models; original
models are immutable, and weak source identities prevent stale geometry after resource-pack reloads.

## Install

1. Download `fast-items-0.1.0.hnmod` from the [v0.1.0 prerelease](https://github.com/Lyvt-Dev/FastItems-for-Horizon/releases/tag/v0.1.0) and put it in the selected instance's `horizon-native-mods/` folder.
2. Use the Horizon launcher's native mod build flow for that instance and review its native-code trust warning.
3. Launch the modded build. Native mods are compiled into a separate game executable; this is not a Java/Fabric JAR.

This bundle is pinned to Horizon `998b1d8301928c0559a0f368809860a30d6d9e53` (Minecraft 26.3) and
horizon-mixins `e8cd0aa38cffef49cb2e088ef716baa107148c02`. A different Horizon revision requires revalidation.
The launcher needs Git and Rust/Cargo to compile native mods.

The release also includes Minisign signatures and the project public key; see [SIGNING.md](SIGNING.md) for Horizon submission and verification.

## Configuration

On first use the mod creates `config/fast-items.json` inside the active game instance. Example:

```json
{
  "enabled": true,
  "entity_shadows": true,
  "render_sides": false,
  "affect_3d_models": true
}
```

Restart the modded game after editing. `enabled: false` restores original item rendering and shadows;
`render_sides: true` keeps sprite side/back geometry while still facing the camera;
`affect_3d_models: false` leaves ordinary 3D/special item orientation unchanged.
The existing global entity-shadow setting still applies. Invalid JSON/unknown keys produce a log message and
use defaults. A configuration file that cannot be read is never overwritten.

## Build and check

```text
cargo test --locked
cargo clippy --all-targets --locked -- -D warnings
python tools/package.py
```

The `Cargo.toml` library compiles the same `runtime.rs` injected into Horizon, testing configuration,
sprite recognition and camera-facing math. It does not by itself compile the Horizon renderer adapter.

On Windows, use a fresh output path for each changed mixin application: the transformer cannot atomically replace an existing stage there.

For full integration, export the exact Horizon revision into a separate directory using `git archive`, place
its SHA in `.horizon-revision`, and use the pinned mixin tool:

```text
horizon-mixins plan --workspace <pristine-horizon> --mods mixins --out target/plan.json
horizon-mixins apply --workspace <pristine-horizon> --mods mixins --out target/modded
cargo check --manifest-path target/modded/Cargo.toml -p horizon-client --lib --no-default-features
```

For visual/performance verification, use scratch game homes and your own prepared 26.3 resources. Compare
vanilla and modded builds with the same dropped stacks (diamond, sword, potion, enchanted item, block,
and a custom model), then check all perspectives, pickups, glow outlines, resource reload and each config switch.
No game assets or compiled Horizon executable are shipped in this package.

## Attribution

Behavior reference: Noryea's Fast Items Modrinth description (CC0-1.0 as listed there). This is an original Rust
implementation using Horizon's public source and native-mixin interfaces. Horizon and horizon-mixins are MIT;
the packager adapts the official MIT native-mod template (see THIRD_PARTY_NOTICES.md). No third-party Java mod source was read.
