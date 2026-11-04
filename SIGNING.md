# Release signatures

Release 0.1.0 is signed with the project Minisign key in `fast-items.pub`.
The public key to enter in Horizon's project form is:

```text
RWQ84d8BvD1EaarVDgHgXyz+MDiL7ONsCZc0BUrJqTmqzXBItnJy918A
```

The release supplies both `fast-items-0.1.0.hnmod.minisign` and
`fast-items-0.1.0.hnmod.minisig`; they contain the same signature. Horizon's
registry documentation calls the conventional signature extension `.minisig`.

Verify a downloaded release with the official Minisign tool:

```text
minisign -Vm fast-items-0.1.0.hnmod -p fast-items.pub -x fast-items-0.1.0.hnmod.minisign
```

The signature covers the exact release archive, not a rebuilt or modified archive.
Future releases must use this same key once it is registered in Horizon.
The encrypted private signing key and its password are kept locally by the maintainer;
neither is part of the repository or release. Back up both securely.

A valid signature verifies the artifact's author key and integrity. It does not replace
native-code review, and the visual/performance limitations in VALIDATION.md still apply.
