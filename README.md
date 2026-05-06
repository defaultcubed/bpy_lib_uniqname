# bpy_lib_uniqname

`uniqname` generates a unique name for items in a Blender
`bpy.types.bpy_prop_collection`.

It returns `basename` when available, or appends an incrementing numeric
suffix when there is a collision.

Function signature:

```python
uniqname(collection, basename, ignore="", separator=".", zfill=3, check_params=True) -> str
```

- `collection`: Blender collection to check against.
- `basename`: Base name to try first.
- `ignore`: Name or set of names excluded from collision checks.
- `separator`: String placed before the numeric suffix.
- `zfill`: Width of the numeric suffix (for example, `3` -> `001`).
- `check_params`: Enables runtime type/value validation.

Example:

```python
name = uniqname(objects, "Cube", separator=".", zfill=3)
# "Cube" if free, otherwise "Cube.001", "Cube.002", ...
```
