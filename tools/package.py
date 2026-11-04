# Packaging adapted from horizon-native-mod-template (MIT).
# Copyright (c) 2026 Horizon Veinminer contributors
# Copyright (c) 2026 Horizon native mod contributors
# Modified for the Fast Items bundle, packaged notices and output layout.
"""Build a deterministic Horizon native-mod archive from the reviewed bundle."""
import hashlib
import json
from pathlib import Path
import tomllib
import zipfile

ROOT = Path(__file__).resolve().parents[1]

def package():
    compat = json.loads((ROOT / 'compatibility.json').read_text())
    bundle = ROOT / 'mixins/fast_items'
    mod = tomllib.loads((bundle / 'horizon-mixin.toml').read_text())
    assert mod['compatibility']['horizon_revision'] == compat['horizon_revision']
    manifest = dict(schema=1, id=mod['mod']['id'], version=mod['mod']['version'],
                    game=compat['game'], horizon=compat['horizon_revision'],
                    mixins=compat['horizon_mixins_revision'])
    files = {'horizon-native.json': (json.dumps(manifest, indent=2) + '\n').encode()}
    for path in sorted(bundle.iterdir()):
        if path.is_file() and (path.suffix in ('.rs', '.toml') or path.name.startswith(('LICENSE', 'NOTICE', 'README'))):
            files[path.relative_to(ROOT).as_posix()] = path.read_bytes().replace(b'\r\n', b'\n')
    destination = ROOT / 'dist' / 'fast-items-0.1.0.hnmod'
    destination.parent.mkdir(exist_ok=True)
    with zipfile.ZipFile(destination, 'w') as archive:
        for name, content in sorted(files.items()):
            info = zipfile.ZipInfo(name, (2026, 1, 1, 0, 0, 0))
            info.compress_type = zipfile.ZIP_DEFLATED
            info.external_attr = 0o100644 << 16
            archive.writestr(info, content)
    print(json.dumps(dict(file=str(destination), sha256=hashlib.sha256(destination.read_bytes()).hexdigest()), indent=2))
    return destination

if __name__ == '__main__':
    package()
