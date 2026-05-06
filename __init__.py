import bpy # pyright: ignore[reportMissingImports]

def uniqname(
    collection: 'bpy.types.bpy_prop_collection',
    basename: str,
    ignore: str|set[str]="",
    separator: str=".",
    zfill: int=3,
    check_params: bool=True
) -> str:
    """Generate a unique name for an item in a Blender collection.

    :param collection: Collection whose item names are checked for collisions.
    :type collection: bpy.types.bpy_prop_collection
    :param basename: Base name to use before adding any numeric suffix.
    :type basename: str
    :param ignore: Name or set of names to exclude from collision checks.
    :type ignore: str | set[str]
    :param separator: Separator inserted between ``basename`` and the
        numeric suffix.
    :type separator: str
    :param zfill: Zero-padding width for the numeric suffix (for example,
        ``3`` yields ``<separator>001``).
    :type zfill: int
    :param check_params: If ``True``, validate input argument types and values.
    :type check_params: bool
    :returns: A unique name. If ``basename`` is already taken, appends an
        incrementing suffix in the form ``<separator><number>`` with zero
        padding.
    :rtype: str
    """
    if check_params:
        if not isinstance(collection, bpy.types.bpy_prop_collection):
            raise TypeError(f"uniqname(collection, basename, ignore, separator, zfill, check_params) "
                            f"expects collection to be bpy.types.bpy_prop_collection, "
                            f"not {type(collection)}")
        if not isinstance(basename, str):
            raise TypeError(f"uniqname(collection, basename, ignore, separator, zfill, check_params) "
                            f"expects basename to be str, not {type(basename)}")
        if basename == "":
            raise ValueError(f"uniqname(collection, basename, ignore, separator, zfill, check_params) "
                             f"expects basename to be non-empty")
        if not isinstance(ignore, (str, set)):
            raise TypeError(f"uniqname(collection, basename, ignore, separator, zfill, check_params) "
                            f"expects ignore to be str or set, not {type(ignore)}")
        if isinstance(ignore, str) and not all(isinstance(item, str) for item in ignore):
            raise TypeError(f"uniqname(collection, basename, ignore, separator, zfill, check_params) "
                            f"expects all items in ignore to be str")
        if not isinstance(separator, str):
            raise TypeError(f"uniqname(collection, basename, ignore, separator, zfill, check_params) "
                            f"expects separator to be str, not {type(separator)}")
        if not isinstance(zfill, int):
            raise TypeError(f"uniqname(collection, basename, ignore, separator, zfill, check_params) "
                            f"expects zfill to be int, not {type(zfill)}")
        if zfill < 0:
            raise ValueError(f"uniqname(collection, basename, ignore, separator, zfill, check_params) "
                             f"expects zfill to be non-negative")
    if ignore:
        if isinstance(ignore, str):
            ignore = {ignore}
        index = {item.name for item in collection if item.name not in ignore}
    else:
        index = {item.name for item in collection}
    result = basename
    i = 1
    while result in index:
        result = f"{basename}{separator}{str(i).zfill(zfill)}"
        i += 1
    return result
